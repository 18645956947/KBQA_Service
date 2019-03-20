from KB_query.questions_model.classification import Base
from KB_query.questions_model.keywords import *
from KB_query.questions_model.templates import *


# 年度范围问题查询条件生成器
class Extent(Base):

    def __init__(self, word_objects, rules_list):
        super(Extent, self).__init__(word_objects, rules_list)

        self.num = None
        self.select = u"?z"
        self.select2 = u"?o"

        # 初始化参数
        self.__init_property()

    # 初始化参数
    def __init_property(self):
        for w in self.word_objects:
            if w.pos == pos_number:
                self.num = w.token

        self.init_province_and_city()

    # 生成器主函数
    def run(self):
        # Q22:近10年上海浦东的平均人口数是多少？
        if self.province is not None and self.city is not None:
            return self.__province_and_city()

        # Q?:近10年上海的平均人口数是多少？
        if self.province is not None and self.city is None:
            return self.__province()

    # Q22:近10年上海浦东的平均人口数是多少？
    def __province_and_city(self):
        e = u"?x ex:provName '{province}';\n" \
            u"?x ex:cityName '{city}';\n" \
            u" ex:population ?z;\n" \
            u" ex:year ?t." \
            .format(province=self.province.decode('utf-8'),
                    city=self.city.decode('utf-8'))

        e2 = u"?x ex:year ?o."

        return SPARQL_SUM_O.format(prefix=SPARQL_PREXIX,
                                   select=self.select,
                                   select2=self.select2,
                                   expression=e,
                                   num=self.num.decode('utf-8'),
                                   expression2=e2)

    # Q?:近10年上海的平均人口数是多少？
    def __province(self):
        e = u"?x ex:provName '{province}';\n" \
            u" ex:population ?z;\n" \
            u" ex:year ?t." \
            .format(province=self.province.decode('utf-8'))

        e2 = u"?x ex:year ?o."

        return SPARQL_SUM_O.format(prefix=SPARQL_PREXIX,
                                   select=self.select,
                                   select2=self.select2,
                                   expression=e,
                                   num=self.num.decode('utf-8'),
                                   expression2=e2)
