# from flask import Flask
# app = Flask(__name__)  #create flask application object 

# @app.route('/') # define a route for the root URL
# def home():
#     return "<h2>Welcome to the first Webpage</h2>"
# @app.route('/about') # define a route for the root URL
# def about():
#     return "<h2>Welcome to the  about section of Webpage</h2>"
# @app.route('/contact<name>') # define a route for the root URL
# def contact():
#     return "<h2>Welcome to the contact info{{tej}}  </h2>"


# if __name__ == '__main__':  #run the application
#     app.run(debug = True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    username = "Tejashwini"   # you can change this or take from user
    return render_template("home.html", uname=username)

@app.route("/about")
def about():
    return "<h2>This is the About Page</h2>"

if __name__ == "__main__":
    app.run(debug=True)
