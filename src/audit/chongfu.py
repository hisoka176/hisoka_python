#encoding:utf-8

# 该模块的主要作用去重复评论
# 需要添加布隆过滤器功能，实现去重复,可以节约很多内存
class Chongfu(object):
    def __init__(self,filepath):
        self.filepath = filepath
        self.orignal_length = None
        self.current_length = None
        self.content = None

        self.content,self.orignal_length = self.qu_chong_fu()
        self.current_length = len(self.content)



    def __str__(self):
        string = '-'*40
        string += '\noriginal:%d\tnow:%d\n' % (self.orignal_length,self.current_length)
        string += '-'*40
        return string

    def __len__(self):
        return self.current_length

    # 去重复数据
    def qu_chong_fu(self):
        result = set()
        r_count = 0
        with open(self.filepath,'r',encoding='utf-8') as f:
            for line in f:
                if '{' in line and '}' in line:
                    continue
                r_count += 1
                line = line.rstrip('\n').rstrip('\r')
                array = line.split('  ')[0]

                result.add(array)
        return list(result),r_count

    def __iter__(self):
        return self

    def __next__(self):
        for line in self.content:
            return line

if __name__=='__main__':
    a = Chongfu(r'E:\eclipse_workspace\eclipse\Hisoka_Python\input\audit\julei\leibie_n.txt')
    for line in a:
        print(line)
        break

    print(a)


