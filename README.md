This Repository contains two utility:
* ToolsManager - Using this a user can install/update/uninstall tools which are not present in PentestBox by default. 
* Update - This is a new version of update utility. Basically can update all tools category wise or all at one time. Also this is responsible for updating config files.

Modules folder contains modules through which tools can be installed which are not present in PentestBox by default.

Every module need to have five inputs

* DESCRIPTION
* INSTALLATION_DIRECTORY
* COMMANDS
* PATH_FOR_ALIAS
* TERMINAL_ALIAS

Order is not neccessary. Value to these parameters should be on different lines.

* DESCRIPTION should contain description of the tool. You can also include website link in the value.
* INSTALLATION_DIRECTORY should contain category name. In case for **webApplications** it should be **/webApplications**.
* COMMANDS should contain all the commands which should be passed to the terminal to install that tool.
  * If any tool require python module, it can installed through **pip**. In that case add **python -m pip install module_name** to the COMMANDS.
  * If any tool require ruby gem, it can be installed. In that case add **gem install gem_name** to the COMMANDS.
* PATH_FOR_ALIAS should contain path as well it's requirement.
* TERMINAL_ALIAS should contain alias for calling that tool.

####Example of a Module

Let us consider an example of [/modules/passwordAttacks/oclHashcat-amd-2.01](https://github.com/PentestBox/scripts/blob/master/modules/passwordAttacks/oclhashcat-amd-2.01)

DESCRIPTION="Worlds fastest password cracker and only GPGPU based rule engine. FOR AMD"
INSTALLATION_CATEGORY="/passwordAttacks"
COMMANDS="wget --no-check-certificate https://hashcat.net/files/oclHashcat-2.01.7z,7za x oclHashcat-2.01.7z,rm oclHashcat-2.01.7z"
PATH_FOR_ALIAS="%pentestbox_ROOT%/bin/tools/oclHashcat-2.01/oclHashcat64.exe" $*
TERMINAL_ALIAS=oclhashcat64

COMMANDS should all commands needs to be passed to terminal.
PATH_FOR_ALIAS should contain path to the file for which alias need to be created.
TERMINAL_ALIAS should contain actual alias need to be set.

You can create a pull request with your module after testing that on PentestBox.


