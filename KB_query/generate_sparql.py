from KB_query.questions_model import question2sparql


def generate_sparql(question):
    q2s = question2sparql.Question2Sparql([
        '../KB_query/external_dict/province_name.txt',
        '../KB_query/external_dict/time_name.txt',
        '../KB_query/external_dict/person_name.txt',
        '../KB_query/external_dict/movie_title.txt'])

    return q2s.get_sparql(question)
