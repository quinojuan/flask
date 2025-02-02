from flask import Flask
from flask import render_template
from flask import request, jsonify
# from flask import request
# from markupsafe import escape
# from flask import url_for

app = Flask(__name__)

# @app.route("/user/<username>")
# def show_user_profile(username):
#   # show the user profile for that user
#   return f"User {escape(username)}"

# @app.route("/hola/<name>")
# def hello(name):
#   return f"Hola {name}"

# @app.route("/post/<int:post_id>")
# def show_post(post_id):
#   # show the post with the given id, the id is integer
#   return f"Post {post_id}"

# @app.route("/path/<path:subpath>")
# def show_subpath(subpath):
#   # show the subpath after /path/
#   return f"Subpath {escape(subpath)}"

# @app.route("/projects/")
# def projects():
#   return "The project page"

# @app.route("/about")
# def about():
#   return "The about page"

# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))


#################################################
# @app.route('/login', methods=['GET', 'POST']) #
#################################################

@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name=None):
  return render_template("hello.html", person=name)

# @app.route("/login", methods=["POST", "GET"])
# def login():
#   if request.method == "POST":
#     return request.form["username"]
#   else:
#     return f"<p>No hay nada en el body</p>"

# útil para revisar a posterior
# @app.route("/login", methods=["POST", "GET"])
# def login():
#   if request.method == "POST":
#     data = request.get_json()
#     if data and "username" in data:
#       return jsonify({"username": data["username"]})
#     return jsonify({"error": "No se encontró username en el JSON"}), 400
#   else:
#     return jsonify({"message": "No hay nada en el body"}), 400