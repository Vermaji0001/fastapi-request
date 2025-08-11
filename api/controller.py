from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from app.schemas.dummy import S1
from app.schemas.dummy import updateitem
from app.schemas.dummy import S2
app = FastAPI()




# 1 # user get spacific data

#User dummy data
user_db=[{"id":1,"name":"prince","addhar_no":12345,"father_name":"vijender","village":"kharar alipur hisar"},
         {"id":2,"name":"sachin","addhar_no":54321,"father_name":"maharana tersem","village":"mangali"}] 
@app.get("/getuser/{id}",response_model=S1)
def getuser(id:int):
    for i in user_db:
        if i["id"]==id:
            return i








# Get all data
db=[{"id":1,"name":"prince","addhar_no":12345,"father_name":"vijender","village":"kharar alipur hisar"},
         {"id":2,"name":"sachin","addhar_no":54321,"father_name":"maharana tersem","village":"mangali"}] 
@app.get("/getall")
def getall():
    return db
    









#task

xyz_db=[{"id":1,"name":"prince","addhar_no":12345,"father_name":"vijender","village":"kharar alipur hisar"},
         {"id":2,"name":"sachin","addhar_no":54321,"father_name":"maharana tersem","village":"mangali"}] 
@app.patch("/patch/{id}",response_model=S1)
def xyz(id:int,changedata:updateitem):
    for i in xyz_db:
        if i["id"]==id:
            if changedata.id is not None:
                i["id"]=changedata.id
            if changedata.name is not None:
                i["name"]=changedata.name
            if changedata.addhar_no is not None:
                i["addhar_no"]=changedata.addhar_no
            if changedata.father_name is not None:
                i["father_name"]=changedata.father_name
            if changedata.village is not None:
                i["village"]=changedata.village
            return i                







# Post user data

data_save=[]
@app.post("/post",response_model=S2)
def post_data(user:S2):
    data_save.append(user)
    return user









# delete data

data_base=[{"name":"sandeep","school":"sd"},{"name":"sachin","school":"pd"}]
@app.get("/delete1/{name}")
def deletedata(name:str):
    for i in data_base:
        if i["name"]==name:
            data_base.remove(i)
        return data_base






#task

dummy1=[{"id":1,"name":"jatin"},{"id":2,"name":"vineet"}]


class User(BaseModel):
    id: int
    name: str

@app.get("/user/{id}",response_model=User)
def get_user_by_id(id: int):
    for user in dummy1:
        if user["id"] == id:
            return user
        



#task 
        