from KB_query.questions_model.classification import Base
from KB_query.questions_model.templates import *


# 人口省份更多问题查询条件生成器
class MorePopulation(Base):

    def __init__(self, word_objects, rules_list):
        super(MorePopulation, self).__init__(word_objects, rules_list)

        self.select = u"?y"
        self.select2 = u"?z"

        # 初始化参数
        self.__init_property()

    # 初始化参数
    def __init_property(self):
        self.init_time_and_province_and_city()

    # 生成器主函数
    def run(self):
        # Q36:2018年，比上海人口多的省有哪些？
        if self.province is not None and self.time is not None:
            return self.__province_and_time()

        # Q37:比上海人口多的省有哪些？
        if self.province is not None and self.time is None:
            return self.__province()

    # Q36:2018年，比上海人口多的省有哪些？
    def __province_and_time(self):
        e = u"?x ex:provName ?y;\n" \
            u" ex:population ?t;\n" \
            u" ex:year {time}." \
            .format(time=self.time.decode('utf-8'))

        e2 = u"?x ex:provName '{province}';\n" \
             u" ex:population ?z;\n" \
             u" ex:year {time}." \
            .format(province=self.province.decode('utf-8'),
                    time=self.time.decode('utf-8'))

        return SPARQL_SUM_S.format(prefix=SPARQL_PREXIX,
                                   select=self.select,
                                   select2=self.select2,
                                   expression=e,
                                   expression2=e2)

    # Q37:比上海人口多的省有哪些？
    def __province(self):
        e = u"?x ex:provName ?y;\n" \
            u" ex:population ?t."

        e2 = u"?x ex:provName '{province}';\n" \
             u" ex:population ?z." \
            .format(province=self.province.decode('utf-8'))

        return SPARQL_SUM_S.format(prefix=SPARQL_PREXIX,
                                   select=self.select,
                                   select2=self.select2,
                                   expression=e,
                                   expression2=e2)
