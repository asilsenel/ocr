import os
import platform
from tempfile import TemporaryDirectory
from pathlib import Path
import cv2
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

_path = 'C:/Users/LENOVO/PycharmProjects/ocr/file'
_file = '/out_text.txt'
PDF_file = 'C:/Users/LENOVO/PycharmProjects/ocr/ytu/YTU_Ogrenci_Rehberi(1).pdf'


def ocrText(pdf,path,txtFile):
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
            pdf_pages = convert_from_path(PDF_file, 500)
        for page_enumeration, page in enumerate(pdf_pages, start=1):
            filename = f"{tempdir}\page_{page_enumeration:03}.jpg"
            page.save(filename, "JPEG")
            image_file_list.append(filename)
        with open('ytu/output.txt', 'w') as output_file:
            for image_file in image_file_list:
                text = str((pytesseract.image_to_string(Image.open(image_file))))
                text = text.replace("-\n", "")
                output_file.write(text)