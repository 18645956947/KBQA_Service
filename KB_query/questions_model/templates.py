# SPARQL前缀和模板
SPARQL_PREXIX = u"""
PREFIX ex: <http://population/>
"""
SPARQL_PREXIX2 = u"""
PREFIX ri: <http://rincome/>
"""
# 模板A 人口问题
SPARQL_SUM_A = u"{prefix}\n" + \
               u"SELECT (SUM({select}) AS ?SUM)\n" + \
               u"WHERE {{\n" + \
               u"{expression}\n" + \
               u"}}\n"
# 模板B 人口问题
SPARQL_SUM_B = u"{prefix}\n" + \
               u"SELECT (SUM({select}) AS ?{word1}) (SUM({select2}) AS ?{word2}) WHERE {{\n" + \
               u"{expression}\n" + \
               u"}}\n"
# 模板C
SPARQL_SUM_C = u"{prefix}\n" + \
               u"SELECT (SUM({select})/SUM({select2}) AS ?proportion) WHERE {{\n" + \
               u"{expression}\n" + \
               u"}}\n"
# 模板D
SPARQL_SUM_D = u"{prefix}\n" + \
               u"SELECT (SUM({select})/SUM(SUM ({select2}+{select3}) AS ?proportion) WHERE {{\n" + \
               u"{expression}\n" + \
               u"}}\n"
# 模板E
SPARQL_SUM_E = u"{prefix}\n" + \
               u"SELECT ((SUM({select})+SUM({select2}))/SUM({select3}) AS ?proportion) WHERE {{\n" + \
               u"{expression}\n" + \
               u"}}\n"
# 模板F
SPARQL_SUM_F = u"{prefix}\n" + \
               u"{prefix2}\n" + \
               u"SELECT (SUM({select})*SUM({select2}) AS ?result) WHERE {{\n" + \
               u"{expression}\n" + \
               u"}}\n"
# 模板G-------------------------------------
SPARQL_SUM_G = u"{prefix}\n" + \
               u"SELECT {select} WHERE {{\n" + \
               u"?x provName {select}" + \
               u"{{\n" + \
               u"SELECT ?x (MAX(?y/?y+?z) AS ?proportion) WHERE  {{\n" + \
               u"{expression2}\n" + \
               u"}}\n" + \
               u"GROUP BY ?x" + \
               u"}}\n"
# 模板H
SPARQL_SUM_H = u"{prefix}\n" + \
               u"SELECT {select} WHERE {{\n" + \
               u"?x ex:{word} {select}" + \
               u"{{\n" + \
               u"SELECT ?x (MAX(?y/(?y+?z)) AS ?proportion) WHERE {{\n" + \
               u"{expression}\n" + \
               u"}}\n" + \
               u"GROUP BY ?x" + \
               u"}}\n" + \
               u"}}\n"
# 模板I
SPARQL_SUM_I = u"{prefix}\n" + \
               u"SELECT {select} WHERE {{\n" + \
               u"?x ex:provName {select}.\n" + \
               u"{{\n" + \
               u"SELECT ?x MAX(abs((?y/?z)-1)) AS ?MaxP) WHERE {{\n" + \
               u"{expression}\n" + \
               u"}}\n" + \
               u"GROUP BY ?x\n" + \
               u"}}\n" + \
               u"}}\n"
# 模板J
SPARQL_SUM_J = u"{prefix}\n" + \
               u"SELECT {select} WHERE {{\n" + \
               u"{expression}\n" + \
               u"FILTER(\n" + \
               u"?z >?y)\n" + \
               u"}}\n"
# 模板K
SPARQL_SUM_K = u"{prefix}\n" + \
               u"SELECT (AVG({select}/({select}+{select2})) AS ?avg) WHERE {{\n" + \
               u"{expression}\n" + \
               u"}}\n"
# 模板M
SPARQL_SUM_M = u"{prefix}\n" + \
               u"SELECT {select} {select2}  WHERE {{\n" + \
               u"{{\n" + \
               u"{expression}\n" + \
               u"FILTER({expression2})\n" + \
               u"}}\n" + \
               u"ORDER BY ASC({select})"
# 模板M2
SPARQL_SUM_M2 = u"{prefix}\n" + \
                u"SELECT {select} (SUM({select2}) AS ?SUM)  WHERE {{\n" + \
                u"{{\n" + \
                u"{expression}\n" + \
                u"FILTER({expression2})\n" + \
                u"}}\n" + \
                u"ORDER BY ASC({select})"
# 模板N
SPARQL_SUM_N = u"{prefix}\n" + \
               u"SELECT {select} ({select2}/{select3} AS ?proportion) WHERE {{\n" + \
               u"{{\n" + \
               u"{expression}\n" + \
               u"}}\n" + \
               u"FILTER({expression2})" + \
               u"}}\n" + \
               u"}}\n" + \
               u"ORDER BY ASC({select})"
# 模板O
SPARQL_SUM_O = u"{prefix}\n" + \
               u"SELECT (AVG({select}) AS ?avg) WHERE {{\n" + \
               u"{expression}\n" + \
               u"FILTER(?t>=(?MaxY-{num}) && ?t<=?MaxY)" + \
               u"{{\n" + \
               u"SELECT (MAX({select2}) AS ?MaxY) WHERE {{\n" + \
               u"{{\n" + \
               u"{expression2}\n" + \
               u"}}\n" + \
               u"}}\n" + \
               u"}}\n"

# 模板J2
SPARQL_SUM_J2 = u"{prefix}\n" + \
                u"SELECT {select} {select2} WHERE {{\n" + \
                u"{expression}\n" + \
                u"}}\n" + \
                u"FILTER(\n" + \
                u"?z >?y)\n"
# 模板U
SPARQL_SUM_U = u"{prefix}\n" + \
               u"SELECT (COUNT(DISTINCT {select}) AS ?number) WHERE {{\n" + \
               u"{expression}\n" + \
               u"}}\n"
# 模板S
SPARQL_SUM_S = u"{prefix}\n" + \
               u"SELECT DISTINCT {select} WHERE {{\n" + \
               u"{expression}\n" + \
               u"{{\n" + \
               u"SELECT (SUM({select2}) AS ?sum) WHERE {{\n" + \
               u"{expression2}\n" + \
               u"}}\n" + \
               u"}}\n" + \
               u"FILTER(" + \
               u"?t >?sum)\n" + \
               u"}}\n"
# 模板T
SPARQL_SUM_T = u"{prefix}\n" + \
               u"SELECT ({select}/{select2}/?MaxP AS ?proportion) WHERE {{\n" + \
               u"{expression}\n" + \
               u"{{\n" + \
               u"SELECT (MAX({select3}/{select4}) AS ?MaxP) WHERE {{\n" + \
               u"{expression2}\n" + \
               u"MINUS" + \
               u"{{" + \
               u"{expression3}" + \
               u"}}\n" + \
               u"}}\n" + \
               u"}}\n" + \
               u"}}\n"
# 模板Z
SPARQL_SUM_Z = u"{prefix}\n" + \
               u"SELECT * WHERE {{\n" + \
               u"{expression}\n" + \
               u"}}\n" + \
               u"LIMIT 10"
