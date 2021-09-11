# Made by @venaxyt on Github | https://github.com/venaxyt
try:  # Install wmi if w mi is not installed, you don't need to do it if you are going to compile your script as executable.
    import wmi
except:
    from os import system; system("py -m pip install wmi >nul")

# It will check if user is using an Oracle virtual machine.
def virtual_check():
    if wmi.WMI().Win32_ComputerSystem()[0].Manufacturer == "innotek GmbH":
        return True
    else:
        return False
