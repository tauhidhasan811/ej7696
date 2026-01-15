from langchain_core.prompts import PromptTemplate
from langchain.messages import SystemMessage, HumanMessage, AIMessage

def PromptGenBook():
    sys_message = SystemMessage(
        content=""
    )

    hum_message = HumanMessage(
        content=""
    )

    temp = PromptTemplate(
        template="{sys_message}\n\nCodes: {hum_meesage}",
        input_variables=['sys_message', 'hum_message']
    )

    prompt = temp.invoke(
        input={
            'sys_message': sys_message,
            'hum_message': hum_message
        }
    )