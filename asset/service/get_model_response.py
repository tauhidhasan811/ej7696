from asset.core.prompts import GenQuestionPrompt
from asset.core.clear_data import CleanData
from asset.core.process_gemi3_response import get_text

def GetModelResponse(model, ex_name, sheet_content, 
                     knowledge_content, n_question):
    
    prompt = GenQuestionPrompt(ex_name=ex_name, sheet_content=sheet_content, 
                            knowledge_content=knowledge_content, n_question=n_question)
        
    response = model.invoke(prompt).content

    if model.model.startswith('gemini-3'):
            response = get_text(response)
        
    response = CleanData(response)

    return response