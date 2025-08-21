from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from typing import List

app = FastAPI ()





#############################################################################

#USERS SCHEMAS       # use schemas for get all data
class Users123(BaseModel):
      id:int
      name:str
#  USERS RESPONSE SECHEMAS   #use schemas for get all data
class UsersResponse(BaseModel) :
   msg: str
   status_code:int
   data: Optional[List[Users123]]

################################################################################





################################################################################

#USER RESPONSE SCHEMAS   #use schemas for get by id

class UserResponse(BaseModel) :
   msg: str
   status_code:int
   data: Optional[Users123]

#################################################################################





#################################################################################

# #POST SCHEMAS

class SaveData(BaseModel):
    name:str
    age:int
class SaveResponse(BaseModel):
    msg:str
    status_code:int
    data:Optional[SaveData]

##################################################################################






##################################################################################

#DELETE USER BY ID SCHEMAS

class Xyz(BaseModel):
    id:int
    name:str

class XyzResponse(BaseModel):
    msg:str 
    status_code:int

###################################################################################





####################################################################################

#patch data
class Patchdata(BaseModel):
    id:int
    name:str
class opdata1(BaseModel):
    id:Optional[int]=None
    name:Optional[str]=None    
class patchres(BaseModel):
    msg:str
    status_code:int
    data:Optional[Patchdata]    

########################################################################################






########################################################################################
#PUT SCHEMAS
class Putdata(BaseModel):
    name:str
    village:str
class opdata2(BaseModel):
    name:str=None
    village:str=None  
        
class Putresponse(BaseModel):
    msg:str
    status_code:int
    data:Optional[Putdata]    
###########################################################################################    