import os
from os.path import exists
import platform
from tempfile import TemporaryDirectory
from pathlib import Path
import fitz
from tqdm import tqdm
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import socket

# ethernet
_s = socket.socket()  # Create a socket object
host = "192.168.2.11"  # Get local machine name
port = 51728

# function pass values
directoryPath = "C:/Users/LENOVO/PycharmProjects/ocr"
fileName = "/output.txt"
folderName = "file"
imageFolder = "/pics"
PDF_file = 'C:/Users/LENOVO/PycharmProjects/ocr/000-579e-5.0.pdf'


# functions
def receiveFile(s, _host, _port):
    s.bind((_host, _port))  # Bind to the port
    f = open('000-579e-5.0.pdf', 'wb')
    s.listen(5)
    while True:
        c, addr = s.accept()  # Establish connection with client.
        print('Got connection from', addr)
        print("Receiving...")
        l = c.recv(1024)
        while l:
            print("Receiving...")
            f.write(l)
            l = c.recv(1024)
        f.close()
        print("Done Receiving")
        # c.send('Thank you for connecting')
        c.close()
        break


def checkOCR(path, file, imageF):
    checkImage = None
    checkText = None
    if os.listdir(path + "/file"+ imageF):
        print("Images exist")
        checkImage = True
    else:
        print("No images")
        checkImage = False
    if os.stat(path + "/file" + file).st_size == 0:
        print("Text file empty")
        checkText = False
    else:
        print("Text file is not empty")
        checkText = True

    if checkText or checkImage:
        print("OCR Process is done successfully!")
        return True
    else:
        print("OCR Process error.")
        return False


def ocrImage(workdir):
    for each_path in os.listdir(workdir):
        if "000-579e-5.0.pdf" in each_path:
            print("PDF File is ready for OCR Image.")
            doc = fitz.Document((os.path.join(workdir, each_path)))
            for i in tqdm(range(len(doc)), desc="pages"):
                for img in tqdm(doc.get_page_images(i), desc="page_images"):
                    xref = img[0]
                    image = doc.extract_image(xref)
                    pix = fitz.Pixmap(doc, xref)
                    pix.save(os.path.join(workdir + "/file/pics/", "%s_p%s-%s.jpg" % (each_path[:-4], i, xref)))
            print("PDF File processing.")


def ocrText(pdf, path, folder, txtFile):
    image_file_list = []
    if platform.system() == "Windows":
        pytesseract.pytesseract.tesseract_cmd = (
            r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        )
        path_to_poppler_exe = Path(r"C:\Users\LENOVO\PycharmProjects\ocr\poppler-0.67.0\bin")
        out_directory = Path(r"~\PycharmProjects\ocr").expanduser()
    else:
        out_directory = Path("~").expanduser()
    with TemporaryDirectory() as tempdir:
        if platform.system() == "Windows":
            pdf_pages = convert_from_path(
                pdf, 500, poppler_path=path_to_poppler_exe
            )
        else:
            pdf_pages = convert_from_path(pdf, 500)
        for page_enumeration, page in enumerate(pdf_pages, start=1):
            filename = f"{tempdir}\page_{page_enumeration:03}.jpg"
            page.save(filename, "JPEG")
            image_file_list.append(filename)
        with open(folder + txtFile, 'w') as output_file:
            for image_file in image_file_list:
                text = str((pytesseract.image_to_string(Image.open(image_file))))
                text = text.replace("-\n", "")
                output_file.write(text)
            print("Text file is processed.")


receiveFile(_s, host, port)  # receive pdf file
file_exists = exists(PDF_file)
if file_exists:
    print("File exists.")
    ocrImage(directoryPath)
    ocrText(PDF_file, directoryPath, folderName, fileName)

checkOCR(directoryPath, fileName, imageFolder)
