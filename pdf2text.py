import pdfplumber
import pandas as pd
import re


def process(path):
    with pdfplumber.open(path) as pdf:
        content = ''
        for i in range(len(pdf.pages)):
            # 读取PDF文档第i+1页
            page = pdf.pages[i]

            # page.extract_text()函数即读取文本内容，下面这步是去掉文档最下面的页码
            page_content = '\n'.join(page.extract_text().split('\n')[:-1])
            content = content + page_content
    content = content.replace('\n', '')
    content = content.replace(' ', '')
    ret = re.match(r"(.*)摘要(.*)", content)
    docment = ret.group(2)
    return docment
