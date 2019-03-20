from KB_query.questions_model.classification import Base
from KB_query.questions_model.templates import *


# XX年性别失调省问题查询条件生成器
class MaxDisorder(Base):

    def __init__(self, word_objects, rules_list):
        super(MaxDisorder, self).__init__(word_objects, rules_list)

        self.select = u"?w"

        # 初始化参数
        self.__init_property()

    # 初始化参数
    def __init_property(self):
        self.init_time()

    # 生成器主函数
    def run(self):
        # Q15:1986年男女比例最失调的是哪个省？
        if self.time is not None:
            return self.__time()

    # Q15:1986年男女比例最失调的是哪个省？
    def __time(self):
        e = u"?x ex:malePopulation ?y;\n" \
            u" ex:femalePopulation ?z;\n" \
            u" ex:year {time}." \
            .format(time=self.time.decode('utf-8'))

        return SPARQL_SUM_I \
            .format(prefix=SPARQL_PREXIX,
                    select=self.select,
                    expression=e)
