# encoding=utf-8

"""
@desc: 将自然语言转为SPARQL查询语句
"""

from KB_query.questions_model import rules, word_tagging

people_list = ["省份", "城市", "农村人口", "城镇人口", "男性人口", "女性人口", "人口数", "人口", "总人口", "年份", "更新时间", "男女比例"]


class Question2Sparql:
    def __init__(self, dict_paths):
        self.tw = word_tagging.Tagger(dict_paths)
        self.rules = rules

    def get_sparql(self, question):
        """
        进行语义解析，找到匹配的模板，返回对应的SPARQL查询语句
        """
        word_objects = self.tw.get_word_objects(question)
        classify = self.classify(word_objects)
        queries_dict = dict()
        rules_list = []

        if classify == 'people':
            rules_list = self.rules.p_rules
        else:
            rules_list = self.rules.rules

        for rule in rules_list:
            query, num = rule.apply(word_objects)
            if query is not None:
                queries_dict[num] = query

        if len(queries_dict) == 0:
            return None
        elif len(queries_dict) == 1:
            v = list(queries_dict.values())
            return v[0]
        else:
            # 匹配多个语句，以匹配关键词最多的句子作为返回结果
            sorted_dict = sorted(queries_dict.items(), key=lambda item: item[0], reverse=True)
            return sorted_dict[0][1]


    def classify(self, word_objects):
        for word_object in word_objects:
            print(str(word_object.token, 'utf-8'))
            if str(word_object.token, 'utf-8') in people_list:
                return "people"
