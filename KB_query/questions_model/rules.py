from refo import Star, Any

from KB_query.questions_model.keywords import *
from KB_query.questions_model.sets import QuestionSet, PropertyValueSet, RulesList

# 问题模板/匹配规则
p_rules = [
    # 人口数
    Rule(condition_num=4,
         condition=time_entity +
                   Star(Any(), greedy=False) +
                   (place_entity | national) +
                   (place_entity | Star(Any(), greedy=False)) +
                   Star(Any(), greedy=False) +
                   (country | gender | Star(Any(), greedy=False)) +
                   Star(Any(), greedy=False) +
                   (people | different) +
                   Star(Any(), greedy=False),
         action=QuestionSet.has_population),

    # 人口数
    Rule(condition_num=4,
         condition=(place_entity | national) +
                   (place_entity | Star(Any(), greedy=False)) +
                   Star(Any(), greedy=False) +
                   time_entity +
                   Star(Any(), greedy=False) +
                   (country | gender | Star(Any(), greedy=False)) +
                   Star(Any(), greedy=False) +
                   (people | different) + Star(Any(), greedy=False),
         action=QuestionSet.has_population),

    # 人口数
    Rule(condition_num=4,
         condition=time_entity +
                   Star(Any(), greedy=False) +
                   (place_entity | national) +
                   (place_entity | Star(Any(), greedy=False)) +
                   Star(Any(), greedy=False) +
                   (country | gender) +
                   Star(Any(), greedy=False) +
                   proportion +
                   Star(Any(), greedy=False),
         action=QuestionSet.has_proportion),

    # 人口数
    Rule(condition_num=4,
         condition=(place_entity | national) +
                   (place_entity | Star(Any(), greedy=False)) +
                   Star(Any(), greedy=False) +
                   time_entity +
                   Star(Any(), greedy=False) +
                   (country | gender) +
                   Star(Any(), greedy=False) +
                   proportion +
                   Star(Any(), greedy=False),
         action=QuestionSet.has_proportion),

    # 人口数
    Rule(condition_num=4,
         condition=place_entity +
                   Star(Any(), greedy=False) +
                   (country | gender | Star(Any(), greedy=False)) +
                   Star(Any(), greedy=False) +
                   (people | different) +
                   Star(Any(), greedy=False),
         action=QuestionSet.has_population),
]
rules = [
    # 个数
    Rule(condition_num=4,
         condition=(time_entity | place_entity | national | Star(Any(), greedy=False)) +
                   (place_entity | national | Star(Any(), greedy=False)) +
                   Star(Any(), greedy=False) +
                   (count | data) + (city | province | Star(Any(), greedy=False)),
         action=QuestionSet.has_count),
    
    # 个数
    Rule(condition_num=4,
         condition=(place_entity | national | Star(Any(), greedy=False)) +
                   Star(Any(), greedy=False) +
                   (time_entity | place_entity | national | Star(Any(), greedy=False)) +
                   Star(Any(), greedy=False) +
                   (count | data) +
                   (city | province | Star(Any(), greedy=False)),
         action=QuestionSet.has_count),

    # 总数比较
    Rule(condition_num=4,
         condition=place_entity +
                   Star(Any(), greedy=False) +
                   place_entity +
                   Star(Any(), greedy=False) +
                   compare +
                   Star(Any(), greedy=False) +
                   place_entity,
         action=QuestionSet.has_sum_compare),

    # 地区收入
    Rule(condition_num=4,
         condition=time_entity +
                   Star(Any(), greedy=False) +
                   place_entity +
                   Star(Any(), greedy=False) +
                   income +
                   Star(Any(), greedy=False),
         action=QuestionSet.has_sum_income),

    # 地区收入
    Rule(condition_num=4,
         condition=place_entity +
                   Star(Any(), greedy=False) +
                   time_entity +
                   Star(Any(), greedy=False) +
                   Star(Any(), greedy=False) +
                   income +
                   Star(Any(), greedy=False),
         action=QuestionSet.has_sum_income),

    # XX年性别高低省
    Rule(condition_num=4,
         condition=time_entity +
                   Star(Any(), greedy=False) +
                   gender +
                   Star(Any(), greedy=False) +
                   top +
                   Star(Any(), greedy=False),
         action=QuestionSet.has_max_gender),

    # XX年性别高低省
    Rule(condition_num=4,
         condition=gender +
                   Star(Any(), greedy=False) +
                   time_entity +
                   Star(Any(), greedy=False) +
                   top +
                   Star(Any(), greedy=False),
         action=QuestionSet.has_max_gender),

    # XX年性别失调省
    Rule(condition_num=4,
         condition=time_entity +
                   Star(Any(), greedy=False) +
                   gender +
                   Star(Any(), greedy=False) +
                   disorder +
                   Star(Any(), greedy=False),
         action=QuestionSet.has_max_disorder),

    # XX年性别失调省
    Rule(condition_num=4,
         condition=gender +
                   Star(Any(), greedy=False) +
                   time_entity +
                   Star(Any(), greedy=False) +
                   disorder +
                   Star(Any(), greedy=False),
         action=QuestionSet.has_max_disorder),

    # 男女人数比较Q31，Q32
    Rule(condition_num=4,
         condition=(time_entity | place_entity) +
                   Star(Any(), greedy=False) +
                   (when | city | province) +
                   Star(Any(), greedy=False) +
                   gender +
                   (Star(Any(), greedy=False) | prefer) +
                   Star(Any(), greedy=False) +
                   compare,
         action=QuestionSet.has_gender_compare),

    # 男女人数比较Q31，Q32
    Rule(condition_num=4,
         condition=(when | city | province) +
                   Star(Any(), greedy=False) +
                   (time_entity | place_entity) +
                   Star(Any(), greedy=False) +
                   gender +
                   (Star(Any(), greedy=False) | prefer) +
                   Star(Any(), greedy=False) +
                   compare,
         action=QuestionSet.has_gender_compare),

    # Rule(condition_num=2,
    #      condition=(sample | data) +
    #                (sample | data | Star(Any(), greedy=False)),
    #      action=QuestionSet.has_sample),

    # Q18
    Rule(condition_num=4,
         condition=time_entity +
                   Star(Any(), greedy=False) +
                   national +
                   Star(Any(), greedy=False) +
                   avg +
                   Star(Any(), greedy=False) +
                   proportion,
         action=QuestionSet.has_avg_proportion),

    # Q18
    Rule(condition_num=4,
         condition=national +
                   Star(Any(), greedy=False) +
                   time_entity +
                   Star(Any(), greedy=False) +
                   avg +
                   Star(Any(), greedy=False) +
                   proportion,
         action=QuestionSet.has_avg_proportion),

    # 趋势问题
    Rule(condition_num=4,
         condition=time_entity +
                   Star(Any(), greedy=False) +
                   time_entity +
                   Star(Any(), greedy=False) +
                   (place_entity | national) +
                   (place_entity | Star(Any(), greedy=False)) +
                   Star(Any(), greedy=False) +
                   trend +
                   Star(Any(), greedy=False),
         action=QuestionSet.has_trend),

    # 趋势问题
    Rule(condition_num=4,
         condition=(place_entity | national) +
                   (place_entity | Star(Any(), greedy=False)) +
                   time_entity +
                   Star(Any(), greedy=False) +
                   time_entity +
                   Star(Any(), greedy=False) +
                   Star(Any(), greedy=False) +
                   trend +
                   Star(Any(), greedy=False),
         action=QuestionSet.has_trend),

    # 年度范围问题
    Rule(condition_num=4,
         condition=extent +
                   (number_entity | Star(Any(), greedy=False)) +
                   Star(Any(), greedy=False) +
                   (place_entity | national) +
                   (place_entity | Star(Any(), greedy=False)) +
                   Star(Any(), greedy=False) +
                   avg,
         action=QuestionSet.has_extent),

    # Rule(condition_num=4,
    #      condition=extent +
    #                (number_entity | Star(Any(), greedy=False)) +
    #                Star(Any(), greedy=False) +
    #                (place_entity | national) +
    #                (place_entity | Star(Any(), greedy=False)) +
    #                Star(Any(), greedy=False) +
    #                avg,
    #      action=QuestionSet.has_more_population),

    # 人口省份更多
    Rule(condition_num=4,
         condition=(time_entity | Star(Any(), greedy=False)) +
                   (place_entity | national | Star(Any(), greedy=False)) +
                   Star(Any(), greedy=False) +
                   prefer +
                   Star(Any(), greedy=False) +
                   compare +
                   Star(Any(), greedy=False) +
                   (city | province) +
                   Star(Any(), greedy=False),
         action=QuestionSet.has_more_population),

    # 最高人口比例
    Rule(condition_num=4,
         condition=(time_entity | Star(Any(), greedy=False)) +
                   (place_entity | national | Star(Any(), greedy=False)) +
                   Star(Any(), greedy=False) +
                   gender +
                   Star(Any(), greedy=False) +
                   proportion +
                   Star(Any(), greedy=False) +
                   top,
         action=QuestionSet.has_most_proportion),

    # 最高人口比例
    Rule(condition_num=4,
         condition=(place_entity | national | Star(Any(), greedy=False)) +
                   (time_entity | Star(Any(), greedy=False)) +
                   Star(Any(), greedy=False) +
                   prefer +
                   Star(Any(), greedy=False) +
                   compare +
                   Star(Any(), greedy=False) +
                   (city | province) +
                   Star(Any(), greedy=False),
         action=QuestionSet.has_more_population),

    # 最高人口比例
    Rule(condition_num=4,
         condition=(place_entity | national | Star(Any(), greedy=False)) +
                   (time_entity | Star(Any(), greedy=False)) +
                   Star(Any(), greedy=False) +
                   gender +
                   Star(Any(), greedy=False) +
                   proportion +
                   Star(Any(), greedy=False) +
                   top,
         action=QuestionSet.has_most_proportion)
]

compare_keyword_rules = [
    # 大于
    KeywordRule(condition=(time_entity | place_entity | national | Star(Any(), greedy=False)) +
                          (city | province | gender | Star(Any(), greedy=False)) +
                          (higher | gender | Star(Any(), greedy=False)) +
                          (higher | city | province | Star(Any(), greedy=False)),
                action=PropertyValueSet.return_higher_value),

    # 小于
    KeywordRule(condition=(time_entity | place_entity | national | Star(Any(), greedy=False)) +
                          (city | province | gender | Star(Any(), greedy=False)) +
                          (lower | gender | Star(Any(), greedy=False)) +
                          (lower | city | province | Star(Any(), greedy=False)),
                action=PropertyValueSet.return_lower_value),

    # 大于
    KeywordRule(condition=(city | province | gender | Star(Any(), greedy=False)) +
                          (time_entity | place_entity | national | Star(Any(), greedy=False)) +
                          (higher | gender | Star(Any(), greedy=False)) +
                          (higher | city | province | Star(Any(), greedy=False)),
                action=PropertyValueSet.return_higher_value),

    # 小于
    KeywordRule(condition=(city | province | gender | Star(Any(), greedy=False)) +
                          (time_entity | place_entity | national | Star(Any(), greedy=False)) +
                          (lower | gender | Star(Any(), greedy=False)) +
                          (lower | city | province | Star(Any(), greedy=False)),
                action=PropertyValueSet.return_lower_value)
]

population_keyword_rules = [
    # KeywordRule(condition=time_entity +
    #                       Star(Any(), greedy=False) +
    #                       (place_entity | national) +
    #                       (place_entity | Star(Any(), greedy=False)) +
    #                       (gender | Star(Any(), greedy=False)),
    #             action=PropertyValueSet.return_gender_value),

    # gender
    KeywordRule(condition=time_entity +
                          Star(Any(), greedy=False) +
                          (place_entity | national) +
                          (place_entity | Star(Any(), greedy=False)) +
                          Star(Any(), greedy=False) +
                          gender +
                          Star(Any(), greedy=False) +
                          proportion +
                          Star(Any(), greedy=False),
                action=PropertyValueSet.return_gender_value),

    # gender
    KeywordRule(condition=(place_entity | national) +
                          (place_entity | Star(Any(), greedy=False)) +
                          Star(Any(), greedy=False) +
                          time_entity +
                          Star(Any(), greedy=False) +
                          gender +
                          Star(Any(), greedy=False) +
                          proportion +
                          Star(Any(), greedy=False),
                action=PropertyValueSet.return_gender_value),

    # type
    KeywordRule(condition=time_entity +
                          Star(Any(), greedy=False) +
                          (place_entity | national) +
                          (place_entity | Star(Any(), greedy=False)) +
                          Star(Any(), greedy=False) +
                          country +
                          Star(Any(), greedy=False) +
                          proportion +
                          Star(Any(), greedy=False),
                action=PropertyValueSet.return_type_value),

    # type
    KeywordRule(condition=(place_entity | national) +
                          (place_entity | Star(Any(), greedy=False)) +
                          Star(Any(), greedy=False) +
                          time_entity +
                          Star(Any(), greedy=False) +
                          country +
                          Star(Any(), greedy=False) +
                          proportion +
                          Star(Any(), greedy=False),
                action=PropertyValueSet.return_type_value),
]

keyword_rules = [
    # gender
    # KeywordRule(condition=time_entity +
    #                       Star(Any(), greedy=False) +
    #                       (place_entity | national) +
    #                       (place_entity | Star(Any(), greedy=False)) +
    #                       (gender | Star(Any(), greedy=False)),
    #             action=PropertyValueSet.return_gender_value),

    # gender
    KeywordRule(condition=time_entity +
                          Star(Any(), greedy=False) +
                          (place_entity | national) +
                          (place_entity | Star(Any(), greedy=False)) +
                          Star(Any(), greedy=False) +
                          gender +
                          Star(Any(), greedy=False) +
                          (people | different) +
                          Star(Any(), greedy=False),
                action=PropertyValueSet.return_gender_value),

    # gender
    KeywordRule(condition=(place_entity | national) +
                          (place_entity | Star(Any(), greedy=False)) +
                          Star(Any(), greedy=False) +
                          time_entity +
                          Star(Any(), greedy=False) +
                          gender +
                          Star(Any(), greedy=False) +
                          (people | different) +
                          Star(Any(), greedy=False),
                action=PropertyValueSet.return_gender_value),

    # type
    KeywordRule(condition=time_entity +
                          Star(Any(), greedy=False) +
                          (place_entity | national) +
                          (place_entity | Star(Any(), greedy=False)) +
                          Star(Any(), greedy=False) +
                          country +
                          Star(Any(), greedy=False) +
                          (people | different) +
                          Star(Any(), greedy=False),
                action=PropertyValueSet.return_type_value),

    # type
    KeywordRule(condition=(place_entity | national) +
                          (place_entity | Star(Any(), greedy=False)) +
                          Star(Any(), greedy=False) +
                          time_entity +
                          Star(Any(), greedy=False) +
                          country +
                          Star(Any(), greedy=False) +
                          (people | different) +
                          Star(Any(), greedy=False),
                action=PropertyValueSet.return_type_value),
]

trend_keyword_rules = [
    # KeywordRule(condition=time_entity +
    #                       Star(Any(), greedy=False) +
    #                       (place_entity | national) +
    #                       (place_entity | Star(Any(), greedy=False)) +
    #                       (gender | Star(Any(), greedy=False)),
    #             action=PropertyValueSet.return_gender_value),

    # gender
    KeywordRule(time_entity +
                Star(Any(), greedy=False) +
                time_entity +
                Star(Any(), greedy=False) +
                (place_entity | national) +
                (place_entity | Star(Any(), greedy=False)) +
                Star(Any(), greedy=False) +
                gender +
                Star(Any(), greedy=False) +
                trend,
                action=PropertyValueSet.return_gender_value),

    # gender
    KeywordRule((place_entity | national) +
                (place_entity | Star(Any(), greedy=False)) +
                Star(Any(), greedy=False) +
                time_entity +
                Star(Any(), greedy=False) +
                time_entity +
                Star(Any(), greedy=False) +
                gender +
                Star(Any(), greedy=False) +
                trend,
                action=PropertyValueSet.return_gender_value)
]

count_keyword_rules = [
    # cityName
    KeywordRule(condition=(time_entity | place_entity | national) +
                          (place_entity | national | Star(Any(), greedy=False)) +
                          Star(Any(), greedy=False) +
                          count +
                          city +
                          Star(Any(), greedy=False),
                action=PropertyValueSet.return_urban_value),

    # provName
    KeywordRule(condition=(time_entity | place_entity | national) +
                          (place_entity | national | Star(Any(), greedy=False)) +
                          Star(Any(), greedy=False) +
                          count +
                          province +
                          Star(Any(), greedy=False),
                action=PropertyValueSet.return_province_value),

    # cityName
    KeywordRule(condition=(place_entity | national | Star(Any(), greedy=False)) +
                          (time_entity | place_entity | national) +
                          Star(Any(), greedy=False) +
                          count +
                          city +
                          Star(Any(), greedy=False),
                action=PropertyValueSet.return_urban_value),

    # provName
    KeywordRule(condition=(place_entity | national | Star(Any(), greedy=False)) +
                          (time_entity | place_entity | national) +
                          Star(Any(), greedy=False) +
                          count +
                          province +
                          Star(Any(), greedy=False),
                action=PropertyValueSet.return_province_value),
]

most_keyword_rules = [
    # male
    KeywordRule(condition=(time_entity | Star(Any(), greedy=False)) +
                          (place_entity | national | Star(Any(), greedy=False)) +
                          Star(Any(), greedy=False) +
                          male +
                          Star(Any(), greedy=False) +
                          proportion +
                          Star(Any(), greedy=False) +
                          top,
                action=PropertyValueSet.return_male_value),

    # female
    KeywordRule(condition=(time_entity | Star(Any(), greedy=False)) +
                          (place_entity | national | Star(Any(), greedy=False)) +
                          Star(Any(), greedy=False) +
                          female +
                          Star(Any(), greedy=False) +
                          proportion +
                          Star(Any(), greedy=False) +
                          top,
                action=PropertyValueSet.return_female_value),

    # male
    KeywordRule(condition=(place_entity | national | Star(Any(), greedy=False)) +
                          (time_entity | Star(Any(), greedy=False)) +
                          Star(Any(), greedy=False) +
                          male +
                          Star(Any(), greedy=False) +
                          proportion +
                          Star(Any(), greedy=False) +
                          top,
                action=PropertyValueSet.return_male_value),

    # female
    KeywordRule(condition=(place_entity | national | Star(Any(), greedy=False)) +
                          (time_entity | Star(Any(), greedy=False)) +
                          Star(Any(), greedy=False) +
                          female +
                          Star(Any(), greedy=False) +
                          proportion +
                          Star(Any(), greedy=False) +
                          top,
                action=PropertyValueSet.return_female_value),
]

RulesList.keyword_rules = keyword_rules
RulesList.compare_keyword_rules = compare_keyword_rules
RulesList.population_keyword_rules = population_keyword_rules
RulesList.trend_keyword_rules = trend_keyword_rules
RulesList.count_keyword_rules = count_keyword_rules
RulesList.most_keyword_rules = most_keyword_rules
