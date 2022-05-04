from sklearn.feature_extraction.text import CountVectorizer
from pprint import pprint
import operator
import jieba
from extrect_absreact import encode_sen, cosin_distance, doc_list2str, MMR
from pdf2text import process
import os


if __name__ == '__main__':
    path = 'papers'
    all_file = list()
    for f in os.listdir(path):  # listdir返回文件中所有目录
        f_name = os.path.join(path, f)
        all_file.append(f_name)
    print(all_file)
    for file in all_file:
        if file[file.index('.'):] != '.pdf':
            continue
        docment = process(file)
        sen_list = docment.strip().split("。")
        # sen_list.remove("")
        doc_list = [jieba.lcut(i) for i in sen_list]
        corpus = [" ".join(i) for i in doc_list]

        # print(MMR(doc_list,corpus,1))
        sentence = MMR(doc_list, corpus, 1)[0]
        sentence = sentence.replace(" ", '')
        txt_name = file[:file.index('.')] + '.txt'
        f = open(txt_name, 'w', encoding='utf-8')
        f.write(sentence)
        f.close()
        dir_txt_path = path + '/files.txt'
        f = open(dir_txt_path, 'w')
        f.write(txt_name)
        f.close()
        print(sentence)
