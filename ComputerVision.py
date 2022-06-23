# Importaciones
from array import *
from azure.cognitiveservices.vision.computervision import *
from azure.cognitiveservices.vision.computervision.models import *
from msrest.authentication import *
from PIL import *
import os, sys, time

from pyparsing import ParseSyntaxException

# Autenticación
subscription_key = ""
end_point = ""

# Iniciando cliente de computer vision
computer_vision_client = ComputerVisionClient(end_point, CognitiveServicesCredentials(subscription_key))

# Definien do imagen desde archivos
images_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

# Definiendo imagen desde enlace
url_remote = "URL"

# Obtener etiquetas
tags_result_remote = computer_vision_client.tag_image(url_remote)

# Validar obtención de etiquetas
if (len(tags_result_remote.tags) == 0):

    print("No hay etiquetas detectadas")

else:

    for tag in tags_result_remote.tags:

        print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))

print("Termina la prueba de Computer Vision")