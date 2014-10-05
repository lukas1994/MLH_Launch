#email = "taimurlukas@gmail.com"
#password = "mlhmlh"
clientID = "938"
clientSecret = "bkzasRJgHn9tcvT3"

from mendeley import Mendeley

mendeley = Mendeley(clientID, clientSecret)
session = mendeley.start_client_credentials_flow().authenticate()

#doi = raw_input('Enter a DOI: ')

#doc = session.catalog.by_identifier(doi=doi, view='all')

highest_index = 0
visited = []
nodes = []
links = []

def search(author, dist = 0):
	global highest_index

	author = author.encode('utf-8')

	print dist, author

	if dist >= 4:
		return
	if author in visited:
		return
	visited.append(author)

	nodes.append({'name': author, 'group': 1})

	docs = map(lambda x: map(lambda a: a.last_name, x.authors), session.catalog.advanced_search(author=author).list(10).items)
	coauthors = []

	for doc in docs:
		others = filter(lambda a: False if a == author else True, doc)
		if len(others) == len(doc):
			continue
		coauthors += others

	for co in set(coauthors):
		idx = search(co, dist+1)
		if idx:
			links.append({'source': highest_index, 'target': idx, 'value': 1})

	highest_index += 1

	return highest_index - 1

author1 = "Erdoes"
search(author1)

def o_str(o):
	s = "{"
	s += ",".join(["\"" + key + "\": \"" + str(value) + "\"" for key, value in o.iteritems()])
	s += "}"
	return s
def l_str(l):
	s = "["
	s += ",".join([o_str(o) for o in l])
	s += "]"
	return s
import json
print json.dumps({"nodes": nodes, "links": links})
#print "{\"nodes\": "+l_str(nodes)+",\"links\":"+l_str(links)+"}"


