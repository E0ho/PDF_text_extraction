# pip install pypdf2
from PyPDF2 import PdfWriter, PdfReader
import os, errno

def split(directory, filename):
    inputpdf = PdfReader(open('./PDF_Data/' + filename, "rb"))

    try:
        os.makedirs(directory)

    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    for i in range(len(inputpdf.pages)):
        output = PdfWriter()
        output.add_page(inputpdf.pages[i])     

        with open(directory + "/%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)

if __name__ == "__main__":

    filename = "sample2.pdf"
    directory = "splitted/" + filename

    split(directory, filename)