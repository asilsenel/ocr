import os
import platform
from tempfile import TemporaryDirectory
from pathlib import Path
import cv2
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

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

text_file = open('C:/Users/LENOVO/Desktop/atatürk ve kadın hakları/atatürk_ve_kadin.txt', 'w')


def main():
    with TemporaryDirectory() as tempdir:
        with open('out_text.txt', 'w') as output_file:
            text = str((pytesseract.image_to_string(Image.open(image_file))))
            text = text.replace("-\n", "")
            output_file.write(text)
            print(text)
            impath = 'C:/Users/LENOVO/PycharmProjects/ocr/' + file_name + ".jpg"
            image = cv2.imread(impath)
            cv2.imshow('image', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
