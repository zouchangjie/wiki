# coding=utf-8
import pandas as pd
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class Spider1():


    array_all = [[0] * 5600 for i in range(5600)]
    array_all[1][0] = 1
    for n in range(2,5600):
        # n = 1
        m = 0
        filename = './data1/test' + str(n-1) + '.csv'
        data = pd.read_csv(filename)
        # print file1
        dat_all = './data2/all' + str(n-2) + '.csv'
        data_all = pd.read_csv(dat_all, sep='\n', header=None,encoding='utf-8')
        user_name = [""] * 2
        banben = [""] * 2
        for i in range(len(data)):
            row = data.iloc[i, 0]
            if i == 0:
                row1 = data.iloc[i, 1]
                name1 = row.split('(view source)')
                name2 = name1[1].split('(')
                user_name[0] = name2[0]
                banben[0] = n+1
            else:
                if not pd.isnull(row):
                    line1 = row.split(':')
                    line2 = line1[0].split(' ')
                    if line2[0] == 'Line':
                        line_count = line2[1]
                        # m = int(line_count) - 1
                    else:
                        #  i!=0 row!=nan
                        if row == '−':
                            #- （） + ()
                            if data.iloc[i, 2] == '+':
                                # if pd.isnull(data.iloc[i, 1])&pd.isnull(data.iloc[i, 3]):

                                if pd.isnull(data.iloc[i, 1])&pd.isnull(data.iloc[i, 3]):
                                    # - nan nan nan
                                    print('- nan + nan   can pass')
                                else:
                                    #- nan + data
                                    if pd.isnull(data.iloc[i, 1])&(not pd.isnull(data.iloc[i, 3])):
                                        #insert - nan + data
                                        array_all[int(banben[0]) - 1][int(banben[0]) - 2] = 1
                                        # insert1 = data.iloc[i,3]
                                        insert = 'banben:' + str(banben[0]) + 'banben:user:' + str(
                                            user_name[0]) + 'user:' + str(data.iloc[i, 3])
                                        insertrow = pd.DataFrame([insert])
                                        above = data_all.iloc[:m]
                                        below = data_all.iloc[m:]
                                        data_all = above.append(insertrow, ignore_index=True).append(below,
                                                                                                     ignore_index=True)
                                    else:
                                        if (not pd.isnull(data.iloc[i, 1]))&(not pd.isnull(data.iloc[i, 3])):
                                            #- data1 + data2
                                            #  i!=0  - +
                                            data_texy = data.iloc[i,1]

                                            m = 0
                                            while True:
                                                # index = data_all.query(0 == data_texy)
                                                while True:

                                                    data_all1 = data_all.iloc[m, 0]
                                                    if data_all.iloc[m,0] == 'nothing':
                                                        m= m + 1
                                                    else:
                                                        break
                                                data_all1 = data_all.iloc[m, 0]
                                                # print(data_all1)
                                                user1 = data_all1.split('user:')
                                                data_text_1 = user1[2]
                                                if data_texy == data_text_1:
                                                    print('okokok')
                                                    banben1 = data_all1.split('banben:')
                                                    banben[1] = banben1[1]
                                                    # review version line
                                                    array_all[int(banben[0]) - 1][int(banben[1]) - 1] = 1
                                                    #recover
                                                    data_all.iloc[m, 0] = 'banben:' + str(banben[0]) + 'banben:user:' + str(user_name[0]) + 'user:' + str(data.iloc[i, 3])
                                                    break
                                                else:
                                                    m = m + 1
                                                if m>=len(data_all):
                                                    print('- () + ()   not find error!!!')
                                                    file_error0 = open("./errordata/errorurl.csv", 'a')
                                                    file_error0.write(filename + '   ' + dat_all + '\n')
                                                    file_error0.write(str(data.iloc[i, 0]) + '   ' + str(data.iloc[i, 1]) + '   ' + str(data.iloc[i, 2]) + '   ' + str(data.iloc[i, 3]) + '   ' + dat_all + '\n')
                                                    file_error0.close()
                                                    break
                                        else:
                                            if (not pd.isnull(data.iloc[i, 1]))&(pd.isnull(data.iloc[i, 3])):
                                                #- data + nan  delete  data.iloc[i, 1]
                                                data_texy = data.iloc[i, 1]
                                                m = 0
                                                while True:
                                                    # while True:
                                                    #     # data_all2 = data_all.iloc[m, 0]
                                                    #     if data_all.iloc[m, 0] == 'nothing':
                                                    #         m = m + 1
                                                    #     else:
                                                    #         break
                                                    data_all2 = data_all.iloc[m, 0]
                                                    user2 = data_all2.split('user:')
                                                    data_text_2 = user2[2]
                                                    if data_texy == data_text_2:
                                                        banben1 = data_all2.split('banben:')
                                                        banben[1] = banben1[1]
                                                        # review version line
                                                        array_all[int(banben[0]) - 1][int(banben[1]) - 1] = 1
                                                        data_all.drop([m])
                                                        # m = m - 1
                                                        break
                                                    else:
                                                        m = m + 1

                                                    if m >= len(data_all):
                                                        # - nan nan nan
                                                        print('- data + nan  data not find  so error!!!')

                                                        file_error0 = open("./errordata/errorurl.csv", 'a')
                                                        file_error0.write(filename + '   ' + dat_all + '\n')
                                                        file_error0.write(str(data.iloc[i, 0]) + '   ' + str(
                                                            data.iloc[i, 1]) + '   ' + str(
                                                            data.iloc[i, 2]) + '   ' + str(
                                                            data.iloc[i, 3]) + '   ' + dat_all + '\n')
                                                        file_error0.close()
                                                        file_error0.close()
                                                        # print('error ver err   pass')
                                                        break
                                            else:
                                                print('(not pd.isnull(data.iloc[i, 1]))&(pd.isnull(data.iloc[i, 3]))) - () + ()  error!!!')
                                                file_error0 = open("./errordata/errorurl.csv", 'a')
                                                file_error0.write(filename + '   ' + dat_all + '\n')
                                                file_error0.write(
                                                    str(data.iloc[i, 0]) + '   ' + str(data.iloc[i, 1]) + '   ' + str(
                                                        data.iloc[i, 2]) + '   ' + str(
                                                        data.iloc[i, 3]) + '   ' + dat_all + '\n')
                                                file_error0.close()

                            else:
                                #- ( ) data[i,2]!=+
                                if pd.isnull(data.iloc[i,2]):

                                    # - ( ) data[i,2]=nan
                                    data_texy = data.iloc[i, 1]
                                    if pd.isnull(data.iloc[i,1]):
                                        # - nan nan nan
                                        print('- nan nan nan   can pass')
                                        # print('error ver err   pass')
                                    else:
                                        m = 0
                                        while True:
                                            # while True:
                                            #     # data_all2 = data_all.iloc[m, 0]
                                            #     if data_all.iloc[m, 0] == 'nothing':
                                            #         m = m + 1
                                            #     else:
                                            #         break
                                            data_all2 = data_all.iloc[m, 0]
                                            user2 = data_all2.split('user:')
                                            data_text_2 = user2[2]
                                            if data_texy == data_text_2:
                                                banben1 = data_all2.split('banben:')
                                                banben[1] = banben1[1]
                                                # review version line
                                                array_all[int(banben[0]) - 1][int(banben[1]) - 1] = 1
                                                data_all.drop([m])
                                                # m = m-1
                                                break
                                            else:
                                                m = m + 1

                                            if m >= len(data_all):
                                                #- nan nan nan

                                                print('- data nan nan   can pass m >= len(data_all): not find so error!!!')
                                                file_error0 = open("./errordata/errorurl.csv", 'a')
                                                file_error0.write(filename + '   ' + dat_all + '\n')
                                                file_error0.write(
                                                    str(data.iloc[i, 0]) + '   ' + str(data.iloc[i, 1]) + '   ' + str(
                                                        data.iloc[i, 2]) + '   ' + str(
                                                        data.iloc[i, 3]) + '   ' + dat_all + '\n')
                                                file_error0.close()
                                                # print('error ver err   pass')
                                                break
                                else:
                                    print('-  +  data.iloc[i,2] not the same and not nan  so error!!')
                        else:
                            print('data.iloc[i, 0] not - and nan so error!!')
            #data.iloc[i, 0] is nan
                else:
                    # data.iloc[i, 0] [i,1] is nan
                    if pd.isnull(data.iloc[i,1]):
                        print('shi nan nan  do not do pass')

                    else :
                    # data.iloc[i, 0] is nan [i,1] is not nan
                        if data.iloc[i, 1] == '+':

                            if pd.isnull(data.iloc[i,2])&pd.isnull(data.iloc[i,3]):
                                print('shi nan + nan  nan do not do can pass')
                                #nan + nan nan
                                #insert nothing
                                # array_all[int(banben[0]) - 1][int(banben[0]) - 2] = 1
                                # insert = 'nothing'
                                # insertrow = pd.DataFrame([insert])
                                # above = data_all.iloc[:m]
                                # below = data_all.iloc[m:]
                                # data_all = above.append(insertrow, ignore_index=True).append(below, ignore_index=True)

                            #nan + data nan
                            else:
                                #nan + data nan
                                if not pd.isnull(data.iloc[i,2]):
                                    ##insert data.iloc[i,2]
                                    array_all[int(banben[0]) - 1][int(banben[0]) - 2] = 1
                                    # insert1 = data.iloc[i,2]
                                    insert = 'banben:' + str(banben[0]) + 'banben:user:' + str(user_name[0]) + 'user:' + str(data.iloc[i, 2])
                                    insertrow = pd.DataFrame([insert])
                                    above = data_all.iloc[:m]
                                    below = data_all.iloc[m:]
                                    data_all = above.append(insertrow, ignore_index=True).append(below,ignore_index=True)
                                    # m = m + 1
                            # insert data.iloc[i,3]
                                else:
                                    print('insert data.iloc[i,2] error')
                        else:
                            #data.iloc[i, 0] is nan [i,1] is not nan and not + mean clound data
                            if pd.isnull(data.iloc[i,2])&(not pd.isnull(data.iloc[i,3])):
                                print('nan data nan data the same can pass')
                                m = m + 1
                            else:
                                print('nan data nan nan so error !!!')

        filename1 = './data2/all' + str(n-1) + '.csv'

        data_all.to_csv(filename1, index=False, header=False,encoding='utf-8')
        print (n)

    data_array = pd.DataFrame(array_all)
    data_array.to_csv('./data3/array.csv', index=False, header=False, encoding='utf-8')


spider1 = Spider1()

#############################
#
# dataframe 格式 中 一直指针每次操作都会向下一次，比如插入，修改，替换这些，
# 但指针调向下一行就会报错，但版本插入还没循环玩，怎么办，指针回一直往下跳


#
#     for i in range(len(data)):
#         row = data.iloc[i,0]
#         if i==0:
#             row1 = data.iloc[i,0]
#             name1 = row.split('(edit)')
#             name2 = name1[1].split('(')
#             user_name[0] = name2[0]
#             row1 = data.iloc[i, 1]
#             name1_2 = row.split('(edit)')
#             name2_2 = name1[1].split('(')
#             user_name[1] = name2[0]
#         else:
#             if pd.isnull(row):
#                 if data.iloc[i,1] == '+':
#                     if not pd.isnull(data.iloc[i,2]):
#                         list_all_file.write('banben:2banben:user:'+str(user_name[1])+'uer:'+str(data.iloc[i,2])+'\n')
#                     else:
#                         list_all_file.write('nothiong' + '\n')
#                 else:
#                     if pd.isnull(data.iloc[i,1]):
#                         list_all_file.write('nothiong' + '\n')
#                     else:
#                         if data.iloc[i,1] == data.iloc[i,3]:
#                             list_all_file.write('banben:1banben:user:' + str(user_name[0]) + 'uer:' + str(data.iloc[i, 1]) + '\n')
#                         else:
#                             print 'data.iloc[i,1] == data.iloc[i,3]bu deng'
#             else:
#                 if row == "−":
#                     print ###########
#                     list_all_file.write('banben:2banben:user:' + str(user_name[1]) + 'uer:' + str(data.iloc[i, 3]) + '\n')
#
#                 # if pd.isnull(data.iloc[i,2])&pd.isnull(data.iloc[i,3]):
#                 #     print str(data.iloc[i,0])+'&&'+str(data.iloc[i,1])
#                 else:
#                     print str(data.iloc[i, 0]) + '&&' + str(data.iloc[i, 1])
#                     # print 'pd.isnull(data.iloc[i,2])&&pd.isnull(data.iloc[i,3])bu wei kong'
#
#
#
#
#
#         # for j in range(4):
#         #     row = data.iloc[i, j]
#         #
#         #     if i == 0:
#         #         if not pd.isnull(row):
#         #             row = data.iloc[i, j]
#         #             name1 = row.split('(edit)')
#         #             name2 = name1[1].split('(')
#         #             user_name = name2[0]
#         #             user_time1 = name1[0].split('of')
#         #             user_time = user_time1[1]
#         #             list_all_file.write(str(user_name) + ',' + str(user_time) + '\n')
#         #         else:
#         #             break
#         #     elif not pd.isnull(row):
#         #         line = row.split(' ')
#         #         if line[0] == 'Line':
#         #             line1 = line.split(':')
#         #             line_count = line1[0]
#         #
#         #             list_all_file.write(row + '\n')
#         #         else:
#         #             print 22
#         #             # aa = np.isnan(row)pd.np.nan
#         #             print 22
#
#
# # print row

