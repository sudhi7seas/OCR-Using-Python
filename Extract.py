from PIL import Image
import pytesseract
import glob

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#print(pytesseract.image_to_string(Image.open('image1.jpg')))
#path = glob.glob("C:\\Users\\saptassu\\PycharmProjects1\\pythonProject_1\\*.jpg")
path = glob.glob("C:\\Work\\Obsolete\\*.jpg")
#directory = "C://Users/saptassu/PycharmProjects1/pythonProject_1"
#print(path)
with open('file.txt', 'w') as file:
    for file_name in path:
        #try:
        print (file_name)
        img = Image.open(file_name)
        print(img)
        text = pytesseract.image_to_string(img)
        print(text)

        file.write(text)
    #except Exception:
        #pass