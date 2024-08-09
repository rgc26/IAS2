#symmetric-keyencrytion - 
# the data is incode and decode by the same key

#Fernet symmetric encryption
#encsure that a message is encrypted using it
#connot be manupulated or read w/out the key

#AES algorithm 128-bit key

#provide pravable security
#meaning that the decryption w/out the key is impossible

from cryptography.fernet import Fernet

#we will encrypting the string

message = "IAS week 3"


#generate a key for encryption and decryption
#using a fernet to generate
#the key or use ramdom key generator


key = Fernet.generate_key()

#adding instance the fernet class w/ the key

fernet =Fernet(key)

#the use of the Fernet class instance
#to encrypt the message and 
#the message must be encoded to byte string bofore encryption


encMessage =fernet.encrypt(message.encode())

print("the message: ", message )

print("the encrypt message: ", encMessage)


# decrypt the encrypt string with the fernet instance key
# it is used for encrypting the message
# encode the byte message that is returned by decrypt method
#decode to string w/ decode methods


decMessage = fernet.decrypt(encMessage).decode()

print ("Decrypted message: ", decMessage)
