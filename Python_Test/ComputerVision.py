import io
import json
from unittest import result
from msrest.authentication import *
from azure.cognitiveservices.vision.computervision import *
from azure.cognitiveservices.vision.computervision.models import *
import requests
from PIL import Image, ImageFont

credential = json.load(open('Credential.json'))

API_KEY = credential['API_KEY']
ENDPOINT = credential['ENDPOINT']
SUBS_KEY = credential['SUBS_KEY']

cv_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))

domain = 'zorro'
image_url = 'https://docs.microsoft.com/en-us/azure/synapse-analytics/machine-learning/media/tutorial-computer-vision-use-mmlspark/dog.jpg'
anaylisis = cv_client.analyze_image_by_domain(model=domain, url=image_url)