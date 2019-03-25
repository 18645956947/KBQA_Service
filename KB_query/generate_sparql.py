from KB_query.questions_model import question2sparql


def generate_sparql(question):
    q2s = question2sparql.Question2Sparql([
        '../KB_query/external_dict/province_name.txt',
        '../KB_query/external_dict/time_name.txt',
        '../KB_query/external_dict/person_name.txt',
        '../KB_query/external_dict/movie_title.txt'])

    return q2s.get_sparql(question)

q2s = question2sparql.Question2Sparql([
    '../KB_query/external_dict/province_name.txt',
    '../KB_query/external_dict/time_name.txt',
    '../KB_query/external_dict/person_name.txt',
    '../KB_query/external_dict/movie_title.txt'])

s = q2s.get_sparql("1984年上海的农村人口和城镇人口")
print(s)