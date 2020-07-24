from database import *
import time
#from LoginSignup import *
list2_player=[]
list4_player=[]
list44_player=[]
def search_prepare(parms):
    list_lvl_user=[]
    player=exe_query("SELECT * FROM user WHERE prepare=%s ", (parms,), 2)
    return player
    #list_lvl_user.append(player[2])
    #list_lvl_user.append(player[1])
    #exe_query("UPDATE user SET prepare=0 WHERE name=%s ", (player[1],), 0)
    return list_lvl_user
def search(parms):
    player=exe_query("SELECT * FROM user WHERE prepare=%s ", (parms,), 1)
    if(player):
        return -1
def search_friend(parms):
    freind=exe_query("SELECT * FROM user WHERE name=%s", (parms[1],), 1)
    if(freind[7]==parms[0]):
        return True
    else:
        return False
def prepare_for_friend(parms):
    exe_query("UPDATE user SET freind=%s WHERE name=%s",(parms[1],parms[0],),0)
def end_prepare(parms):
    exe_query("UPDATE user SET freind=0 WHERE name=%s",(parms,),0)
def clear_prepare(user):
    exe_query("UPDATE user SET prepare=0 WHERE name=%s ", (user,), 0)


dictionary_2=[]
def game_2player():
    global dictionary_2
    temp_list=[]
    count=0
    #lvl_list=list(dictionary_2.keys())
    new_player=search_prepare(2)
    #print(new_player)
    #for i in range(len(dictionary_2)):
        #if(lvl_list[i]==new_player[0]):
            #temp_list.append(new_player[1])
            #temp_list.append(dictionary_2[lvl_list[i]])
            #del dictionary_2[lvl_list[i]]
            #list2_player.append(temp_list)
            #count+=1
            #break
    for s in range(len(new_player)):

        if(dictionary_2):
            for player in new_player:
                #print(player)
                for i in range(len(dictionary_2)):
                    if(dictionary_2[i][0]==player[2]):
                        if(dictionary_2[i][1]==player[1]):
                            break
                        dictionary_2[i].append(player[1])
                        #count+=1
                        #print(dictionary_2)
                        break
                for i in range(len(dictionary_2)):
                    if(len(dictionary_2[i])==3):
                        time.sleep(3)
                        del dictionary_2[i][0]
                        for u in dictionary_2[i]:
                            clear_prepare(u)
                        list2_player.append(dictionary_2[i])
                        del dictionary_2[i]
                        break
        if(count==0):
            for player in new_player:
                #print(player)
                temp=[player[2],player[1]]
                dictionary_2.append(temp)
                #print(dictionary_2)
                break
            count+=1

        #dictionary_2.update({new_player[0]:new_player[1]})
    #else:
        #count-=1
dictionary_4=[]
def game_4player():
    global dictionary_4
    temp_list=[]
    new_player=search_prepare(4)
    count=0
    for s in range(len(new_player)):
        if(dictionary_4):
            for player in new_player:
                repeat=0
                for i in range(len(dictionary_4)):
                    if(dictionary_4[i][0]==player[2]):
                        for s in range(len(dictionary_4[i])):

                            if(dictionary_4[i][s]==player[1]):
                                repeat+=1
                                break
                        #if(dictionary_44[i][2]):
                            #if(dictionary_44[i][2]==player[1]):
                                #break
                        #if(dictionary_44[i][3]):
                            #if(dictionary_44[i][3]==player[1]):
                                #break
                        if(repeat==0):
                            dictionary_4[i].append(player[1])
                            #print(dictionary_44)
                            count+=1
                        break
                for i in range(len(dictionary_4)):
                    if(len(dictionary_4[i])==5):
                        del dictionary_4[i][0]
                        time.sleep(8)
                        for u in dictionary_4[i]:
                            clear_prepare(u)
                        list4_player.append(dictionary_4[i])
                        del dictionary_4[i]
                        #break
        if(count==0):
            for player in new_player:
                #print(player)
                temp=[player[2],player[1]]
                dictionary_4.append(temp)
                #print(dictionary_2)
                break
            count+=1
    #count-=1
dictionary_44=[]
def game_44player():
    global dictionary_44
    temp_list=[]
    new_player=search_prepare(44)
    count=0

    for s in range(len(new_player)):
        if(dictionary_44):
            #print("1")
            for player in new_player:
                repeat=0
                for i in range(len(dictionary_44)):
                    if(dictionary_44[i][0]==player[2]):
                        for s in range(len(dictionary_44[i])):

                            if(dictionary_44[i][s]==player[1]):
                                repeat+=1
                                break
                        #if(dictionary_44[i][2]):
                            #if(dictionary_44[i][2]==player[1]):
                                #break
                        #if(dictionary_44[i][3]):
                            #if(dictionary_44[i][3]==player[1]):
                                #break
                        if(repeat==0):
                            dictionary_44[i].append(player[1])
                            #print(dictionary_44)
                            count+=1
                        break
                for i in range(len(dictionary_44)):
                    if(len(dictionary_44[i])==5):
                        del dictionary_44[i][0]
                        time.sleep(8)
                        for u in dictionary_44[i]:
                            clear_prepare(u)
                        list44_player.append(dictionary_44[i])
                        del dictionary_44[i]
                        break
        if(count==0):
            for player in new_player:
                #print(player)
                temp=[player[2],player[1]]
                dictionary_44.append(temp)
                #print(dictionary_2)
                break
            count+=1
        #count-=1
def game_freind(user):
    time_out=time.time()+60*2
    prepare_for_friend(user)
    freind_ready=0
    while(True):
        ready=search_friend(user)
        if(ready or time.time()>time_out):
            freind_ready=1
            break
    if(freind_ready==1):
        end_prepare(user[0])
        return True
    else:
        end_prepare(user[0])
        return False

def match_user2(user):
    global list2_player
    #time_out=time.time()+30
    #while(True):
        #print(list2_player)
        #if(time.time()>time_out):
            #player=-1
            #break
    if(len(list2_player)==0):
        player=-1
    else:
        for i in list2_player:
            if(i[0]==user):
                player=i
                break
            elif(i[1]==user):
                player=i
                break
        #if(player):
            #break
    if(player==-1):
        count=0
        for i in dictionary_2:
            if user in i:
                del dictionary_2[count]
                break
        count+=1
        return -1
    else:
        count=0
        time.sleep(5)
        for i in list2_player:
            if(i[0]==user):
                del list2_player[count]
                break
            elif(i[1]==user):
                del list2_player[count]
                break
            count+=1
        return player

def match_user4(user):
    global list4_player
    #time_out=time.time()+60*2
    #while(True):
        #if(time.time()>time_out):
            #player=-1
            #break
    if(len(list4_player)==0):
        player=-1
        #continue
    else:
        for i in list4_player:
            if(i[0]==user):
                player=i
                break
            if(i[1]==user):
                player=i
                break
            if(i[2]==user):
                player=i
                break
            if(i[3]==user):
                player=i
                break
            #if(player):
                #break
    if(player==-1):
        count=0
        for i in dictionary_4:
            if user in i:
                del dictionary_4[count]
                break
            count+=1
        return -1
    else:
        time.sleep(3)
        count=0
        for i in list4_player:
            if user in i:
                del list4_player[count]
                break
            count+=1
        return player
def match_user44(user):
    global list44_player
    #time_out=time.time()+60*2
    #while(True):
        #if(time.time()>time_out):
            #player=-1
            #break
    if(len(list44_player)==0):
        player=-1
        #continue
    else:
        for i in list44_player:
            if(i[0]==user):
                player=i
                break
            if(i[1]==user):
                player=i
                break
            if(i[2]==user):
                player=i
                break
            if(i[3]==user):
                player=i
                break
            #if(player):
                #break
    if(player==-1):
        count=0
        for i in dictionary_44:
            if user in i:
                del dictionary_44[count]
                break
            count+=1
        return -1
    else:
        time.sleep(3)
        count=0
        for i in list44_player:
            if user in i:
                del list44_player[count]
                break
            count+=1
        return player
def action_find(stop):
        #stop2=search(2)
        #stop4=search(4)
        #stop44=search(44)
    if(stop==2):
        game_2player()
    elif(stop==4):
        game_4player()
    elif(stop==44):
        game_44player()
