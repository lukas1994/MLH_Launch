from mendeley import Mendeley
import json

mendeley = Mendeley("938", "bkzasRJgHn9tcvT3")
session = mendeley.start_client_credentials_flow().authenticate()

highest_index = 0
visited = []
nodes = []
links = []

def search(author, dist = 0):
	global highest_index

	author = author.encode('utf-8')

	if dist >= 4:
		return
	if author in visited:
		return
	visited.append(author)

	nodes.append({'name': author, 'group': 1})

	docs = map(lambda x: map(lambda a: a.last_name, x.authors), session.catalog.advanced_search(author=author).list(100).items)
	coauthors = []

	for doc in docs:
		others = filter(lambda a: False if a == author else True, doc)
		if len(others) == len(doc):
			continue
		coauthors += others

	coauthors = coauthors[:8]

	my_idx = highest_index
	highest_index += 1
	for co in set(coauthors):
		idx = search(co, dist+1)
		if idx:
			links.append({'source': my_idx, 'target': idx, 'value': 1, 'weight':1})

	return my_idx


from flask import Flask
app = Flask(__name__)

@app.route('/data/<author>')
def hello_world(author):
	print author
	search(author)
	return json.dumps({"nodes": nodes, "links": links})

#url_for('static', filename='index.html')

if __name__ == '__main__':
    app.run()


