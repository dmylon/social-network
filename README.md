# social-network

### Project Description

ChitChat is a Twitter-like social media website, that allows users to share their thoughts, like posts, and follow other users. This website was developed back in March 2021 as a small project made for fun and getting familiar with full stack development technologies like HTML,CSS, JavaScript and Python(Django). By no means it is intended to be put into production or used for any commercial purposes. In the current version, the platform is designed to be desktop-only.

By first visiting the website, it is required to be logged in, or create a new account if there one does not exist.

![Screenshot_15](https://user-images.githubusercontent.com/47897459/229605799-f2d64673-c669-4ea6-890e-a386e3706be2.png)

After logging in, the user views the main page, in which they can create a new post, view all other user's posts, and like them if they want. Also, for their own posts, users have an edit option in which they can change the content of a previous made post.

![Screenshot_16](https://user-images.githubusercontent.com/47897459/229607706-89fcf2ae-ebb6-44d1-9674-bd6263b14d22.png)

When clicking in a username, a profile page is shown, containing the number of followers and following users, and the posts made by this person. In addition, there is a follow/unfollow option.

![Screenshot_17](https://user-images.githubusercontent.com/47897459/229608645-a00ec404-8805-4c04-a6c7-3035689be4bf.png)

Last but not least, in the "Following" section the user is able to view all the posts a webpage containing all the posts from the people that the user has selected to follow.

![Screenshot_18](https://user-images.githubusercontent.com/47897459/229614023-65d3d9cb-ba04-42f6-9dcc-e8aa68dca3ad.png)

### How to run

In order to run the app locally on your desktop,follow these steps:

1. Clone the repository to you local terminal.
2. Navigate to the project folder using the command-line(or powershell for Windows users).
3. Install the required dependencies(assuming python is already installed) using the command ```pip install -r requirements.txt```
4. Start the app using the command ```python manage.py runserver```. If the local server has started successfully you should see a message saying "Starting development server at http://127.0.0.1:8000/" amongst the rest of the message.
5. Open a web browser and type the following URL ```http://127.0.0.1:8000/```. If all the previous steps are executed correctly, you should be able to see a live demo of the webpage.
6. Have fun!

