import datetime,function,indicator
import sys

Date=datetime.datetime.now().strftime("%Y%m%d")

Sid=sys.argv[1]
BrokerID='Capital'
OrderNum='1'

StartTime = datetime.datetime.strptime(Date+'09:00:00.00','%Y%m%d%H:%M:%S.%f')
EndTime = datetime.datetime.strptime(Date+'13:26:00.00','%Y%m%d%H:%M:%S.%f')

Index=0

for i in function.getSIDMatch(Date,Sid):
    time=datetime.datetime.strptime(Date+i[0],'%Y%m%d%H:%M:%S.%f')
    price=float(i[2])
    ask=float(i[5])
    bid=float(i[6])
    
    if time > StartTime:
            Index=1
            OrderTime=time
            OrderPrice=price
            #OrderInfo=Order(BrokerID,Sid,'B',bid,OrderNum,'0')
            #OrderPrice=OrderInfo[0][4]
            #OrderTime=datetime.datetime.strptime(OrderInfo[0][6],'%Y/%m/%d %H:%M:%S')
            print(OrderTime,"Order Buy Price:",OrderPrice,"Success!")
            break
         
for i in function.getSIDMatch(Date,Sid):
    time=datetime.datetime.strptime(Date+i[0],'%Y%m%d%H:%M:%S.%f')
    price=float(i[2])
    
    if time > EndTime:
            Index=0
            CoverTime=time
            CoverPrice=price
            #OrderInfo=Order(BrokerID,Sid,'S',bid,OrderNum,'3')
            #OrderPrice=OrderInfo[0][4]
            #OrderTime=datetime.datetime.strptime(OrderInfo[0][6],'%Y/%m/%d %H:%M:%S')
            print(CoverTime,"Cover Buy Price:",CoverPrice,"Success!")
            break     
