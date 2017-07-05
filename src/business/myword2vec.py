#encoding:utf-8
from gensim.models  import  Word2Vec
import logging
import os
import jieba
from src.audit.stopword import StopWord
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


file_path = r'G:\aa'
class MyFiles(object):

    def __init__(self, filepath):

        import re
        self.filepath = filepath
        self.zhongwen = re.compile('[\u4e00-\u9fa5]+')
        self.stopword = StopWord()

    def __iter__(self):

        for file in os.listdir(self.filepath):
            if not file.endswith('txt'):
                continue

            filepath = os.path.join(self.filepath,file)
            with open(filepath,'r',encoding='utf-8') as f:
                mark = True
                for line in f:

                    if mark:
                        mark = False
                        continue
                    line = line.rstrip('\n').rstrip('\r')
                    array = line.split(",")
                    content = array[5]
                        
                    seg_list = jieba.cut(array[5],cut_all=False)

                    content = [ self.zhongwen.findall(x) for x in seg_list ]
                    content = [x[0] for x in content if x ]
                    content = filter(lambda x:not self.stopword.is_stop_word(x),content)
                 
                    yield list(content)

def main():

    file_path = r'G:\aa'
    my_files = MyFiles(file_path)

    for line in my_files:
        print(','.join(my_files))

    model = Word2Vec(my_files,size=100,window=5, min_count=2, workers=4)

    model.save('myword2vec.model')
    # model = Word2Vec.load('myword2vec.model')


if __name__ == '__main__':
    a = MyFiles(file_path)
    for line in a:
        print(line)