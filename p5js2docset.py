# create a docset from p5 data
import sqlite3, json, shutil

class Database:
	def __init__(self, dbpath):
		self._cnx = sqlite3.connect(dbpath)
		self._cursor = self._cnx.cursor()

		try: self.execute('DROP TABLE searchIndex;')
		except: pass
		self.execute('CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
		self.execute('CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

	def __del__(self):
		self._cnx.commit()
		self._cnx.close()

	def execute(self, query):
		self._cursor.execute(query)

	def insert_new_index(self, data):
		self._cursor.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', data)

def import_file (filename, database):
	with open(filename) as datafile:
		datajson = json.load(datafile)

		# load modules
		k = 'modules'
		for j in datajson[k]:
			if 'classes' in datajson[k][j] and 'is_submodule' not in datajson[k][j]:
				name = datajson[k][j]['name']
				object_type = 'Module'
				if 'itemtype' in datajson[k][j] and 'main' in datajson[k][j]['itemtype']:
					# Module with itemtype main
					# https://p5js.org/reference/#/p5.SoundFile
					# https://p5js.org/reference/#/p5.MediaElement
					path = 'index.html#' + name
					print('register ' + object_type + ': ' + name)
					data = (name, object_type, path)
					database.insert_new_index(data)
				
				object_type = 'Class'
				for classe in datajson[k][j]['classes']:
					name = classe
					path = 'index.html#' + name
					print('register ' + object_type + ': ' + name)
					data = (name, object_type, path)
					database.insert_new_index(data)

		# load methods
		k = 'classitems'
		object_type = 'Method'
		for item in datajson[k]:
			if 'itemtype' in item and 'method' in item['itemtype']:
				# Method
				# https://p5js.org/reference/#/p5/background
				name = item['name']
				classe = item['class']
				path = 'index.html#/' + classe + '/' + name
				print('register ' + object_type + ': ' + name)
				data = (name, object_type, path)
				database.insert_new_index(data)

def main():
	docset_ressources_path = 'p5js.docset/Contents/Resources'
	sqlite_path = docset_ressources_path + '/docSet.dsidx'
	p5_doc_reference = '../p5.js/docs/reference'
	data_json_path = p5_doc_reference + '/data.min.json'
	
	database = Database(sqlite_path)
	import_file (data_json_path, database)
	
	print ('copy data.min.json to ' + docset_ressources_path + '/Documents')
	shutil.copy(data_json_path, docset_ressources_path + '/Documents/data.min.json')

	print ('Done.')

if __name__ == "__main__":
    main()