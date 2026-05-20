'''Timestamp module.

The module contains a class to redefine the built-in print() method.
'''


from datetime import datetime


now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class Timestamp:
    
    def __init__(self, message):
        self.time = now
        self.message = message
    

    def __str__(self):
        return f'{self.time} {self.message}'
