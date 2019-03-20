from KB_query.questions_model.classification import Base
from KB_query.questions_model.templates import *


# 个数问题查询条件生成器
class Count(Base):

    def __init__(self, word_objects, rules_list):
        super(Count, self).__init__(word_objects, rules_list)

        self.select = u"?y"

        # 初始化参数
        self.__init_property()

    # 初始化参数
    def __init_property(self):
        self.init_time_and_province_and_city_and_keyword(self.rules_list.count_keyword_rules)

    # 生成器主函数
    def run(self):
        # 问题包含城市、省等关键词的
        if self.keyword is not None:
            # 包含城市、省等关键词的 Q40:上海有几个城市？
            if self.province is not None and self.time is None:
                return self.__keyword_province()

            # Q41:2018年，上海有几个城市？
            if self.province is not None and self.time is not None:
                return self.__keyword_province_and_time()

            # Q42:2018年，全国有几个省？ Q44:2018年，全国有几个城市？
            if self.province is None and self.time is not None:
                return self.__keyword_time()

            # Q43:全国有几个省？
            if self.province is None and self.time is None:
                return self.__keyword_none()

        # 问题不包含城市、省等关键词的
        else:
            # Q45:上海市，有多少年的数据在这里？
            if self.province is not None and self.city is None:
                return self.__province()

            # Q?:上海浦东，有多少年的数据在这里？
            if self.province is not None and self.city is not None:
                return self.__province_and_city()

    # 问题包含城市、省等关键词的 Q40:上海有几个城市？
    def __keyword_province(self):
        e = u"?x ex:provName '{province}';\n" \
            u" ex:{keyword} ?y." \
            .format(province=self.province.decode('utf-8'),
                    keyword=self.keyword)

        return SPARQL_SUM_U \
            .format(prefix=SPARQL_PREXIX,
                    select=self.select,
                    expression=e)

    # 问题包含城市、省等关键词的 Q41:2018年，上海有几个城市？
    def __keyword_province_and_time(self):
        e = u"?x ex:provName '{province}';\n" \
            " ex:year {time};\n" \
            u" ex:{keyword} ?y." \
            .format(province=self.province.decode('utf-8'),
                    time=self.time.decode('utf-8'),
                    keyword=self.keyword)

        return SPARQL_SUM_U \
            .format(prefix=SPARQL_PREXIX,
                    select=self.select,
                    expression=e)

    # 问题包含城市、省等关键词的 Q42:2018年，全国有几个省？ Q44:2018年，全国有几个城市？
    def __keyword_time(self):
        e = u"?x ex:{keyword} ?y;\n" \
            u" ex:year {time}." \
            .format(time=self.time.decode('utf-8'),
                    keyword=self.keyword)

        return SPARQL_SUM_U \
            .format(prefix=SPARQL_PREXIX,
                    select=self.select,
                    expression=e)

    # 问题包含城市、省等关键词的 Q43:全国有几个省？
    def __keyword_none(self):
        e = "?x ex:{keyword} ?y.;" \
            .format(keyword=self.keyword)

        return SPARQL_SUM_U \
            .format(prefix=SPARQL_PREXIX,
                    select=self.select,
                    expression=e)

    # 问题不包含城市、省等关键词的 Q45:上海市，有多少年的数据在这里？
    def __province(self):
        e = u"?x ex:provName '{province}';\n" \
            u" ex:year ?y." \
            .format(province=self.province.decode('utf-8'))

        return SPARQL_SUM_U \
            .format(prefix=SPARQL_PREXIX,
                    select=self.select,
                    expression=e)

    # 问题不包含城市、省等关键词的 Q?:上海浦东，有多少年的数据在这里？
    def __province_and_city(self):
        e = u"?x ex:provName '{province}';\n" \
            u"?x ex:cityName '{city}';\n" \
            u" ex:year ?y." \
            .format(province=self.province.decode('utf-8'),
                    city=self.city.decode('utf-8'), )

        return SPARQL_SUM_U \
            .format(prefix=SPARQL_PREXIX,
                    select=self.select,
                    expression=e)
