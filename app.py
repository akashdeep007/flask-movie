from flask import Flask
from database.db import initialize_db
from resources.movies import movies


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://akashdeep:Dyhal9Jo06NVc7GU@cluster0-dosbk.mongodb.net/Movie_Flask?retryWrites=true&w=majority'
}
initialize_db(app)


app.register_blueprint(movies)


app.run()
