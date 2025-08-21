from fastapi import APIRouter
from controller.user2 import get_users
from controller.user2 import get_by_id
from schemas.dummy import UserResponse
from schemas.dummy import UsersResponse
from schemas.dummy import XyzResponse
from controller.user2 import deleteUser
from schemas.dummy import SaveResponse
from schemas.dummy import SaveData
from controller.user2 import xyz
from schemas.dummy import patchres
from controller.user2 import xyz2
from schemas.dummy import opdata1
from schemas.dummy import Putresponse
from schemas.dummy import opdata2
from controller.user2 import Pudata1
router=APIRouter()


#################################################################
# GET USERS ALL DATA

@router.get("/users",response_model=UsersResponse) #endpiont or response
def get_xyz():    #make Fuction
    users=get_users()    #call function
    if users!="error":
        return {"msg":"ALL DATA SUCCESFULLY GET","data":users,"status_code":200}
    
    
################################################################    







#################################################################

#GET USER DATA BY ID 

@router.get("/user/{id}",response_model=UserResponse)
def xyz123(id:int):
    user1=get_by_id(id)
    if user1!="error":
        return {"msg":"YOUR DATA SUCESSFULLY GET","data":user1,"status_code":200}
    return {"msg":"YOUR ID NOT MATCH","data":None,"status_code":404}
#################################################################






#################################################################
#POST USER DATA


@router.post("/savedata",response_model=SaveResponse)
def post_data(user11:SaveData):
    new=xyz(user11)
    if new!="error":
        return {"msg":"POST YOUR DATA","data":new,"status_code":201}
    else:
        return{"msg":"","data":None,"status_code":404}
   
##################################################################  




##################################################################
# DELETE USER BY ID

@router.delete("/userremove/{id}",response_model=XyzResponse)
def del_by_id(id:int):
    user=deleteUser(id)
    if user!="error":
        return {"msg":"DELETE YOUR DATA","status_code":200}
    else:
       return {"msg":"NOT MATCH YOUR ID","status_code":404}
##################################################################





##################################################################

#PATCH DATA 
@router.patch("/patchdata/{id}",response_model=patchres)
def patch_data(id:int,changedata:opdata1):
    user=xyz2(id,changedata)
    if user!="error":
        return {"msg":"CHANGE YOUR DATA","data":user,"status_code":200}
    
    return {"msg":"NOT MATCH YOUR ID","data":None,"status_code":404}

###################################################################    








###################################################################
#PUT ROUTES
@router.put("/putnewdata/{name}",response_model=Putresponse)
def xyz12(name:str,newdata:opdata2):
        user=Pudata1(name,newdata)
        if user!="error":
            return {"msg":"put new data","data":user,"status_code":200}
        return {"msg":"id not matvh","data":None,"status_code":404}

#####################################################################