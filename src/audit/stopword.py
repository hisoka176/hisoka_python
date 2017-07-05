#encoding:utf-8

STOP_WORD_FILE_PATH = r'E:\eclipse_workspace\eclipse\src_python\keyword\stopword.txt'


class StopWord(object):

    """
        加载停用词
    """
    def __init__(self):
        self.stop_word = set()

    def load_word(self):
        with open(STOP_WORD_FILE_PATH,'r',encoding='utf-8') as f:

            for line in f:
                word = line.rstrip('\n').rstrip('\r').strip(' ')
                self.stop_word.add(word)

    def is_stop_word(self, word):

        if word in self.stop_word:
            return True
        else:
            return False
