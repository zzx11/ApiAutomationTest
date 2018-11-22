"""
读取excel用例数据
"""
import os

import xlrd

path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
pd = path_dir + '\\Files\\'
def get_data(file_name):
    dir_case = pd + file_name
    data = xlrd.open_workbook(dir_case)
    table = data.sheets()[0]
    nor = table.nrows
    nol = table.ncols
    info_list = []
    for i in range(1, nor):
        info_dic = {}
        for j in range(nol):
            title = table.cell_value(0, j)
            value = table.cell_value(i, j)
            info_dic[title] = value
        info_list.append(info_dic)
    return info_list

def get_data_list(file_name):
    dir_case = pd +file_name
    data = xlrd.open_workbook(dir_case)
    table = data.sheets()[0]
    nor = table.nrows
    nol = table.ncols
    info_list = []
    for i in range(1, nor):
        info_dic = []
        for j in range(nol):
            if j == 9:
                continue
            else:
                info_dic.append(table.cell_value(i, j))
        info_list.append(info_dic)
    return info_list


if __name__ == '__main__':
    print(pd)
    print(get_data_list('iwherelink.xlsx'))
