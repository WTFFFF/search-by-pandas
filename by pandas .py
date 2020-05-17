import pandas as pd

path = r'C:\Users\付昌\Desktop\search\test.xlsx'  #文件路径
data = pd.DataFrame(pd.read_excel(path))    #读取数据，创建DataFrame对象
consignor = '江春'    #委托人信息，有输入框给定
ordernumber = 's'    #委托单号，由输入框给定

#获取委托人一列中，内容为‘XX’的所在行的相应信息并且订单编号为xxx的相应信息
information = (data['委托人'] == '王可心')&(data['订单编号'] == 'GHW202001130002')    #需要筛选的信息
result = data.loc[information,['订单编号','样品名称','生产厂家','车型','到样日期','检测项目','预计完成时间','试验状态']]    #只选择information值为True的那些行，并且只选择所需要的的列
print (result)
Show = result.unstack() #将输出值行列转置显示
print (Show)






