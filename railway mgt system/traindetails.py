import mysql.connector



class details:
    def __init__ (self):
        self.conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password="1223456",
        database="railway"
        )

    def insertdetails(self,tno,src,dst,tname):
        self.cur=self.conn.cursor()
        self.cur.execute(f"INSERT INTO TRAIN_DETAILS VALUES({tno},'{src}','{dst}','{tname}')")
        self.conn.commit()
        print("Data has been inserted sucessfully")
    
    def trainnofetch(self):
        self.cur=self.conn.cursor()
        self.cur.execute('''select train_details.train_no from train_details 
                         left join
                        train_capacity 
                         on train_details.train_no=train_capacity.train_no
                         where ac_1 is null''')
        print(self.cur.fetchall())

    def trainnofetchroutes(self):
        self.cur=self.conn.cursor()
        self.cur.execute('''select train_details.train_no,train_details.source,train_details.destination from train_details 
                         left join
                        ROUTES 
                         on train_details.train_no=routes.train_no
                         where stop1 is null''')
        print(self.cur.fetchall())