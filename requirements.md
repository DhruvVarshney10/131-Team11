## Functional Requirements

1. Login
2. Logout
3. Create new account
4. delete account
5. User home page (users can see tweets of users they follow)
6. Create a Post
7. Adding an image to a tweet
8. Re-tweet a tweet
9. Comment/Like a tweet
10. Delete/Edit a tweet
11. Search users/Friends
12. Send messages to followers

## Non-functional Requirements

1. Limited Length Tweets - A tweet cannot exceed 140 words

2. Compatibility - The webApp should run on Chrome Web Browser

3. The image format for a tweet must be .png or .jpg

4. All passwords must be at least 8 characters, 1 capital, 1 number

## Use Cases

1. Send messages to followers
- **Pre-condition:** Sender should have receiver as a follower.

- **Trigger:** Sender identifies the receiver and inputs the text that would be sent as a message. 

- **Primary Sequence:**
  
  1. Select a receiver.
  2. Type a text in the box that needs to be sent. 
  3. Press send to send the text.
  4. Receiver receives the text on their account.

- **Primary Postconditions:** The receiver sees the text on their account.  

- **Alternate Sequence:** The receiver may not be a follower of the sender
  
  1. The text shows under requests tab to receiver.
  2. Receiver can accept the sender and receive any future texts.
  3. Receiver can block the sender.
 
2. Adding an image to a post
- **Pre-conditions:** User should create a draft for the post and include an image in .jpeg format.

- **Trigger:** User uploads an image on the draft post before posting it.

- **Primary Sequence:**
  
  1. Create a post.
  2. Select and upload an image.
  3. Preview the image and change if needed to.
  4. Post the draft on the profile.

- **Primary Postconditions:** The post shows up on the user's profile

- **Alternate Sequence:** The image may not be in a .jpeg format.

  1. User tries to upload an image of an unsupported type.
  2. User gets an error message saying "unsupported format. Use .jpeg".
  3. User can re upload their image in .jpeg format.

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

5. MORE USE CASES
