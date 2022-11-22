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
 
2. Use Case Name (Should match functional requirement name)
   ...
