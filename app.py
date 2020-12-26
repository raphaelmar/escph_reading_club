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

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_reviews")
def get_reviews():
    reviews = mongo.db.reviews.find()
    return render_template("reviews.html", reviews=reviews)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            flash("email already used")
            return redirect(url_for("register"))

        register = {
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email").lower()
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("email").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", email=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if email already exists in db
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("email").lower()
                flash("Welcome, {}".format(
                    request.form.get("email")))
                return redirect(url_for(
                    "profile", email=session["user"]))
            else:
                # invalid password match
                flash("Incorrect email and/or password")
                return redirect(url_for("login"))

        else:
            # email doesn't exist
            flash("Incorrect email and/or password")
    return render_template("login.html")


@app.route("/profile/<email>", methods=["GET", "POST"])
def profile(email):
    # grab the sessions user's email form db
    email = mongo.db.users.find_one(
        {"email": session["user"]})["email"]

    if session["user"]:
        return render_template("profile.html", email=email)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        review = {
            "review_title": request.form.get("review_title"),
            "review_author": request.form.get("review_author"),
            "language_name": request.form.get("language_name"),
            "genre_name": request.form.get("genre_name"),
            "review_text": request.form.get("review_text"),
            "created_by": session["user"]

        }
        mongo.db.reviews.insert_one(review)
        flash("Review Succesfully added")
        return redirect(url_for("get_reviews"))

    genres = mongo.db.genres.find().sort("genre_name", 1)
    languages = mongo.db.languages.find().sort("language_name", 1)

    return render_template(
        "add_review.html", genres=genres, languages=languages)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        submit = {
            "review_title": request.form.get("review_title"),
            "review_author": request.form.get("review_author"),
            "language_name": request.form.get("language_name"),
            "genre_name": request.form.get("genre_name"),
            "review_text": request.form.get("review_text"),
            "created_by": session["user"]

        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Review succesfully updated")

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    genres = mongo.db.genres.find().sort("genre_name", 1)
    languages = mongo.db.languages.find().sort("language_name", 1)

    return render_template(
        "edit_review.html", genres=genres, languages=languages, review=review)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Task successfully deleted")
    return redirect(url_for("get_reviews"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
