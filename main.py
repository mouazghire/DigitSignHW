from rsa import newkeys, encrypt, decrypt, encrypt_str, decrypt_str

def reading(filepath):
    try:
        with open(filepath) as file:
            return file.read()
    except:
        print("Filepath incorrect:" + filepath)
        return None

def writing(text: str):
    try: 
        with open("output.txt", "w") as output:
            output.write(str(text))
    except FileNotFoundError:
        print("File not found")

def encrypt_decrypt(msg, keys):
    print('Enter path to the .txt file:')
    file_path = input("> ")
    text = reading(file_path)
    if text is None:
        print("Nothing to encrypt.")
        return
    
    encrypted = encrypt_str(msg, keys['public'])
    decrypted = decrypt_str(encrypted, keys['private'])
    writing(msg)
    print("Encryption done.")
    print(f'Original message: {msg}')
    print(f'Encrypted message: {encrypted}')
    print(f'Decrypted message: {decrypted}')
    