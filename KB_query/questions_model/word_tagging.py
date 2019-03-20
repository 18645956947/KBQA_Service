# encoding=utf-8

"""
@desc: 定义Word类的结构；定义Tagger类，实现自然语言转为Word对象的方法。
"""
import jieba
import jieba.posseg as pseg


class Word(object):
    def __init__(self, token, pos):
        self.token = token
        self.pos = pos


class Tagger:
    def __init__(self, dict_paths):
        # 加载外部词典
        for p in dict_paths:
            jieba.load_userdict(p)

        # jieba不能正确切分的词语，我们人工调整其频率。
        jieba.suggest_freq(('上海', '浦东'), True)
        jieba.suggest_freq(('云南', '东城'), True)
        jieba.suggest_freq(('云南', '西城'), True)
        jieba.suggest_freq(('内蒙古', '呼和浩特'), True)
        jieba.suggest_freq(('北京', '海淀'), True)
        jieba.suggest_freq(('北京', '东城'), True)
        jieba.suggest_freq(('浙江', '杭州'), True)
        jieba.suggest_freq(('男女', '比例'), True)
        jieba.suggest_freq(('人口', '比例'), True)
        jieba.suggest_freq(('上海', '市'), True)
        jieba.suggest_freq(('北京', '市'), True)
        jieba.suggest_freq(('杭州', '市'), True)
        jieba.suggest_freq(('年', '间'), True)

    @staticmethod
    def get_word_objects(sentence):
        # type: # (str) -> list
        """
        把自然语言转为Word对象
        :param sentence:
        :return:
        """
        return [Word(word.encode('utf-8'), tag) for word, tag in pseg.cut(sentence)]


# 用于测试
if __name__ == '__main__':
    tagger = Tagger(
        ['external_dict/province_name.txt',
         'external_dict/time_name.txt',
         'external_dict/movie_title.txt',
         'external_dict/person_name.txt'])
    while True:
        s = input()
        for i in tagger.get_word_objects(s):
            first = i.token
            second = i.pos
            print(first.decode('utf-8'), second)
