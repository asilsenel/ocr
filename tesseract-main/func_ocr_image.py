import os
import fitz
from tqdm import tqdm

workdirection = 'C:/Users/LENOVO/PycharmProjects/ocr/file'

def ocrImage(workdir):
    for each_path in os.listdir(workdir):
        if ".pdf" in each_path:
            doc = fitz.Document((os.path.join(workdir, each_path)))
            for i in tqdm(range(len(doc)), desc="pages"):
                for img in tqdm(doc.get_page_images(i), desc="page_images"):
                    xref = img[0]
                    image = doc.extract_image(xref)
                    pix = fitz.Pixmap(doc, xref)
                    pix.save(os.path.join(workdir + "/pics", "%s_p%s-%s.jpg" % (each_path[:-4], i, xref)))