import subprocess
#import main
from pathlib import Path
import platform
import webbrowser
import sys







def install():
    try:
        installed_packages = {pkg.split("==")[0].strip(): pkg.split("==")[1].strip()
        for pkg in subprocess.check_output(["pip", "freeze"]).decode("utf-8").splitlines()}

        print("installing all requirement package with requirement.txt")
        current_dir = Path(__file__).parent
        requirements_path = current_dir / "requirements.txt"
        with open(requirements_path, "r") as file:
            requirements = file.readlines()
        packages_to_install = []
        
        for requirement in requirements:
            # ignore empty line
            requirement = requirement.strip()
            if not requirement or requirement.startswith("#"):
                continue

            # check empty line format
            if "==" in requirement:
                req_name, req_version = requirement.split("==")
                req_name, req_version = req_name.strip(), req_version.strip()  # list package and ver

            if req_name not in installed_packages or installed_packages[req_name] != req_version:

                packages_to_install.append(requirement.strip())
        if packages_to_install:
         subprocess.check_call(["pip", "install"] + packages_to_install)
         print("all package installing ✅")
        else:
            print("✅ All packages are already installed.") 
        #install()
    except subprocess.CalledProcessError:
        print("⚠️ Internet connection is required to open the browser!")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

#install() #test
# variable

MIN_VERSION = (3, 6, 0)  # min version py
DOWNLOAD_URL = {
    'Windows': 'https://www.python.org/downloads/windows/',
    'Linux': 'https://www.python.org/downloads/source/',
    'Darwin': 'https://www.python.org/downloads/macos/' #mac
}
def parse_version(version_str):
    parts = []
    for part in version_str.split('.')[:3]:  # sort number with 3 first number
        part = ''.join(c for c in part if c.isdigit()) or '0'  # sort just number
        parts.append(int(part))
    return tuple(parts + [0]*(3-len(parts))) #place 0
def check_python_version(): #check py version
    
    try:
        current_version = parse_version(platform.python_version())
        os_type = platform.system()  
        download_url = DOWNLOAD_URL.get(os_type, 'https://www.python.org/downloads/')  # Set default value
        current_version = parse_version(platform.python_version())
        
        if current_version < MIN_VERSION:
            print(f"\n your python version old{platform.python_version()})")
            print(f"you need python{'.'.join(map(str, MIN_VERSION))}+ version")
                
            download_url = DOWNLOAD_URL.get(os_type, 'https://www.python.org/downloads/')
            if os_type == "Windows":
                    print("\nHelp")
                    print("1. download with this url :", download_url)
                    print("2.run installer (exe) ")
                    print("3. Enable 'Add Python to PATH' in installer Gui")
            elif os_type == "Linux":
                    print("\nTerminal command")
                    print("sudo apt update && sudo apt install python3.9")
                    print("or with newer version")
                    print("sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt install python3.11")    

            else:
                    print("\n download", download_url)

            print("\n🔗Opening Browser ...")
            try:
                webbrowser.open(download_url)
            except Exception:
                 print("⚠️ Internet connection is required to open the browser!")
            sys.exit(1)
        else:
            print(f"Your Python version ({platform.python_version()}) is up-to-date.")
    except Exception as e:
        print(f"❌ we cant check your py version: {str(e)}")
        sys.exit(1)        
     