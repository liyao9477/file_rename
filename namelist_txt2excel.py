#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 10:53:55 2024

@author: boyly
"""

# coding=utf-8
import xlwt
import time

startTimes = time.time()
content = './list.txt'
f = open(content, "r")  
book=xlwt.Workbook(encoding='gbk',style_compression=0)
sheet=book.add_sheet('Sheet',cell_overwrite_ok=True)
i = 0
while True:  
	line = f.readline()  
	if line:  
		pass    
		strl = line.strip()
		sline = strl.split('|')
		j=0
		for sdata in sline:
			sheet.write(i,j,sdata)
			j=j+1
		i=i+1
	else:  
		break
f.close()
# save_addr = raw_input("Please enter a save address &name: ").strip()
save_addr = './list.xlsx'
book.save(save_addr)

endTimes = time.time()
times = endTimes - startTimes
print('共耗时：' + repr(times) + '秒')