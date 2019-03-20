from KB_query.questions_model import question2sparql


# q2s = question2sparql.Question2Sparql([
#     'external_dict/province_name.txt',
#     'external_dict/time_name.txt',
#     'external_dict/person_name.txt',
#     'external_dict/movie_title.txt'])
#
# print(q2s.get_sparql('北京的人口数是多少?'))

def generate_sparql(question):
    q2s = question2sparql.Question2Sparql([
        '../KB_query/external_dict/province_name.txt',
        '../KB_query/external_dict/time_name.txt',
        '../KB_query/external_dict/person_name.txt',
        '../KB_query/external_dict/movie_title.txt'])

    return q2s.get_sparql(question)
