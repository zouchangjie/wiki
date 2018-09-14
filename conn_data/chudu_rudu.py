# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# filie = pd.read_csv('./array_data/array.csv', header=None)
#截取前2000版本
# a = filie.ix[:, 0:1999]
# a.to_csv('./array_data/array_2000.csv', index=None)
# print 22
# for i in range(len())
# row_sum = filie.apply(sum)
# print 11
# for i in range(len(filie)):


filie = pd.read_csv('./array_data/array_2000.csv')
row_sum = filie.apply(sum)#chudu
row_sum = row_sum.values
filie_T = filie.T
hang_sum2 = filie_T.apply(sum)#rudu
hang_sum2 = hang_sum2.values
# aa = hang_sum2[0]
file = open('./array_data/churudu_2000.csv', 'w')
file.write('出度' + ',' + '入度' + '\n')
for i in range(len(filie)):
    file.write(str(row_sum[i]) + ',' + str(hang_sum2[i]) + '\n')
file.close()
print 22
