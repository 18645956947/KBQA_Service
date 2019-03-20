from KB_query.questions_model.classification import Base
from KB_query.questions_model.templates import *


# 地区收入问题查询条件生成器
class SumIncome(Base):
    def __init__(self, word_objects, rules_list):
        super(SumIncome, self).__init__(word_objects, rules_list)

        self.select = u"?y"
        self.select2 = u"?w"

        # 初始化参数
        self.__init_property()

    # 初始化参数
    def __init_property(self):
        self.init_time_and_province_and_city()

    # 生成器主函数
    def run(self):
        # Q52:2018年上海城镇人口的总收入是多少?
        if self.province is not None and self.city is None:
            return self.__province()

        # Q?:2018年上海浦东城镇人口的总收入是多少？
        if self.province is not None and self.city is not None:
            return self.__province_and_city()

    # Q52:2018年上海城镇人口的总收入是多少?
    def __province(self):
        e = u"?x ri:year {time};\n" \
            u" ri:provName '{province}';\n" \
            u" ri:Urpi ?y.\n" \
            u"?z ex:provName '{province}';\n" \
            u" ex:population ?w;\n" \
            u" ex:year {time}." \
            .format(province=self.province.decode('utf-8'),
                    time=self.time.decode('utf-8'))

        return SPARQL_SUM_F \
            .format(prefix=SPARQL_PREXIX,
                    prefix2=SPARQL_PREXIX2,
                    select=self.select,
                    select2=self.select2,
                    expression=e)

    # Q?:2018年上海浦东城镇人口的总收入是多少？
    def __province_and_city(self):
        e = u"?x ri:year {time};\n" \
            u" ri:provName '{province}';\n" \
            u" ri:cityName '{city}';\n" \
            u" ri:Urpi ?y.\n" \
            u"  ex:provName '{province}';\n" \
            u"?z   ex:cityName '{city}';\n" \
            u" ex:population ?w;\n" \
            u" ex:year {time}." \
            .format(province=self.province.decode('utf-8'),
                    city=self.city.decode('utf-8'),
                    time=self.time.decode('utf-8'))

        return SPARQL_SUM_F \
            .format(prefix=SPARQL_PREXIX,
                    prefix2=SPARQL_PREXIX2,
                    select=self.select,
                    select2=self.select2,
                    expression=e)
