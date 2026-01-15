import os
from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse, FileResponse

app = FastAPI()

@app.post('/api/load_book/')
def load_book():
    f_path = r'data\response\response_1.txt'
    f_name = os.path.split(f_path)[-1]
    return FileResponse(
        path=f_path,
        media_type='text',
        filename=f_name
    )