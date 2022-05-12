# 处理两列式pdf
from PIL import Image
import os
import pytesseract
import cv2 as cv
import fitz
from extrect_absreact import encode_sen, cosin_distance, doc_list2str, MMR
import jieba

def pdf_image(pdfPath,imgPath,zoom_x,zoom_y,rotation_angle):
    # 打开PDF文件
    pdf = fitz.open(pdfPath)
    # 逐页读取PDF
    for pg in range(0, pdf.pageCount):
        page = pdf[pg]
        # 设置缩放和旋转系数
        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotation_angle)
        pm = page.getPixmap(matrix=trans, alpha=False)
        # 开始写图像
        pm.writePNG(imgPath+str(pg)+".png")
        pathes.append(imgPath+str(pg)+".png")
        #pm.writePNG(imgPath)
    pdf.close()


if __name__ == '__main__':
    pathes = []
    pdf_path = 'papers/test2.pdf'
    img_path = 'papers/papers_imgs/test2_'
    txt_path = pdf_path[:-4] + '.txt'
    pdf_image(pdf_path, img_path, 5, 5, 0)
    for path in pathes:
        # 依赖opencv
        img = cv.imread(path)
        print(img)
        # text = pytesseract.image_to_string(Image.fromarray(img), lang='chi_tra')
        text = pytesseract.image_to_string(Image.fromarray(img), lang='chi_sim')
        f = open(txt_path, 'a')
        text = text.replace(' ', '')
        text = text.replace('\n', '')
        f.write(text)
        # 不依赖opencv写法
        # text=pytesseract.image_to_string(Image.open(img_path))
        print(text)
        f.close()
    f = open(txt_path, 'r')
    text = ""
    for s in f.readlines():
        text += str(s)
    
    # print(text)
    # sen_list = text.strip().split("。")
    # doc_list = [jieba.lcut(i) for i in sen_list]
    # corpus = [" ".join(i) for i in doc_list]
    # sentence = MMR(doc_list, corpus, 1)[0]
    # sentence = sentence.replace(" ", '')
    # print(sentence)
        