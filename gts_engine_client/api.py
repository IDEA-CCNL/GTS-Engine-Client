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
@File    :   api.py
@Time    :   2022/10/31 10:35
@Author  :   Kunhao Pan
@Version :   1.0
@Contact :   pankunhao@idea.edu.cn
@License :   (C)Copyright 2022-2023, CCNL-IDEA
'''

import os
import sys
import requests

class GTSEngineClient(object):
    def __init__(self, ip, port):
        self._base_url = "http://{ip}:{port}".format(ip=ip, port=port)

    def __post(self, url, data=None, files=None):
        if files and data:
            resp = requests.post(url, data, files=files)
        elif data:
            resp = requests.post(url, json=data)
        else:
            resp = requests.post(url)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"ret_code": resp.status_code, "message": "Server Failed"}

    def create_task(self, task_name: str, task_type: str):
        create_task_api_url = self._base_url + "/api/create_task/"
        payload = {
            "task_name": task_name,
            "task_type": task_type,
        }
        resp_data = self.__post(create_task_api_url, payload)
        return resp_data

    def delete_task(self, task_id: str):
        delete_task_url = self._base_url + "/api/delete_task/"
        payload = {
            "task_id": task_id,
        }
        resp_data = self.__post(delete_task_url, payload)
        return resp_data

    def check_task_status(self, task_id: str):
        check_task_url = self._base_url + "/api/check_task_status/"
        payload = {
            "task_id": task_id
        }
        resp_data = self.__post(check_task_url, payload)
        return resp_data

    def list_tasks(self):
        list_task_url = self._base_url + "/api/list_task"
        resp_data = self.__post(list_task_url)
        return resp_data

    def upload_file(self, task_id, local_data_path):
        upload_file_url = self._base_url + "/api/upfiles"
        files = {
            "files": open(local_data_path, mode="rb")
        }
        payload = {
            "task_id": task_id
        }
        resp_data = self.__post(upload_file_url, data=payload, files=files)
        return resp_data

    def start_train(self, task_id, train_data, val_data, label_data):
        train_api_url = self._base_url + "/api/train"
        payload = {
            "task_id": task_id,
            "train_data": train_data,
            "val_data": val_data,
            "test_data": val_data,
            "label_data": label_data,
        }
        resp_data = self.__post(train_api_url, payload)
        return resp_data

    def stop_train(self, task_id):
        stop_train_url = self._base_url + "/api/stop_train/"
        payload = {
            "task_id": task_id
        }
        resp_data = self.__post(stop_train_url, payload)
        return resp_data

    def start_inference(self, task_id):
        pass

    def stop_inference(self, task_id):
        pass

    def inference(self, task_id, samples):
        pass
