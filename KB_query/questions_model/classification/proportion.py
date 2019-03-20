from KB_query.questions_model.classification import Base
from KB_query.questions_model.templates import *


# 比例问题查询条件生成器
class Proportion(Base):

    def __init__(self, word_objects, rules_list):
        super(Proportion, self).__init__(word_objects, rules_list)

        self.select = u"?y"
        self.select2 = u"?z"
        self.blank1 = None
        self.blank2 = None

        # 初始化参数
        self.__init_property()

    # 初始化参数
    def __init_property(self):
        self.init_time_and_province_and_city_and_keyword(self.rules_list.population_keyword_rules)

        if self.keyword == ':gender':
            self.blank1 = 'malePopulation'
            self.blank2 = 'femalePopulation'

        if self.keyword == ':type':
            self.blank1 = 'urbanPopulation'
            self.blank2 = 'ruralPopulation'

    # 生成器主函数
    def run(self):
        # 关键词：男女 比例 比重 占比 占
        if self.keyword is not None:
            # Q6：1986年上海的男女比例是多少？
            if self.province is not None and self.city is None:
                return self.__keyword_province()

            # Q5: 1986年上海浦东的男女比例是多少？
            if self.province is not None and self.city is not None:
                return self.__keyword_province_city()

            # Q7：1986年全国的男女比例是多少？
            if self.province is None and self.city is None and self.time is not None:
                return self.__keyword_time()

    # 包含关键词 Q6：1986年上海的男女比例是多少？
    def __keyword_province(self):
        e = u"?x ex:provName '{province}';\n" \
            "  ex:year {time};\n" \
            u"   ex:{blank1} ?y;\n" \
            u"   ex:{blank2} ?z." \
            .format(province=self.province.decode('utf-8'),
                    time=self.time.decode('utf-8'),
                    blank1=self.blank1,
                    blank2=self.blank2)

        return SPARQL_SUM_C \
            .format(prefix=SPARQL_PREXIX,
                    select=self.select,
                    select2=self.select2,
                    expression=e)

    # 包含关键词 Q5: 1986年上海浦东的男女比例是多少？
    def __keyword_province_city(self):
        e = u"?x ex:provName '{province}';\n" \
            u"   ex:cityName '{city}';\n" \
            "    ex:year {time};\n" \
            u"   ex:{blank1} ?y;\n" \
            u"   ex:{blank2} ?z." \
            .format(province=self.province.decode('utf-8'),
                    city=self.city.decode('utf-8'),
                    time=self.time.decode('utf-8'),
                    blank1=self.blank1,
                    blank2=self.blank2)

        return SPARQL_SUM_C \
            .format(prefix=SPARQL_PREXIX,
                    select=self.select,
                    select2=self.select2,
                    expression=e)

    # 包含关键词 Q7：1986年全国的男女比例是多少
    def __keyword_time(self):
        e = "?x  ex:year {time};\n" \
            u" ex:{blank1} ?y;\n" \
            u" ex:{blank2} ?z." \
            .format(time=self.time.decode('utf-8'),
                    blank1=self.blank1,
                    blank2=self.blank2)

        return SPARQL_SUM_C \
            .format(prefix=SPARQL_PREXIX,
                    select=self.select,
                    select2=self.select2,
                    expression=e)
