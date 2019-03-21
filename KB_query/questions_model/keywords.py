from KB_query.questions_model.refo_obj import *

# 定义关键词
pos_person = "nr"
pos_movie = "nz"
pos_number = "num"
pos_place = "ns"
pos_time = "t"

person_entity = (W(pos=pos_person))
movie_entity = (W(pos=pos_movie))
number_entity = (W(pos=pos_number))
place_entity = (W(pos=pos_place))
time_entity = (W(pos=pos_time))
city_entity = (W(pos=pos_place))

trend = W("趋势")
national = (W("全国") | W("我国"))
male = (W("男") | W("男性") | W("男人"))
female = (W("女") | W("女性") | W("女人"))
mf = (W("男女"))
proportion = (W("比例") | W("比重") | W("占比") | W("占"))
prefer = (W("比"))
gender = (male | female | mf)
country = (W("城镇") | W("城镇人口") | W("城乡") | W("城乡人口"))

people = (W("人") | W("人口") | W("人数") | W("人口数")| W("总人口数")| W("总人口")| W("总人数"))
several = (W("多少") | W("是多少") | W("有多少"))
verb = (W("有") | W("是") | W("为"))
population = (people | several | verb)

count = (W("几个") | W("几"))
city = (W("城市"))
province = W("省")
sample = (W("样例") | W("例子"))
data = W("数据")
disorder = W("失调")
company = W("和")
avg = W("平均")
extent = W("近")
higher = (W("大于") | W("高于") | W("多于") | W("多") | W("超过"))
lower = (W("小于") | W("低于") | W("少于") | W("少"))
compare = (higher | lower)
top = (W("最高") | W("最大") | W("最多"))
different = (W("分别") | W("各有"))
income = (W("收入") | W("总收入"))

when = (W("何时") | W("时候") | W("时间"))
where = (W("哪里") | W("哪儿") | W("何地") | W("何处") | W("在") + W("哪"))
