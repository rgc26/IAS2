#Asymmetric key encryption
#use a 2 key a public and the private key
#the public ket is used to encrypt the data and 
#the private is used to decryp the data

import rsa

publicKey, privateKey = rsa.newkeys(512)


#this is the message that we will be encryting


message = "IAS week 123"

#rsa.encrypt method to encrypt the message w/ public key
#this message should be encode to byte string
#bytes string sequence of bytes
#each byte represents a value 0 to 255

#byte string store any data w/out interpreting as specific characters
#b' a' represents the ASCII value of the letter a - 61


encMessage = rsa.encrypt(message.encode(), publicKey)

print("original message: ", message)

print(" encrypt message:", encMessage)

#the encrypt msg can be decrypted with 
#rsa.decrypt method w/ private key

decMessage = rsa.decrypt(encMessage, privateKey).decode()

print(" decrypt message:", decMessage)




