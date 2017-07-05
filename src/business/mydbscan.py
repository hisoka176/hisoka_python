#encoding:utf-8

import sklearn.cluster import DBSCAN
from dictionary import Dictionary
import numpy as np

class MyDbscan(object):

    def __init__(self,eps=0.5,min_samples=20,metric='jaccard',algorithm='brute'):
        self.eps = eps
        self.min_samples = min_samples
        self.metric = metric
        self.algorithm = algorithm

    def generate_numpy(self,content,x,y):
        array = np.array((x,y),dtype=np.int8)
        for i,index in enumerate(content):

            for v in index:
                array[i,v] = 1

        return array

    def generate_array(self):
        
        content = list()
        dictionary = Dictionary()
        for index,line in dictionary:
            content.append(index)

        x,y = len(content),dictionary.count

        array = self.generate_numpy(content,x,y)

        return array

    def run_model(self):
        array = self.generate_array()
        dbscan = DBSCAN(self.eps,self.min_samples,self.metric,self.algorithm)
        labels = dbscan.fit_predict()

    def output_result(self):
        output = dict()
        labels = self.run_model()
        dictionary = Dictionary()
        for i,(index,line) in enumerate(dictionary):
            content = output.setdefault(labels[i],[])
            content.append(line)
    def dump_file(self,output):
        
        with open(r'../output/audit/julei.txt','w',encoding='utf-8') as f:
            for key,value in output:
                string = "%s\n%s\n" % (key,'\n'.join(value))
                f.write(string)

    def main(self):
        output = self.output_result()
        self.dump_file(output)


if __name__=='__main__':
    mydbscan = Mydbscan()
    mydbscan.main()
