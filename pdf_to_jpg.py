# pip install wand
# ImageMagick 설치 
# - https://docs.wand-py.org/en/latest/guide/install.html#install-imagemagick-on-windows 
# - https://imagemagick.org/script/download.php#windows

from wand.image import Image
import os, errno

def pdf_to_jpg(input_file, output_dir):

    try:
        os.makedirs(output_dir)

    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    with Image(filename = input_file, resolution=300) as img:

        img.format = 'jpg'

        for i, page in enumerate(img.sequence):
            with Image(page) as single_page:
                output_file = f"{output_dir}/page_{i+1}.jpg"
                single_page.save(filename = output_file)


if __name__ == "__main__":

    pdf_file = "business-report-template-04.pdf"      # 변경하고 싶은 PDF 경로

    input_path = "PDF_Data/" + pdf_file # 입력할 PDF 파일 경로
    output_path = "PDF2JPG/" + pdf_file  # 출력할 JPG 이미지 저장 디렉토리 경로

    pdf_to_jpg(input_path, output_path)

