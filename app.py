#py -m pip install termcolor
#whenever u get no module -> py -m pip install module
#pip3 install pyfiglet or py -m pip install pyfiglet
#py -m pip install requests  after ^ 


import os
import pyfiglet
import requests
import warnings
from termcolor import colored
from flask import Flask, request
from flask_cors import *
# abover r the libraries

app = Flask(__name__) # init Flask web server

CORS(app)

@app.route('/', methods=['POST']) # every time person hits url, run respondWithData()
def respondWithData(): # add function for responding
    print(request.get_json())
    url = request.get_json()['url']

    try:  #new thing i learnt. it tests the code for erroers.
        os.system('clear')
        """print((colored(pyfiglet.figlet_format('Rick Roll Checker'), color='blue')))
        print((colored('\t' + '*'*27, color='yellow')))
        print((colored('\t[+] Rick Roll Checker', color='green')))
        print((colored('\t[+] Built during winter break 21', color='green')))
        print((colored('\t[+] Built by Sanjay/Bronco', color='green'))) #bronco is my online name lol
        print((colored('\t' + '*'*27 + '\n\n', color='yellow')))"""


        warnings.filterwarnings("ignore")

        #ina =input(colored('[+] Please input the link: ', color='yellow'))
        httpis='http://'
    #if else statement 
        if url.startswith("http"):
            ot=requests.request("GET",url)
            cont = ot.text
            warnings.filterwarnings("ignore")
        else:
            ot=requests.request("GET",httpis+url, verify=False)
            cont = ot.text
            warnings.filterwarnings("ignore")


        if "never gonna give you up" in cont or 'dQw4w9WgXcQ' in cont:   #this is to check if the song name is on the link. or the url
            print(colored('\n[!] The link is a Rick Roll. Do not open it unless u actually like rick astley which is VERY RARE\n', color='red'))
            return {
                "Result": "[!] The link is a Rick Roll. Do not open it unless u actually like rick astley which is VERY RARE"
            }
        else:
            print(colored('\n[+] The link IS NOT a Rick Roll. You can safely open it in your browser\n', color='red'))
            return {
                "Result": "[+] The link IS NOT a Rick Roll. You can safely open it in your browser"
            }

    except:
        print(colored('\n\n[-] There was an error\n[-] 1. Check if the URL is correct\n', color='red')) #if the user uploads something other than a link it will send this 
        return {
            "Result": "[-] There was an error. Check if the URL is correct"
        }

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000', debug=True)