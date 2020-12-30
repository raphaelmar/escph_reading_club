# European School of Copenhagen Reading club

The European School of Copenhagen is a multicultural and multilingual school, where students are encouraged to develop skills that allow them to thrive in a diverse environment by promoting their use of languages. Reading is an essential part of this process. The aim of the Reading Club is to provide students with a place where they can share a review of their favourite stories with their peers and can search for new reading ideas based on their peers' positive experiences. The site is in English as it is the official communication language of the school, but the reviews and the reviewed books can be in the language of their choice, the other official languages of the school being French, German and Danish. 

## UX

The Reading club is aimed at students who are independent readers and who are able to write a concise book review (upper end of primary school and secondary school). Visually, the site re-uses the colour code that is used by the school's main website [Europaskolen](https://europaskolen.sag.dk/). It is simple, clear and clutter free, focusing on the main element that are the review cards.

### User stories

As a user of the of the Reading club:
* I can enter the basic details of the book I have read (title, author, language, genre) so that it can be easily identified by other users.
* I can write a review of the book I have enjoyed so that it is shared with other users and they are encouraged to read the book through my review.
* I can edit and delete my own reviews so that I can amend any mistakes or completely remove a review if I do not want it on the Club any longer.
* I can read other users' reviews so that I can discover new stories and be encouraged to read them. 
* I can "like" other users' reviews to express my appreciation of the review and/or the book reviewed.
* I can search the bank of reviews using keywords if I am looking for something in particular (books in French only for example).
* I can be a registered user and log in if I want to write and publish my own reviews or I can be a non-registered user if I just want to read reviews and "like" them.

### Wireframes

![Home page](/static/images/ESCPHRC_home.png)
![Review card](/static/images/review_card.png)
![User's own review](/static/images/user_own_review.png)
![Log in mobile view](/static/images/login_mobile_view.png)
![Log in tablet view with side navbar](/static/images/login_tablet_sidenav.png)


## Features

* Home page
    * The landing page of the site greets the user with a welcome message in the 4 official languages of the school, and briefly indtroduces the concept to them. They can directly search the existing reviews or scroll through them, but they are invited to register/log in and write their own. The links to the login and register pages are visible on the right-hand side of the navbar. They can also click on the like button for each of the reviews.
* Register page
    * The user is invited to provide their first name, last name, password and email address to become a registered user. They can also click on a log in link if they are already registered.
* Log in page
    * Registered users can log in directly using the email address and password or click on the registeer account button if they are not registered yet.
*  Profile page
    * Here, the user can see a personalised welcome message and all the reviews that they have written. For each review they can also access via two buttons the edit and delete reviews functions. In the navbar they can access the new review link where they will be able to write their review. Hitting the delete button triggers a modal that asks the users if they really want to delete the review, they can confirm or click anywhere else to go back to the profile page.
* Add review page
    * This is a form containing 5 fields (3 texts and 2 dropdowns) that the user must fill in to complete their review. They should provide a book title, the name of the author, the language, the genre and finally they can write their review, at the moment they are limited to 500 signs, but this could be changed if longer reviews are required.
* Edit review page
    * The user is presented with the form that they have previously filled in and they can amend any of the fields then submit the changes by hitting the edit button and then return to their Home or Profile page to see the changes, they can also choose to cancel those changes.

## Features left to implement

* The user's profile page will use the first name rather than the email to greet the user.
* "Likes" will be limited to one per user per review.

## Technologies used

* HTML 5
* CSS 3
* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) (micro framework used for jinja templates and werkzeug toolkit)
* Javascript (opening and closing of delete modal)
* [Google Fonts](https://fonts.google.com/) (Open Sans)
* [Font Awesome](https://fontawesome.com/) (all icons)
* [Materialize](https://materializecss.com/) (overall design of website)
* [JQuery](https://jquery.com/) (triggering sidenav bar, collapsible and forms)
* [Github](https://github.com/) (code hosting platform for version control)
* [Gitpod](https://gitpod.io/) (development environment) 
* [MongoDB](https://www.mongodb.com/) (database for the project)
* [Heroku](https://heroku.com/) (platform where the site is deployed)

## Testing

* Code validity:

HTML has been validated using [W3 validator](https://validator.w3.org/) and formatted using [Freeformater](https://www.freeformatter.com/). The validator displays errors because it doesn't not recognise jinja templating, but HTML is otherwise valid.
CSS has been validated using [W3 CSS validator](http://jigsaw.w3.org/css-validator/validator).
Javascript code has been validated using [JSHINT](https://jshint.com/).
Python code has been validated using [PEP8](http://pep8online.com/).
Lightouse testing from Chrome developer's tools returned positive results (all above 90%).

* Functionalities:

The following functionalities have been tested on different browsers (Safari, Chrome, Edge, Firefox) and screen sizes (laptop, tablet and mobile): accessing home page, navigating through all pages of the site using navbars, logging in/out, registering, reading, creating, liking, updating and deleting reviews. No problems have been found with any of those functionalities.  In terms of display, the site is usable on all formats, even though the display of buttons on mobile version is not as pleasing, it remains usable. I have not been able to fix this issue at this point for lack of time.

## Deployment in heroku

After creating the app and the MongoDB database.
In terminal:

* pip 3 freeze --local > requirements.text
* echo web: python app.py > Procfile

In Heroku:
* create a new app (choose name and region)
* choose the deployment method = Connect to Github
* select this repository: raphaelmar/escph_reading_club
* Click connect
* in Settings, click reveal config Vars and enter the following: IP, PORT, SECRET KEY, MONGO_URI, MONGODB_Name

In terminal:
* Git add/commit/push requirements.txt and Procfile files

In Heroku:
* click enable automatic deploys

## Credits

### Media

* The Wireframes were created using [Balsamiq](https://balsamiq.com/).
* The 2 images used on the site are by DariuszSankowski and SCY , they were obtained from [Pixabay](https://pixabay.com/)

### Acknowledgements

* The main structure of this site is based on the code provided by Tim Nelson for the Task Manager mini-project presented in the Data centric module of the Full stack Web Developer course form Code Institute.
* The code for the modal used for the delete functionality is based on [Delete Modal](https://www.w3schools.com/howto/howto_css_delete_modal.asp)

### Thank you

* To Everyone at Code Institute for their patience!
* To the dedicated team of tutors who are always helpful.
* To my mentor Reuben Ferrante for making time for me outside his timetabled hours.

