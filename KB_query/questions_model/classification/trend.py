from KB_query.questions_model.classification import Base
from KB_query.questions_model.keywords import *
from KB_query.questions_model.templates import *


# 趋势问题查询条件生成器
class Trend(Base):

    def __init__(self, word_objects, rules_list):
        super(Trend, self).__init__(word_objects, rules_list)

        self.time1 = None
        self.time2 = None
        self.select = u"?t"
        self.select2 = u"?y"
        self.select3 = u"?z"

        # 初始化参数
        self.__init_property()

    # 初始化参数
    def __init_property(self):
        for w in self.word_objects:
            if w.pos == pos_time:
                if self.time1 is None:
                    self.time1 = w.token
                else:
                    self.time2 = w.token

        self.init_province_and_city()
        self.init_keyword(self.rules_list.trend_keyword_rules)

    # 生成器主函数
    def run(self):
        # 问题包含男女的
        if self.keyword == ':gender':
            # Q21:1986年到2018年间上海浦东的男女比例趋势如何？
            if self.province is not None and self.city is not None:
                return self.__keyword_province_and_city()

            # Q?:1986年到2018年间上海的男女比例趋势如何？
            if self.province is not None and self.city is None:
                return self.__keyword_province()

            # Q?:1986年到2018年间全国的男女比例趋势如何？
            if self.province is None and self.city is None and self.time1 is not None:
                return self.__keyword_time1()

        # 问题不包含男女的
        if self.keyword is None and self.time1 is not None and self.time2 is not None:
            # Q20:1986年到2018年间上海浦东的人口趋势如何？
            if self.province is not None and self.city is not None:
                return self.__province_and_city()

            # Q?:1986年到2018年间上海的人口趋势如何？
            if self.province is not None and self.city is None:
                return self.__province()

            # Q?:1986年到2018年间全国的人口趋势如何？
            if self.province is None and self.city is None:
                return self.__none()

    # 问题包含男女的 Q21:1986年到2018年间上海浦东的男女比例趋势如何？
    def __keyword_province_and_city(self):
        e = u"?x ex:malePopulation ?y;\n" \
            u" ex:femalePopulation ?z;\n" \
            u" ex:provName '{province}';\n" \
            u" ex:cityName  '{city}';\n" \
            u" ex:year ?t." \
            .format(province=self.province.decode('utf-8'),
                    city=self.city.decode('utf-8'))

        e2 = u"?t>={time1} && ?t<={time2}" \
            .format(time1=self.time1.decode('utf-8'),
                    time2=self.time2.decode('utf-8'))

        return SPARQL_SUM_N.format(prefix=SPARQL_PREXIX,
                                   select=self.select,
                                   select2=self.select2,
                                   select3=self.select3,
                                   expression=e,
                                   expression2=e2)

    # 问题包含男女的 Q?:1986年到2018年间上海的男女比例趋势如何？
    def __keyword_province(self):
        e = u"?x ex:malePopulation ?y;\n" \
            u" ex:femalePopulation ?z;\n" \
            u" ex:provName '{province}';\n" \
            u" ex:year ?t." \
            .format(province=self.province.decode('utf-8'))

        e2 = u"?t>={time1} && ?t<={time2}" \
            .format(time1=self.time1.decode('utf-8'),
                    time2=self.time2.decode('utf-8'))

        return SPARQL_SUM_N.format(prefix=SPARQL_PREXIX,
                                   select=self.select,
                                   select2=self.select2,
                                   select3=self.select3,
                                   expression=e,
                                   expression2=e2)

    # 问题包含男女的 Q?:1986年到2018年间全国的男女比例趋势如何？
    def __keyword_time1(self):
        e = u"?x ex:malePopulation ?y;\n" \
            u" ex:femalePopulation ?z;\n" \
            u" ex:year ?t."

        e2 = u"?t>={time1} && ?t<={time2}" \
            .format(time1=self.time1.decode('utf-8'),
                    time2=self.time2.decode('utf-8'))

        return SPARQL_SUM_N.format(prefix=SPARQL_PREXIX,
                                   select=self.select,
                                   select2=self.select2,
                                   select3=self.select3,
                                   expression=e,
                                   expression2=e2)

    # 问题不包含男女的 Q20:1986年到2018年间上海浦东的人口趋势如何？
    def __province_and_city(self):
        e = u"?x ex:provName '{province}';\n" \
            u" ex:cityName  '{city}';\n" \
            u" ex:population ?y;\n" \
            u" ex:year ?t." \
            .format(province=self.province.decode('utf-8'),
                    city=self.city.decode('utf-8'))

        e2 = u"?t>={time1} && ?t<={time2}" \
            .format(time1=self.time1.decode('utf-8'),
                    time2=self.time2.decode('utf-8'))

        return SPARQL_SUM_M.format(prefix=SPARQL_PREXIX,
                                   select=self.select,
                                   select2=self.select2,
                                   expression=e,
                                   expression2=e2)

    # 问题不包含男女的 Q20:1986年到2018年间上海的人口趋势如何？
    def __province(self):
        e = u"?x ex:provName '{province}';\n" \
            u" ex:population ?y;\n" \
            u" ex:year ?t." \
            .format(province=self.province.decode('utf-8'),
                    city=self.city.decode('utf-8'))

        e2 = u"?t>={time1} && ?t<={time2}" \
            .format(time1=self.time1.decode('utf-8'),
                    time2=self.time2.decode('utf-8'))

        return SPARQL_SUM_M.format(prefix=SPARQL_PREXIX,
                                   select=self.select,
                                   select2=self.select2,
                                   expression=e,
                                   expression2=e2)

    # 问题不包含男女的 Q?:1986年到2018年间全国的人口趋势如何？
    def __none(self):
        e = u" ex:population ?y;\n" \
            u" ex:year ?t."
        e2 = u"?t>={time1} && ?t<={time2}" \
            .format(time1=self.time1.decode('utf-8'),
                    time2=self.time2.decode('utf-8'))

        return SPARQL_SUM_M2.format(prefix=SPARQL_PREXIX,
                                    select=self.select,
                                    select2=self.select2,
                                    expression=e,
                                    expression2=e2)
