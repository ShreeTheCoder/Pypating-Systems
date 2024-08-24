import time
import subprocess

directory = ""

commands = ["exit"]

while True:
    user_cmd = input(directory + ">").lower()

    if user_cmd == "cd \"boot\"":
        directory = "/boot"

    else:
        user_cmd = input(directory + ">").lower()

    if directory == "boot":
        user_cmd = input(directory + ">").lower()

    elif user_cmd == "exit":
        exit()
