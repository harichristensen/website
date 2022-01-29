Purpose:
To display my resume in a creative and professional way while learning new concepts. Used Flask and Flask Freezer to test and build the static site, and CloudFlare to deploy the static site.

Thoughts:
In the future I want to research more about adding non-static attributes to the site such as forms and payment options.

I learned a lot about the deployment and building of websites, the different apps that could be used, python virtual environments.


To set-up:

Clone repository

Go to proper directory:
$ cd website

Create virtual environment:
$ python -m venv venv

Activate virtual environment:
$ source venv venv/bin/activate

Download requirements:
$ pip install -r requirements

To test using flask: 
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ flask run


Build command:
$ python build.py

Build output directory:
./project/build