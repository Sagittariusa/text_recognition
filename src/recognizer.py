import base64
import boto3
import io

from PIL import Image


def extract_text(image):
    textract_client = boto3.client('textract', region_name='eu-west-1')
    response = textract_client.detect_document_text(
        Document={
            "Bytes": image
        }
    )

    strings = []

    # Extract text from the response
    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            strings.append(item['Text'])

    return ' '.join(strings)


def read_image(img_string: str):
    img_string = img_string.split('base64,')[-1].strip()
    image_stream = io.BytesIO(base64.b64decode(img_string))
    image = Image.open(image_stream)
    image.save(image_stream, format='PNG')
    text = extract_text(image_stream.getvalue())

    return text
