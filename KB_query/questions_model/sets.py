from KB_query.questions_model.classification import *


class RulesList():
    keyword_rules = []
    count_keyword_rules = []
    population_keyword_rules = []
    trend_keyword_rules = []
    most_keyword_rules = []


class QuestionSet:
    def __init__(self):
        pass

    @staticmethod
    def has_population(word_objects):
        """
        人口问题 Q1,Q2,Q3,Q4
        """
        return Population(word_objects, RulesList).run()

    @staticmethod
    def has_count(word_objects):
        """
        个数问题 Q41,Q42,Q43,Q45
        """
        return Count(word_objects, RulesList).run()

    @staticmethod
    def has_proportion(word_objects):
        """
        比例问题 Q5,Q6,Q7
        """
        return Proportion(word_objects, RulesList).run()

    @staticmethod
    def has_sum_compare(word_objects):
        """
        总省之间比较 Q49
        """
        return SumCompare(word_objects, RulesList).run()

    @staticmethod
    def has_sum_income(word_objects):
        """
        地区收入 Q52
        """
        return SumIncome(word_objects, RulesList).run()

    @staticmethod
    def has_max_gender(word_objects):
        """
        XX年性别比例最高|低省 Q14
        """
        return MaxGender(word_objects, RulesList).run()

    @staticmethod
    def has_max_disorder(word_objects):
        """
        XX年性别失调省 Q15
        """
        return MaxDisorder(word_objects, RulesList).run()

    @staticmethod
    def has_gender_compare(word_objects):
        """
        男女人数比较Q31，Q32
        """
        return GenderCompare(word_objects, RulesList).run()

    @staticmethod
    def has_with_gender_compare(word_objects):
        """
        Q33:男人比女人少的时期和城市有哪些
        """
        return WithGenderCompare(word_objects, RulesList).run()

    @staticmethod
    def has_sample(word_objects):
        """
        Q54:给些样例数据
        """
        return Sample(word_objects, RulesList).run()

    @staticmethod
    def has_avg_proportion(word_objects):
        """
        Q18:1986年全国平均城镇人口占比是多少？
        """
        return AvgProportion(word_objects, RulesList).run()

    @staticmethod
    def has_trend(word_objects):
        """
        趋势问题 Q20,Q21
        """
        return Trend(word_objects, RulesList).run()

    @staticmethod
    def has_extent(word_objects):
        """
        年度范围问题 Q22
        """
        return Extent(word_objects, RulesList).run()

    @staticmethod
    def has_more_population(word_objects):
        """
        人口省份更多 Q36,Q37
        """
        return MorePopulation(word_objects, RulesList).run()

    @staticmethod
    def has_most_proportion(word_objects):
        """
        最高人口比例 Q38,Q39
        """
        return MostProportion(word_objects, RulesList).run()


class PropertyValueSet:
    def __init__(self):
        pass

    @staticmethod
    def return_higher_value():
        return u'>'

    @staticmethod
    def return_lower_value():
        return u'<'

    @staticmethod
    def return_gender_value():
        return u':gender'

    @staticmethod
    def return_proportion_value():
        return u':proportion'

    @staticmethod
    def return_type_value():
        return u':type'

    @staticmethod
    def return_urban_value():
        return u'cityName'

    @staticmethod
    def return_province_value():
        return u'provName'

    @staticmethod
    def return_male_value():
        return u'male'

    @staticmethod
    def return_male_province():
        return u'male', u'province'

    @staticmethod
    def return_male_city():
        return u'male', u'city'

    @staticmethod
    def return_female_province():
        return u'female', u'province'

    @staticmethod
    def return_female_city():
        return u'female', u'city'

    @staticmethod
    def return_female_value():
        return u'female'
