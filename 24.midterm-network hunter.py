
#alright the goal for this version is to make it considerably shorter for class
#clean up the code keep it simplistic and user friendly

#some goals
#1. better ranking system scoring sytem whatever
#2. better functions
#3. port dictionary for ablities 
#4. some little animation loops
#5. make sure the program actually does something lol

#import time
import time

#import os as terminal because i use os as a variable name
import os as terminal

#import random
import random

#main function responsible for handling most of the inputs and calling the host function
def main():

    #port_active = True

    #global port_list

    #draw_title()

    #draw_terminal_header()

#while loop 

    while True:

        terminal.system("cls")

        #port_active_counter = 0

        #port_list = []

        #function which draws the title
        draw_title()

        #function which draws the header
        draw_terminal_header()

        #nested while loop
        while True:

            #try block
            try:

                #print statement
                print("Enter the information below to discover a monster!\n")

                #ask user to enter an ip address strip and lower case the result
                ip_address = input("Enter an ipv4 address(ex. 192.168.0.1)\n> ").strip()

                #split the ip address into octets at each .
                octet_one,octet_two,octet_three,octet_four = ip_address.split(".")

                #turn each octet into an integer
                octet_one = int(octet_one)

                octet_two = int(octet_two)

                octet_three = int(octet_three)

                octet_four = int(octet_four)

                #if each octet is not in the range 0 - 255 we raise a value error
                if not 0 <= octet_one <= 255 or not 0 <= octet_two <= 255 or not 0 <= octet_three <= 255 or not 0 <= octet_four <= 255:
                    raise ValueError

            #except block for the value error we raise
            except ValueError:

                #print statement asking user to try again
                print("\ninvalid ip address try again\n")

            else:
                break

        #clear the terminal after a successful ip attempt
        terminal.system("cls")

        #draw title 
        draw_title()

        #draw terminal header    
        draw_terminal_header()

        #print statement
        print("Enter the information below to discover a monster!")

        print(r"""
select from operating systems:
windows
linux
mac
""")

        #ask user for an operating system name. Strip and lowercase the result    
        os = input("\nEnter your operating system: \n>").strip().lower()

        #clear the terminal screen
        terminal.system("cls")

        #draw title    
        draw_title()

        #draw header        
        draw_terminal_header()

        print("Enter the information below to discover a monster!")

        #print statement using r""" displays devices users can choose from
        print(r"""
select from devices:
laptop
phone
desktop
""")
        
        #ask user to enter a device
        device = input("\nEnter your device: \n>").strip().lower()

        #clear screen
        terminal.system("cls")

        #draw title
        draw_title()

        #draw header
        draw_terminal_header()

        #print statement
        print("Enter the information below to discover a monster!")

        #print statement using r""" displays ports users can choose from
        print(r"""
select from the available ports:
21
22
25
53
80
443                    
""")

        #print statement asking for user to choose 3 ports from the list entered one at a time
        print("choose 3 ports from the list. enter them one at a time ")

        #set the port_function in variable port_f
        selected_ports = port_function()

        # settting the ip_info function equal to the variable private_or_public
        private_or_public = ip_info(octet_one,octet_two)

        host(os,ip_address,octet_one,octet_two,octet_three,octet_four,device,private_or_public,selected_ports)

#function draw_title
#print the ascii art using r"""
def draw_title():
        print(r"""
███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗
████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝
██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝█████╔╝
██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██╔═██╗
██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗
╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝

    ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗
    ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
    ███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
    ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
    ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
""")

#define function draw_terminal_header draws the header
def draw_terminal_header():

    print("===========================")
    
    print ("Network Hunter")
    
    print("===========================\n")


#def bit_check(octet_one,octet_two,octet_three,octet_four):

#    if 0 <= octet_one <= 255 and 0 <= octet_two <= 255 and 0 <= octet_three <= 255 and 0 <= octet_four <= 255:
#        return True
    
#    else:

#        return "invalid ip"

#define function ip_info which takes two parameters octet_one and octet_two 
def ip_info(octet_one,octet_two):

    #return string private
    if octet_one == 10:

        #return string private
        return "private"

    #elif octet_one equivelant to 172 and octet two is in the range of numbers 16-31
    elif octet_one == 172 and 16 <= octet_two <= 31:

        #return string private
        return "private"

    #elif octet_one equivelant to 192 and octet_two equivelant to 168
    elif octet_one == 192 and octet_two == 168:

        #return string private
        return "private"

    #elif octet_one equivelant to 127
    elif octet_one == 127:

        #return string loopback
        return "loopback"

    #else statement catch all for all other addresses
    else:

        #return string not private
        return "not private"

#define a function called os_l takes a parameter called os
def os_l(os):

    #list of os
    os_list = ["windows", 
               "linux", 
               "mac"]

    #if the os is in the list
    if os in os_list:

        #we return the os
        return os

#define a function called port_function 
def port_function():

    #create an empty list
    port_list = []

    #create a variable set it equal to 0
    port_active_counter = 0


    #create a number list 1-3
    num_list = [1,2,3]

    #for number in the number list
    for num in num_list:

        # ask for a port number and convert it to an integer
        ports = int(input(f"enter port {num}: "))

        # make the 
        #port_active_counter += 1

        #add ports to the port list
        port_list.append(ports)

    #return the port list
    return port_list

#define a function called device_check it takes a parameter called device
def device_check(device):

    #create a list containing available devices
    device_list = ["laptop","desktop","phone"]

    #if device in theh device list
    if device in device_list:

        #return the device
        return device

# define a function called submenu_ip_address it takes 4 paramaters octet_one octet_two octet_three and octet_four
def submenu_ip_address(octet_one,octet_two):

    
    #
    sub_ip_info = ip_info(octet_one,octet_two)

    if sub_ip_info == "private":
        return "A private address commonly used within local networks, such as homes, schools, and businesses."
    elif sub_ip_info == "loopback":
        return "A loopback address Refers back to the same device; commonly used for testing local services."
    else:
        return "Outside the private ranges. May be public or belong to another special-use range."

        

# define a function called sub_menu_os 
def sub_menu_os(os):

    #set sub_os_info equal to os_l(os)
    sub_os_info = os_l(os)

    #create an empty list called os_container
    os_container = []

    #os dictionary which contains info for each os
    os_dict = {
        "windows": {
                   "family":"windows NT",
                   "Primary Strength":"Broad hardware compatibility",
                   "Primary Weakness":"Most commonly targeted desktop OS",
                   "Typical Uses":"Gaming, Business, General Desktop"
        },
        "mac": {
               "family": "macOS",
               "Primary Strength": "Strong integration with Apple hardware and software",
               "Primary Weakness": "Limited hardware customization",
               "Typical Uses": "Creative Work, Development, General Desktop"
        },

        "linux": {
                "family": "Linux",
                "Primary Strength": "Highly customizable and open source",
                "Primary Weakness": "Steeper learning curve for some users",
                "Typical Uses": "Servers, Development, Cybersecurity"
        }
    }       




    #if the os is in the os_dict return the dictoinary for that os
    if os in os_dict:
        return os_dict[os] 

# define a function called port_info which takes one parameter
def port_info(selected_ports):

    #create an empty list calles to hold port information
    port_container = []

    #nested dictionaries using containing information for each indivdual port
    port_dict = {
    21: {
        "port_number": "21",
        "service": "FTP",
        "description": "Controls file transfers; file data uses a separate connection.",
        "ability": "File Swipe",
        "effect": "Steals an item.",
        "attack": "+4",
        "defense": "-2",
    },
    22: {
        "port_number": "22",
        "service": "SSH",
        "description": "Provides secure remote login and command execution.",
        "ability": "Secure Shell",
        "effect": "Raises defense.",
        "attack": "+1",
        "defense": "+6",
    },
    25: {
        "port_number": "25",
        "service": "SMTP",
        "description": "Transfers email, commonly between mail servers.",
        "ability": "Spam Barrage",
        "effect": "Fires a burst of small attacks.",
        "attack": "+6",
        "defense": "-1",
    },
    53: {
        "port_number": "53",
        "service": "DNS",
        "description": "Looks up DNS records, such as a domain's IP address.",
        "ability": "Name Reveal",
        "effect": "Identifies the enemy.",
        "attack": "+3",
        "defense": "+2",
    },
    80: {
        "port_number": "80",
        "service": "HTTP",
        "description": "Handles web requests and responses.",
        "ability": "Web Trap",
        "effect": "Slows the enemy.",
        "attack": "+4",
        "defense": "+1",
    },
    443: {
        "port_number": "443",
        "service": "HTTPS",
        "description": "Secures web communication using TLS encryption.",
        "ability": "Encrypted Armor",
        "effect": "Reduces incoming damage.",
        "attack": "+1",
        "defense": "+7",
    }
}

    #for loop for each port that is in the selected ports
    for port in selected_ports:

        # if that port is in port dictionary
        if port in port_dict:

            #add that port to the empty list we created earlier
            port_container.append(port_dict[port])

            #return the list containing our selected ports and their descriptions
    return port_container

# define attack defense function which takes one parameter
def attack_defense(selected_ports):

    #variable to store attack power
    attack = 0

    #variable to store defense power
    defense = 0

    #total_attack = 0

    #total_defense = 0

    #port_attack_defense = port_info(selected_ports)

    # for port in selected ports
    for port in selected_ports:

        # if elif statements which determine how many points to add or subtract

        if port == 21:
            attack += 4
            defense -= 2
            
        elif port == 22:
            attack += 1
            defense += 6

        elif port == 25:
            attack += 6
            defense -= 1

        elif port == 53:
            attack += 3
            defense += 2
    
        elif port == 80:
            attack += 4
            defense += 1

        elif port == 443:
            attack += 1
            defense += 7

    #return the attack and defense total
    return(f"attack: {attack}\ndefense: {defense}")


# define a function called moster_list which takes one parameter

def monster_list(private_or_public):

#private list of monsters
    private = ["ooze",
            
            "ghoul",

            "skeleton",

            #"pest",

            #"dwarf",

            #"bat",

            #"critter",

            #"beast"
            ]

    #loop back monsters
    loopback = ["mimic"]

    #public monsters
    public = ["unknown"]

    #if 
    if private_or_public == "private":
        return private
    
    elif private_or_public == "loopback":
        return loopback

    elif private_or_public == "not private":
        return public



def found():

    you_found = input("You found.......")

    if you_found == "":

        return you_found

#def port_list_page(ports):

    #port_list = port_check(ports)

    #for number, port in enumerate(port_list, start=1):
        #print (f"{number}. {port}\n")

def host(os,ip_address,octet_one,octet_two,octet_three,octet_four,device,private_or_public,selected_ports):


        ooze_frames = [
r"""
      ______
    /        \
   /  o    o  \
  /     __     \
 /______________\
""",
r"""
                 
     ________
   /  o    o  \
 /      __      \
/________________\
""",
r"""
       ____
     /      \
    / o    o \
   /    __    \
  /____________\
"""
]
        
        ghoul_frames = [
r"""
   .---.
   |O O|
   | = |
 /~|   |~\
   /   \
""",
r"""
   .---.
   |O O|
   | = |
 _/|   |\_
   /   \
""",
r"""
   .---.
   |- -|
   | = |
 /~|   |~\
   /   \
"""
]

        skeleton_frames = [
r"""
   .-----.
  /       \
 | (O) (O) |
  \   ^   /
   |=====|
   '-----'
""",
r"""
   .-----.
  /       \
 | (-) (-) |
  \   ^   /
   |=====|
   '-----'
""",
r"""
   .-----.
  /       \
 | (O) (O) |
  \   ^   /
   |T T T|
   '-----'
"""
]

        mimic_frames = [
r"""
   _________
  /________/|
 |    O    ||
 |---------||
 |_________|/
""",
r"""
   _________
  /________/|
  \ V V V V /
   |      |
  / A A A A \
 |_________|/
""",
r"""
   _________
  /________/|
  \ V V V V /
   |  U   |
  / A A A A \
 |_________|/
"""
]

        unknown_frames = [
r"""
       _.-------._
    .-'   .---.   '-.
  <      / (@) \      >
    '-.  \_____/  .-'
       '---------'
""",
r"""
                     
       ___________
  <_______________>
      /  | | |  \
                     
""",
r"""
       _.-------._
    .-'   .---.   '-.
  <      / (@) \      >
    '-.  \_____/  .-'
       '---------'
"""
]

        #set monster_name_list equal to monster_list
        monster_name_list = monster_list(private_or_public)

        #set monster_name =  to a random name in the list returned from monster_name_list
        monster_name = random.choice(monster_name_list)

        # set device_name equal to device_check
        device_name = device_check(device)

        #print a name display
        print("==================\n",device_name,monster_name,"\n""==================\n")

        #if the monster name is equivelant to one of the strings we create a variable that contains said monsters frames
        if monster_name == "ooze":
            frames = ooze_frames
        elif monster_name == "ghoul":
            frames = ghoul_frames
        elif monster_name == "skeleton":
            frames = skeleton_frames
        elif monster_name =="mimic":
            frames = mimic_frames
        elif monster_name == "unknown":
            frames = unknown_frames
            
        #for loop which repeats the animation 3 times
        for repeat in range(3):

            #for the frame number(the postition of the frame in the list of frames)
            for frame_number in [0, 1, 0, 2]:

                #we clear the screen
                terminal.system("cls")

                #print the name label
                print("==================\n",device_name,monster_name,"\n""==================\n")

                #print the the frame inside the list
                print(frames[frame_number])

                #
                time.sleep(0.3)
                    


        #we crate a variable equal to the Boolean True
        active = True

        sub_active = True

        #while active
        while active:

            terminal.system("cls")

            print("==================\n",device_name,monster_name,"\n""==================\n")

            print(frames[2])
            

            #print statements for the menu
            print("enter a number (0-3) to investigate further")
            print("enter 0 to generate a new monster")
            print("1. Operating system\n2. Ports\n3. Ip address\n0. Generate a new monster")

            #ask for input from the user
            message = input("Enter a menu option (1-3): ")

            # if the input was equivelant to 1
            if message == "1":

                #clear the terminal screen
                terminal.system("cls")

                print(frames[2])

                #print header
                print("\n=========operating system=========\n")

                #o
                os_dispay = sub_menu_os(os)

                while sub_active:
                    print (f"Family: {os_dispay["family"]}")
                    print (f"Primary Strength: {os_dispay["Primary Strength"]}")
                    print (f"Primary Weakness: {os_dispay["Primary Weakness"]}")
                    print (f"Typical Uses: {os_dispay["Typical Uses"]}")
                    submenu = input("enter 0 to go back to menu: ")

                    if submenu == "0":

                        break

            elif message == "2":

                #clear the terminal screen
                terminal.system("cls")

                print(frames[2])

                print("\n=========Ports=========\n")

                port_display = port_info(selected_ports)

                while sub_active:
                    for port in port_display:

                        print(f"port number: {port["port_number"]}\n")
                        print(f"service: {port["service"]}\n")
                        print(f"descrption: {port["description"]}\n")
                        print(f"ability: {port["ability"]}\n")
                        print(f"effect: {port["effect"]}\n------------------------\n")

                    port_attack_defense_display = attack_defense(selected_ports)

                    print(f"\n{port_attack_defense_display}")

                    submenu = input("enter 0 to go back to menu: ")

                    if submenu == "0":
                        break

            elif message == "3":

                terminal.system("cls")
                
                print(frames[2])

                ip_display = submenu_ip_address(octet_one,octet_two)

                while sub_active:

                    print(ip_address)
                    print(ip_display)

                    submenu = input("enter 0 to go back to menu: ")
                
                    if submenu == "0":
                        break

            elif message == "0":
                break

main()