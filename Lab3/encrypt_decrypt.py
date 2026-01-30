from cryptography.fernet import Fernet

#Generate a key
key=Fernet.generate_key()
cipher_suite=Fernet(key)        

#Get input from the user
message=input("Enter a message to encrypt: ")   

#Encode the string to bytes
encoded_message=message.encode()

#Encrypt the message
encrypted_message=cipher_suite.encrypt(encoded_message) 

#decrypt the message
decrypted_message=cipher_suite.decrypt(encrypted_message)

#decode back to string
decoded_message=decrypted_message.decode()

print("Encrypted message:", encrypted_message)
print("Decrypted message:", decoded_message)