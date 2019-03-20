from KB_query.questions_model.classification import Base
from KB_query.questions_model.templates import *


# 平均比例问题查询条件生成器
class AvgProportion(Base):

    def __init__(self, word_objects, rules_list):
        super(AvgProportion, self).__init__(word_objects, rules_list)

        self.select = u"?y"
        self.select2 = u"?z"

        # 初始化参数
        self.__init_property()

    # 初始化参数
    def __init_property(self):
        self.init_time()

    # 生成器主函数
    def run(self):
        # Q18:1986年全国平均城镇人口占比是多少？
        if self.time is not None:
            return self.__time()

    # Q18:1986年全国平均城镇人口占比是多少？
    def __time(self):
        e = u"?x ex:UrbanPopulation ?y;\n" \
            u" ex:RuralPopulation  ?z;\n" \
            u" ex:year {time}." \
            .format(time=self.time.decode('utf-8'))

        return SPARQL_SUM_K \
            .format(prefix=SPARQL_PREXIX,
                    select=self.select,
                    select2=self.select2,
                    expression=e)
