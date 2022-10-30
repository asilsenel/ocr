import os
import platform
from tempfile import TemporaryDirectory
from pathlib import Path
import fitz
from tqdm import tqdm
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

workdir = 'C:/Users/LENOVO/Desktop/atatürk ve kadın hakları'

if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )
    path_to_poppler_exe = Path(r"C:\Users\LENOVO\PycharmProjects\ocr\poppler-0.67.0\bin")
    out_directory = Path(r"~\PycharmProjects\ocr").expanduser()
else:
    out_directory = Path("~").expanduser()
PDF_file = 'C:/Users/LENOVO/Desktop/atatürk ve kadın hakları/atatürk ve kadın hakları.pdf'
image_file_list = []
text_file = open('C:/Users/LENOVO/Desktop/atatürk ve kadın hakları/atatürk_ve_kadin.txt', 'w')


def main():
    with TemporaryDirectory() as tempdir:
        if platform.system() == "Windows":
            pdf_pages = convert_from_path(
                PDF_file, 500, poppler_path=path_to_poppler_exe
            )
        else:
            pdf_pages = convert_from_path(PDF_file, 500)
        for page_enumeration, page in enumerate(pdf_pages, start=1):
            filename = f"{tempdir}\page_{page_enumeration:03}.jpg"
            page.save(filename, "JPEG")
            image_file_list.append(filename)
        with open('atatürk ve kadın hakları/atatürk_ve_kadin.txt', 'w') as output_file:
            for image_file in image_file_list:
                text = str((pytesseract.image_to_string(Image.open(image_file))))
                text = text.replace("-\n", "")
                output_file.write(text)


if __name__ == "__main__":
    main()
