"""
getpass.getpass() doesn't work properly in git bash. 

Do the following steps:

    1. change directory
        cd ~ 
    2. create .bashrc
        vi .bashrc
    3. add the following command to .bashrc
        alias python='winpty python.exe'
    4. restart git bash terminal or run
        source .bashrc 
    5. in .bash file, add 'winpty' before 'python' 
         winpty python test.py
"""
import getpass

a = getpass.getpass()
print("password received!")

