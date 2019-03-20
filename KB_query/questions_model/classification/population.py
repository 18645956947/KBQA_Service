from KB_query.questions_model.classification import Base
from KB_query.questions_model.templates import *


# 人口问题查询条件生成器
class Population(Base):

    def __init__(self, word_objects, rules_list):
        super(Population, self).__init__(word_objects, rules_list)

        self.select = u"?y"
        self.select2 = u"?z"
        self.word1 = None
        self.word2 = None

        self.blank1 = None
        self.blank2 = None

        # 初始化参数
        self.__init_property()

    # 初始化参数
    def __init_property(self):
        self.init_time_and_province_and_city_and_keyword(self.rules_list.keyword_rules)

        if self.keyword == ':gender':
            self.blank1 = 'malePopulation'
            self.blank2 = 'femalePopulation'
            self.word1 = 'maleSUM'
            self.word2 = 'femaleSUM'

        if self.keyword == ':type':
            self.blank1 = 'urbanPopulation'
            self.blank2 = 'ruralPopulation'
            self.word1 = 'urbanSUM'
            self.word2 = 'ruralSUM'

    # 生成器主函数
    def run(self):
        # 性别或分别问题
        if self.keyword is not None:
            # Q?：1986年上海男女分别有多少？
            if self.province is not None and self.city is None:
                return self.__keyword_time_and_province()

            # Q4：1986年上海浦东男女分别有多少？
            if self.province is not None and self.city is not None:
                return self.__keyword_time_and_province_and_city()

            # Q?：1986年全国男女分别有多少？
            if self.province is None and self.city is None and self.time is not None:
                return self.__keyword_time()

        # 不是性别或分别问题
        else:
            # Q2：1986年上海的人口数是多少?
            if self.province is not None and self.city is None:
                return self.__time_and_province()

            # Q1：1986年上海浦东有多少人？
            if self.province is not None and self.city is not None:
                return self.__time_and_province_and_city()

            # Q3：1986年全国有多少人？
            if self.province is None and self.city is None and self.time is not None:
                return self.__time()

    # 性别或分别问题 Q?：1986年上海男女分别有多少？
    def __keyword_time_and_province(self):
        e = u"?x ex:provName '{province}';\n" \
            "  ex:year {time};\n" \
            u"   ex:{blank1} ?y;\n" \
            u"   ex:{blank2} ?z." \
            .format(province=self.province.decode('utf-8'),
                    time=self.time.decode('utf-8'),
                    blank1=self.blank1,
                    blank2=self.blank2)

        return SPARQL_SUM_B \
            .format(prefix=SPARQL_PREXIX,
                    select=self.select,
                    select2=self.select2,
                    word1=self.word1,
                    word2=self.word2,
                    expression=e)

    # 性别或分别问题 Q4：1986年上海浦东男女分别有多少？
    def __keyword_time_and_province_and_city(self):
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

        return SPARQL_SUM_B \
            .format(prefix=SPARQL_PREXIX,
                    select=self.select,
                    select2=self.select2,
                    word1=self.word1,
                    word2=self.word2,
                    expression=e)

    # 性别或分别问题 Q?：1986年全国男女分别有多少？
    def __keyword_time(self):
        e = "   ex:year {time};\n" \
            u"?x ex:{blank1} ?y;\n" \
            u"?x ex:{blank2} ?z." \
            .format(time=self.time.decode('utf-8'),
                    blank1=self.blank1,
                    blank2=self.blank2)

        return SPARQL_SUM_B \
            .format(prefix=SPARQL_PREXIX,
                    select=self.select,
                    select2=self.select2,
                    word1=self.word1,
                    word2=self.word2,
                    expression=e)

    # 不是性别或分别问题 Q2：1986年上海的人口数是多少?
    def __time_and_province(self):
        e = u"?x ex:provName '{province}';\n" \
            "   ex:year {time};\n" \
            u"   ex:population ?y." \
            .format(province=self.province.decode('utf-8'),
                    time=self.time.decode('utf-8'))

        return SPARQL_SUM_A \
            .format(prefix=SPARQL_PREXIX,
                    select=self.select,
                    expression=e)

    # 不是性别或分别问题 Q1：1986年上海浦东有多少人？
    def __time_and_province_and_city(self):
        e = u"?x ex:provName '{province}';\n" \
            u"   ex:cityName '{city}';\n" \
            "   ex:year {time};\n" \
            u"   ex:population ?y." \
            .format(province=self.province.decode('utf-8'),
                    city=self.city.decode('utf-8'),
                    time=self.time.decode('utf-8'))

        return SPARQL_SUM_A \
            .format(prefix=SPARQL_PREXIX,
                    select=self.select,
                    expression=e)

    # 不是性别或分别问题 Q3：1986年全国有多少人？
    def __time(self):
        e = u"?x ex:population ?y;\n" \
            "   ex:year {time}." \
            .format(time=self.time.decode('utf-8'))

        return SPARQL_SUM_A \
            .format(prefix=SPARQL_PREXIX,
                    select=self.select,
                    expression=e)
