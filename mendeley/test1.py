from mendeley import Mendeley
import json

mendeley = Mendeley("938", "bkzasRJgHn9tcvT3")
session = mendeley.start_client_credentials_flow().authenticate()


highest_index = 0
viewsAll = []

def search(author):
	global highest_index
	global views
	highest_index = 0
	visited = []
	nodes = []
	links = []

	def dfs(author, dist = 0):
		global highest_index
		author = author.encode('utf-8')
		subject = ""
		views = 0
		author = author.split[0].capitalize()
		docs = map(lambda x: map(lambda a: a.last_name.capitalize().split(' ')[0], x.authors), session.catalog.advanced_search(author=author).list(10).items)
		iterDocs = session.catalog.advanced_search(author=author, view = 'all').iter()

		for i in range(1,2):
			v = False
			if iterDocs.__sizeof__() > 0:
				v = iterDocs.next()
			if v:
				views += v.reader_count

		if dist >= 5:
			return
		if author in visited:
			return
		visited.append(author)

		nodes.append({'name': author, 'group': dist, 'views': views})

		coauthors = []

		for doc in docs:
			others = filter(lambda a: False if a == author else True, doc)
			#if len(others) == len(doc):
			#	continue
			coauthors += others

		coauthors = coauthors[:3]

		my_idx = highest_index
		highest_index += 1
		for co in set(coauthors):
			idx = dfs(co, dist+1)
			if idx:
				links.append({'source': my_idx, 'target': idx, 'value':1})

		return my_idx

	dfs(author)

	maxv = max([n['views'] for n in nodes])
	minv = min([n['views'] for n in nodes])

	for i in range(len(nodes)):
		nodes[i]['views'] = (nodes[i]['views']-minv)*1.0/(maxv-minv)*10+4

	return {"nodes": nodes, "links": links}

#print json.dumps(search("Knuth"))

from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
	return app.send_static_file('index.html')

@app.route('/data/<author>')
def hello_world(author):	
	return json.dumps(search(author))



if __name__ == '__main__':
   app.run(debug=True)


