import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# setting the environment variables
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


# ------------------------------------------------- home page
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


# ------------------------------------------------- profile
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})
    print(username)
    # if the user in session is true they get directed to their profile page
    if session["user"]:
        return render_template("profile.html", username=username)
    return redirect(url_for("login"))


# ------------------------------------------------- about page
@app.route("/about")
def about():
    return render_template("about.html")


# ------------------------------------------------- meal card page
@app.route("/get_meals")
def get_meals():
    site_meals = mongo.db.meals.find()
    # returns the page with all meals in the database
    return render_template("recipes.html", site_meals=site_meals)


# ---------------------------------- route to page with the full recipe on
@app.route("/meal_detail/<meal_id>")
def meal_detail(meal_id):

    # requesting the database to find the id of the meal name user has selected
    each_meal = mongo.db.meals.find_one({"_id": ObjectId(meal_id)})

    # user gets directed to the single meal page with all data related to it
    return render_template("meal_page.html", each_meal=each_meal)



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
