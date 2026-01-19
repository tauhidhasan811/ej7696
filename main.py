import os
from dotenv import load_dotenv
from fastapi import FastAPI, Form
from asset.hyperparameters import hyper
from fastapi.responses import JSONResponse, FileResponse
from asset.config.gen_model import LoadGenModel
from asset.core.clear_data import CleanData
from asset.core.prompts import GenQuestionPrompt#, GenBookPrompt

app = FastAPI()

load_dotenv()

model = LoadGenModel()

@app.post('/api/gen-question/')
async def generate_question(ex_name= Form(str), 
                            sheet_content=Form(str), 
                            knowledge_content=Form(str), 
                            n_question=Form(int)):
    try:
        prompt = GenQuestionPrompt(ex_name=ex_name, sheet_content=sheet_content, 
                            knowledge_content=knowledge_content, n_question=n_question)
        
        response = model.invoke(prompt).content
        response = CleanData(response)

        message = JSONResponse(
            status_code=200,
            content={
                'status': True,
                'status_code': 200,
                'text': response 
            }
        )
        return message
    
    except Exception as ex:
        message = JSONResponse(
            status_code=500,
            content={
                'status': False,
                'status_code': 500,
                'text': str(ex) 
            }
        )

        return message

"""
out_dir = hyper['output_dir']
os.makedirs(out_dir, exist_ok=True)

@app.post('/api/create-book/')
async def create_book(ex_name, sheet_content, knowledge_content):
    prompt = GenBookPrompt(ex_name=ex_name, sheet_content=sheet_content, 
                           knowledge_content=knowledge_content)
    
    try:
        response = model.invoke(prompt).content
        
        serial = len(os.listdir(out_dir))+1
        path = os.path.join(out_dir, f'response_{serial}.txt')
        with open(path, 'w') as file:
            file.write(response)
        
        message = JSONResponse(
            status_code=200,
            content={
                'status': True,
                'status_code': 200,
                'text': response
            }
        )
        return message
    
    except Exception as ex:
        message = JSONResponse(
            status_code=500,
            content={
                'status': False,
                'status_code': 500,
                'text': str(ex)
            }
        )
        return message


@app.get('/api/view-responses/')
async def gen_question():
    dirs = [os.path.join(out_dir, p) for p in os.listdir(out_dir)]

    print(dirs)
    response = []
    for d in dirs:
        with open(d, 'r') as f:
            data = f.read()
        response.append(data)


    message = JSONResponse(
        status_code=200,
        content={
            'status': True,
            'status_code': 200,
            'text': response
        }
    )

    return message


@app.post('/api/load_book/')
def load_book():
    f_path = r'data\response\response_1.txt'
    f_name = os.path.split(f_path)[-1]
    return FileResponse(
        path=f_path,
        media_type='text',
        filename=f_name
    )

"""