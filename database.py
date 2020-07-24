
import pymysql


def exe_query(query,parms,i):
    connection = pymysql.connect(host="localhost", user="root", passwd="3490349", database="basketball")
    cursor = connection.cursor()
    courser=cursor.execute(query,parms)
    if(i==1):
        cursor.execute(query,parms)
        rows = cursor.fetchone()
        connection.commit()
        connection.close()
        return rows
    if(i==2):
        cursor.execute(query,parms)
        rows = cursor.fetchall()
        connection.commit()
        connection.close()
        return rows

    connection.commit()
    connection.close()

def create_user(users,passwords):
    exe_query("INSERT INTO user (name,lvl,lastgame,password,prepare,point,freind) VALUES (%s,1,'0',%s,0,-1,0)",(users,passwords,),0)

def search_user(users):
    same=exe_query("SELECT name FROM user WHERE name = %s",(users,),1)
    if(same):
        return True
    else:
        return False

def search_lvl(users):
    level=exe_query("SELECT * FROM user WHERE name=%s", (users,), 1)
    res=level[2]
    return res

def edit_lvl(users,i):
    level=exe_query("SELECT * FROM user WHERE name=%s", (users,), 1)
    res=level[2]
    if(i<0 and res==1):
        return
    res+=i

    exe_query("UPDATE user SET lvl=%s WHERE name=%s", (res,users,), 0)

def edit_lastgame(users,newvalue):
    exe_query("UPDATE user SET lastgame=%s WHERE name=%s", (newvalue,users,), 0)

def search_login(users,passwords):
    first=exe_query("SELECT * FROM user WHERE name = %s",(users,),1)
    #print(first)
    if(first[4]==passwords):
        return True
    else:
        return False

def search_id(user):
    id=exe_query("SELECT * FROM user WHERE name = %s",(user,),1)
    return id[0]

def show_user(id):
    user=exe_query("SELECT * FROM user WHERE id = %s",(id,),1)
    return user[1]

def prepare_game(user,parm):
    exe_query("UPDATE user SET prepare=%s WHERE name=%s", (parm,user,), 0)

def check_score(user):
    all=exe_query("SELECT * FROM user WHERE name = %s",(user,),1)
    score=all[6]
    if(score==-1):
        return -1
    else:
        return score
