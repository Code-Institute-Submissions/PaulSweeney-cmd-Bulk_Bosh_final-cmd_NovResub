# Bulk Bosh - Milestone 3 Project.

### Bulk Bosh is a Health app focussed targeting the weight training demographic. Users can log in and upload their recipes. There are nutritional recipes on the home page to follow and try for themselves.
#


[![Am I Responsive?](/static/images/logo.png)](https://bulk-bosh-final-cmd.herokuapp.com/home)
# UX

![Am I Responsive?](/static/images/am-i-responsive.png)

# User Stories
First time Visitor Goals As a first time visitor I would like to do the following:

- To follow pre loaded recipes for my own meal times
- To create an account where I can enter my own recipes and food hacks
- To Create, Read, Update and Delete my information

Site Owners goals:

- To attract more people to eat healthily with straight forward information, macros belong on Google!. 
- This is a straight talking recipe app (break away from the 5 shakes a day lifestyle)

Future site goals:

- Add functionality to share recipes to external platforms like WhatsApp, Facebook and Instagram
- Add more functionality to allow the user to share thweir profile to their external platforms if they wanted to use their      profile to network.
- Chop and change the recipes on the recipe page on a regular basis
- Allow the user to download recipes from the site
- Add a category function once the site has gained enough following to allow for easier navigation
- Allow user to upload thjeir own images for the profile and meals 

# Features

- An array of recipes to choose from
- Clear navigation with the use of a navigation bar and side navigation bar on mobile and tablet format
- Log in/out of their profile and add their own recipes
- Register for an account

# Future Features

- Incorporate sponsorship from supplement companies to promote their products
- Link up the app to a fitness app
- Share their recipes on social media and incorp[orate reaction buttons to each recipe

------------------------------------------------------------------------------------------------
## WIREFRAMES:
### Register & About pages
![Am I Responsive?](/static/images/iPad-one.jpg)
### Login, Profile, Add Meal, Meals & Home
![Am I Responsive?](/static/images/iPad-two.jpg)
### About, Profile, Side Nav & Meals
![Am I Responsive?](/static/images/iPhone-one.jpg)
### Login, Home & Register
![Am I Responsive?](/static/images/iPhone-twoejpg)

------------------------------------------------------------------------------------------------
## Desk-top View
![Am I Responsive?](/static/images/desktop-view.jpg)

## STRATEGY:
- The goal is for the site is to allow users to self promote and connect through their love of healthy food for a healthy lifestyle. Simple and straight forward social networking for a person that likes to cut the hassle and have an app with clear navigation, good food and new connections.
#
## SCOPE:
- HOME: The user is welcomed on to the site showing a welcome message with a brief overview of the aim of the site. 
- WHO WE ARE: They can click on the the about page which gives them a breif insight in to the site creators story.
- MEALS: They can have a look at the pre-loaded recipes on the second tab along with the opportunity to click on the users name which will take them to that users profile where they can connect through Facebook and Instagram.
- LOGIN: directs them to a login page with a link to register 
- REGISTER: This asks for all information to buid their profile and incluide any social links. This will then direct them to their created profile. Once registered they can upload recipes, edit and delete them. See below for availability for registered and non-registered users:

### Registered:
* Upload recipes
* Edit recipes
* The ability to attach social network links to recipes
* Connect to other users through external social networks
* Login / Logout 
* Read the about section
* Navigate to Home page
* View meals
* View a users profile via the meals section
### Non-registered:
* Read the about section
* Navigate to Home page
* Register
* View Meals
* View users profile via the meals section but not their contact information



# Technologies and Design
- DataBase Schema was created with [Moqups](https://moqups.com/)
![Am I Responsive?](/static/images/final-schema.png)
- Font Icons from [Font-Awesome](https://fontawesome.com/)
- I used Barlow & Big Shoulders fonts from [HTML](https://fonts.google.com/)

# Imagery
- Background imagery courtesy of Cottonbro at [Pexels](https://www.pexels.com//)
- Images for pre loaded meals were sourced from the same recipes at [BodyBuilding.com](https://www.bodybuilding.com)

# Programming languages
- [HTML](https://en.wikipedia.org/wiki/HTML/) for the building blocks
- [CSS](https://en.wikipedia.org/wiki/CSS/) for the makeup
- [JavaScript](https://www.javascript.com/) for the moving parts
- [Python](https://www.python.org/) because it looks cool

# Libraries & Frameworks
- [Materialize](https://materializecss.com/getting-started.html)
- [JQuery](https://jquery.com/)  
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- PyMongo  
- Werkzeug

# Resources
- W3Schools for syntax references
- Slack for tutor support
- YouTube for the glass button effects
- Pre Loaded meals were sourced from [BodyBuilding.com](https://www.bodybuilding.com/)


# Credits and Acknowledgements
- Recipe card bug was discussed and resolved with Scott from Tutor Support at [Code Institute](https://codeinstitute.net//)
- Add meal function in python was discussed in depth with Sheryl from Tutor support at [Code Institute](https://codeinstitute.net//)
- Creator profile App route issue discussed and rectified with Sean from Tutor Support at [Code Institute](https://codeinstitute.net//)
- I would like to thank my Mentor Nishant Kumar for his valuable insight in to the improvements needed for UX 
- Preloaded recipes were sourced from [BodyBuilding.com](https://www.bodybuilding.com)
- Python functionality sourced from Task Manager walkthrough  with Tim Nelson as well as the same functionality code extended for adding recipes and editing recipes discussed with code institute and written by myself.
- Python code for linking profile to meal cards written by myself.

#  Bugs & Fixes
#  Imagery and Presentation:

## Bug/Issue: 
### Icons & text wouldn't center on full screen view

![Am I Responsive?](static/images/icon_position.png)
## Resolved/Remaining?
### - Resolved: div class="col m4 s12" to re-position them.
#
## Bug/Issue: 
### Meals template in the recipes.html file not rendering after new meal is added in the add_recipe template.

![Am I Responsive?](static/images/recipe-card.png)
## Resolved/Remaining?
### - Resolved: Removed for loop in add_meal function - code commented out.
#

## Bug/Issue: 
### Recipe cards not positioning horizontally next to each other, tried altering grid sizes and applying container outside the for loop in the recipes.html file.

![Am I Responsive?](static/images/recipe-div.png)
## Resolved/Remaining?
### - Resolved: Moved the row div above the for loop and below the endfor in the recipes.html file to allow cards to sit horizontally.
#
### Bug/Issue: New users profile information isn't being displayed when the profile page renders
![Am I Responsive?](static/images/profile-info.png)

## Resolved/Remaining?
### - Resolved: The original idea was to extract the new profile information from a seperate collection to the user collection, which only had the username and password. I combined the profile info fields in with the register fields in the register function. this allowed an updated collection and for me to get info using jinja templating.
#
# Data:

## Bug/Issue
### - Data sent to MongoDB from the add recipe form not being displayed.

## Resolved/Remaining?

### - Resolved: Re-structured the python app route for adding a meal, had to declare the ingredients to a new variable and append to another variable with the value of an empty list, this allowed the cloned html ingredients form to pass the data back to mongo db and then render to the recipe card on the recipe page.
#

## Bug/Issue
### -  Meal creator profile not rendering when user clicks on their username
## Resolved/Remaining?
### - Resolved: Syntaxt incoerrect in the app route, tried targeting user Id instead of username.
#

# Deployment:

### -  To view the live version go to [My Page](https://github.com/PaulSweeney-cmd/Bulk_Bosh_final-cmd)
### -  Click on the Bulk_Bosh logo at the top of the page
![Am I Responsive?](static/images/BULK.png)

## Run Local:

- Log in to GitHub
- Go to [My Page](https://github.com/PaulSweeney-cmd/Bulk_Bosh_final-cmd)
- Find my Repositories
- Select CODE button

![Am I Responsive?](static/images/select-code.png)

- Copy the URL and open your chosen IDE
- Open up a command terminal and paste in the URL you coped
- Make sure you enter git clone before you paste the URL and press enter
------------------------------------------------------------------------------------------------
## MongoDB

Log in to your MongoDB account and create a new cluster and a new Database
then go back to GitHub, create an env.py file in your workspace
Store your variables as follows:
 
 - os.environ.setdefault("IP", "0.0.0.0")
 - os.environ.setdefault("PORT", "5000")
 - os.environ.setdefault("SECRET_KEY", "some-value")
 - os.environ.setdefault("MONGO_URI", "some-value")
 - os.environ.setdefault("MONGO_DBNAME", "some-value")

### You can customise your password or use RandomKeygen.com
------------------------------------------------------------------------------------------------

- Go back to MongoDB and select collections from the tabs above your cluster
- Click CONNECT underneath your cluster name
- Select "Connect your application" making sure you choose Python as your driver and 3.6 or later for the version
- Copy the connection string below that
- Make sure you update the Password and Database name in that string with your own, DO NOT USE THE CREDENTIALS YOU LOG IN WITH!
- If you're unsure of what your passowrd is then go to Database Access on the left
- Click the edit button on the right to get your password
------------------------------------------------------------------------------------------------
- Go back to your workspace and create a .gitignore file by typing touch .gitignore
- The reason for this is so GitHub doesnt share sensitive data, this file should include the following:
- env.py
- __pycache__/

- Type git status to make sure the env.py file isn't being tracked, you can see the results in the terminal. If it is then go back in to your file and make sure it's saved properly.
- If everything checks out you can type pythone app.py to run your app.
------------------------------------------------------------------------------------------------
## Creating and Deploying an app with Heroku

### In GitHub:

- Create a requirements.txt file type the following into your terminal: pip3 freeze --local > requirements.txt
- Create a Procfile by typing the following: echo web: python3 app.py > Procfile
- Add and commit both files

### In Heroku:

- Create an account and create a new app by clicking NEW in the top right hand corcer of the screen
- Choose the best region closest to you
- Click Create App
#
- Click on the deploy tab and then navigate to the GitHub button and select
- Scroll down to Reveal Config Vars and select
- Enter the environment variables and their values you entered in to your env.py file in GitHub
- Once you have completed those fields click on Automatic Deploys and select the Deploy Branch button, this will then connect to GitHub and a code window will open up below and start to build your app
- Once it has finished select View and you'll be abkle to see any codce you wrote to test your repository.


HAPPY CODING!

# HTML CHECKER
------------------------------------------------------------------------------------------------
### - About Page
![Am I Responsive?](static/images/about.png)
### - Add Recipe
![Am I Responsive?](static/images/add-recipe.png)
### - Creator-profile
![Am I Responsive?](static/images/creator-profil.png)
### Edit Recipe
![Am I Responsive?](static/images/edit-recipe.png)
### - Home Page
![Am I Responsive?](static/images/home.png)
### - Index.html
![Am I Responsive?](static/images/index.png)
### - Login
![Am I Responsive?](static/images/login.png)
### Meal Page
![Am I Responsive?](static/images/meal-page.png)
### - Profile
![Am I Responsive?](static/images/profile.png)
### - Recipes
![Am I Responsive?](static/images/recipes.png)
### - Register
![Am I Responsive?](static/images/register.png)
------------------------------------------------------------------------------------------------
# CSS Validator
![Am I Responsive?](static/images/css-validate.png)

















