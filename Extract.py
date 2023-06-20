#This script extracts a character from images and saves in a text file
#Pre-requisites are pytesseract and PIL modules needed to be installed

from PIL import Image
import pytesseract
import glob

# we need to provide the location of the executable where tesseract is located

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#the below line extracts the required files from the desired folder
path = glob.glob("C:\\Work\\Obsolete\\*.jpg")

#In order to write the contents to the new file, create a new file 'file.txt'
with open('file.txt', 'w') as file:
  #iterate through the files that are present in the location indicated by 'path'
  for file_name in path:
    print(file_name)
    img = Image.open(file_name)
    print(img)
    text = pytesseract.image_to_string(img)
    print(text)

    #write the content to the text file
    file.write(text)
