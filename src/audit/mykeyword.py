#encoding:utf-8
""""
@author hisoka
@version 1.0
@function 该模块负责提取关键词
"""

# 关键词文件目录
FILEPATH = r'fdsfds'


class KeyWord(object):

    """
    负责提取关键词，读取关键词文件，利用正则返回关键词
    """

    def __init__(self):
        self.regex = None
        self.regex_reverse = None
        self.regex,self.regex_reverse = self.load_file()

    # 加载关键词文件 正则表达式只扣取一部分，所以正反处理
    def process_file(self):
        import re
        result = set()
        with open(FILEPATH, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.rstrip('\n').rstrip('\r')
                result.add(line)

        result = list(result)
        result_reverse = result[:]
        result_reverse.reverse()

        string = '|'.join(result)
        string_reverse = '|'.join(result_reverse)

        regex_keyword = re.compile(string)
        regex_keyword_reverse = re.compile(string_reverse)

        return regex_keyword, regex_keyword_reverse

    # 返回关键词
    def get_keyword(self, string):
        word1 = self.regex_reverse.findall(string)
        word2 = self.regex.findall(string)
        word = set(word1) | set(word2)
        return list(word)


# if __name__ == '__main__':
#     pass











