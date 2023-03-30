from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    return {'data': f'{limit} blog list {published}'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': "all unpublished blogs"}


@app.get('/blog/{id}')
def about(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id: int, limit=10):
    return {'data': '123'}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return request


# if __name__ == '__main__':
#     uvicorn.run(app,host='127.0.0.1',port=9000)