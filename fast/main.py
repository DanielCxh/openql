# -*- coding:utf-8 -*-
from typing import List,Set,Dict
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import HTTPException
import uvicorn

from pydantic import Json, BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static") # 挂载静态文件，指定目录
templates = Jinja2Templates(directory="templates") # 模板目录


# 创建数据模型
class Item(BaseModel):
    df: Dict

@app.get("/")
async def read_data(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/data/{data}")
async def read_data(request: Request, data: str):
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

@app.get("/hello")
async def hello(request: Request):
    return templates.TemplateResponse("hello.html", {"request": request, "mydata": "xxx1"})

@app.post("/bar")
async def read_item(name : str, time : str):
    print("{} {}".format(name, time))
    return {"foo": "1", "age": "2", "name": "3"}

@app.post("/jsoned")
async def get_json(item:Item):
    df = {"title":"TITLE!","lst":[1,2,3,4,5]}
    # print(item.df)
    print(item.dict())
    return {"data":df}

@app.exception_handler(Exception)
async def unicorn_exception_handler(request: Request, exc: Exception):
    return templates.TemplateResponse("404.html", {"request": request})


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)