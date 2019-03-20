from KB_query.questions_model.classification import Base
from KB_query.questions_model.templates import *


# 男女人数比较Q31，Q32问题查询条件生成器
class GenderCompare(Base):

    def __init__(self, word_objects, rules_list):
        super(GenderCompare, self).__init__(word_objects, rules_list)

        self.select = u"?w"

        # 初始化参数
        self.__init_property()

    # 初始化参数
    def __init_property(self):
        self.init_time_and_province()

    # 生成器主函数
    def run(self):
        # Q32:上海在什么时间男人比女人少？
        if self.province is not None:
            return self.__province()

        # Q31:1986年有哪些城市男人比女人少？
        if self.province is None and self.time is not None:
            return self.__province_and_time()

    # Q32:上海在什么时间男人比女人少？
    def __province(self):
        e = u"?x ex:malePopulation ?y;\n" \
            u" ex:femalePopulation ?z;\n" \
            u" ex:provName '{province}';\n" \
            u" ex:year ?w." \
            .format(province=self.province.decode('utf-8'))

        return SPARQL_SUM_J \
            .format(prefix=SPARQL_PREXIX,
                    select=self.select,
                    expression=e)

    # Q31:1986年有哪些城市男人比女人少？
    def __province_and_time(self):
        e = u"?x ex:malePopulation ?y;\n" \
            u" ex:femalePopulation ?z;\n" \
            u" ex:cityName ?w;\n" \
            u" ex:year {time}." \
            .format(time=self.time.decode('utf-8'))

        return SPARQL_SUM_J \
            .format(prefix=SPARQL_PREXIX,
                    select=self.select,
                    expression=e)
