from mendeley import Mendeley
import json

mendeley = Mendeley("938", "bkzasRJgHn9tcvT3")
session = mendeley.start_client_credentials_flow().authenticate()


highest_index = 0

def search(author):
	global highest_index
	highest_index = 0
	visited = []
	nodes = []
	links = []

	def dfs(author, dist = 0):
		global highest_index
		author = author.encode('utf-8')
		author = author.split(' ')[0]
		author = author.capitalize()

		print author, dist

		if dist >= 5:
			return
		if author in visited:
			return
		visited.append(author)

		nodes.append({'name': author, 'group': dist})

		docs = map(lambda x: map(lambda a: a.last_name.capitalize().split(' ')[0], x.authors), session.catalog.advanced_search(author=author).list(10).items)
		print len(docs)
		coauthors = []

		for doc in docs:
			others = filter(lambda a: False if a == author else True, doc)
			#if len(others) == len(doc):
			#	continue
			coauthors += others

		coauthors = coauthors[:3]

		print len(coauthors)

		my_idx = highest_index
		highest_index += 1
		for co in set(coauthors):
			idx = dfs(co, dist+1)
			if idx:
				links.append({'source': my_idx, 'target': idx, 'value': 1})

		return my_idx

	dfs(author)

	return {"nodes": nodes, "links": links}


from flask import Flask
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
	return app.send_static_file('index.html')

@app.route('/data/<author>')
def hello_world(author):
 	print "search for:", author
	
 	return json.dumps(search(author))


#url_for('static', filename='index.html')

if __name__ == '__main__':
    app.run()


