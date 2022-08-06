import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

playerName = ""

required = ("\nUse only A, B, or C\n") #Cutting down on duplication

#The story is broken into sections, starting with "intro"
def intro():
  print ("Welcome player, you have been summoned to defeat C'tri the Lord of fire")
  time.sleep(1)
  playerName = input(">>> What shall thou be called henceforth? ")
  print ("We are happy to have you with us " + playerName)
  time.sleep(1)
  print("***INTERRUPTION***")
  time.sleep(2)
  print("A minion has appeared, but rest assured, you are not without deadly options!!! You look around the room and see a bucket and a stick\n")
  print("""
  
                 ..::.  .::..                     
              .::^^~!!:^!!~^^::.                  
             ::::::::::::::^^^^^:                 
            .:..:::::::::::^^^^^^.                
           ...:^!!!~~~~^^~~!!!!~~^.               
          .::~77~^^^!7!~7~^:^~77!!^.              
         .JY~?7. :??^77?~~?7. :?7JP7              
          ~7^77: ^?7^!!7!~?7..^7!!?^              
           .:^!7~~~~!~7!!!~~~!7~^~^               
          ..:::^^~~~!777!~~~~~~~~~^.              
           .:::::^^^^^^^^^~~~~~~~~^               
          ::.::::::::^^^^^^^^^^^^^~:              
          !!~::::::::::::::^^^^~!?5?              
          :~77?7!!~!!!!!!!77?JY5P5?^              
         .:::!55Y?JJYYYY5555PGGP7~~~:             
        .:^^::????JJJ5PPP55555PY^^!!^             
        .:7~:^7????JYGGGB55555PJ~!J?^.            
         :?77?????JYY5PP5555555555PJ^             
        ^!JYJJ?JJJYYYY5555555555PPGY7:            
        7B#BYYY55555555PPPPPPP555Y##B^            
        JBB&&Y.:~5GBBBJ5#BB#G7!!B@#BB?~~~^^^::.   
        :^757  ..7#&&B7?B&&#?777?PBYJ?777777!~:.  
          .::::^!5##BY775###Y!!!!~~~~^^:::...     
                 :::.   ..::..                  
  """)
  time.sleep(1)
  print ("""  A. Grab the bucket and throw it at the minion
  B. grab a stick and poke the miRnion
  C. Run""")
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    option_bucket()
  elif choice in answer_B:
     option_stick()
  elif choice in answer_C:
    print ("\nWelp, that was quick. "
    "\n\nYou died!")
  else:
    print (required)
    intro()

def option_bucket(): 
  print ("\nThe minon is stunned")
  time.sleep(1)
  print ("""  A. Kick the minion whilst yelling out like Bruce Lee ©"
  B. Punch the minion whilst grunting like the Hulk©
  C. Run """)
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nTODO")
  elif choice in answer_B:
    print ("\nTODO")
  elif choice in answer_C:
    print ("\nTODO")
  else:
    print (required)
    print ("\nWelp, that was quick. "
    "\n\nYou died!")

def option_stick():
  print ("\nYou pick up the stick and swing at the minion in the: ")
  time.sleep(1)
  print ("""  A. Eye
  B. Mouth
  C. Run""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nTODO")
  elif choice in answer_B:
    print ("\nTODO")
  elif choice in answer_C:
      print ("\nYou're no match for an orc. "
    "\n\nYou died!")
  else:
    print (required)
    print ("\nTODO")

def option_finalboss():
    print("""
............   ..::^^~~~~~~^^^^:..   ............:
            .:^^^:::!7~^^..:::^^^^^^:            :
         .^^^:..    !5?YJ!^.::::...:^~^:.        :
       :~^.   .:::::~G###&P^::^^:......^~^.      :
     :~^.   ..::^^^^:~Y#&&&BY!^^^::::... :~~.    :
   .~~. .:^^^~~~~~^:...~7YB@@#P7::::::... .:!:   :
  .!^ ..:~~~77!~::^^:.....^JG&@&P?~^^:::... .!^  :
 .!:..:^^!?YB#BGJ~:::.......:!Y#@@BY~^^^:.....!^ :
 !^..::^?B@@@&#BG?~..:........:~JG&@BJ~^^:.....7:.
^7..:^~P@@@#BPY7~~^...^!!~~....::^!Y&@B?~^::.. ^7:
7~.::^G@@@GJ!^^~^^:...JY^!J!....::^^7G@@G!^:....7:
7^.::^Y&@@G?^::^^^^:..:J~7J^::....:^^7#@@P^:....!:
7^..:^^?#@@5~::::::..^~!7~:...~^..::^!#@G~::....!:
!!...::^!G@#!^::... ^!~^.......~: .::!&P^::... :7:
.!....:::~P@5^:... :~::^:.......^~...~?:.....  ~~:
 ^~......::?P~...:7?: .~:..  .. :!!^:: ..     :~.:
  ^~.  .....:::^~7!:  .:....  .:   ..        :~. :
   ^~.       .:::    ......   .^^           ^~.  :
    .~^.       ..   ......     .:.        .~^    :
      :~:.         ..       .....:.     :^^.     :
        :^^:.      .           . ..  .^^^.       :
          .:^^::..             ...:^^:.          :
.             .::^^^^:::::::^^^^^:..             :
    
    """)


intro()