from __future__ import print_function
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="keyfile.json"
from google.cloud import vision

def detect_text(path):
    """Detects text in the file."""
    import io
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    # print('Texts:')
    testing = '\n"{}"'.format(texts[0].description)
    #for text in texts:
     #   print('\n"{}"'.format(text.description))

       # vertices = (['({},{})'.format(vertex.x, vertex.y)
       #              for vertex in text.bounding_poly.vertices])

        #print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    return testing
text123 = detect_text(r"essay.png")
print(text123)