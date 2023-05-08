# encrypted-chat-app
This is a small program I built while learning about sockets, ports and encrytion.

# The idea
The idea is that two people launch the program. One choses to be a 'host' and the other chooses to be a 'guest' the host will share their ip address with the guest and the guest will type in that ip address. If the ip address is correct then each program will share the encryption keys with the other. The users can then send messages back and forth between each other. These messages are encrypted with the public key and decrypted with the private key for each user.  

# Commands
Once the program starts the user will be prompted whether they want to be a guest or a host. Once they have chosen they will type in a user name. The guest will then be prompted for the host's ip address. Once the chat has started the host can leave by sending the message 'close' and the guest can leave by sending the message 'leave'.
