from KB_query.questions_model.classification import Base
from KB_query.questions_model.templates import *


# Q33:男人比女人少的时期和城市有哪些问题查询条件生成器
class WithGenderCompare(Base):

    def __init__(self, word_objects, rules_list):
        super(WithGenderCompare, self).__init__(word_objects, rules_list)

        self.select = u"?w"
        self.select2 = u"?t"

        # 初始化参数
        self.__init_property()

    # 初始化参数
    def __init_property(self):
        self.init_time_and_province()

    # 生成器主函数
    def run(self):
        # Q33:男人比女人少的时期和城市有哪些？
        if self.province is None and self.time is None:
            return self.__none()

    # Q33:男人比女人少的时期和城市有哪些？
    def __none(self):
        e = u"?x ex:malePopulation ?y;\n" \
            u" ex:femalePopulation ?z;\n" \
            u" ex:cityName ?w'\n;" \
            u" ex:year ?t."

        return SPARQL_SUM_J2 \
            .format(prefix=SPARQL_PREXIX,
                    select=self.select,
                    select2=self.select2,
                    expression=e)
