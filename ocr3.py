import platform
from pathlib import Path

import pytesseract
from PIL import Image

if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )

    out_directory = Path(r"~\PycharmProjects\ocr").expanduser()
else:
    out_directory = Path("~").expanduser()

# file_name = input()
image_file = Path("tire.jpg")

text_file = open('C:/Users/LENOVO/PycharmProjects/ocr/out_text.txt', 'w')


def main():
    with open('out_text.txt', 'w') as output_file:
        text = str((pytesseract.image_to_string(Image.open(image_file))))
        text = text.replace("-\n", "")
        last_index = 0
        vehicle_type = ""
        section_width = ""
        aspect_ratio = ""
        radial_construction = ""
        rim_diameter = ""
        load_index = ""
        speed_index = ""

        for i in range(last_index, len(text)):
            if text[i].isalpha():
                vehicle_type += text[i]
                last_index += 1
            elif not text[i].isalpha():
                break

        if not text[i].isnumeric() and not text[i].isalpha():
            last_index += 1

        for i in range(last_index, len(text)):
            if text[i].isnumeric():
                section_width += text[i]
                last_index += 1
            elif not text[i].isnumeric():
                break

        if not text[i].isnumeric() and not text[i].isalpha():
            last_index += 1

        for i in range(last_index, len(text)):
            if text[i].isnumeric():
                aspect_ratio += text[i]
                last_index += 1
            elif not text[i].isnumeric():
                break

        if not text[i].isnumeric() and not text[i].isalpha():
            last_index += 1

        for i in range(last_index, len(text)):
            if text[i].isalpha():
                radial_construction += text[i]
                last_index += 1
            elif not text[i].isalpha():
                break

        if not text[i].isnumeric() and not text[i].isalpha():
            last_index += 1

        for i in range(last_index, len(text)):
            if text[i].isnumeric():
                rim_diameter += text[i]
                last_index += 1
            elif not text[i].isnumeric():
                break

        if not text[i].isnumeric() and not text[i].isalpha():
            last_index += 1

        for i in range(last_index, len(text)):
            if text[i].isnumeric():
                load_index += text[i]
                last_index += 1
            elif not text[i].isnumeric():
                break

        for i in range(last_index, len(text)):
            if text[i].isalpha():
                speed_index += text[i]
                last_index += 1
            elif not text[i].isalpha():
                break

        if not text[i].isnumeric() and not text[i].isalpha():
            last_index += 1

        output_file.write(text)
        output_file.write("\nvehicle_type: " + vehicle_type)
        output_file.write("\nsection_width: " + section_width)
        output_file.write("\naspect_ratio: " + aspect_ratio)
        output_file.write("\nradial_construction: " + radial_construction)
        output_file.write("\nrim_diameter: " + rim_diameter)
        output_file.write("\nload_index: " + load_index)
        output_file.write("\nspeed_index: " + speed_index)


if __name__ == "__main__":
    main()
