import pytesseract
from PIL import Image
image = Image.open('5bd25bc8a5a5f.jpg')


result_text = pytesseract.image_to_string(image)
print(result_text)