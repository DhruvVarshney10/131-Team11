# Team 11 Twitter (Elon Take Down)
- Dhruv Varshney(@DhruvVarshney10) - Team Lead
- Anchal Mandavia (@AnchalMandavia)
- Gunraj Singh (@gunrajsingh15)
- Ari Grady (@Smalls141414)

## Table of Contents
* [Necessary Libraries and Technologies](#necessary-libraries-and-technologies)
* [How to Run](#how-to-run)
* [Features](#features)

## Necessary Libraries and Technologies
- Python 3.6
- Flask
- flask-wtf
- flask-sqlalchemy
- flask-login
- werkzeug.security
- datetime

## How to Run
- Clone the 131-Team11 repo
- Cd to 131-Team11 folder
- Run "python3 run.py"
- Open http://localhost:5000/ in your Google Chrome browser

## Features
1. From starting login page, click link to sign-up page.
2. Create unique username and password for your user.
- This will automatically sign you in, henceforth you can login with those same credentials
3. Use our new functions
- Search
	1. Type in keyword you want to search for other users in the system
	2. Click search button on the header
	3. Select follow next to users you want to follow
	- Please note that this user will have to accept your follow request before you follow one another
- Post
	1. Click post button in header
	2. Type in body section and/or add an image link to your new post
	3. Click post and your post will appear on your homepage as well as the homepage of those you have friended
- Messages
	1. Select messages button in header
	2. You will be able to see messages you have been sent as well as a link to send your own message.
	3. Under this link, select from list of followers the one you wish to receive the message.
	4. Type out message and click send to send your message.
- Follow Requests
	1. Under the messages tab, select follow requests
	2. User will be able to see the requests from users who want to follow them and accept them
- Settings
	1. By selecting settings from the header, user will be able to delete their account.
	2. By selecting delete account, they will be prompted to input password to delete account.
- Logout
	1. By selecting logout from the header, user will be logged out instantly.
- Post interactions
	1. Posts from people you follow display on the user home page with a few options.
	2. Your own posts are able to be deleted with a delete tweet button that displays only under your own tweets
	3. For every post you are able to leave a like on the post.
	4. For every post you are able to repost the same one
	- This will display who you reposted from
