import sys
import os
from subprocess import call, STDOUT
from colors import *
import time
from textwrap import *
from terminaltables import *
#Getting location of PentestBox
pentestbox_ROOT_DIRECTORY=os.environ['pentestbox_ROOT']
#Setting location
scripts_location=pentestbox_ROOT_DIRECTORY+"/bin/scripts/"
bin_location=pentestbox_ROOT_DIRECTORY+"/bin"
custom_tool_location=bin_location+"/customtools"
#Updating Function for updating all files in scripts folder
def updating_scripts():
    print green("Updating Required Files")
    os.chdir(scripts_location)
    os.system('git fetch --all')
    os.system('git reset --hard origin/master')
    time.sleep(1)
    os.system('clear')
#First go to customaliases path and then append alias to that file.
def add_alias(filename):
    customaliasespath=pentestbox_ROOT_DIRECTORY+"/bin/customtools"
    os.chdir(customaliasespath)
    customaliasesfile=open('customaliases','a')
    terminal_alias=file_parser(filename, "TERMINAL_ALIAS")
    path_for_alias=file_parser(filename, "PATH_FOR_ALIAS")
    customaliasesfile.write(terminal_alias+"="+path_for_alias+"\n")
    customaliasesfile.close()
#welcome menu
def welcome():
    print cyan("Welcome to PentestBox tools installation Utility.")
    print ("You can install any of the tool from the categories given below. Choose the corresponding number.")
    print ("Enter ")+ cyan("exit")+ (" to exit.")
    print("     0. Android")
    print("     1. Exploitation Tools")
    print("     2. Forensics")
    print("     3. Information Gathering")
    print("     4. Password Attacks")
    print("     5. Privacy")
    print("     6. Reverse Engineering")
    print("     7. Sniffing")
    print("     8. Stress Testing")
    print("     9. Vulnerability Analysis")
    print("     10. Web Applications")
    print("     11. Update all installed Modules")

    choice = raw_input("Enter Your Choice: ")
    if choice=="0":
        os.system("clear")
        print ("\n")
        print "Android Security Tools"
        header()
        parse_tools("/modules/android")
    elif choice=="1":
        os.system("clear")
        print ("\n")
        print ("Exploitation Tools" )
        header()
        parse_tools("/modules/exploitationTools")
    elif choice=="2":
        os.system("clear")
        print ("\n")
        print ("Forensics Tools" )
        header()
        parse_tools("/modules/forensic")
    elif choice=="3":
        os.system("clear")
        print("\n")
        print "Information Gathering Tools"
        header()
        parse_tools("/modules/informationGathering")
    elif choice=="4":
        os.system("clear")
        print("\n")
        print "Password Attacks Tools"
        header()
        parse_tools("/modules/passwordAttacks")
    elif choice=="5":
        os.system("clear")
        print("\n")
        print "Privacy Tools"
        header()
        parse_tools("/modules/privacy")
    elif choice=="6":
        os.system("clear")
        print("\n")
        print "Reverse Engineering Tools"
        header()
        parse_tools("/modules/reverseEngineering")
    elif choice=="7":
        os.system("clear")
        print("\n")
        print "Sniffing Tools"
        header()
        parse_tools("/modules/sniffing")
    elif choice=="8":
        os.system("clear")
        print("\n")
        print "Stress Testing Tools"
        header()
        parse_tools("/modules/stressTesting")
    elif choice=="9":
        os.system("clear")
        print("\n")
        print "Vulnerability Analysis"
        header()
        parse_tools("/modules/vulnerabilityAnalysis")
    elif choice=="10":
        os.system("clear")
        print("\n")
        print "Web Applications Analysis Tools"
        header()
        parse_tools("/modules/webApplications")
    elif choice=="11":
            tools_updater("/android")
            tools_updater("/exploitationTools")
            tools_updater("/forensic")
            tools_updater("/informationGathering")
            tools_updater("/passwordAttacks")
            tools_updater("/privacy")
            tools_updater("/reverseEngineering")
            tools_updater("/sniffing")
            tools_updater("/stressTesting")
            tools_updater("/vulnerabilityAnalysis")
            tools_updater("/webApplications")
    elif choice=="exit":
        os.system("clear")
        sys.exit
    else:
        print("\n")
        print "         Invalid Option!"
#List out all tools of a category and then present options
def parse_tools(categoryPath):
    modules_path = scripts_location + categoryPath
    table_data_short=[]
    for path, subdirs, files in os.walk(modules_path):
        for name in files:
            if ".md" not in name:
                filename = os.path.join(path, name)
                description=file_parser(filename, "DESCRIPTION")
                long_string=(str(description))
                if len(long_string) > 120:
                    table=DoubleTable([[name,'']])
                    max_width = table.column_max_width(1)
                    wrapped_string = '\n'.join(wrap(long_string, max_width))
                    table.table_data[0][1] = wrapped_string
                    print(table.table)
                else:
                    table_data_short.append([name,long_string])
    table_short=DoubleTable(table_data_short)
    table_short.inner_heading_row_border = False
    table_short.inner_row_border = False
    print (table_short.table)

    print "\n"
    print ("Install/Update/Uninstall any of the above tool.\nFor example:")+yellow("install xyz") +" will install xyz, "+yellow("update xyz")+" will update xyz and "+yellow("uninstall xyz")+" will Uninstall xyz \nEnter "+ cyan("back")+ (" for main menu and ")+green("exit")+(" to exit\n")
    value=raw_input("")
    if value=="exit":
        os.system("clear")
        sys.exit
    elif value=="back":
        os.system("clear")
        welcome()
    elif "install"==value[0:7]:
            for path, subdirs, files in os.walk(modules_path):
                for name in files:
                    filename = os.path.join(path, name)
                    if name.lower() == value[8:] or name.lower() == value[8:]:
                        install_module(filename)
                        add_alias(filename)
                        print yellow(name) + (" Successfully Installed")
                        print ("Restart or open a new tab to run ")+yellow(name)
                        terminal_alias=file_parser(filename,"TERMINAL_ALIAS")
                        print ("Alias for ")+yellow(name)+(": ")+blue(terminal_alias)
    elif "update"==value[0:6]:
            for path, subdirs, files in os.walk(modules_path):
                for name in files:
                    filename = os.path.join(path, name)
                    if name.lower() == value[7:] or name == value[7:]:
                        update_module(filename,name)
                        os.system("clear")
                        welcome()
    elif "uninstall"==value[0:9]:
        for path, subdirs, files in os.walk(modules_path):
            for name in files:
                filename = os.path.join(path, name)
                if name.lower() == value[10:] or name == value[10:]:
                    remove_module(filename,name)
                    Print ("Succesfully removed: ")+yellow(name)
                    welcome()

    else:
        os.system('clear')
        print red("   Invalid Command!")
        welcome()
#For Updating single module
def update_module(filename,name):
    update_location = file_parser(filename, "INSTALLATION_CATEGORY")
    update_location=custom_tool_location+update_location
    update_location = update_location +"/"+ name + "/"
    os.chdir(update_location)
    if is_git_directory():
        os.system("git pull origin master")
    else:
        print cyan("Not a git repository.Only git repository can be updated.")
#Check all the folder in a directory and then update them if there are git directory
def tools_updater(tools_category):
    folder_path=custom_tool_location+tools_category
    for f in os.listdir(folder_path):
        tools_folder=os.path.join(folder_path,f)
        os.chdir(tools_folder)
        if is_git_directory():
            print cyan("Updating: ")+yellow(f)
            os.system("git pull origin master")
#Determines if directory is a git directory or not
def is_git_directory():
    if call(["git", "log"], stderr=STDOUT, stdout=open(os.devnull, 'w')) != 0:
        return 0
    else:
        return 1
#Install module by passing commands in the tool directory
def install_module(filename):
    install_location = file_parser(filename, "INSTALLATION_CATEGORY")
    install_location=custom_tool_location+ str(install_location)
    command = file_parser(filename, "COMMANDS")
    if os.path.isdir(install_location):
        os.chdir(install_location)
    else:
        os.mkdir(install_location)
        os.chdir(install_location)
    if "," in command:
        original_command = command
        command = command.split(",")
        for commands in command:
        	if "cd" in commands:
			commands=commands.replace("cd ","")
			os.chdir(commands)
		else:
               		os.system("pwd")
	            	os.system(commands)
    else:
        os.system(command)
#This function remove module, first removing folder then removing alias.
def remove_module(filename,name):
    install_location = file_parser(filename, "INSTALLATION_CATEGORY")
    install_location=custom_tool_location+ str(install_location)+"/"
    os.chdir(install_location)
    remove_command="rm -rf "+str(name)
    os.system(remove_command)
    terminal_alias=file_parser(filename, "TERMINAL_ALIAS")
    path_for_alias=file_parser(filename, "PATH_FOR_ALIAS")
    complete_alias=str(terminal_alias)+"="+str(path_for_alias)
    complete_alias_n=complete_alias+"\n"
    os.chdir(custom_tool_location)
    print complete_alias_n
    f=open("customaliases","r")
    lines=f.readline()
    f.close()
    f=open("customaliases","w")
    for line in lines:
        if line!=complete_alias or line!=complete_alias_n:
            f.write(line)
    f.close()
#This Function add Name and Description in tabular form for modules listing
def header():
    print ("""=================================

      """) + ("""Name                                                 Description """)
#Check for string a file
def file_parser(filename, term):
    if os.path.isfile(filename):
        counter = 0
        fileopen = file(filename)
        for line in fileopen:
            line = line.rstrip()
            if line.startswith(term):
                line = line.replace(term + "=", "")
                line = line.replace('"', "", 2)
                counter = 1
                return line
    if not os.path.isfile(filename):
        return None
updating_scripts()
welcome()
