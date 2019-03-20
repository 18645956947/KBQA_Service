from KB_query.questions_model import question2sparql

q2s = question2sparql.Question2Sparql([
    'external_dict/province_name.txt',
    'external_dict/time_name.txt',
    'external_dict/person_name.txt',
    'external_dict/movie_title.txt'])
my_query = q2s.get_sparql('杭州的男性人口比例是不是全国最高的？')

print(my_query)
