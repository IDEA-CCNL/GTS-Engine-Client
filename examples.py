# -*- encoding: utf-8 -*-
'''
Copyright 2022 The International Digital Economy Academy (IDEA). CCNL team. All rights reserved.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
@File    :   examples.py
@Time    :   2022/11/02 11:39
@Author  :   Kunhao Pan
@Version :   1.0
@License :   (C)Copyright 2022-2023, CCNL-IDEA
'''

from gts_engine_client import GTSEngineClient

client = GTSEngineClient("192.168.190.2", "5207")

# 创建任务
print(client.create_task(task_name="test_task1", task_type="classification"))
print(client.create_task(task_name="test_task2", task_type="classification"))

# 列出任务列表
print(client.list_tasks())

# 查看任务状态
print(client.check_task_status(task_id="test_task1"))

# 删除任务
print(client.delete_task(task_id="test_task2"))

# 上传文件
print(client.upload_file(task_id="test_task1", local_data_path="train.json"))

# 开始训练
print(client.start_train(task_id="test_task1", train_data="train.json", val_data="test.json", label_data="label.json"))

# 终止训练
print(client.stop_train(task_id="test_task1"))

