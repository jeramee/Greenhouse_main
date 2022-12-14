# INF360 - Programming in Python
# Jeramee Oliver
# Final Project - Greenhouse website

# Greenhouse_main

This program creates a webpage that is a greenhouse object.
You can go to individual greenhouses and see what is available to add to the greenhouse.
It reads in a dictionary of devices, fruits, vegetables, and herbs as potential inventory for the greenhouse, and displays those things to the screen.
It loads this data on the backend of an SQLite database.
However, the database is incomplete. The program itself will not crash. However, if you try to add and remove things from the greenhouse using the database it will crash because the database in incomplete.
The reason for this is that each greenhouse is a separate object and would need a separate database for each, or a separate table for each at a bare minimum.
I am not sure how to implement this, but I was able to generate a webpage with the 3rd part software Django as well as generate an SQLite database.

Website Instructions:

These steps are necessary.

pip install django

pip install django-extensions

or 

conda install django (if you use Anaconda which I do, used to use venv.)

pip install django-extensions 

If you get into my Greenhouse_main folder the one with the manage.py

python manage.py runserver

Then: 
http://127.0.0.1:8000

This will access the website

Database:

I did change the database up a bit.
You no longer need to create a superuser for the database

Just go to here:

http://127.0.0.1:8000/admin/

Type:

admin 

password

This will get you into the database.

I also tried to create a Jupyterlite Lab with all environmental configurations working right out of the box.
I was unable to do this without paid for static webhosting. That is why I did not create a simple Arduino Interface. I’m pretty good with that kind of stuff. Terrible with the front ends. Which is why I am working on a front-end project.
It’s not developed enough to warrant paying a monthly subscription for something like Heroku.
I’d like to at some point recreate Gregory Mendel’s research into inheritance. 
However, I will need to know how to marry JS with Python to add radial buttons, and make everything look nice. (Although, I may just use Ajax instead of JS because Django uses Ajax straight out of the box, but I must first learn Ajax.)

As an example of how I would recreate Mendel’s work:

I can create radial buttons for:

Pea Color

Yellow Peas

Green Peas

Pea shape

Wrinkled Peas

Unwrinkled Peas

Then, I’d like to create a way that users can add radial buttons from the SQLite database without the necessity of coding anything. (I am not there yet, but this isn’t that hard.)
Also, a way to add a written description as an option in place of a radial button.
A Jupyter Lab that monitors the greenhouse for the individual greenhouse objects.
Another words, full reproducible research that can be accessed by multiple agroindustry sites or university sites. 
Probably that will be all but possibly inventory and online sales options.
This is kind of a lot for one program to do, and usually you would see a team of programmers’ tackle something like this. Either that or I am just not that good at programming.

