import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('apikey')

lt=LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)

lt.set_service_url('url')

def englishToFrench(englishText):
    translation = lt.translate(text=englishText, model_id='en-fr').get_result()
    frenchText= translation['translations'][0]['translation']
    return frenchText

englishToFrench('Hello World')
    
def frenchToEnglish(frenchText):
    translation = lt.translate(text=frenchText, model_id='fr-en').get_result()
    englishText = translation['translation'][0]['translation']
    return englishText

frenchToEnglish('Bonjour')