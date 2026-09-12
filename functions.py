import time
import subprocess
import os
import threading
import msvcrt
import tkinter as tk

from dialogue import log_in_dialogue
from winotify import Notification

skip_clear = False
has_name_already = False
has_password_already = False

def clear_terminal():
    global skip_clear
    if skip_clear:
        skip_clear = False
        return
    command = 'cls' if os.name == 'nt' else 'clear'

    subprocess.run(command, shell=True)

def arrow_selector(choice1, choice2):
    select_yes = True
    while msvcrt.kbhit():
        msvcrt.getch()

    while True:
        # \r resets to the start of the line to update the menu animation
        if select_yes:
            print(f"\r -> [ {choice1} ]      [ {choice2} ]  ", end="", flush=True)
        else: 
            print(f"\r    [ {choice1} ]   -> [ {choice2} ]  ", end="", flush=True)

        key = msvcrt.getch()

        if key in [b'\x00', b'\xe0']:  
            key = msvcrt.getch()  # Get the actual key code
            
            # b'K' is Left Arrow, b'M' is Right Arrow
            if key == b'K' or key == b'M':
                select_yes = not select_yes  # Toggle selection
                
        # b'\r' is the Enter key code in msvcrt
        elif key == b'\r':
            return choice1 if select_yes else choice2

def type_writter(name, text, delay=0.1, ask_question=False):
    global skip_clear

    spacer = "         "

    if ask_question:
        skip_clear = True

    words = text.split(" ")
    needs_space = False
    word_count = 0

    speaker_name = name
    border_len = 64 - len(speaker_name)

    # Calculate how many lines the text needs
    visible_words = [word for word in words if word not in ["<pause>", "<space>", "<clear>"]]
    text_lines = (len(visible_words) + 7) // 8

    if speaker_name != "":
        print("=" * 4, end=" ")
        print(speaker_name, end=" ")
        print("=" * border_len)

    else:
        print("=" * 70)

    # Reserve enough lines for the text
    for _ in range(text_lines + 2):
        print()

    # Bottom border
    print("=" * 70)

    print(f"\033[{text_lines + 2}A", end="", flush=True)

    print(spacer, end="", flush=True)

    for index, word in enumerate(words):

        if word == "<pause>":
            time.sleep(1.5)
            continue

        if word == "<space>":
            print(" ", end="", flush=True)
            continue

        if word == "<clear>":
            clear_terminal()
            needs_space = False
            continue

        if needs_space:
            print(" ", end="", flush=True)

        for char in word:
            print("|", end="", flush=True)
            time.sleep(delay)
            print(f"\b \b{char}", end="", flush=True)

            if char in [".", "!", "?"]:
                time.sleep(0.6)
            elif char in [",", "-", ";"]:
                time.sleep(0.3)

        word_count += 1

        if word_count > 7:
            print()
            print(spacer, end="", flush=True)

            word_count = 0
            needs_space = False

        else:
            needs_space = True

    if not ask_question:
        time.sleep(1.5)

    for _ in range(2):
        print()

    enter()
    
    clear_terminal()

def notification(id, title, msg):
    toast = Notification(
        app_id=id,
        title=title,
        msg=msg,
        duration="short"
    )

    toast.show()

def timer(sec):
    timer_end = threading.Event()
    def countdown():
        time.sleep(sec)
        timer_end.set()

        notification("Mia", "WAKE UP!!!", "") 

    timer_threading = threading.Thread(target=countdown)
    timer_threading.start()

    return timer_end
      

#--------- screen -----------------
def screen_background_whole():
    root = tk.Tk()

    # Make it cover the entire screen
    root.attributes("-fullscreen", True)
    root.configure(bg="black")
    root.attributes("-topmost", True)
    
    root.after(5000, root.destroy)

    root.mainloop()


#-------computer function----------
def header_mcs():
    clear_terminal()
    print("MICROSTAR COMPUTER SYSTEMS")
    print("--------------------------")
    print()
    print("SYSTEM LOGIN")
    print()

def log_in():
    redo = log_in_dialogue[2].get("redo")
    while True:
        header_mcs()
        player_name = input("Name: ").strip()

        if not player_name.isalpha():
            print("Error: LETTERS ONLY")
            time.sleep(0.5)
            continue

        password = ""

        print("Password: ", end="", flush=True)

        while True:
            key = msvcrt.getch()

            if key == b"\r":
                break

            elif key == b"\x08":
                if password:
                    password = password[:-1]
                    print("\b \b", end="", flush=True)

            else:
                password += key.decode()
                print("*", end="", flush=True)

        saved_name, saved_password = checks_for_saved_account()

        if saved_name is not None or saved_password is not None:
            if player_name != saved_name:
                print("\nInvalid Name")
                for space in range(2): #spacer
                    print()

                wrong_name = log_in_dialogue[0].get("wrong_name")
                type_writter(saved_name, wrong_name)
                time.sleep(0.5)
                type_writter(saved_name, redo)
                time.sleep(0.5)
                continue

            elif password != saved_password:
                print("\nInvalid Password")
                for space in range(2): #spacer
                    print()

                wrong_pass = log_in_dialogue[1].get("wrong_pass")
                type_writter(saved_name, wrong_pass)
                time.sleep(0.5)
                type_writter(saved_name, f"\r {redo}")
                time.sleep(0.5)
                clear_terminal()
                continue

                

        break

    save_account(player_name, password)
    print("\nPassword Entered")

def checks_for_saved_account():
    if os.path.exists("save_data.txt"):
        with open("save_data.txt", "r") as file:
            lines = file.readlines()

            if len(lines) >= 2:
                saved_name = lines[0].strip()
                saved_password = lines[1].strip()

                return saved_name, saved_password

    return None, None

def save_account(name, password):
    saved_name, saved_password = checks_for_saved_account()

    if saved_name is not None:
        return

    with open("save_data.txt", "w") as file:
        file.write(name + "\n")
        file.write(password)

def back():
    while True:
        print(f"\r -> [ Back ]", end="", flush=True)

        while msvcrt.kbhit():
            msvcrt.getch()
    
        key = msvcrt.getch()
    
        if key == b'\r':
            clear_terminal()
            return "Back"

def enter():
    while True:
        print(f"\r -> [ Enter ]", end="", flush=True)

        while msvcrt.kbhit():
            msvcrt.getch()
    
        key = msvcrt.getch()
    
        if key == b'\r':
            clear_terminal()
            return "Enter"

def emails(email1, email2, email3, email4):
    row = 0
    col = 0

    emails = [
        [email1, email3],
        [email2, email4],
    ]

    while msvcrt.kbhit():
        msvcrt.getch()

    while True:
        # Clear the previous two lines
        print("\033[2A", end="")

        for r in range(2):
            line = ""

            for c in range(2):
                email = emails[r][c]

                if row == r and col == c:
                    line += f" -> [ {email} ]"
                else:
                    line += f"    [ {email} ]"

                if c == 0:
                    line += "      "

            print(line)

        key = msvcrt.getch()

        if key in [b'\x00', b'\xe0']:
            key = msvcrt.getch()

            if key == b'H':       # Up
                row = 0

            elif key == b'P':     # Down
                row = 1

            elif key == b'K':     # Left
                col = 0

            elif key == b'M':     # Right
                col = 1

        elif key == b'\r':
            return emails[row][col]