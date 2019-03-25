# encoding=utf-8

"""
@desc: 将自然语言转为SPARQL查询语句
"""

from KB_query.questions_model import rules, word_tagging
#人口问题
people_list = ["省份", "城市", "农村人口", "城镇人口", "男性人口", "女性人口", "人口数", "人口", "总人口", "年份", "更新时间", "男女比例"]
#销售记录
sales_list = ["销售额", "利润", "营业额", "订单量", "销量", "日期", "订单id", "合同id", "合同金额", "渠道", "京东商城", "地区", "种类"]
#股价及舆情监控
price_monitoring_opinion = ['股票代码', '公司名', '科大讯飞', '泰山集团', '日期', '股价', '涨跌', '成交量', '子公司', '爽口食品', "负面舆情数", "评论数", "热门帖子", "帖子评论量", "营业额"]
#微博数据
Microblogging_Data = ["话题", "热门帖子", "评论数", "点赞量", "阅读量", "评论数", "转发数"]

class Question2Sparql:
    def __init__(self, dict_paths):
        self.tw = word_tagging.Tagger(dict_paths)
        self.rules = rules

    def get_sparql(self, question):
        """
        进行语义解析，找到匹配的模板，返回对应的SPARQL查询语句
        """
        word_objects = self.tw.get_word_objects(question)
        classify = self.classify(word_objects)
        queries_dict = dict()
        rules_list = []

        if classify == 'people':
            rules_list = self.rules.p_rules
        else:
            rules_list = self.rules


        for rule in rules_list:
            query, num = rule.apply(word_objects)
            if query is not None:
                queries_dict[num] = query

        if len(queries_dict) == 0:
            return None
        elif len(queries_dict) == 1:
            v = list(queries_dict.values())
            return v[0]
        else:
            # 匹配多个语句，以匹配关键词最多的句子作为返回结果
            sorted_dict = sorted(queries_dict.items(), key=lambda item: item[0], reverse=True)
            return sorted_dict[0][1]


    def classify(self, word_objects):
        for word_object in word_objects:
            print(str(word_object.token, 'utf-8'))
            if str(word_object.token, 'utf-8') in people_list:
                return "people"
