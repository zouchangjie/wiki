import pandas as pd
import numpy as np

n = 0
filename1 = './data1/test' + str(n) + '.csv'
data = pd.read_csv(filename1)
# print file1
list_all_file = open('./data2/all.csv','w')
for i in range(len(data)):
    row = data.iloc[0]
    for j in range(len(row)):
        row = data.iloc[i, j]

        if i == 0:
            if not pd.isnull(row):
                row = data.iloc[i, j]
                name1 = row.split('(edit)')
                name2 = name1[1].split('(')
                user_name = name2[0]
                user_time1 = name1[0].split('of')
                user_time = user_time1[1]
                list_all_file.write(str(user_name) + ',' + str(user_time) + '\n')
            else:
                break
        elif not pd.isnull(row):
            line = row.split(' ')
            if line[0] == 'Line':
                line1 = line[1].split(':')
                line_count = line1[0]

                print 22
                # aa = np.isnan(row)pd.np.nan
                print 22
            else:
                list_all_file.write(row + '\n')

        elif pd.isnull(row):
            list_all_file.write('\n')

print row
