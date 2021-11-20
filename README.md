# Bulk Bosh - Milestone 3 Project.
### [Click here for the Live Site](https://bulk-bosh-final-cmd.herokuapp.com/home)
<p align="center">
    <img width="400" height="400" src="static/images/logo.png">
</p>

### *Bulk Bosh is a Health app focussed targeting the weight training demographic. Users can log in and upload their recipes. There are nutritional recipes on the home page to follow and try for themselves. Click on the logo below for the live site.* ###

<br>

![Am I Responsive?](/static/images/responsive.png)
<br>

# **Site Creator Overview** - UX
## Presentation 
 * I wanted to create a site that gives users a meaningful and relevant experience. This needed to be visually and physically practical. The site layout works perfectly as it's not too overwhelming in regards to styling. Some sites can be noisy on a visual level, my colour scheme for pretty much every project I've made up to this point follow a similar pattern and I've based it on my own preferences as if I was acting as the end user. I feel the site could improve as time goes and theres always room for more functionality and styling on but for now I've kept it simple and to the point. a black white and yellow colour scheme works perfectly for my target demographic. It's eye catching, sharp and well structured.
 * The text content backdrop works well against the image, the page image would not have been viable to use if I didn't style the containers with HEX code: ```#070707e3```, the original idea was to have a plain black backdrop but I felt this would've de-valued the site and made it too basic, this way the content stands out better and gives the user a positive experience as it shows effort. This style also works well across the rest of the site in regards to containers, forms etc as it looks more structured and professional.
 * This section is just a site creators overview, functionality from an end user point can be found in the end user testing section.


# **User Stories**
## *First time Visitor Goals*
- To browse the site for a variety of meals.
- Easily navigate through the site via a well presented navigation menu.
- To have the ability to access the site on a variety of devices on the go if I'm not at a computer desk.
- To create an account and register my information.
- To find out more about the site.
- To check the site for any new recipes for me to follow.
## *Registered user goals*
- To log in and out of my account.
- To easily navigate through the pages.
- Create my own meals for people to look at and try for themselves.
- Edit my own meals.
- Delete my meals if I want to.
- To browse meals created by others.
- To access users profile information and connect via their social network links and or email address.
- To check the site for any new recipes for me to follow.
## *Site Owner goals*
- To attract more people to eat healthily with straight forward information, macros belong on Google!. 
- This is a straight talking recipe app (break away from the 5 shakes a day lifestyle).
## *Future site goals*
- Add functionalioty for users to be able to update their profile information.
- Add functionality to share recipes to external platforms like WhatsApp, Facebook and Instagram.
- Add more functionality to allow the user to share their profile to their external platforms if they wanted to use their profile to network.
- Chop and change the recipes on the recipe page on a regular basis.
- Allow the user to download recipes from the site.
- Add a category function once the site has gained enough following to allow for easier navigation.
- Allow user to upload thjeir own images for the profile and meals.

<br>

# **Features**
- An array of recipes to choose from
- Clear navigation with the use of a navigation bar and side navigation bar on mobile and tablet format
- Log in/out of their profile and add their own recipes
- Register for an account

# **Future Features**

- Incorporate sponsorship from supplement companies to promote their products
- Link up the app to a fitness app
- Share their recipes on social media and incorp[orate reaction buttons to each recipe
- Add an image upload form so they dont have to copy and paste a URL

<br>

# **Strategy**
- The goal is for the site is to allow users to self promote and connect through their love of healthy food for a healthy lifestyle. Simple and straight forward social networking for a person that likes to cut the hassle and have an app with clear navigation, good food and new connections.
# **Scope**
- HOME: The user is welcomed on to the site showing a welcome message with a brief overview of the aim of the site. 
- WHO WE ARE: They can click on the the about page which gives them a breif insight in to the site creators story.
- MEALS: They can have a look at the pre-loaded recipes on the second tab along with the opportunity to click on the users name which will take them to that users profile where they can connect through Facebook and Instagram.
- LOGIN: directs them to a login page with a link to register 
- REGISTER: This asks for all information to buid their profile and incluide any social links. This will then direct them to their created profile. Once registered they can upload recipes, edit and delete them. See below for availability for registered and non-registered users:

<br>

# **User Accessibility & Restrictions**
## *Registered*
1. Upload recipes
2. Edit recipes
3. The ability to attach social network links to recipes
4. Connect to other users through external social networks
5. Login / Logout 
6. Read the about section
7. Navigate to Home page
8. View meals
9. View a users profile via the meals section
## *Un-registered*
1. Read the about section
2. Navigate to Home page
3. Register
4. View Meals
5. View users profile via the meals section but not their contact information

<br>

# **Technologies and Design**
* DataBase Schema was created with [Moqups](https://moqups.com/)

<br>


<p align="left">
    <img width="900" height="500" src="static/images/final-schema.png">
</p>


<br>

## *Typography*

* Font Icons from [Font-Awesome](https://fontawesome.com/)
* I used Barlow & Big Shoulders fonts from [Google Fonts](https://fonts.google.com/)

<br>

## *Wireframes*
* [Desktop View](/static/images/MONITOR.png)
* [Mobile View](/static/images/PHONE.png)
* [Tablet View](/static/images/TABLET.png)

<br>

## *Imagery & Presentation*
- Background imagery spanning across all pages courtesy of [Cottonbro @ Pexels](https://www.pexels.com/@cottonbro)
- Images for pre loaded meals were sourced from the same recipes at [BodyBuilding.com](https://www.bodybuilding.com)

 <br>

## *Programming languages*
* [HTML](https://en.wikipedia.org/wiki/HTML/) for the building blocks
* [CSS](https://en.wikipedia.org/wiki/CSS/) for the makeup
* [JavaScript](https://www.javascript.com/) for the moving parts
* [Python](https://www.python.org/) for the functionality

<br>

## *Libraries & Frameworks*
* [Materialize](https://materializecss.com/getting-started.html)
* [JQuery](https://jquery.com/)  
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)

<br>

## *MongoDB Python Driver*
* [PyMongo](https://docs.mongodb.com/drivers/pymongo/)  

<br>

## *Resources*
- W3Schools for syntax references
- Slack for tutor support
- YouTube for the glass button effects
- Pre Loaded meals were sourced from [BodyBuilding.com](https://www.bodybuilding.com/)

<br>

# **TESTING**
## **Production Bugs & Fixes - PRESENTATION**

<br>

## *Bug/Issue?*
Icons & text wouldn't center on full screen view

![Am I Responsive?](static/images/icon_position.png)
## *Resolved/Remaining?* - Resolved
```div class="col m4 s12"``` to re-position them.

## *Bug/Issue?*
* Meal creator profile not rendering when user clicks on their username
## *Resolved/Remaining?* - Resolved
Syntaxt incoerrect in the app route, tried targeting user Id instead of username.


## *Bug/Issue?*
* Meals template in the recipes.html file not rendering after new meal is added in the add_recipe template.

![Am I Responsive?](static/images/recipe-card.png)
## *Resolved/Remaining?* - Resolved
Removed for loop in ```add_meal()``` - code commented out.

<br>

## *Bug/Issue?* 
* Recipe cards not positioning horizontally next to each other, tried altering grid sizes and applying container outside the for loop in the recipes.html file.

![Am I Responsive?](static/images/recipe-div.png)
## *Resolved/Remaining?* - Resolved

Moved the row div above the for loop and below the endfor in the recipes.html file to allow cards to sit horizontally.

<br>

## *Bug/Issue?* 

* New users profile information isn't being displayed when the profile page renders
![Am I Responsive?](static/images/profile-info.png)

## *Resolved/Remaining?* - Resolved
The original idea was to extract the new profile information from a seperate collection to the user collection, which only had the username and password. I combined the profile info fields in with the register fields in the register function. this allowed an updated collection and for me to get info using jinja templating.

<br>

## **Production Bugs & Fixes - DATA**

<br>

## *Bug/Issue?*
* Data sent to MongoDB from the add recipe form not being displayed.

## *Resolved/Remaining?* - Resolved
Re-structured the python app route for adding a meal, had to declare the ingredients to a new variable and append to another variable with the value of an empty list, this allowed the cloned html ingredients form to pass the data back to mongo db and then render to the recipe card on the recipe page.

<br>

# **End User Testing**
### **Home Page**
| Desktop | Phone | Tablet |
| :---: | :---: | :---: |
| ![](/test-images/desktop-home.png) | ![](test-images/home-phone-top.png) | ![](test-images/tablet-home.png) |
|| ![](test-images/home-phone-bottom.png) |

**User Feeedback** 

When I come on to the site the first thing I see is a well laid out home page. The colours are eye catching and I can see all the available pages at the top. The page has a great structure. The background looks really good with the colours.

<br>

## *First time Visitor Goals*
### **To find out more about the site.**
| Desktop | Phone | Tablet |
| :---: | :---: | :---: |
| ![](/test-images/desktop-about.png) | ![](test-images/about-phone-top.png) | ![](test-images/tablet-about.png) |
||![](test-images/about-phone-bottom.png) |

**User Feeedback**

The information on the page is thorough and interesting. It explains what the site is about and why they have created it. It also explains what they are looking to do to the site in future and lets you know there are people to connect with. It also has a button you can click on to register or log in which informs me that I can create an account if I wanted to.|

<br>

### **To browse the site for a variety of meals.**
| Desktop | Phone | Tablet |
| :---: | :---: | :---: |
| ![](/test-images/desktop-meals.png) | ![](test-images/phone-meals.png) | ![](test-images/tablet-meals.png) |

**User Feedback**

The page is really well laid out, everything is the same size and the pictures look really appealing and colourful. I also like the way the creators have made it to look like a menu from a restaurant. It's a nice touch and finishes off the theme of the site nicely.

<br>

### **Meal Details**
| Select button from meals page | Desktop | Phone | Tablet |
| :---: | :---: | :---: | :---: |
| ![](/test-images/view-button.png) | ![](/test-images/desktop-meal.png) | ![](test-images/meal-phone-top.png) | ![](test-images/meal-tablet-top.png) |
|| |![](test-images/meal-phone-bottom.png) | ![](test-images/meal-tablet-bottom.png) |

**User Feedback**

The page is full of useful information, it's clear and simple for me to read. The nutrition infomation can come in handy if I'm following a strict diet as it gives me an idea of what I can and can't have. The directions are simple to follow and I also like that I can see how long a meal would take to cook and how many people I can cook it for.

<br>

### **To create an account and register my information.**
| Desktop | Phone | Tablet |
| :---: | :---: | :---: |
| ![](/test-images/desktop-register-top.png) | ![](test-images/register-phone-top.png) | ![](test-images/register-tablet-top.png) |
| ![](/test-images/desktop-register-bottom.png) | ![](test-images/register-phone-bottom.png) | ![](test-images/register-tablet-bottom.png) |

**User Feedback**

I like that the register form asks you what your likes and dislikes are which adds a personal touch to my account. It also asks for my contact infomation which is great for me to connect with other people that like staying healthy. This could also be a way for me to connect with people that go to the gym in my area. The guides are good as they tell you what you can and can't write.

<br>

### **Easily navigate through the site via a well presented navigation menu.**
*The screenshots only display what the user would see in mobile view as page navigation functionality has already been demonstrated for the main nav bar so far*

| Logged In  | Logged Out | Logged In | Logged Out |
| :---: | :---: | :---: | :---: |
| ![](test-images/phone-side-nav.png)  | ![](test-images/side-nav-phone.png)  | ![](test-images/tablet-side-nav.png)  | ![](test-images/side-nav-tablet.png)

**User Feedback**

When I access the site on my phone the menu has a really eye catching icon at the top, the colours look great and they match the rest of the site, the name stands out in a good way for a food based website. The page title text looks good.

<br>

## *Registered User Goals*
### **To log in and out of my account.** ###
| Desktop | Phone | Tablet |
| :---: | :---: | :---: |
| ![](/test-images/desktop-login.png) | ![](test-images/phone-login.png) | ![](test-images/tablet-login.png) |
| Profile | Profile | Profile | Profile |                                                                                  
| ![](/test-images/desktop-profile.png) | ![](test-images/phone-profile.png) | ![](test-images/tablet-profile.png) |
| Logged Out | Logged Out | Logged Out |                                                                                                     
| ![](/test-images/desktop-logout.png) | ![](test-images/phone-logout.png) | ![](test-images/tablet-logout.png) |

**User Feedback**

I like the way my profile page shows straight away when I log in to my account.

<br>

### **Create my own meals for people to look at and try for themselves.** ###
| Desktop | Phone | Tablet |
| :---: | :---: | :---: |
| ![](/test-images/desktop-add_meal-top.png) | ![](test-images/phone-add_meal_top.png) | ![](test-images/tablet-add_meal-top.png) |
| ![](/test-images/desktop-add_meal-bottom.png) | ![](test-images/phone-add_meal-bottom.png) | ![](test-images/tablet-add_meal-bottom.png) |

**User Feedback**

The form is really thorough, it asks me for all kinds of information I need to put for my recipe. I like that I can add a picture and that it has to be a certain size. There is a button at the bottom of the page that allows me to add more ingredients which is great if I needed to add a recipe for a good meal. The guidelines on what you can write and hoe much you can write shows the page is structured and has to be a certain way for it to work.

<br>

### *Meal Added*
| Desktop | Phone | Tablet |
| :---: | :---: | :---: |
| ![](/test-images/desktop-meal_added-top.png) | ![](test-images/phone-meal_added-top.png) | ![](test-images/tablet-meal_added-top.png) |
| ![](/test-images/desktop-added_meal-bottom.png) | ![](test-images/phone-meal_added-bottom.png) | ![](test-images/tablet-meal_added-bottom.png) |

**User Feedback**

I like the fact my meal has been added to the rest of the meals instead of separately, they look part of the page as if the site creators have added it themselves. It's exciting to see it there and to know that I've made a contribution to the site to help others learn new meals and ways of cooking.

<br>

### *New Meal Details*
| Select view button | Desktop | Phone | Tablet |
| :---: | :---: | :---: | :---: |
| ![](/test-images/user-meal.png) |![](/test-images/desktop-new_meal.png) | ![](test-images/phone-new_meal-top.png) | ![](test-images/tablet-new_meal-top.png) |
|| |![](test-images/phone-new_meal-bottom.png) |![](test-images/tablet-new_meal-bottom.png) |

**User Feedback**

My meal looks great in detail, I can see all my information just like the ones that are on the site. The picture shows perfectly and it's all laid out and clear to read.

<br>

### **To access users profile information and connect via their social network links and or email address.**
*Only users that have created an account can view other users contact info and social media links.*

| Click on 'Creator' username  | Desktop | Phone | Tablet | 
| :---: | :---: | :---: | :---: |
| ![](/test-images/user-profile-name.png) | ![](test-images/desktop-user-profile.png) | ![](test-images/phone-user-profile.png) | ![](test-images/tablet-user-profile.png) |

**User Feedback**

I think this is a great feature to have on a recipe site. It targets people that are in to the same thing. If any of the users are personal trainers of dieticians this can take a lot of headache out of contacting them as their contact information is right there. I can also learn about them a little though their likes and dislikes. We can all follow each other on social media and take inspiration from workouts and nutrition. It's a great thing to have on this site. Impressive.

<br>

### **Edit my own meals.**
| Select edit button | Desktop | Phone | Tablet |
| :---: | :---: | :---: | :---: |
| ![](/test-images/user-meal.png) | ![](/test-images/desktop-edit_meal-top.png) | ![](test-images/phone-edit_meal-top.png) | ![](test-images/tablet-edit_meal-top.png) |
|| ![](/test-images/desktop-edit_meal-bottom.png) | ![](test-images/phone-edit_meal-bottom.png) | ![](test-images/tablet-edit_meal-bottom.png) |
|| ![](/test-images/desktop-meal_updated.png) | ![](test-images/phone-meal_updated.png) | ![](test-images/tablet-meal_updated.png) |

**User Feedback**

The site brought up all my current meal information which works well as I can select everything I want to edit there and then. I can make slight adjustments to what I want without having to type everything out again. This is really convenient and I can even change my image to an updated one if my recipe changes in looks.

<br>


### **Delete my meals if I want to.**
| Select remove button | Desktop | Phone | Tablet |
| :---: | :---: | :---: | :---: |
| ![](/test-images/user-meal.png) | ![](/test-images/desktop-meal_deleted.png) | ![](test-images/phone-meal_deleted.png) | ![](test-images/tablet-meal_deleted.png) |

**User Feedback**

I was able to delete my meal instantly with no problems.

<br>

# **TESTING - Responsivness & Devices Used**

## Devices
**Samsung Galaxy A21s**
- Responsiveness = ```Good.```
- Speed = ```Good.```
- Imagery = ```Good.```
- Resolution = ```Good.```
- Issues regarding overlapping text, page structure different? = ```None found.```
## Browsers
**Google Chrome**
- Responsiveness = ```Good.```
- Speed = ```Good.```
- Imagery = ```Good.```
- Resolution = ```Good.```
- Issues regarding overlapping text, page structure different? = ```None found.```

**Firefox**
- Responsiveness = ```Good.```
- Speed = ```Excellent.```
- Imagery = ```Good.```
- Resolution = ```Good.```
- Issues regarding overlapping text, page structure different? = ```None found.```

## Additional Comments
Nothing to add.

<br>

# **Deployment**

* To view the live version go to [BulkBosh Live](https://github.com/PaulSweeney-cmd/Bulk_Bosh_final-cmd)
* Click on the Bulk_Bosh logo at the top of the page

<br>

<p align="left">
    <img width="400" height="400" src="static/images/BULK.png">
</p>

<br>

## *Run Local*

Log in to GitHub
* Go to [My Page](https://github.com/PaulSweeney-cmd/Bulk_Bosh_final-cmd)
* Find my Repositories
* Select CODE button

![Am I Responsive?](static/images/select-code.png)

* Copy the URL and open your chosen IDE
* Open up a command terminal and paste in the URL you coped
* Make sure you enter git clone before you paste the URL and press enter
#
## *MongoDB*

Log in to your MongoDB account and create a new cluster and a new Database
then go back to GitHub, create an env.py file in your workspace
Store your variables as follows:
 
* > ```os.environ.setdefault("IP", "0.0.0.0")```
* > ```os.environ.setdefault("PORT", "5000")```
* > ```os.environ.setdefault("SECRET_KEY", "some-value")```
* > ```os.environ.setdefault("MONGO_URI", "some-value")```
* > ```os.environ.setdefault("MONGO_DBNAME", "some-value")```

<br>

* You can customise your password or use RandomKeygen.com for an auto generated secure password
* Go back to MongoDB and select collections from the tabs above your cluster
* Click CONNECT underneath your cluster name
* Select "Connect your application" making sure you choose Python as your driver and 3.6 or later for the version
* Copy the connection string below that
* Make sure you update the Password and Database name in that string with your own, DO NOT USE THE CREDENTIALS YOU LOG IN WITH!
* If you're unsure of what your passowrd is then go to Database Access on the left
* Click the edit button on the right to get your password
* Go back to your workspace and create a .gitignore file by typing touch .gitignore
* The reason for this is so GitHub doesnt share sensitive data, this file should include the environment variable page
- Type ```git status``` to make sure yur environment variable file isn't being tracked, you can see the results in the terminal. If it is then go back in to your file and make sure it's saved properly.
- If everything checks out you can type ```python3 app.py``` to run your app.
#
## **Creating and Deploying an app with Heroku**

## *GitHub*

Create a requirements.txt file type the following into your terminal: pip3 freeze --local > requirements.txt
* Create a Procfile by typing ```echo web: python3 app.py > Procfile```
* Add and commit both files

## *Heroku*

* Create an account and create a new app by clicking NEW in the top right hand corcer of the screen
* Choose the best region closest to you
* Click Create App
* Click on the deploy tab and then navigate to the GitHub button and select
* Scroll down to Reveal Config Vars and select
* Enter the environment variables and their values you entered in to your environment variable file in GitHub
* Once you have completed those fields click on Automatic Deploys and select the Deploy Branch button, this will then connect to GitHub and a code window will open up below and start to build your app
* Once it has finished select View and you'll be abkle to see any code you wrote to test your repository.


## <p align="center">```Happy Coding!```</p>
# 
## *Assessment Feedback*
This can be found in a seperate file [Here](/Assessment_feedback.md). This file includes the issues highlighted and what I've done to improve and rectify them. 
#
<br>

## *Credits and Acknowledgements*
- Recipe card bug was discussed and resolved with Scott from Tutor Support at [Code Institute](https://codeinstitute.net//)
- Add meal function in python was discussed in depth with Sheryl from Tutor support at [Code Institute](https://codeinstitute.net//)
- Creator profile App route issue discussed and rectified with Sean from Tutor Support at [Code Institute](https://codeinstitute.net//)
- I would like to thank my Mentor Nishant Kumar for his valuable insight in to the improvements needed for UX 
- Preloaded recipes were sourced from [BodyBuilding.com](https://www.bodybuilding.com)
- Python functionality sourced from Task Manager walkthrough  with Tim Nelson as well as the same functionality code extended for adding recipes and editing recipes discussed with code institute and written by myself.
- Python code for linking profile to meal cards written by myself.
