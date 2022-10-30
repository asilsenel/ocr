import os
import platform
from tempfile import TemporaryDirectory
from pathlib import Path
import cv2
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import socket

HOST = "192.168.1.2"  # The server's hostname or IP address
PORT = 51692   # The port used by the server

if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )
    path_to_poppler_exe = Path(r"C:\Users\LENOVO\PycharmProjects\ocr\poppler-0.67.0\bin")
    out_directory = Path(r"~\PycharmProjects\ocr").expanduser()
else:
    out_directory = Path("~").expanduser()

file_name = input()
image_file = Path(file_name + ".jpg")

text = str((pytesseract.image_to_string(Image.open(image_file))))
text = text.replace("-\n", "")
text = bytes(text, 'utf-8')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(text)
    data = s.recv(1024)

print('Received', repr(data))
impath = 'C:/Users/LENOVO/PycharmProjects/ocr/' + file_name + ".jpg"
image = cv2.imread(impath)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
