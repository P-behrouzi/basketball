import pymysql

def freind_base(query,parms,i):
    mydb=pymysql.connect(host="localhost", user="root", password="3490349",database="basketball")
    cursor = mydb.cursor()
    #mycursor=mydb.cursor()
    courser=cursor.execute(query,parms)
    if(i==1):
        cursor.execute(query,parms)
        freind=cursor.fetchall()
        mydb.commit()
        mydb.close()
        return freind
    mydb.commit()
    mydb.close()



def show_freind(user_id):
    freind=freind_base("SELECT * FROM freind WHERE id=%s",(user_id,),1)
    return freind

def add_freind(userid,freindid):
    freind_base("INSERT INTO freind (id,freind_id) VALUES (%s,%s)", (userid,freindid,),0)

def repeat_freind(userid,freindid):
    freind=freind_base("SELECT * FROM freind WHERE id=%s", (userid,), 1)
    if(freind):
        for i in freind:
            if(i[1]==freindid):
                return -1
