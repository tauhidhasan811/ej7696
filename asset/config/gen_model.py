from langchain_google_genai.chat_models import ChatGoogleGenerativeAI

def LoadGenAI(model_name, temp):
    model = ChatGoogleGenerativeAI(
        model=model_name,
        temperacture = temp
    )
    return model