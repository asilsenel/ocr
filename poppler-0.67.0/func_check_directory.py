import os

# path of the directory
directoryPath = "C:/Users/LENOVO/PycharmProjects/ocr/file"
fileName = "/output.txt"
imageFolder = "/pics"

def checkOCR(path, file, imageF):
    checkImage = None
    checkText = None
    if os.listdir(path+imageF):
        print("No images")
        checkImage = False
    else:
        print("Images exist")
        checkImage = True
    if os.stat(path + file).st_size == 0:
        print("Text file empty")
        checkText = False
    else:
        print("Text file is not empty")
        checkText = True

    if checkText or checkImage:
        print("OCR Process is done successfully!")
    else:
        print("OCR Process error.")


checkOCR(directoryPath)
