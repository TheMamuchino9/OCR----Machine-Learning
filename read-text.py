from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials

# Import a few utility libraries
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import os
import time

key = 'c25488f3e6a04fbab1be1bbb8302d2fd'
endpoint = 'https://udacity-cog-services-mamuchino9.cognitiveservices.azure.com/'

print('Ready to perform OCR using the Computer Vision service at "{}" using the key "{}."''"'.format(endpoint, key))
credentials = CognitiveServicesCredentials(key)
client = ComputerVisionClient(endpoint, credentials)


##Read text from images 

path = os.path.join('images', 'sign.jpg')
fig = plt.figure(figsize=(7, 7))

# Display the image with its extracted text inside bounding boxes
img = Image.open(path)
draw = ImageDraw.Draw(img)
with open(path, "rb") as stream:
    ocr = client.recognize_printed_text_in_stream(stream)

text = ''

for region in ocr.regions:
    for line in region.lines:
        # Read the OCR'ed text from each line
        for word in line.words:
            text += word.text + ' '

# Process the text one line at a time, drawing the appropriate bounding box
for region in ocr.regions:
    for line in region.lines:
        # Draw the bounding box for each line of text
        l,t,w,h = list(map(int, line.bounding_box.split(',')))
        draw.rectangle(((l,t), (l+w, t+h)), outline='magenta', width=5)


# Display the image with its extracted text
plt.axis('off')
plt.imshow(img)
fig.suptitle(text)
plt.show() 


###Read scanned documents####

path = os.path.join('images', 'diagnosis.jpg')

# Send an async request to read text within the image
with open(path, "rb") as stream:
    operation = client.read_in_stream(stream, raw=True)
    
# Extract the operation ID from the response headers
locationHeader = operation.headers["Operation-Location"]
operationId = locationHeader.split("/")[-1]

# Wait for the asynchronous operation to complete
while True:
    result = client.get_read_result(operationId)
    if result.status not in [OperationStatusCodes.running]:
        break
    time.sleep(1)

# When the operation has completed successfully, print each line of text returned to the output
if result.status == OperationStatusCodes.succeeded:
    for res in result.analyze_result.read_results:
        for line in res.lines:
            print(line.text)

# Display the image analyzed for comparision to the OCR'ed text results
print('\n')
fig = plt.figure(figsize=(12,12))
img = Image.open(path)
plt.axis('off')
plt.imshow(img)
plt.show()



###Read Handwritten Text###


# Read an image file into a stream
path = os.path.join('images', 'note.jpg')

# Send an async request to read text within the image
with open(path, "rb") as stream:
    operation = client.read_in_stream(stream, raw=True)
    
# Extract the operation ID from the response headers
locationHeader = operation.headers["Operation-Location"]
operationId = locationHeader.split("/")[-1]

# Wait for the asynchronous operation to complete
while True:
    result = client.get_read_result(operationId)
    if result.status not in [OperationStatusCodes.running]:
        break
    time.sleep(1)

# When the operation has completed successfully, print each line of text returned to the output
if result.status == OperationStatusCodes.succeeded:
    for res in result.analyze_result.read_results:
        for line in res.lines:
            print(line.text)

# Display the image analyzed for comparision to the OCR'ed text results
print('\n')
fig = plt.figure(figsize=(12,12))
img = Image.open(path)

plt.axis('off')
plt.imshow(img)
plt.show()






