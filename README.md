# Amazing Gym Project

This application was created using Python, PostgreSQL, Flask, Jinja, HTML and CSS.

![amazing-gym-home-page](https://user-images.githubusercontent.com/100124261/166433653-0c45f78d-bcde-4ff9-8c8c-e89468d38126.png)

## Project Brief

> A local gym has asked you to build a piece of software to help them to manage memberships, and register members for classes.

## Amazing Gym Membership System

The membership system was created using tables and classes for:

- Members
- Activities (Referred to as classes on the front-end)
- Bookings

### Installation & Management

This application can be run by executing the the app.py file, which can be found in the root directory

- python3 app.py

A seed file can be found in the db directory. The seed file can be run by entering the following command from the root directory.

- psql -d amazing_gym -f db/amazing_gym.sql

The database can be managed from the command line using the following command (where amazing_gym is the name of the database)

- psql -d amazing_gym

### Members

Members can be assigned a standard or premium membership. Standard members are not permitted to book an activity during peak hours, whilst premium members can book any activity.

Members can have their membership deactivated. Deactivated members are not permitted to be booked into an activity.

### Activities

Each activity (class) has a maximum capacity. When the activity has reached capacity, no further bookings can be made for the class.

### Bookings

Gym staff can create a new booking by assigning a specific member to a class. The booking form is divided between standard and premium members to ensure standard members are not booked into a class during peak hours.

### Editing


In addition to creating new members, activities and bookings, gym staff can also edit entries.

- You can change the member name, membership level and account status
- You can amend an activity's name, time, date and capacity
- You can assign a booking to another member 

Please note that when if an activity is on during peak hours, you cannot assign a standard member to the booking on the edit page.
