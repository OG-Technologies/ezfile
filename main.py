import os
from colorama import *
from sys import *

print(Fore.GREEN)
print("EZ-File v1.001 by OG-Technologies")
print("Type 'help' for a list of the commands")
print(Fore.RESET)

while True:
    choice = input(Fore.GREEN + "EZ-File@:> " + Fore.RESET)

    if choice == "help":
        print("\n+─────────────────────────── Help Center ───────────────────────────+")
        print("help")
        print("file create")
        print("file write")
        print("file read")
        print("file list")
        print("clear")
        print("echo")
        print("+───────────────────────────────────────────────────────────────────+\n")

    if choice == "clear":
        os.system("cls")

    if choice == "file create":
        os.system("cls")
        file_name = input(Fore.GREEN + "EZ-File Name@:> " + Fore.RESET)

        with open(file_name, "w") as file:
            file.write("File created by EZFile")

        print(f"File '{file_name}' created and written to successfully.")

    if choice == "file read":
        os.system("cls")
        file_name = input(Fore.GREEN + "EZ-File Name@:> " + Fore.RESET)

        try:
            with open(file_name, "r") as file:
                os.system("cls")
                content = file.read()
                print(content)
        except FileNotFoundError:
            print(Fore.RED)
            print(f"Error: The file '{file_name}' was not found." + Fore.RESET)

    if choice == "file write":
        os.system("cls")
        file_name = input(Fore.GREEN + "EZ-File Name@:> " + Fore.RESET)

        new_content = input(Fore.GREEN + "EZ-File Content@:> " + Fore.RESET)

        try:
            with open(file_name, "w") as file:
                file.write(new_content)
            print(f"File '{file_name}' has been updated successfully.")
        except FileNotFoundError:
            print(Fore.RED)
            print(f"Error: The file '{file_name}' was not found." + Fore.RESET)

    if choice == "file list":
        os.system("cls")
        folder_path = input(Fore.GREEN + "EZ-File Folder Path (leave empty for this directory) @:> " + Fore.RESET)
        os.system("cls")

        if not folder_path:
            folder_path = os.getcwd()

        try:
            files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            
            if files:
                print("Files in the folder:")
                for file in files:
                    print(file)
            else:
                print("No files found in the folder.")
        except FileNotFoundError:
            print(f"Error: The folder '{folder_path}' was not found.")

    if choice == "echo":
        os.system("cls")
        user_input = input(Fore.GREEN + "EZ-File Echo@:> " + Fore.RESET)

        if user_input.startswith("echo "):
            text_to_echo = user_input[5:].strip()
            print(text_to_echo)
        else:
            print(Fore.RED)
            print("Invalid command. Please start your input with 'echo'." + Fore.RESET)
