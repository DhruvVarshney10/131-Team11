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

3. USE CASE 3
