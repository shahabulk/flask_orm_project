from api.blingblong import create_app
from api.lib.db import *

app = create_app(dbname = DB_NAME, user = DB_USER, password = DB_PASSWORD)

app.run(debug = True) 