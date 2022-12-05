## Functional Requirements

1. Login
2. Logout
3. Create new account
4. delete account
5. User home page (users can see messages of users they follow)
6. Send messages to followers
7. Adding an image to a post
8. Search users/Friends
9. Block a User/Friend
10. Re-tweet a tweet
11. Comment/Like a post
12. Delete/Edit a post
13. See followers and following users
14. Create a Post


## Non-functional Requirements

1. Speed & Smoothness - The app should be capable of managing an increasing load of users & data. 
2. Security
    A. Account Locking - After a certain number of login attempts, the system could lockt he user’s account is locked and protect from hackers.
    B. Strong Password Generation - Ensure the the user created passwords are strong, (contain atleast a capital lette and a number)
3. Compatibility - Should be able to run on any Web browser ?
4. Real-Time updating feed - The feed updates in real time ?
5. Limited Length Tweets - Each tweet is limited to 120 words. 
6. Tag Other users in a tweet - and the tweets sows up on their feed aswell. 


## Use Cases

1. Send messages to followers
- **Pre-condition:** The user is logged in and is on home page.

- **Trigger:** Pressing the Send Message Button.

- **Primary Sequence:**
  
  1. Select the messages page.
  2. Select a receiver from list of followers.
  3. Type a text in the box that needs to be sent. 
  4. Press send to send the text.

- **Primary Postconditions:** The text shows up on the message thread for both users.  

- **Alternate Sequence:** The receiver account does no longer exist (the receiver account was deleted before the message was sent).
  
  1. Select the messages page.
  2. Select a receiver from list of followers.
  3. Type a text in the box that needs to be sent. 
  4. Press send to send the text.
  5. An error is displayed "User does no longer exist" (the message remains unsent).

2. Adding an image to a post
- **Pre-conditions:** User is logged in and is on the create a post tab.

- **Trigger:** Pressing the Upload Image option in your tweet.

- **Primary Sequence:**
  
  1. Press the "create post" button.
  2. Press the "upload image" button.
  3. Select an image (.jpeg).
  4. Press the "upload" button.

- **Primary Postconditions:** The image is added to the tweet draft.

- **Alternate Sequence:** The image may not be in a .jpeg format.

  1. Press the "create post" button.
  2. Press the "upload image" button.
  3. Select an image.
  4. Press the "upload" button.
  5. An error is display "Unsupported format. Please use .jpeg".
  6. The user is redirected to "Create a Post" tab.

3. Search users/Friends
- **Pre-conditions:** User should select a search button to search up someone

- **Trigger:** User inputs a username and clicks search

- **Primary Sequence:**
  
  1. Select search from main page.
  2. Type username or keyword for username to search.
  3. Press button to search for that username
  4. All users who have the keyword searched or the exact username are displayed

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
  
  1. The text shows under requests tab to receiver.
  2. Receiver can accept the sender and receive any future texts.
  3. Receiver can block the sender.
 
2. Use Case Name (Should match functional requirement name)
   ...
