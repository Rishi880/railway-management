import mysql.connector



class book:
    def __init__ (self):
        self.conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password="1223456",
        database="railway"
        )

    def trainfetch(self,src,dest):
        cur=self.conn.cursor()
        cur.execute(f'''select routes.train_no,source,stop1,stop2,stop3,stop4,destination
                    from routes inner join train_details on
                    routes.train_no=train_details.train_no
                    where source='{src}' OR STOP1='{src}' OR STOP2='{src}' OR STOP3='{src}' 
                    OR STOP4='{src}';''')
        dt= cur.fetchall()
        try:
            tr=[]
            for i in dt:
               for j in i[i.index(src)+1:]:
                   if j==dest:
                      tr.append(i)
        except:
            pass
        print(tr)
    
    def addpassenger(self,pid,pname,age,gen,mn):
        self.cur = self.conn.cursor()
        self.cur.execute(f"INSERT INTO PASSENGERS VALUES({pid},'{pname}',{age},{mn},'{gen}')")
        self.conn.commit()
        print("Passenger added sucessfully")
    def addtransaction(self,tid,pid,amount,mode):
        self.cur = self.conn.cursor()
        self.cur.execute(f"INSERT INTO TRANSACTIONS VALUES({tid},{pid},{amount},'{mode}')")
        self.conn.commit()
        print("Transaction Sucessfull")
    def bookticket(self,bid,pid,cls,stno,tid,source,dest,traino):
        self.cur = self.conn.cursor()
        self.cur.execute(f"INSERT INTO BOOK_TICKETS VALUES({bid},{pid},'{cls}',{stno},{tid},'{source}','{dest}',{traino})")
        self.conn.commit()
        print("****************** TICKET HAS BEEN BOOKED ******************")
        print("PID         ====>",pid)
        print("SEAT NO     ====>",stno)
        print("BID         ====>",bid)
        print("CLASS       ====>",cls)
        print("SOURCE      ====>",source)
        print("DESTINATION ====>",dest)
        print("TRAIN NO    ====>",traino)
        print("TRAIN ID    ====>",tid)