from PIL import Image
import sys, pytesseract

im = Image.open(sys.argv[1])
print im
vcode = pytesseract.image_to_string(im)
print vcode
