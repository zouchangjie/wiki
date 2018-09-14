# coding=utf-8
import pandas as pd
import numpy as np


class Spider():
    n = 0
    filename1 = './data1/test' + str(n) + '.csv'
    data = pd.read_csv(filename1)
    # print file1
    data_all = pd.DataFrame(columns=[0])
    # list_all_file = open('./data2/all.csv','w')
    user_name = [""] * 2
    # print data.iloc[22,0]
    # ss = data.iloc[22,0]
    # if ss == '-':
    #     print  ###########
    # if ss == '-':
    #     print  ###########
    for i in range(len(data)):
        row = data.iloc[i,0]
        if i==0:
            row1 = data.iloc[i,0]
            name1 = row.split('(view source)')
            name2 = name1[1].split('(')
            user_name[0] = name2[0]
            row1 = data.iloc[i, 1]
            name1_2 = row.split('(view source)')
            name2_2 = name1[1].split('(')
            user_name[1] = name2[0]
        else:
            if pd.isnull(row):
                if data.iloc[i,1] == '+':
                    if not pd.isnull(data.iloc[i,2]):
                        aa = 'banben:2banben:user:'+str(user_name[1])+'user:'+str(data.iloc[i,2])
                        insertrow = pd.DataFrame([aa])

                        data_all=data_all.append(insertrow,ignore_index=True)
                        # list_all_file.write('banben:2banben:user:'+str(user_name[1])+'user:'+str(data.iloc[i,2])+'\n')
                    else:
                        print('sssss')
                        # list_all_file.write('nothing' + '\n')
                else:
                    if pd.isnull(data.iloc[i,1]):
                        print('sssss')

                        # list_all_file.write('nothing' + '\n')
                    else:
                        if data.iloc[i,1] == data.iloc[i,3]:
                            aa = 'banben:1banben:user:' + str(user_name[0]) + 'user:' + str(data.iloc[i, 1])
                            insertrow = pd.DataFrame([aa])
                            data_all = data_all.append(insertrow, ignore_index=True)
                            # list_all_file.write('banben:1banben:user:' + str(user_name[0]) + 'user:' + str(data.iloc[i, 1]) + '\n')
                        else:
                            print ('data.iloc[i,1] == data.iloc[i,3]bu deng')
            else:
                if row == "−":
                    aa = 'banben:2banben:user:' + str(user_name[1]) + 'user:' + str(data.iloc[i, 3])
                    insertrow = pd.DataFrame([aa])

                    data_all = data_all.append(insertrow, ignore_index=True)
                    # list_all_file.write('banben:2banben:user:' + str(user_name[1]) + 'user:' + str(data.iloc[i, 3]) + '\n')

                # if pd.isnull(data.iloc[i,2])&pd.isnull(data.iloc[i,3]):
                #     print str(data.iloc[i,0])+'&&'+str(data.iloc[i,1])
                else:
                    print (str(data.iloc[i, 0]) + '&&' + str(data.iloc[i, 1]))
                    # print 'pd.isnull(data.iloc[i,2])&&pd.isnull(data.iloc[i,3])bu wei kong'
    data_all.to_csv('./data2/all0.csv',encoding='utf-8',index=False,header=False)





        # for j in range(4):
        #     row = data.iloc[i, j]
        #
        #     if i == 0:
        #         if not pd.isnull(row):
        #             row = data.iloc[i, j]
        #             name1 = row.split('(edit)')
        #             name2 = name1[1].split('(')
        #             user_name = name2[0]
        #             user_time1 = name1[0].split('of')
        #             user_time = user_time1[1]
        #             list_all_file.write(str(user_name) + ',' + str(user_time) + '\n')
        #         else:
        #             break
        #     elif not pd.isnull(row):
        #         line = row.split(' ')
        #         if line[0] == 'Line':
        #             line1 = line.split(':')
        #             line_count = line1[0]
        #
        #             list_all_file.write(row + '\n')
        #         else:
        #             print 22
        #             # aa = np.isnan(row)pd.np.nan
        #             print 22


# print row
spider1 = Spider()
