import os
import time
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
        print("file delete")
        print("file rename")
        print("file append")
        print("file search")
        print("file info")
        print("dir create")
        print("dir delete")
        print("clear")
        print("echo")
        print("exit")
        print("+───────────────────────────────────────────────────────────────────+\n")

    elif choice == "clear":
        os.system("cls")

    elif choice == "file create":
        os.system("cls")
        file_name = input(Fore.GREEN + "EZ-File Name@:> " + Fore.RESET)

        with open(file_name, "w") as file:
            file.write("File created by EZFile")

        print(f"File '{file_name}' created and written to successfully.")

    elif choice == "file read":
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

    elif choice == "file write":
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

    elif choice == "file append":
        os.system("cls")
        file_name = input(Fore.GREEN + "EZ-File Name@:> " + Fore.RESET)
        additional_content = input(Fore.GREEN + "EZ-File Append Content@:> " + Fore.RESET)

        try:
            with open(file_name, "a") as file:
                file.write("\n" + additional_content)
            print(f"Content appended to '{file_name}' successfully.")
        except FileNotFoundError:
            print(Fore.RED + f"Error: The file '{file_name}' was not found." + Fore.RESET)

    elif choice == "file delete":
        os.system("cls")
        file_name = input(Fore.GREEN + "EZ-File Name@:> " + Fore.RESET)
        os.system("cls")
        try:
            os.remove(file_name)
            print(f"File '{file_name}' deleted successfully.")
        except FileNotFoundError:
            print(Fore.RED + f"Error: The file '{file_name}' was not found." + Fore.RESET)
        except PermissionError:
            print(Fore.RED + f"Error: Permission denied for file '{file_name}'." + Fore.RESET)

    elif choice == "file rename":
        os.system("cls")
        old_name = input(Fore.GREEN + "Current EZ-File Name@:> " + Fore.RESET)
        os.system("cls")
        new_name = input(Fore.GREEN + "New EZ-File Name@:> " + Fore.RESET)
        os.system("cls")
        try:
            os.rename(old_name, new_name)
            print(f"File renamed from '{old_name}' to '{new_name}' successfully.")
        except FileNotFoundError:
            print(Fore.RED + f"Error: The file '{old_name}' was not found." + Fore.RESET)
        except FileExistsError:
            print(Fore.RED + f"Error: A file with the name '{new_name}' already exists." + Fore.RESET)

    elif choice == "file search":
        os.system("cls")
        search_query = input(Fore.GREEN + "EZ-File Search Query@:> " + Fore.RESET)
        os.system("cls")
        folder_path = input(Fore.GREEN + "EZ-File Folder Path (leave empty for this directory) @:> " + Fore.RESET)
        os.system("cls")
        if not folder_path:
            folder_path = os.getcwd()
        try:
            files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            results = [f for f in files if search_query in f]
            if results:
                print("Search results:")
                for result in results:
                    print(result)
            else:
                print("No files matched the search query.")
        except FileNotFoundError:
            print(Fore.RED + f"Error: The folder '{folder_path}' was not found." + Fore.RESET)

    elif choice == "file info":
        os.system("cls")
        file_name = input(Fore.GREEN + "EZ-File Name@:> " + Fore.RESET)
        os.system("cls")
        try:
            file_stat = os.stat(file_name)
            print(f"File: {file_name}")
            print(f"Size: {file_stat.st_size} bytes")
            print(f"Last Modified: {time.ctime(file_stat.st_mtime)}")
        except FileNotFoundError:
            print(Fore.RED + f"Error: The file '{file_name}' was not found." + Fore.RESET)

    elif choice == "file list":
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

    elif choice == "dir create":
        os.system("cls")
        dir_name = input(Fore.GREEN + "EZ-Dir Name@:> " + Fore.RESET)
        os.system("cls")
        try:
            os.makedirs(dir_name, exist_ok=True)
            print(f"Directory '{dir_name}' created successfully.")
        except OSError as e:
            print(Fore.RED + f"Error: {e}" + Fore.RESET)

    elif choice == "dir delete":
        os.system("cls")
        dir_name = input(Fore.GREEN + "EZ-Dir Name@:> " + Fore.RESET)
        os.system("cls")
        try:
            os.rmdir(dir_name)
            print(f"Directory '{dir_name}' deleted successfully.")
        except FileNotFoundError:
            print(Fore.RED + f"Error: The directory '{dir_name}' was not found." + Fore.RESET)
        except OSError:
            print(Fore.RED + f"Error: The directory '{dir_name}' is not empty." + Fore.RESET)

    elif choice == "echo":
        os.system("cls")
        user_input = input(Fore.GREEN + "EZ-File Echo@:> " + Fore.RESET)

        if user_input.startswith("echo "):
            text_to_echo = user_input[5:].strip()
            print(text_to_echo)
        else:
            print(Fore.RED)
            print("Invalid command. Please start your input with 'echo'." + Fore.RESET)

    elif choice == "exit":
        print(Fore.GREEN + "Exiting EZ-File. Goodbye!" + Fore.RESET)
        break
