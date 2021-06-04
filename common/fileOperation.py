#! /usr/bin/python
# coding:utf-8
import json,os,time

def read_file(filename):
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '\\data\\'
    with open(data_path + filename, 'r',encoding='utf-8') as load_f:
        datas = json.load(load_f)
    return datas


def write_file(param, filename):
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '\\data\\'
    with open(data_path + filename, "w",encoding='utf-8') as f:
        json.dump(param, f)

# 更新json文件
def update_file(param, value, filename):
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '\\data\\'
    with open(data_path  + filename, 'r+',encoding='utf-8') as f:
        data = json.load(f)
        data[param] = value  # <--- add `id` value.
        f.seek(0)  # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()  # remove remaining part


# json 追加
#在原来json下追加新内容
def add_write_file(param, filename):
    data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '\\data\\'
    data = read_file(filename)
    json_d = json.dumps(data)
    new = json.dumps({**json.loads(json_d), **param})
    with open(data_path + filename, "w",encoding='utf-8') as f:
        json.dump({**json.loads(json_d), **param}, f)


if __name__ == '__main__':
    date = time.strftime("%Y-%m-%d", time.localtime())
    path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '\\allure-results\\' + date + "\\data\\test-cases"
