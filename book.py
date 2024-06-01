from fastapi import FastAPI
from typing import Optional

app = FastAPI()

BOOKS = {
    'book_1': {'title':'Title One','author':'Author One'},
    'book_2': {'title':'Title two','author':'Author two'},
    'book_3': {'title':'Title three','author':'Author three'},
    'book_4': {'title':'Title four','author':'Author four'},
    'book_5': {'title':'Title five','author':'Author five'},
}

# Read Book Optional

@app.get('/')
async def Read_Book():
    return {'BOOKS':BOOKS}

        
@app.post('/')
async def Create_Book(book_name : str,book_author:str):
    current_book = 0
    for book in BOOKS:
        length = int(book.split('_')[-1])
        if length > current_book:
            current_book = length
    BOOKS[f'book_{current_book + 1}'] = {f'title':book_name,'author':book_author}
    book_create = BOOKS[f'book_{current_book + 1}']
    return {'New Book':book_create}

@app.delete('/')
async def Delete_book(book_title:str):
    del BOOKS[book_title]
    return BOOKS

@app.put('/')
async def Update(book_tittle:str,book_name:str,book_author:str):
    book_infromation = {'title':book_name,'author':book_author}
    BOOKS[book_tittle] = book_infromation
    return {'Update':BOOKS[book_tittle]}
