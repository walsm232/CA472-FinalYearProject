<h1> <div align="center"> CA472 Enterprise Computing Team Project </div> </h1>
<h2> <div align="center"> Grade: 72% </div> </h2>

<h3> <div align="center"> Google Cloud Demo </div> </h3>
<p> <div align="center"> https://student-network-308619.nw.r.appspot.com/ </div> </p>
<h3> <div align="center"> AWS Cloud Demo </div> </h3>
<p> <div align="center"> http://ec2-34-254-242-1.eu-west-1.compute.amazonaws.com:8000/ </div> </p>
<hr>
<div align="center"> <img src="res/student-network-logo2.png"> </div>

## Project Description
We developed this project with the hopes of connecting students across Ireland. The platform allows students to connect and interact with others in universities across the country and provides them with access to valuable student resources such as tutoring services, a student discussion board, and a secondhand books marketplace. Students can sign up to the site using their university email and customize their own profile on the platform. They can also add other students and chat with them through the site. Gamification is also in place which allows students to interact with posts through likes and comments. The platform also provides online tutoring services which offers students who are struggling in a particular field the ability to access grinds.

We chose to develop this as we believe that the original Facebook model for example (confined to your class / university) has gotten lost due to its huge growth and that there is now a need for a social site for students to interact and actually meet each other in real life. Students can meet each other through our platform with the hopes of actually meeting each other in person in the future. This is an aspect that other well-known networking sites tend to neglect due to their intentions of mass marketing their platform worldwide to any user.

## Installation
- Before you run the application, you will have to install the following:
    - Install [Python](https://www.python.org/downloads/) 
    - Install Django using `pip install django` in a terminal
    - Install Pillow using `pip install pillow` in a terminal
    - Install Pylint using `pip install pylint-django` in a terminal
    - Install Stripe using `pip install stripe` in a terminal
    - Install Django Admin Honeypot using `pip install django-admin-honeypot` in a terminal
    - Install Bootstrap Admin using `pip install bootstrap-admin` in a terminal
- Navigate to the `src`directory in your terminal and run `python manage.py runserver` or `python3 manage.py runserver` depending on which Python version you are using.

## Features
**Networking**
- Share posts with other users by writing statuses.
- Delete posts written by you.
- Interact with other users posts by liking them.
- Comment on your friends' posts.
- View the profile of all users on the platform.
- Accept or reject friend requests from other users.
- Send friend requests to other users.
- Update information such as University, Course, Year, Bio, etc. on your own profile and view stats such as number of friends and posts.
    
**Tutoring Services**
- View the listings for all tutors posted on the site.
- Book sessions with these tutors by checking out through our partner Stripe.
- If you are a tutor you can update information on your profile outlining your qualifications, experience, availabity, topics covered, and rate per hour.

**Discussion Board**
- Mock page created for final deliverable - not fully functioning.

**Secondhand Book Marketplace**
- Mock page created for final deliverable - not fully functioning.

**Reaction Game**
- Test your skills in a reactions-based game in order to improve focus and maintain concentration throughout the day.

## Built With
- Django
- Bootstrap
- HTML
- CSS
- jQuery


## Deployment
 - Google Cloud - Hosting / Static Files
 - Google Cloud Storage - Dynamic / Media Files
 - Amazon Web Services EC2 - Hosting / Static Files
 - Amazon Web Services S3 - Dynamic / Media Files

## Credits
**Developer / Maintainer:** Michael Walsh  
**Developer / Maintainer:** Karl Hannigan
**Project Supervisor:** Gareth Jones
