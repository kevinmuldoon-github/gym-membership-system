# Amazing Gym Project

This application was created using Python, PostgreSQL, Flask, Jinja, HTML and CSS.

<table>

  <tr>
    <td><strong>Home Page</strong></td>
     <td><strong>Site Map</strong></td>
     <td><strong>Duplicate Booking Message</strong></td>
  </tr>
  
  <tr>
    <td><img src="https://user-images.githubusercontent.com/100124261/166433653-0c45f78d-bcde-4ff9-8c8c-e89468d38126.png" alt="The Application Home Page" width="300" /></td>
    <td><img src="https://user-images.githubusercontent.com/100124261/166436683-8fface28-aabb-4946-a11d-0b237dbd3395.png" alt="Site Map" width="300" /></td>
    <td><img src="https://user-images.githubusercontent.com/100124261/166436946-bbf01bab-1a74-423a-adb3-208ec5e38ac3.png" alt="Message to User When Booking Cannot Be Made" width="300" /></td>
  </tr>
  
    <tr>
    <td><strong>Members Page</strong></td>
     <td><strong>Classes Page</strong></td>
     <td><strong>Bookings Page</strong></td>
    </tr>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/100124261/166434416-40277fab-be89-40e7-a5fb-de1c237a6cc0.png" alt="The Members Page" width="300" /></td>
    <td><img src="https://user-images.githubusercontent.com/100124261/166435916-d331e959-e2e2-42a1-b23d-9c3234882774.png" alt="The Classes Page" width="300" /></td>
    <td><img src="https://user-images.githubusercontent.com/100124261/166436247-3a0e91e3-d7f1-46e3-9471-86cce8e3b54c.png" alt="The Classes Page" width="300" /></td>
  </tr>
  
      <tr>
    <td><strong>Add a Member</strong></td>
     <td><strong>Add a Class</strong></td>
     <td><strong>Add a Booking</strong></td>
  </tr>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/100124261/166436482-41796d68-c991-433c-8591-12eca41e0b18.png" alt="Add a Member" width="300" /></td>
    <td><img src="https://user-images.githubusercontent.com/100124261/166436529-950450a6-7ba8-46f6-b186-6a5db2ede17c.png" alt="Add a Class" width="300" /></td>
    <td><img src="https://user-images.githubusercontent.com/100124261/166436558-2ac18394-446d-4017-b753-fc6edb24e031.png" alt="Add a Booking width="300" /></td>
  </tr>
  
 </table>

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
