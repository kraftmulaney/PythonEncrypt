from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

    print("Successfully wrote key to file")

def load_key():
    return open("secret.key", "rb").read()

def encrypt_message(message):
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)

    print(encrypted_message.decode())

def decrypt_message(ciphertext):
    encoded_cipher = ciphertext.encode()

    key = load_key()
    f = Fernet(key)
    cleartext = f.decrypt(encoded_cipher)

    print(cleartext.decode())


keepRunning = True

while (keepRunning):
    mode = input("\nEncrypt or Decrypt or Generate key: ").lower()

    if (mode == 'e'):
        message = input("Message: ")
        encrypt_message(message)
    elif (mode == 'd'):
        ciphertext = input("Ciphertext: ")
        decrypt_message(ciphertext)
    elif (mode == 'g'):
        generate_key()
    elif (mode == 'q'):
        keepRunning = False
    else:
        print("Not a valid input")
