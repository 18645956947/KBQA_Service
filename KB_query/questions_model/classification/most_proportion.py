from KB_query.questions_model.classification import Base
from KB_query.questions_model.templates import *


# 最高人口比例问题查询条件生成器
class MostProportion(Base):

    def __init__(self, word_objects, rules_list):
        super(MostProportion, self).__init__(word_objects, rules_list)

        self.select = u"?y"
        self.select2 = u"?z"
        self.select3 = u"?b"
        self.select4 = u"?c"

        # 初始化参数
        self.__init_property()

    # 初始化参数
    def __init_property(self):
        self.init_time_and_province_and_city_and_keyword(self.rules_list.most_keyword_rules)

    # 生成器主函数
    def run(self):
        if self.keyword == 'female':
            gender = 'femalePopulation'
        else:
            gender = 'malePopulation'

        # Q38:2018年，杭州的女性人口比例是不是全国最高的？
        if self.province is not None and self.time is not None:
            return self.__keyword_province_and_time(gender)
        # Q39:杭州的女性人口比例是不是全国最高的？
        if self.province is not None and self.time is None:
            return self.__keyword_province(gender)

    def __keyword_province_and_time(self, gender):
        e = u"?x ex:" + gender + \
            " ?y;\n" \
            u" ex:population ?z;\n" \
            u" ex:cityName '{province}';\n" \
            u" ex:year {time}." \
                .format(province=self.province.decode('utf-8'),
                        time=self.time.decode('utf-8'))

        e2 = u"?a ex:" + gender + \
             " ?b;\n" \
             u" ex:population ?c;\n" \
             u" ex:year {time}." \
                 .format(time=self.time.decode('utf-8'))

        e3 = u"?a ex:cityName '{province}'" \
            .format(province=self.province.decode('utf-8'))

        return SPARQL_SUM_T.format(prefix=SPARQL_PREXIX,
                                   select=self.select,
                                   select2=self.select2,
                                   select3=self.select3,
                                   select4=self.select4,
                                   expression=e,
                                   expression2=e2,
                                   expression3=e3)

    def __keyword_province(self, gender):
        e = u"?x ex:" + gender + \
            " ?y;\n" \
            u" ex:population ?z;\n" \
            u" ex:cityName '{province}'." \
                .format(province=self.province.decode('utf-8'))

        e2 = u"?a ex:" + gender + \
             " ?b;\n" \
             u" ex:population ?c."
        e3 = u"?a ex:cityName '{province}'" \
            .format(province=self.province.decode('utf-8'))

        return SPARQL_SUM_T.format(prefix=SPARQL_PREXIX,
                                   select=self.select,
                                   select2=self.select2,
                                   select3=self.select3,
                                   select4=self.select4,
                                   expression=e,
                                   expression2=e2,
                                   expression3=e3)
