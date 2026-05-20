
'''Data module.

The module contains a class to store constant variables.
'''
from dataclasses import dataclass

@dataclass
class Defaults:
    LICENSE: str = "D:/pa_config/comlicbits.h"
    BUILDS:  str = "D:/gitbash/pa6autotests/Builds"
    SCRIPT:  str = "D:/gitbash/help/testBuild.cmd"
