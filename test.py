"""from asset.core.prompts import GenBookPrompt

prompt = GenBookPrompt()

print(prompt)
"""

"""from dotenv import load_dotenv
from asset.config.gen_model import LoadGenAI

load_dotenv()

model = LoadGenAI(model_name='gemini-2.5-flash')

resp = model.invoke('what is transformer?? explain within five line')

print(resp.content)"""

import os
from random import random
from dotenv import load_dotenv
from asset.core.prompts import GenBookPrompt
from asset.config.gen_model import LoadGenAI

load_dotenv()

model = LoadGenAI(model_name='gemini-2.5-flash')



ex_name='API 510 - Pressure Vessel Inspector',
sheet_content=('FOR: September 2025, January 2026, and May 2026'
                '- API 510, Pressure Vessel Inspection Code: In-service Inspection, Rating, Repair, and Alteration, 11th Edition, October 2022, Errata 1 (March 2023)'
                '- API Recommended Practice 571, Damage Mechanisms Affecting Fixed Equipment in the Refining Industry, 3rd edition, March 2020 (Sections: 2, 3.3, 3.8, 3.9, 3.11, 3.14, 3.15, 3.17, 3.22, 3.27, 3.35, 3.36, 3.37, 3.46, 3.61, 3.67)'
                '- API Recommended Practice 572, Inspection Practices for Pressure Vessels, 5th Edition, November 2023.'
                '- API Recommended Practice 576, Inspection of Pressure-relieving Devices, 5th Edition, September 2024'
                '- API Recommended Practice 577, Welding Processes, Inspection, and Metallurgy, 3rd Edition, October 2020.'
                '- API Recommended Practice 578, Material Verification Program for New and Existing Assets, 4th edition, February 2023'
                '- ASME, Boiler and Pressure Vessel Code, 2023 Edition:'
                    ' - Section V, Nondestructive Examination, Articles 1, 2, 6, 7 and 23 (Section SE-797 only)'
                    '- Section VIII, Rules for Construction of Pressure Vessels, Division 1; Introduction (U), UG, UW, UCS, Appendices 1-4, 6, 8, and 12'
                    ' - Section IX, Qualification Standard for Welding, Brazing, and Fusing Procedures; (Welding only)'
                '- ASME PCC-2, Repair of Pressure Equipment and Piping, 2022 (Articles: 101, 201, 202, 209, 210, 211, 212, 215, 216, 304, 305, 312, 501, 502)))')


knowledge_content=('API Authorized Pressure Vessel Inspectors must have a broad knowledge base relating to maintenance, inspection, repair, and alteration of pressure vessels. The examination is designed to determine if individuals have such knowledge.'
                        'I. THICKNESS MEASUREMENTS, INSPECTION INTERVALS AND VESSEL INTEGRITY: Corrosion Rates and Inspection Intervals, Joint Efficiencies, Static Head, Internal Pressure, External Pressure, Pressure Testing, Impact Testing, Weld Size for Attachment Welds at Openings, Nozzle Reinforcement.'
                        'II. WELDING PROCEDURE AND QUALIFICATION EVALUATION: Based on ASME Section IX, including Weld Procedure Review (WPS, PQR, WPQ) and general welding requirements from ASME Section VIII, Div. 1 and API 510. Welding processes limited to SMAW, GTAW, GMAW, SAW. Base metals limited to P-No. 1, 3, 4, 5, and 8.'
                        'III. NONDESTRUCTIVE EXAMINATION: Based on ASME Section V, including Article 1 (General), Article 2 (Radiography), Article 6 (Liquid Penetrant), Article 7 (Magnetic Particle - Yoke and Prod only), Article 23 (Ultrasonic Thickness - SE-797 only).'
                        'IV. PRACTICAL KNOWLEDGE - GENERAL & SPECIFIC: Requirements from API 510, API RP 571 (specified sections), API RP 572, API RP 576, API RP 577, API RP 578, and ASME PCC-2 (specified articles).')
 




prompt = GenBookPrompt(ex_name=ex_name, sheet_content=sheet_content, knowledge_content=knowledge_content)

#print(prompt)

#path = 'data/text_file'
path = 'data/response'
os.makedirs(path, exist_ok=True)

serial = len(os.listdir(path=path))

f_path = os.path.join(path, f"response_{serial+1}.txt")
resp = model.invoke(prompt)


                       
print(resp.content)

with open(f_path, 'w') as file:
    file.write(resp.content)