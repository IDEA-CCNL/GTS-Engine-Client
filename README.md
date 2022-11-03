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

client = GTSEngineClient(ip="192.168.190.2", port="5207")

# 创建任务
print(client.create_task(task_name="test_task1", task_type="classification"))

# 列出任务列表
print(client.list_tasks())

# 查看任务状态
print(client.check_task_status(task_id="test_task1"))

# 删除任务
print(client.delete_task(task_id="test_task2"))

# 上传文件
print(client.upload_file(task_id="test_task1", local_data_path="train.json"))

# 开始训练
print(client.start_train(task_id="test_task1", train_data="train.json", val_data="dev.json", test_data="test.json", label_data="label.json", gpuid=1))

# 终止训练
print(client.stop_train(task_id="test_task1"))

# 加载已训练好的模型
print(client.start_inference(task_id="test_task1"))

# 开始预测
print(client.inference(task_id="test_task1", samples=["怎样的房子才算户型方正？","文登区这些公路及危桥将 进入封闭施工，请注意绕行！"]))

# 结束预测
print(client.end_inference(task_id="test_task1"))

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

#### 查看任务状态

#### 删除任务

#### 上传文件

#### 开始训练

#### 终止训练

#### 开始推理

#### 推理

#### 终止推理

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
