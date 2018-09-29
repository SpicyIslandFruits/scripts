def decrypt(encrypted_text, decrypt_key):
    plain_text = ""

    for ch in list(encrypted_text):
        if 'A' <= ch <= 'Z':
            plain_text += chr((ord(ch) - ord('A') + decrypt_key) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            plain_text += chr((ord(ch) - ord('a') + decrypt_key) % 26 + ord('a'))
        else:
            plain_text += ch

    return plain_text


if __name__ == '__main__':
    decrypted_text = decrypt(input("PLEASE INPUT TEXT : "), int(input("PLEASE INPUT KEY : ")))

    print("PLAINTEXT : " + decrypted_text)

    input("PLEASE PRESS ANY")
