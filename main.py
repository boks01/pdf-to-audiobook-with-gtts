from typing import Text
import PyPDF2
from gtts import gTTS
import os

pdf_path = "files/the_pdf.pdf"

def convert_pdf_to_text(pdf_path):
    with open(pdf_path, "rb") as f:
        pdf = PyPDF2.PdfFileReader(f)
        pages_num = pdf.getNumPages()
        page = pdf.getPage(pages_num-1)
        plane_text = page.extractText()
    text = []

    for i in plane_text:
        if i == "\n":
            pass
        else:
            text.append(i)

    text = "".join(text)

    return text

speech_obj = gTTS(text=convert_pdf_to_text(pdf_path), lang="en", slow=False)
speech_obj.save("files/result.mp3")
os.system("mpg321 files/result.mp3")

