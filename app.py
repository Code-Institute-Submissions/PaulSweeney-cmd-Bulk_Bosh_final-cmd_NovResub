""" Imorting operating system """
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
    """
    Function to render the home page
    """
    return render_template("home.html")

# ------------------------------------------------- profile
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Render profile page
    """
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
    """
    Render about page
    """
    return render_template("about.html")

# ------------------------------------------------- meal card page
@app.route("/get_meals")
def get_meals():
    """
    Function to render meals added in mongodb
    """
    site_meals = mongo.db.meals.find()
    # returns the page with all meals in the database
    return render_template("recipes.html", site_meals=site_meals)

# ---------------------------------- route to page with the full recipe on
@app.route("/meal_detail/<meal_id>")
def meal_detail(meal_id):
    """
    Render page for individual meal
    """
    # requesting the database to find the id of the meal user has selected
    each_meal = mongo.db.meals.find_one({"_id": ObjectId(meal_id)})

    # user gets directed to the single meal page with all data related to it
    return render_template("meal_page.html", each_meal=each_meal)

# ---------------------------------- route to meal creator profile
@app.route("/creator_profile/<username>")
def creator_profile(username):
    """ Displays profile when
    user clicks on link displayed for meal creator
    """
    # requesting the database to display selected user
    creator = mongo.db.users.find_one({"username": username})
    return render_template("creator_profile.html", creator=creator)

# ------------------------------------------------- register page
@app.route("/register_user", methods=["GET", "POST"])
def register_user():
    """
    Renders register page with functionality
    to add a new account
    """
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
    """
    Functionality to process login info tied to mongodb
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"], request.form.get("password")):
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

# ------------------------------------------------- add meal
@app.route("/add_meal", methods=["GET", "POST"])
def add_meal():
    """
    Processing new meal entries to mongo
    and rendering back to a page
    """
    if request.method == "POST":
        # assignign values as a list
        meal_ingredients = []
        ingredient_name_list = request.form.getlist("ingredient_name")
        ingredient_quantity_list = request.form.getlist("ingredient_quantity")
        ingredient_unit_list = request.form.getlist("ingredient_unit")

        # using for loop to iterate through ingredient values
        for i in range(len(ingredient_name_list)):
            ingredient = {
                "ingredient_name": ingredient_name_list[i],
                "ingredient_quantity": ingredient_quantity_list[i],
                "ingredient_unit": ingredient_unit_list[i]
            }
            # appending new data to the empty list variable above
            meal_ingredients.append(ingredient)

            # passing that new ingredients variable to be added to database
        new_meal = {
            "meal_name": request.form.get("meal_name"),
            "meal_description": request.form.get("meal_description"),
            "meal_ingredients": meal_ingredients,
            "meal_instructions": request.form.get("meal_instructions"),
            "added_by": session["user"],
            "calories": request.form.get("calories"),
            "carbs": request.form.get("carbs"),
            "protein": request.form.get("protein"),
            "cooking_time": request.form.get("cooking_time"),
            "servings": request.form.get("servings"),
            "url": request.form.get("url")
        }
        mongo.db.meals.insert_one(new_meal)
        flash("Your meal has been added! Thanks for sharing")
        return redirect(url_for("get_meals"))

    return render_template("add_recipe.html")

# ------------------------------------------------- edit meal
@app.route("/edit_meal/<meal_id>", methods=["GET", "POST"])
def edit_meal(meal_id):
    """
    Editing fields from mongodb
    and updating page & database
    """
    if request.method == "POST":
        # assignign values as a list
        meal_ingredients = []
        ingredient_name_list = request.form.getlist("ingredient_name")
        ingredient_quantity_list = request.form.getlist("ingredient_quantity")
        ingredient_unit_list = request.form.getlist("ingredient_unit")
        for i in range(len(ingredient_name_list)):
            ingredient = {
                "ingredient_name": ingredient_name_list[i],
                "ingredient_quantity": ingredient_quantity_list[i],
                "ingredient_unit": ingredient_unit_list[i]
            }
            # appending new data to the empty list variable above
            meal_ingredients.append(ingredient)

            # passing that new ingredients variable to be added to database
        update = {
            "meal_name": request.form.get("meal_name"),
            "meal_description": request.form.get("meal_description"),
            "meal_ingredients": meal_ingredients,
            "meal_instructions": request.form.get("meal_instructions"),
            "added_by": session["user"],
            "calories": request.form.get("calories"),
            "carbs": request.form.get("carbs"),
            "protein": request.form.get("protein"),
            "cooking_time": request.form.get("cooking_time"),
            "servings": request.form.get("servings"),
            "url": request.form.get("url")
        }

        mongo.db.meals.update({"_id": ObjectId(meal_id)}, update)
        flash("Your meal has been updated, thanks for sharing!")
        return redirect(url_for("get_meals"))

    meal = mongo.db.meals.find_one({"_id": ObjectId(meal_id)})
    return render_template("edit_recipe.html", meal=meal)

# ------------------------------------------------- delete meal
@app.route("/delete_meal/<meal_id>")
def delete_meal(meal_id):
    """
    Deleting an entry
    """
    # targeting meal id in database
    mongo.db.meals.remove({"_id": ObjectId(meal_id)})
    flash("Your meal has been deleted.")
    return redirect(url_for("get_meals"))

# ------------------------------------------------- logout
@app.route("/logout")
def logout():
    """
    Removing session data
    """
    flash("Goodbye")
    session.pop("user")
    return redirect(url_for("login"))

# -------------------------------------------------
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
