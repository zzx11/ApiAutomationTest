"""
操作数据库，进行数据增删改
"""
import sys

sys.path.append('../DataBase')
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB

# create data
datas = {
    'student2': [
        {'id': 1, 'name': '测试1', 'age': 2000},
        {'id': 2, 'name': '测试2', 'age': 0},
        {'id': 3, 'name': '测试3', 'age': 2000},
        {'id': 4, 'name': '测试4', 'age': 2000},
        {'id': 5, 'name': '测试5', 'age': 2000},
    ],
}


# Inster table datas
def init_data():
    DB().init_data(datas)


def clear_data():
    DB().clear('ds_webservice')


if __name__ == '__main__':
    init_data()
