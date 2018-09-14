import pandas as pd

data_all = pd.read_csv('./data3/array.csv', header=None)
list = []
for i in range(len(data_all)):
    for j in range(len(data_all)):
        if data_all.iloc[i,j] == 1:
          list.append([i,j])
          # list[i][1] = j

test = pd.DataFrame(data=list,columns=None)
# list.to_csv('./data3/array.csv', index=False, header=False, encoding='utf-8')
test.to_csv('./data3/array2.csv',index=False, header=False, encoding='utf-8')
# print(data_all)