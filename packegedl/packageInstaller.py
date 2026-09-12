import sys
import subprocess

def install_package(package_name):
    try:
        # sys.executable automatically finds the exact Python folder running your script
        # -m pip install installs the requested library cleanly
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"Successfully installed {package_name}!")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package_name}. Make sure you are connected to the internet.")

# --- How to use it ---
# Run this right at the beginning of your script
install_package("winotify")