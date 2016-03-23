Every module need to have five inputs

* DESCRIPTION
* INSTALLATION_CATEGORY
* COMMANDS
* PATH_FOR_ALIAS
* TERMINAL_ALIAS

Order is not necessary. Value to these parameters should be on different lines.

* DESCRIPTION should contain description of the tool. You can also include website link in the value.
* INSTALLATION_CATEGORY should contain category name. In case for **passwordAttacks** it should be **/passwordAttacks**.
* COMMANDS should contain all the commands which should be passed to the terminal to install that tool.
  * If any tool require python module, it can installed through **pip**. In that case add **python -m pip install module_name** to the COMMANDS.
  * If any tool require ruby gem, it can be installed. In that case add **gem install gem_name** to the COMMANDS.
* PATH_FOR_ALIAS should contain path as well it's requirement.
* TERMINAL_ALIAS should contain alias for calling that tool.
