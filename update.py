from subprocess import call, STDOUT
import os
import sys
from colors import *
import time
from terminaltables import AsciiTable
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
        if f=="metasploit-framework":
            tools_folder=os.path.join(folder_path,f)
            os.chdir(tools_folder)
            print cyan("Updating: ")+yellow("Metasploit")
            os.system("git fetch --all")
            os.system('git reset --hard origin/master')
            os.system("bundle install")
        else:
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
        tools_folder=os.path.join(folder_path,f)
        os.chdir(tools_folder)
        if is_git_directory():
            print cyan("Updating: ")+yellow(f)
            os.system("git pull origin master")
def welcome():
    print cyan("Welcome to PentestBox tools update Utility.")
    table_data=[["Commands"," "],["update all","Updates Everything in PentestBox"],["update android","Updates Android Security Tools"],
                ["update exploitation","Updates Exploitation Tools"],["update forensics","Updates Forensics Tools"],
                ["update informationgathering","Updates InformationGathering Tools"],["update passwordattacks","Updates Password Attacks Tools"],
                ["update reverseengineering","Updates Reverse Engineering Tools"],["update sniffing","Updates Sniffing Tools"],
                ["update stresstesting","Updates Stress Testing Tools"],["update webapplication","Updates WebApplication Tools"],
                ["update config","Updates PentestBox Config Files"]]
    table=AsciiTable(table_data)
    print table.table
def main():
    if sys.argv[1]=="all":
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
    elif sys.argv[1]=="android":
        os.system("clear")
        tools_updater("/androidsecurity")
    elif sys.argv[1]=="exploitation":
        os.system("clear")
        tools_updater("/ExploitationTools")
    elif sys.argv[1]=="forensic":
        os.system("clear")
        tools_updater("/ForensicTools")
    elif sys.argv[1]=="informationgathering":
        os.system("clear")
        tools_updater("/InformationGathering")
        os.chdir(bin_location+"/nmap")
        os.system("git pull origin master")
        print cyan("Updating: ")+yellow("Nmap")
    elif sys.argv[1]=="passwordattacks":
        os.system("clear")
        tools_updater("/password_attacks")
    elif sys.argv[1]=="revereengineering":
        os.system("clear")
        tools_updater("/ReverseEngineering")
    elif sys.argv[1]=="sniffing":
        os.system("clear")
        tools_updater("/Sniffing")
        os.chdir(bin_location+"/Wireshark")
        os.system("git pull origin master")
        print cyan("Updating: ")+yellow("Nmap")
    elif sys.argv[1]=="stresstesting":
        os.system("clear")
        tools_updater("/StressTesting")
    elif sys.argv[1]=="webapplication":
        os.system("clear")
        tools_updater("/WebApplications")
    elif sys.argv[1]=="config":
        config_updater()
def main2():
    if len(sys.argv) > 1:
        main()
    else:
        welcome()
updating_scripts()
main2()
