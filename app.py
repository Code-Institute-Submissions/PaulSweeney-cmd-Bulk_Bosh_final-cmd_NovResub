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

    # requesting the database to find the id of the meal user has selected
    each_meal = mongo.db.meals.find_one({"_id": ObjectId(meal_id)})

    # user gets directed to the single meal page with all data related to it
    return render_template("meal_page.html", each_meal=each_meal)


# ---------------------------------- route to meal creator profile
@app.route("/creator_profile/<username>")
def creator_profile(username):
    # requesting the database to display the user attahced username in meal card 
    creator = mongo.db.users.find_one({"username": username})
    return render_template("creator_profile.html", creator=creator)


# ------------------------------------------------- register page
@app.route("/register_user", methods=["GET", "POST"])
def register_user():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # error displays if username exists
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register_user"))

        # creating new data to be passed to database
        register_user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "profile_name": request.form.get("profile_name"),
            "profile_age": request.form.get("profile_age"),
            "profile_city": request.form.get("profile_city"),
            "profile_likes": request.form.get("profile_likes"),
            "profile_dislikes": request.form.get("profile_dislikes"),
            "profile_about": request.form.get("profile_about"),
            "social_links": [{
                "facebook": request.form.get("facebook"),
                "instagram": request.form.get("instagram")
            }],
            "email_address": request.form.get("email_address")
        }
        flash("Registration Successful. Nice to meet you")
        mongo.db.users.insert_one(register_user)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        return redirect(url_for('profile', username=session['user']))

    return render_template("register.html")


# ------------------------------------------------- login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get(
                            "username").lower()
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")




if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
