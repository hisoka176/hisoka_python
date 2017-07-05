#encoding:utf-8

FILEPATH = r'fdsfds'

class Dictionary(object):

    #
    def __init__(self):
        self.word_index = dict()
        self.count = 0
        self.word_count = dict()

        self.extract_keyword =

    def __len__(self):
        pass

    def get_data(self):
        with open(FILEPATH,'r',encoding='utf-8') as f:
            for line in f:
                line = line.rstrip('\n').rstrip('\r')



