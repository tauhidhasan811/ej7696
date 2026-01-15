"""from asset.core.prompts import GenBookPrompt

prompt = GenBookPrompt()

print(prompt)
"""

from dotenv import load_dotenv
from asset.config.gen_model import LoadGenAI

load_dotenv()

model = LoadGenAI(model_name='gemini-2.5-flash')

resp = model.invoke('hi')

print(resp.content)