import pystyle, requests, threading, os, logging
from pystyle import Colorate, Colors, Write


logo = """
         __             _,-"~^"-.
       _// )      _,-"~`         `.                ╔═╗╦╔╦╗╔═╗╦═╗╔═╗╔═╗      
     ." ( /`"-,-"`                 ;               ║ ╦║ ║ ╠═╝╠╦╝║ ║╠╣
    / 6                             ;              ╚═╝╩ ╩ ╩  ╩╚═╚═╝╚
   /           ,             ,-"     ;
  (,__.--.      \           /        ;
   //'   /`-.\   |          |        `._________
     _.-'_/`  )  )--...,,,___\     \-----------,)
   ((("~` _.-'.-'           __`-.   )         //
         ((("`             (((---~"`         //
                                            ((________________
                                            `----\"\"\"\"~~~~^^^```
                
"""

print(Colorate.Horizontal(Colors.red_to_yellow, logo, 1))
logging.basicConfig(
    level=logging.INFO,
    format="\033[38;5;21m[\033[0m%(asctime)s.%(msecs)03d\033[38;5;21m] \033[0m%(message)s\033[0m", 
    datefmt="%H:%M:%S" 
)
camourl = Write.Input("Please enter your ReadMe view counter link: ", Colors.red_to_yellow, interval=0.05)

if "https://" in camourl:
  print("\n")
else:
  Write.Print("Error! Invalid url selected, please try again", Colors.red_to_yellow, interval=0.05)

amount = Write.Input("Amount of Threads: ", Colors.red_to_yellow)
total = 0
def rape():
  while True:  
     req = requests.get(camourl)
     if req.status_code == 403:
         logging.info("Unable to fufill request!")
     else:
      global total
      total += 1
      logging.info(f"Request No. {total} sent")

for _ in range(int(amount)):
    t = threading.Thread(target=rape)
    t.start()

