## Functional Requirements

1. Login
2. Logout
3. Create new account
4. delete account
5. User home page (users can see tweets of users they follow)
6. Create a Post
7. Adding an image to a tweet
8. Re-tweet a tweet
9. Like a tweet
10. Delete a tweet
11. Search users/Friends
12. Send messages to followers

## Non-functional Requirements

1. Limited Length Tweets - A tweet cannot exceed 140 words

2. Compatibility - The webApp should run on Chrome Web Browser

3. The image format for a tweet must be an image url

4. All passwords must be at least 8 characters

## Use Cases

1. Send messages to followers
- **Pre-condition:** The user is logged in and is on home page.

- **Trigger:** Pressing the Send Message Button.

- **Primary Sequence:**
  
  1. Select the messages page and then the send message page.
  2. Select a receiver from list of followers.
  3. Type a text in the box that needs to be sent. 
  4. Press send to send the text.

- **Primary Postconditions:** The receiever receives the message on their messages page.

- **Alternate Sequence:** The receiver account does no longer exist (the receiver account was deleted before the message was sent).
  
  1. Select the messages page.
  2. Select a receiver from list of followers.
  3. Type a text in the box that needs to be sent. 
  4. Press send to send the text.
  5. The page refreshes and the receiver account is removed from the selectable list

2. Adding an image to a post
- **Pre-conditions:** User is logged in and is on the create a post tab.

- **Trigger:** Enter a valid Image URL in the create option.

- **Primary Sequence:**
  
  1. Press the "create post" button.
  2. Enter a valid Image URL in the space where it says "If you want to add an image to your post, paste link below:"
  4. Press the "Post" button.

- **Primary Postconditions:** The image is added to the tweet draft.

- **Alternate Sequence:** The image may not have a valid URL.

  1. Press the "create post" button.
  2. An image is doesn't have a valid URL.
  3. The post does not include the image. 

3. Search users/Friends
- **Pre-conditions:** User should select a search button to search up someone

- **Trigger:** User inputs a username and clicks search

- **Primary Sequence:**
  
  1. Select search from main page.
  2. Type username or keyword for username to search.
  3. Press button to search for that username
  4. All users who have the keyword searched are displayed

- **Primary Postconditions:** The page displays the user with that username

- **Alternate Sequence:** No users are available with the username chosen

  1. User tries to search for a keyword or username that no users match
  2. Search page displays that there are no users of that name.
  3. User can type in a new user to search for.

4. User home page
- **Pre-conditions:** User has created an account and is logged in.

- **Trigger:** User logs into their account and is taken to the home page.

- **Primary Sequence:**
  
  1. User completes log-in sequence and enters their account.
  2. User reaches the user home page
  3. User can see posts from other users that they follow.
  4. User can see other sections of the webpage they can access such as messages and search.

- **Primary Postconditions:** The user can see the posts of users that they choose.

- **Alternate Sequence:** The user is not following any users who have created posts.

  1. User enters account.
  2. User sees a message saying that they are not following any accounts.
  3. User is encouraged to create a post or search other users to follow.

5. Post a Tweet
- **Pre-condition:** The user is Logged in & on his Home page

- **Trigger:** Pressing the New Tweet Button

- **Primary Sequence:**
  
  1. The user presses the "New Tweet" Button
  2. A prompt shows up where they can draft a message upto 140 characters
  3. The user can press the "Post tweet" button to Post the Tweet
  4. The post appear of the user's Home page(Feed)

- **Primary Postconditions:** The post appear of the user's Home page(Feed) 

- **Alternate Sequence:** User tries to submit an empty post
  
  1. User does not type anything into the post box
  2. User presses the submit button
  3. The submit button does not create a post and does not redirect to home
  4. The User can create an actual post while on the post page

6. Delete a tweet 

- **Pre-conditions:** User has an account, is logged in and has some posts on their account

- **Trigger:** User clicks on the delete button under the tweet.

- **Primary Sequence:**

  1. User completes the log-in procedure and redirected to their account's home page.
  2. On the home page the user can view their own posts.
  3. The user clicks "Delete" to delete it.    

- **Primary Postconditions:** The tweet that is selected to be deleted is deleted from user's Home page and posts database

- **Alternate Sequence:** The user has not created any posts.

  1. User enters account.
  2. The User does not see any posts 
  3. User sees a message encouraging them to follow new accounts.
