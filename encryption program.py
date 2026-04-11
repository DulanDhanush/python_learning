import random
import string
import argparse
import json
import os

KEY_FILE = "key.json"

chars = list(" " + string.punctuation + string.digits + string.ascii_letters)


def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "r") as f:
            return json.load(f)
    else:
        key = chars.copy()
        random.shuffle(key)
        with open(KEY_FILE, "w") as f:
            json.dump(key, f)
        return key


def encrypt(text, chars, key):
    cipher = ""
    for letter in text:
        if letter in chars:
            index = chars.index(letter)
            cipher += key[index]
        else:
            cipher += letter
    return cipher


def decrypt(text, chars, key):
    plain = ""
    for letter in text:
        if letter in key:
            index = key.index(letter)
            plain += chars[index]
        else:
            plain += letter
    return plain



parser = argparse.ArgumentParser(description="Simple Encryption CLI Tool")

parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode: encrypt or decrypt")
parser.add_argument("message", help="Message to process")

args = parser.parse_args()


key = load_key()


if args.mode == "encrypt":
    result = encrypt(args.message, chars, key)
    print(f"Encrypted: {result}")

elif args.mode == "decrypt":
    result = decrypt(args.message, chars, key)
    print(f"Decrypted: {result}")