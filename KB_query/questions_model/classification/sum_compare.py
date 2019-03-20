from KB_query.questions_model.classification import Base
from KB_query.questions_model.keywords import *
from KB_query.questions_model.templates import *


# 省总数比较问题查询条件生成器
class SumCompare(Base):
    def __init__(self, word_objects, rules_list):
        super(SumCompare, self).__init__(word_objects, rules_list)
        
        self.select = u"?y"
        self.select2 = u"?w"
        self.select3 = u"?t"

        self.province1 = None
        self.province2 = None
        self.province3 = None

        # 初始化参数
        self.__init_property()

    # 初始化参数
    def __init_property(self):
        for w in self.word_objects:
            if w.pos == pos_place:
                if self.province1 is None:
                    self.province1 = w.token
                    continue
                if self.province1 is not None and self.province2 is None:
                    self.province2 = w.token
                    continue
                else:
                    self.province3 = w.token

    # 生成器主函数
    def run(self):
        # Q49:上海和北京的人口总和有没有超过河南？
        if self.province1 is not None and self.province2 is not None and self.province3 is not None:
            return self.__province1_and_province2_and_province3()

    # Q49:上海和北京的人口总和有没有超过河南？
    def __province1_and_province2_and_province3(self):
        e = u"?x ex:provName '{province1}';\n" \
            u" ex:population ?y.\n" \
            u" ?z ex:provName '{province2}';\n" \
            u" ex:population ?w.\n" \
            u"?o ex:provName '{province3}';\n" \
            u" ex:population ?t." \
            .format(province1=self.province1.decode('utf-8'),
                    province2=self.province2.decode('utf-8'),
                    province3=self.province3.decode('utf-8'))

        return SPARQL_SUM_E \
            .format(prefix=SPARQL_PREXIX,
                    select=self.select,
                    select2=self.select2,
                    select3=self.select3,
                    expression=e)
