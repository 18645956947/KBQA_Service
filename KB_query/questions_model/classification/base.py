import abc
from KB_query.questions_model.keywords import *


# 问题查询条件生成器基类
class Base():
    def __init__(self, word_objects, rules_list):
        self.word_objects = word_objects
        self.rules_list = rules_list

        self.time = None  # 时间
        self.province = None  # 省
        self.city = None  # 城市
        self.keyword = None  # 关键词 gender: 性别; type: 占比

    # 初始化参数
    @abc.abstractmethod
    def __init_property(self):
        pass

    # 生成器主函数
    @abc.abstractmethod
    def run(self):
        pass

    # 初始化time
    def init_time(self):
        for w in self.word_objects:
            if w.pos == pos_time:
                self.time = w.token

    # 初始化time province
    def init_time_and_province(self):
        for w in self.word_objects:
            if w.pos == pos_time:
                self.time = w.token
            if w.pos == pos_place:
                self.province = w.token

    # 初始化province city
    def init_province_and_city(self):
        for w in self.word_objects:
            if w.pos == pos_place:
                if self.province is None:
                    self.province = w.token
                else:
                    self.city = w.token

    # 初始化time province city
    def init_time_and_province_and_city(self):
        for w in self.word_objects:
            if w.pos == pos_time:
                self.time = w.token
            if w.pos == pos_place:
                if self.province is None:
                    self.province = w.token
                else:
                    self.city = w.token

    # 初始化keyword
    def init_keyword(self, rules_list):
        for r in rules_list:
            self.keyword = r.apply(self.word_objects)
            if self.keyword is not None:
                break

    # 初始化time province city keyword
    def init_time_and_province_and_city_and_keyword(self, rules_list):
        self.init_time_and_province_and_city()
        self.init_keyword(rules_list)
