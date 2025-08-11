from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI ()

#structure 1

class S1(BaseModel):
    id:int
    name:str     
    addhar_no:int
    father_name:str
    village:str


class updateitem(BaseModel):
    id:Optional[int]=None
    name:Optional[str]=None
    addhar_no:Optional[int]=None
    father_name:Optional[str]=None
    village:Optional[str]=None
    
#structure 2

class S2(BaseModel):
    name:str
    father_name:str
    age:int
