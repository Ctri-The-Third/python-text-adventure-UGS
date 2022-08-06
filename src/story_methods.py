import time


def intro():


    time.sleep(1)
    print(
        """  A. Grab the bucket and throw it at the minion
  B. grab a stick and poke the miRnion
  C. Run"""
    )
    choice = input(">>> ")  # Here is your first choice.
    if choice in answer_A:
        option_bucket()
    elif choice in answer_B:
        option_stick()
    elif choice in answer_C:
        print("\nWelp, that was quick. " "\n\nYou died!")
    else:
        print(required)
        intro()


def option_bucket():
    print("\nThe minon is stunned")
    time.sleep(1)
    print(
        """  A. Kick the minion whilst yelling out like Bruce Lee ©"
  B. Punch the minion whilst grunting like the Hulk©
  C. Run """
    )
    choice = input(">>> ")
    if choice in answer_A:
        print("\nTODO")
    elif choice in answer_B:
        print("\nTODO")
    elif choice in answer_C:
        print("\nTODO")
    else:
        print(required)
        print("\nWelp, that was quick. " "\n\nYou died!")


def option_stick():
    print("\nYou pick up the stick and swing at the minion in the: ")
    time.sleep(1)
    print(
        """  A. Eye
  B. Mouth
  C. Run"""
    )
    choice = input(">>> ")
    if choice in answer_A:
        print("\nTODO")
    elif choice in answer_B:
        print("\nTODO")
    elif choice in answer_C:
        print("\nYou're no match for an orc. " "\n\nYou died!")
    else:
        print(required)
        print("\nTODO")


def option_finalboss():
    print(
        """
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
    
    """
    )
