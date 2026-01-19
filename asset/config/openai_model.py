from langchain_openai import ChatOpenAI

def LoadOpenAIModel(model_name='gpt-4', temp=1.0):
    model = ChatOpenAI(
        model=model_name,
        temperature=temp
    )
    return model 