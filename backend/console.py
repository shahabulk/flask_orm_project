from api.blingblong import create_app

app = create_app(dbname ='imdb_development', user = 'postgres', password = 'postgres')

app.run(debug = True)