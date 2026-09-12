import time
import subprocess

from functions import clear_terminal

def text_cursor_animation(delay=0.3):
    for i in range(10):
        if i % 2 == 0: #even
            print("\r|", end="", flush=True)
        else: #odd
            print("\r ", end="", flush=True)
        time.sleep(delay)

    print("\r ", end="", flush=True)

def arrow_animation__blinking(delay=0.3):
    for counter in range(50):
        if counter % 2 == 0:
            print("\r>", end="", flush=True)
        else:
            print("\r ", end="", flush=True)

        time.sleep(delay)

        counter += 1

    print("\r ", end="", flush=True)

def computer_opening():
    space = "      "

    print("Micro modular BIOS V6.24Bt")
    print("Copyright (c) 1996 MicroStar Computer System")

    cpu = subprocess.check_output(
        ["powershell", "-command", "(Get-CimInstance Win32_Processor).name"],
        text=True
    ).strip()
    print(f"\n{space}{cpu}")

    ram = round(float(subprocess.check_output(
    ["powershell", "-Command", "(Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory / 1MB"],
    text=True
    ).strip()))

    for ram_counter in range(0, ram + 1, 256):
        print(f"\r\0{space}Memory Test: {ram_counter}M", end="\r", flush=True)
        time.sleep(0.05)
    print(f"{space}Memory Test: {ram}M")

    disk_model = subprocess.check_output(
        ["powershell", "-Command", "(Get-CimInstance Win32_DiskDrive).Model"],
        text=True
        ).strip()
    print(f"\n{space}Detecting IDE Primary Master ... {disk_model}")
    time.sleep(0.5)
    print(f"{space}Detecting IDE Primary Slave ... None")
    time.sleep(0.5)
    print(f"{space}Detecting IDE Secondary Master ... None")
    time.sleep(0.5)
    print(f"{space}Detecting IDE Secondary Slave ... None")

    Keyboard_name = subprocess.check_output(
        ["powershell", "-Command", "(Get-CimInstance Win32_Keyboard).Name"],
        text=True
        ).strip().splitlines()[0] #if has more give only 1 
    print(f"\n{space}Detecting Keyboard............ {Keyboard_name}")

    Mouse_name = subprocess.check_output(
            ["powershell", "-Command", "(Get-CimInstance Win32_PointingDevice).Name"],
            text=True
            ).strip().splitlines()[0] 
    print(f"{space}Detecting Mouse............ {Mouse_name}")
    time.sleep(0.5)
    print("CMOS Checksum.................... OK")

    clear_terminal()
    print("Initializing System............ OK")
    time.sleep(0.5)

    print("\nMICROSTAR COMPUTER SYSTEMS")
    time.sleep(0.5)
    print("MicroStar BIOS V6.24Bt")

    time.sleep(1)

def loading_anim():
    clear_terminal()
    loading = ["|", "/", "-", "\\", "|", "/", "-", "\\"]

    for counter in range(2):
        for val in loading:
            time.sleep(0.5)
            print(f"\r{val}", end="", flush=True)

    clear_terminal()
        
