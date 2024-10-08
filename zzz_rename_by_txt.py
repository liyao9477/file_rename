#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 10:33:47 2024

@author: boyly
"""

# -*- coding: UTF-8 -*-
import traceback
import locale
import os
import re
import sys
import time

version = 'v1.0.1'
Action_Get_List = False
Action_Rename_File = True
file_list = []
rename_list = []
exe_path, exe_name = os.path.split(sys.argv[0])
if exe_path:
    os.chdir(exe_path)
else:
    exe_path = ''
print('path:',exe_path)
pattern = re.compile(r'(\d+|[^\d]+)')
pattern2 = re.compile(r'\d+')


def str2key(mystr):
    split_str = pattern.findall(mystr)
    key_bytes = b''
    for ele in split_str:
        if pattern2.findall(ele):
            num_key = int(ele)
            key_bytes += num_key.to_bytes(8, byteorder='big', signed=False)
        else:
            key_bytes += locale.strxfrm(ele).encode(encoding='utf-8')
    return key_bytes


def get_file_list():
    global file_list
    file_list = os.listdir(exe_path)
    if exe_name in file_list:
        file_list.remove(exe_name)
    file_list = sorted(file_list, key=str2key)
    if 'zzz_list.txt' in file_list:
        file_list.remove('zzz_list.txt')
        return Action_Rename_File
    else:
        return Action_Get_List


def write_list_file(m_list):
    with open('zzz_list.txt', 'w', encoding='utf-8') as f:
        for file in m_list:
            f.write(file + '\n')


def read_list_file():
    global rename_list
    with open('zzz_list.txt', 'r', encoding='utf-8') as f:
        rename_list = f.read()
        rename_list = rename_list.split('\n')
        if '' in rename_list:
            rename_list.remove('')


def main():
    global file_list, rename_list
    # print('version: {}'.format(version))
    locale.setlocale(locale.LC_ALL, locale='zh_cn')
    if Action_Rename_File == get_file_list():
        read_list_file()
        if len(rename_list) == len(file_list):
            for i in range(0, len(rename_list)):
                os.rename(file_list[i], rename_list[i])
            write_list_file(sorted(rename_list, key=str2key))
            print('文件重命名完成, 并自动更新zzz_list.txt目录排序')
        else:
            print('文件数量与目录不匹配, 请删除zzz_list.txt再重新运行程序')
    elif Action_Get_List == get_file_list():
        print('已生成目录文件zzz_list.txt, 修改目录并重新执行程序即可重命名文件')
        write_list_file(file_list)


if __name__ == '__main__':
    startTimes = time.time()
    main()
    endTimes = time.time()
    times = endTimes - startTimes
    print('共耗时：' + repr(times) + '秒')

