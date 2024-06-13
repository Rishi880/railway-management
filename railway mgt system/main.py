#importing required modules
from traindetails import details
from traincapacity import capacity
from routes import routs
from booking import book
import numpy as np

print("-------------wecome to Railway management system------------")
print('--------for inserting the data enter-1--------')
print('--------for reading the data enter-2--------')
print('--------for updating the data enter-3--------')
print('--------for delating the data enter-4--------')


opr=int(input("please enter your operation"))
if opr==1:
    print("---For inserting the data in traindetails press-1---")
    print("---For inserting the data in traincapacity press-2---")
    print("---For inserting the data in routs press-3---")
    print("---For Booking a ticket press-4---")
    inopr=int(input("please select an operation"))
    if inopr==1:
        obj=details()
        tno=int(input("Please enter train no:"))
        src = input("Please Enter Source station:")
        dst= input("Please enter Destination station:")
        tname = input("Please enter train name:")
        obj.insertdetails(tno,src,dst,tname)
    if inopr==2:
        obj=capacity()
        obj1=details()
        obj1.trainnofetch()
        trn=int(input("please enter train number:"))
        ac1=int(input("please enter capacity of AC 1:"))
        ac2=int(input("please enter capacity of AC 2:"))
        ac3=int(input("please enter capacity of AC 3:"))
        sl=int(input("please enter capacity of sleeper class:"))
        gen=int(input("please enter capacity general class:"))
        obj.capacityinsert(trn,ac1,ac2,ac3,sl,gen)
    if inopr==3:
        obj=routs()
        obj1=details()
        obj1.trainnofetchroutes()
        trn=(input("please enter train number:"))
        st1=(input("please enter stop 1:"))
        st2=(input("please enter stop 2:"))
        st3=(input("please enter stop 3:"))
        st4=(input("please enter stop 4:"))
        obj.routsinsert(trn,st1,st2,st3,st4)
    if inopr==4:
        source = input("From: ")
        dest = input('To: ')
        obj = book()
        obj.trainfetch(source,dest)
        trainno = int(input("Please Enter Trainno: "))
        cls = input("Please Enter your Coach: ")
        #passenger info
        pid = int(input("Please Enter your Id:"))
        pname = input("Please Enter Your Name:")
        age = int(input("Please Enter your Age:"))
        gen = input("Please Enter your Gender:")
        mn = int(input("Please Enter your mobile no:"))
        obj.addpassenger(pid,pname,age,gen,mn)
        # making Transaction
        tid = int(input("Please Enter Id:"))
        amount = int(input("please Enter amount:"))
        mode = input("Please Enter Payment Mode: ")
        obj.addtransaction(tid,pid,amount,mode)
        # booking ticket
        bid = np.random.randint(0,500000,1)[0]
        stno = np.random.randint(0,50,1)[0]
        obj.bookticket(bid,pid,cls,stno,tid,source,dest,trainno)




# if opr==2:
#     pass
# if opr==3:
#     pass
# if opr==4:
#     pass
