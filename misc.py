'''Miscellaneuos functions module.

The module contains miscellaneous functions, i.e. those which
- print the current time
- close the script
- process the user's input
'''

import os
import sys

from pathlib import Path
from timestamp import now, Timestamp


def printf(message) -> None:
    '''Prints timestamp and a message.'''
    print(Timestamp(message))


def store_exit_values() -> tuple:
    '''Stores exit values.'''
    return (
        "exit",
        "eixt",
        "Exit",
        "EXIT",
        "ext" ,
        "учше",
        "УЧШЕ"
    )


def set_env(nodejs, license, source_data) -> dict:
    '''Sets enviromental variables.'''
    env = os.environ.copy()
    env["MISHARED"] = str(nodejs)
    env["COMLICBITSPATH"] = str(license)
    env["SOURCEDATA"] = str(source_data)
    return env


def get_build_number(exit) -> str:
    '''Gets a build number for a default path.'''
    user_input = input(f"{now} ")
    if user_input in exit:
        printf("Exiting...")
        printf("Exited")
        sys.exit(0)
    return user_input


def get_folder_path(build_number: str, builds: str) -> Path:
    '''Checks if the entered path is a folder.'''
    build_path = Path(f"{builds}\\{build_number}")
    if not build_path.exists() and not build_path.is_dir():
        printf('The folder does not exist or not a folder at all.')
        printf('Press Enter to close to programm.')
        input()
        sys.exit(1)
    else:
        return build_path
