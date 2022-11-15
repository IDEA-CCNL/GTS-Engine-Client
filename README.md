# GTS Engine Client

GTS Engine Client是配合GTS Engine使用的官方API，通过封装HTTP Post请求，让您更方便地使用Python调用GTS Engine，通过几行代码即可轻松训练和部署你的AI模型。

## 快速链接

1. [安装](#安装)
2. [使用示例](#使用示例)
3. [接口详情](#接口详情)
4. [GTS Engine](#GTS-Engine)
5. [引用](#引用)

## 安装

您可以通过pip直接进行安装。

```bash
pip install gts-engine-client
```

也可以clone下github项目后进行安装。

```bash
git clone https://github.com/IDEA-CCNL/GTS-Engine-Client.git
cd GTS-Engine-Client
python setup.py install
```

## 使用示例

下面给出一个简单的使用示例。

首先，您需要使用GTS Engine的开源代码或者Docker启动服务。

```python
from gts_engine_client import GTSEngineClient

#ip和port参数与启动服务的ip和port一致
client = GTSEngineClient(ip="192.168.190.2", port="5207")

# 创建任务 (为了方便演示，创建2个任务)
client.create_task(task_name="test_task1", task_type="classification")
# {'ret_code': 200, 'message': 'task成功创建', 'task_id': 'test_task1'}

client.create_task(task_name="test_task2", task_type="classification")
# {'ret_code': 200, 'message': 'task成功创建', 'task_id': 'test_task2'}

# 列出任务列表
client.list_tasks()
# {'ret_code': 200, 'message': 'Success', 'tasks': ['test_task1', 'test_task2']}

# 查看任务状态
client.check_task_status(task_id="test_task1")
# {'ret_code': 0, 'message': 'Initialized'}

# 删除任务  
client.delete_task(task_id="test_task2")
# {'ret_code': 200, 'message': 'Success'}

client.list_tasks()  #查看任务状态 删除后任务test_task2已经不在任务列表
# {'ret_code': 200, 'message': 'Success', 'tasks': ['test_task1']}

# 上传文件  (文件地址写绝对路径)
client.upload_file(task_id="test_task1", local_data_path="train.json")
# {'ret_code': 200, 'message': '上传成功'}
client.upload_file(task_id="test_task1", local_data_path="dev.json")
# {'ret_code': 200, 'message': '上传成功'}
client.upload_file(task_id="test_task1", local_data_path="test.json")
# {'ret_code': 200, 'message': '上传成功'}
client.upload_file(task_id="test_task1", local_data_path="labels.json")
# {'ret_code': 200, 'message': '上传成功'}

# 开始训练
client.start_train(
  task_id="test_task1", train_data="train.json", val_data="dev.json", test_data="test.json", label_data="labels.json", gpuid=1)
# {'ret_code': 200, 'message': '训练调度成功'}

client.check_task_status(task_id="test_task1")   #查看任务状态  任务在训练中
# {'ret_code': 1, 'message': 'On Training'}


# 终止训练  （若提前终止训练）
client.stop_train(task_id="test_task1")
# {'ret_code': 200, 'message': '终止训练成功'}

client.check_task_status(task_id="test_task1")   #查看任务状态  任务已停止训练
# {'ret_code': 3, 'message': 'Train Stopped'}

# 加载已训练好的模型
client.start_inference(task_id="test_task1")
# {'ret_code': 200, 'message': '加载预测模型'}

client.check_task_status(task_id="test_task1")   #查看任务状态  预测模型已加载
# {'ret_code': 2, 'message': 'On Inference'}

# 开始预测
client.inference(
  task_id="test_task1",
  samples=[{"content":"怎样的房子才算户型方正？"}, {"content":"文登区这些公路及危桥将进入 封闭施工，请注意绕行！"}])

# 结束预测
client.end_inference(task_id="test_task1")
# {'ret_code': 200, 'message': '释放预测模型'}

client.check_task_status(task_id="test_task1")   #查看任务状态  回到训练成功的状态
# {'ret_code': 2, 'message': 'Train Success'}
```

您可以参考GTS Engine的文档来一步一步地使用GTS Engine快速地训练一个FewCLUE任务。

## 接口详情

#### 创建任务

`create_task(self, task_name: str, task_type: str)`

* 输入参数

| 参数名 | 参数类型 | 释义 |
| ---- | ---- | ---- |
| `task_name` | str | 任务名称，需要不同于其他已有的任务 |
| `task_type` | str | 任务类型，目前仅支持以下两种任务：<br> - classification：文本分类 <br> - similarity：句子相似度 |

* 输出参数

函数的返回值是一个字典，字典中包含如下字段：

| 参数名 | 参数类型 | 释义 |
| ---- | ---- | ---- |
| `ret_code` | int | 返回码： <br> - 200：创建成功 <br> - -100：创建失败 |
| `task_id` | str | 任务对应的id，全局唯一，目前它和task_name相同 |

#### 列出任务列表
* 输入参数:空
<br>
* 输出参数

函数的返回值是一个字典，字典中包含如下字段：

| 参数名 | 参数类型 | 释义 |
| ---- | ---- | ---- |
| `ret_code` | int | 返回码： <br> - 200：返回成功 <br> - -100：返回失败 |
| `tasks` | str | 返回任务的列表 |

#### 查看任务状态
* 输入参数

| 参数名 | 参数类型 | 释义 |
| ---- | ---- | ---- |
| `taskid` | str | 任务id |

* 输出参数

| 参数名 | 参数类型 | 释义 |
| ---- | ---- | ---- |
| `retcode` | int | 训练进度：<br>未启动训练：1<br>训练中：2 <br>训练成功：3<br>训练失败：4 |
| `taskid` | str | 任务id |

#### 删除任务
* 输入参数

| 参数名 | 参数类型 | 释义 |
| ---- | ---- | ---- |
| `taskid` | str | 任务id |
* 输出参数

函数的返回值是一个字典，字典中包含如下字段：

| 参数名 | 参数类型 | 释义 |
| ---- | ---- | ---- |
| `ret_code` | int | 返回码： <br> - 200：返回成功 <br> - -100：返回失败 |

#### 上传文件
* 输入参数

| 参数名 | 参数类型 | 释义 |
| ---- | ---- | ---- |
| `taskid` | str | 任务id |
| `filename` | str | 需要上传的文件路径 |
* 输出参数

| 参数名 | 参数类型 | 释义 |
| ---- | ---- | ---- |
| `ret_code` | int | 返回码： <br> - 200：返回成功<br> - -100：返回失败 |

#### 开始训练
* 输入参数

| 参数名 | 参数类型 | 释义 |
| ---- | ---- | ---- |
| `taskid` | str | 任务id |
| `train_data` | str | 训练数据的文件名 |
| `val_data` | str | 验证数据的文件名 |
| `test_data` | str | 测试数据的文件名 |
| `label_data` | str | 标签数据的文件名 |
| `seed` | int | 随机种子 |
| `max_num_epoch` | int | 最大训练轮次 |
| `min_num_epoch` | int | 最小训练轮次 |
* 输出参数

函数的返回值是一个字典，字典中包含如下字段：

| 参数名 | 参数类型 | 释义 |
| ---- | ---- | ---- |
| `ret_code` | int | 返回码： <br> - 200：启动训练成功 <br> - -100：启动训练失败 |
| `message` | str | 其他返回提示消息 |

#### 终止训练
* 输入参数

| 参数名 | 参数类型 | 释义 |
| ---- | ---- | ---- |
| `taskid` | str | 任务id |
* 输出参数

函数的返回值是一个字典，字典中包含如下字段：

| 参数名 | 参数类型 | 释义 |
| ---- | ---- | ---- |
| `ret_code` | int | 返回码： <br> - 200：停止成功 <br> - -100：停止失败 |

#### 开始推理
* 输入参数

| 参数名 | 参数类型 | 释义 |
| ---- | ---- | ---- |
| `taskid` | str | 任务id |
* 输出参数

函数的返回值是一个字典，字典中包含如下字段：

| 参数名 | 参数类型 | 释义 |
| ---- | ---- | ---- |
| `ret_code` | int | 返回码： <br> - 200：推理模型启动成功 <br> - -100：推理模型启动失败 |
#### 推理
* 输入参数

| 参数名 | 参数类型 | 释义 |
| ---- | ---- | ---- |
| `taskid` | str | 任务id |
| `samples` | list | list中每个元素是待预测样本 |
* 输出参数

函数的返回值是一个字典，字典中包含如下字段：

| 参数名 | 参数类型 | 释义 |
| ---- | ---- | ---- |
| `ret_code` | int | 返回码： <br> - 200：推理成功 <br> - -100：未启动推理服务 |
| `predictions` | list | 推理结果的标签列表 |
| `probabilities` | list | 推理结果的概率分布 |
#### 终止推理
* 输入参数

| 参数名 | 参数类型 | 释义 |
| ---- | ---- | ---- |
| `taskid` | str | 任务id |
| `samples` | list | list中每个元素是待预测样本 |
* 输出参数

函数的返回值是一个字典，字典中包含如下字段：

| 参数名 | 参数类型 | 释义 |
| ---- | ---- | ---- |
| `ret_code` | int | 返回码： <br> - 200：推理模型停止成功 <br> - -100：推理模型停止失败 |
| `message` | str | 其他返回提示消息 |

## GTS Engine

GTS Engine是粤港澳大湾区数字经济研究院认知计算与自然语言研究中心（简称IDEA-CCNL）研发的一站式NLP模型训练与部署的工具箱，能够让您轻松训练和部署AI模型，将提供乾坤鼎和八卦炉两个系列。其中，乾坤鼎系列使用13亿参数级别的大模型进行训练，能够获得很高的性能。而八卦炉系列使用1亿参数级别的小模型，在兼顾训练和推理效率的同时，尽可能获得良好的性能。详细介绍可以参考GTS Engine文档。

## 引用

如果您在研究中使用了我们的工具，请引用我们的工作：

```
@misc{GTS-Engine,
  title={GTS-Engine},
  author={IDEA-CCNL},
  year={2022},
  howpublished={\url{https://github.com/IDEA-CCNL/GTS-Engine}},
}
```
