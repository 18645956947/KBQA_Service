from KB_query.questions_model.classification import Base
from KB_query.questions_model.templates import *


# 样例数据问题查询条件生成器
class Sample(Base):

    def __init__(self, word_objects, rules_list):
        super(Sample, self).__init__(word_objects, rules_list)

        # 初始化参数
        self.__init_property()

    # 初始化参数
    def __init_property(self):
        self.init_time_and_province()

    # 生成器主函数
    def run(self):
        # Q54:给些样例数据。
        if self.province is None and self.time is None:
            return self.__none()

    # Q54:给些样例数据。
    def __none(self):
        e = u"?s ?p ?o."
        return SPARQL_SUM_Z.format(prefix=SPARQL_PREXIX,
                                   expression=e)
