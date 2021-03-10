import os
import requests

class Insults:

    def GetInsult(self):
        txt = requests.get("https://insult.mattbas.org/api/insult.txt")
        print(txt.text)
        return txt.text

