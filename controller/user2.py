from schemas.dummy import opdata1
from schemas.dummy import opdata2

################################################################################
#user dummy data 
users_db=[{"id":1,"name":"prince"},{"id":2,"name":"sachin"}]

#get all data funtion
def get_users():
    if not users_db:
        return "error"
    else:
        return users_db
##################################################################################






##################################################################################
# Get user data by id

def get_by_id(id):
    for i in users_db:
       if i["id"]==id:
          return i
    return "error"

###################################################################################






###################################################################################
#POST USER DATA

data_base=[]
def xyz(user):
    if not user:
      return "error"
    data_base.append(user)
    return user

####################################################################################




#######################################################################################
#DELETE USER BY ID

data=[{"id":1,"name":"sandeep"},{"id":2,"name":"mahak"}]
def deleteUser(id):
    for i in data:
        if i["id"]==id:
            data.remove(i)
        else:
            return "error"
########################################################################################       





#########################################################################################
#patch data

ug=[{"id":1,"name":"sandeep"},{"id":2,"name":"mahak"}]
def xyz2(id:int,changedata:opdata1):
    for i in ug:
        if i["id"]==id:
            if changedata.id is not None:
                i["id"]=changedata.id
            if changedata.name is not None:
                i["name"]=changedata.name
                return i
    return "error"  
#########################################################################################





#########################################################################################
#PUT FUNCTION
put_db=[{"name":"prince","village":"sdsd"},{"name":"sachin","village":"mangali"}]
def Pudata1(name:str,newdata:opdata2):
    for i in put_db:
        if i["name"]==name:
            if newdata.name is not None:
                i["name"]=newdata.name
            if newdata.village is not None:
                i["village"]=newdata.village
            
            return i
    return "error"
########################################################################################     