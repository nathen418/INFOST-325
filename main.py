import rsa

publicKey, privateKey = rsa.newkeys(2048)


def encrypt():
    messageToEncrypt = input("Enter a message to encrypt: ") 
    encoded = rsa.encrypt(messageToEncrypt.encode(), publicKey)
    print("Encryption key has been downloaded to 'private.pem")
    # write private key to file "private.pem"
    with open('private.pem', mode='wb') as privatefile:
        privatefile.write(privateKey.save_pkcs1())
    # write encrypted text to file "encrypted.txt"
    with open('encrypted.enc', mode='wb') as encryptedfile:
        encryptedfile.write(encoded)
    print("encrypted string has been writen to 'encrypted.txt'")

def decrypt():
    messageToDecrypt = input("Enter a filename to decrypt: ")
    with open(messageToDecrypt, mode='rb') as encryptedfile:
        messageToDecrypt = encryptedfile.read()
    with open('private.pem', mode='rb') as privatefile:
        keydata = privatefile.read()
    privkey = rsa.PrivateKey.load_pkcs1(keydata)
    decMessage = rsa.decrypt(messageToDecrypt, privkey).decode()
    print("decrypted string: ", decMessage)


def main():
    choice = input("Would you like to encrypt or decrypt? ")
    
    if (choice.lower() == "encrypt"):
        encrypt()
    elif (choice.lower() == "decrypt"):
        decrypt()
    
if (__name__ == "__main__"):
    main()
