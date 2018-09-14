import numpy as np
import pandas as pd
# df = pd.DataFrame({'1':np.random.rand(4),'2':np.random.rand(4),'3':np.random.rand(4)})
# insertrow = pd.DataFrame([[0,0,1]],columns=['1','2','3'])
# # above = df.iloc[:1]
# # below = df.iloc[1:]
# # new = above.append(insertrow,ignore_index=True).append(below,ignore_index=True)
# # print new
# df = pd.DataFrame({0:['1',2,3,4]})
# insert = 'sss'
# insertrow = pd.DataFrame([insert])
# # insert = 'sss'
# print list(df[0]).index('1')
# above = df.iloc[:1]
# below = df.iloc[1:]
# new = above.append(insertrow,ignore_index=True).append(below,ignore_index=True)
# print new
a= open('aaaa.csv','a')
a.write('aaaaaaaaaaaaaaaaaaaaa'+'\n')
a.close()