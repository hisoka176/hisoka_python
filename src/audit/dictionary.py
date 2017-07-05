#encoding:utf-8

FILEPATH = r'fdsfds'

from mykeyword import KeyWord
class Dictionary(object):

    #
    def __init__(self):
        self.word_index = dict()
        self.count = 0
        self.word_count = dict()

        self.extract_keyword = KeyWord()

    def __len__(self):
        pass

    def process_words(self,words):
        
        for word in words:
            if word not in self.word_index:
                self.word_index[word] = self.count
                self.count += 1

            count = self.word_count.setdefault(word,0)
            self.word_count[word] = count + 1
                
    def __iter__(self):
        with open(FILEPATH,'r',encoding='utf-8') as f:
            for line in f:
                line = line.rstrip('\n').rstrip('\r')

                words = self.extract_keyword.get_keyword(line)

                self.process_words(words)
                
                index = [ self.word_index[word] for word in words ]

                yield index,index

    
