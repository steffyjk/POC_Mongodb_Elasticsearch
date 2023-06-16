from flask import Flask

from app.controllers.SearchController import search_module

app = Flask(__name__)
app.register_blueprint(search_module)

if __name__ == '__main__':
    app.run(debug=True)


