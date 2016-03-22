from subprocess import call, STDOUT
import os
import sys
from colors import *
import time
#Getting location of PentestBox
pentestbox_ROOT_DIRECTORY=os.environ['pentestbox_ROOT']
bin_location=pentestbox_ROOT_DIRECTORY+"/bin"
base_location=pentestbox_ROOT_DIRECTORY+"/base/"
config_location=pentestbox_ROOT_DIRECTORY+"/config/"
scripts_location=bin_location+"/scripts"
def updating_scripts():
    print green("Updating Required Files")
    os.chdir(scripts_location)
    os.system('git fetch --all')
    os.system('git reset --hard origin/master')
    time.sleep(1)
    os.system('clear')
def is_git_directory():
    if call(["git", "log"], stderr=STDOUT, stdout=open(os.devnull, 'w')) != 0:
        return 0
    else:
        return 1
def tools_updater(tools_category):
    folder_path=bin_location+tools_category
    for f in os.listdir(folder_path):
        tools_folder=os.path.join(folder_path,f)
        os.chdir(tools_folder)
        if is_git_directory():
            print cyan("Updating: ")+yellow(f)
            os.system("git pull origin master")

def config_updater():
        os.chdir(config_location)
        print cyan("Updating: ")+yellow('config')
        os.system('git fetch --all')
        os.system('git reset --hard origin/master')
def clink_updater():
    for f in os.listdir(base_location):
        tools_folder=os.path.join(base_location,f)
        os.chdir(tools_folder)
        if is_git_directory():
            print cyan("Updating: ")+yellow(f)
            os.system("git pull origin master")
def main():
    print cyan("Welcome to PentestBox tools update Utility.")
    print ("Choose from the numbers given below to update corresponding category.")
    print ("Type ")+green("exit ")+("to exit.")
    print("     0. Update Everything in PentestBox")
    print("     1. Android")
    print("     2. Exploitation Tools")
    print("     3. Forensics")
    print("     4. Information Gathering")
    print("     5. Password Attacks")
    print("     6. Reverse Engineering")
    print("     7. Sniffing")
    print("     8. Stress Testing")
    print("     9. Web Applications")
    print("     10. PentestBox Config Files")
    choice = raw_input("Enter Your Choice: ")
    if choice=="0":
        tools_updater("")
        tools_updater("/androidsecurity")
        tools_updater("/ExploitationTools")
        tools_updater("/ForensicTools")
        tools_updater("/InformationGathering")
        tools_updater("/password_attacks")
        tools_updater("/ReverseEngineering")
        tools_updater("/Sniffing")
        tools_updater("/StressTesting")
        tools_updater("/WebApplications")
        config_updater()
        clink_updater()
    elif choice=="1":
        os.system("clear")
        tools_updater("/androidsecurity")
        os.system("clear")
        main()
    elif choice=="2":
        os.system("clear")
        tools_updater("/ExploitationTools")
        os.system("clear")
        main()
    elif choice=="3":
        os.system("clear")
        tools_updater("/ForensicTools")
        os.system("clear")
        main()
    elif choice=="4":
        os.system("clear")
        tools_updater("/InformationGathering")
        os.chdir(bin_location+"/nmap")
        os.system("git pull origin master")
        print cyan("Updating: ")+yellow("Nmap")
        os.system("clear")
        main()
    elif choice=="5":
        os.system("clear")
        tools_updater("/password_attacks")
        os.system("clear")
        main()
    elif choice=="6":
        os.system("clear")
        tools_updater("/ReverseEngineering")
        os.system("clear")
        main()
    elif choice=="7":
        os.system("clear")
        tools_updater("/Sniffing")
        os.chdir(bin_location+"/Wireshark")
        os.system("git pull origin master")
        print cyan("Updating: ")+yellow("Nmap")
        os.system("clear")
        main()
    elif choice=="8":
        os.system("clear")
        tools_updater("/StressTesting")
        os.system("clear")
        main()
    elif choice=="9":
        os.system("clear")
        tools_updater("/WebApplications")
        os.system("clear")
        main()
    elif choice=="10":
        config_updater()

    elif choice=="exit":
        os.system("clear")
        sys.exit
    else:
        print("\n")
        print "         Invalid Option!"
updating_scripts()
main()
