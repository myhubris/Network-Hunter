
#alright the goal for this version is to make it considerably shorter for class
#clean up the code keep it simplistic and user friendly

#some goals
#1. better ranking system scoring sytem whatever
#2. better functions
#3. port dictionary for ablities 
#4. some little animation loops
#5. make sure the program actually does something lol
import time

import os as terminal

import random

def main():

    port_active_counter = 0

    port_active = True

    global port_list

    port_list = []

    draw_title()

    draw_terminal_header()
     
    ip_address = input("Enter an ipv4 address(ex. 192.168.0.1)\n> ").strip().lower()

    octet_one,octet_two,octet_three,octet_four = ip_address.split(".")

    octet_one = int(octet_one)

    octet_two = int(octet_two)

    octet_three = int(octet_three)

    octet_four = int(octet_four)

    terminal.system("cls")

    draw_title()
    
    draw_terminal_header()
    
    os = input("\nEnter your operating system: ").strip().lower()

    terminal.system("cls")
    
    draw_title()
        
    draw_terminal_header()

    print(r"""
select from devices:
laptop
phone
desktop
""")

    device = input("\nEnter your device: ")

    terminal.system("cls")
    
    draw_title()
        
    draw_terminal_header()

    print(r"""
select from the available ports:
21
22
25
53
80
443
            
            
""")
    while port_active:

        if port_active_counter == 3:

            break
        else:
            print("choose 3 ports from the list. enter them one at a time ")

            num_list = [1,2,3]
            for num in num_list:
                ports = int(input(f"enter port {num}: "))

                port_active_counter += 1

                port_list.append(ports)


    private_or_public = ip_info(octet_one,octet_two)

    host(os,ip_address,octet_one,octet_two,octet_three,octet_four,device,private_or_public,ports)

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

def draw_terminal_header():

    print("===========================")
    
    print ("Network Hunter")
    
    print("===========================\n")


def bit_check(octet_one,octet_two,octet_three,octet_four):

    if 0 <= octet_one <= 255 and 0 <= octet_two <= 255 and 0 <= octet_three <= 255 and 0 <= octet_four <= 255:
        return True
    
    else:

        return "invalid ip"
 
def ip_info(octet_one,octet_two):

    if octet_one == 10:

        return "private"
    
    elif octet_one == 172 and 16 <= octet_two <= 31:

        return "private"
    
    elif octet_one == 192 and octet_two == 168:

        return "private"

    elif octet_one == 127:

        return "loopback"
    
    else:

        return "not private"

def os_info(os):

    os_list = ["windows", 
               "linux", 
               "mac"]

    if os in os_list:

        return os

def device_check(device):

    device_list = ["laptop","desktop","phone"]

    if device in device_list:

        return device

def submenu_ip_address(A,B,C,D):

    sub_ip_info = ip_info(A,B,C,D)

    for info,value in sub_ip_info.items():

        print (f"{info}:{value}")

def sub_menu_os(os):

    sub_os_info = os_info(os)

    os_dict = {"windows":{"family":"windows NT","Primary Strength":"Broad hardware compatibility","Primary Weakness":"Most commonly targeted desktop OS","Tyical Uses":"Gaming Business General Desktop"}}

    if sub_os_info in os_dict:

        print (f"\nOperating System: {sub_os_info}\n\nFamily: {os_list[sub_os_info]['family']}\n\nPrimary Strength: {os_list[sub_os_info]['Primary Strength']}\n\n===================\n")

def port_info():
    port_container = []

    port_dict = {
    21: {
        "service": "FTP",
        "description": "Controls file transfers; file data uses a separate connection.",
        "ability": "File Swipe",
        "effect": "Steals an item."
    },
    22: {
        "service": "SSH",
        "description": "Provides secure remote login and command execution.",
        "ability": "Secure Shell",
        "effect": "Raises defense."
    },
    25: {
        "service": "SMTP",
        "description": "Transfers email, commonly between mail servers.",
        "ability": "Spam Barrage",
        "effect": "Fires a burst of small attacks."
    },
    53: {
        "service": "DNS",
        "description": "Looks up DNS records, such as a domain's IP address.",
        "ability": "Name Reveal",
        "effect": "Identifies the enemy."
    },
    80: {
        "service": "HTTP",
        "description": "Handles web requests and responses.",
        "ability": "Web Trap",
        "effect": "Slows the enemy."
    },
    443: {
        "service": "HTTPS",
        "description": "Secures web communication using TLS encryption.",
        "ability": "Encrypted Armor",
        "effect": "Reduces incoming damage."
    }
}

    for port in port_list:
        if port in port_dict:
            port_container.append(port_dict[port])
    return port_container



def monster_list(private_or_public):

    private = ["ooze",
            
            "ghoul",

            "skeleton",

            #"pest",

            #"dwarf",

            #"bat",

            #"critter",

            #"beast"
            ]
    loopback = ["mimic"]

    public = ["unknown"]

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

def host(os,ip_address,octet_one,octet_two,octet_three,octet_four,device,private_or_public,ports):


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

        monster_name_list = monster_list(private_or_public)

        monster_name = random.choice(monster_name_list)
  
        device_name = device_check(device)

        print("==================\n",device_name,monster_name,"\n""==================\n")

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
        for repeat in range(3):
            for frame_number in [0, 1, 0, 2]:
                terminal.system("cls")
                print("==================\n",device_name,monster_name,"\n""==================\n")
                print(frames[frame_number])
                time.sleep(0.3)
                    


            #rarity_classification(A,B,C,D,os,ports)
        active = True
        while active:
            print("1. Operating system\n2. Ports\n3. Ip address\n")
            message = input("Enter a menu option (1-3): ")
            if message == "1":
                print("\n=========operating system=========\n")

                os_result = os_info(os)
            
                print (f"os:",os_result,"\n")
        
                #submenu = input("type the value of any category for detailed analysis")

                sub_active = True

                while sub_active:

                    submenu = input("press one for analysis: ")

                    if submenu == "1":
                       
                       sub_menu_os(os)

                       #submenu_ip_address(A,B,C,D)
                    elif submenu == "0":

                        break

            elif message == "2":

                print("\n=========Ports=========\n")

                port_display = port_info()
                for port in port_display:
                    print(port["service"])
                    print(port["description"])
                    print(port["ability"])
                    print(port["effect"])




                #port_list_page(ports)
                
                #port_list = port_info(ports)

                #print (port_list)
                
                #port_info(ports)

                


                #Port_ability = port_info(ports)

                #print ("\n======================\n")

            
                    #print(Port_ability)

                #elif message == "submenu":
                    #submenu = input("type the value of any category for detailed analysis")

                    #sub_active = True
                    #while sub_active:
                        #submenu = input("type the value of any category for detailed analysis")
                        #if submenu == ip_address:

                            #submenu_ip_address(A,B,C,D)

            elif message == "0":
                break

                
                


#this will be the sub menu eventually

                #submenu = input("type the value of any category for detailed analysis")

                #sub_active = True
                #while sub_active:
                    #submenu = input("type the value of any category for detailed analysis")
                    #if submenu == ip_address:

                        #print

            #individual_port(ports)
            
            #ip_result = ip_check(ip_address)

            #print(private_or_public(A,B,C,D),"\n")

            #score_ip = rarity_generator_ip(A,B,C,D)

            #score_os = rartity_generator_os(os)

            #score_port = rarity_generator_port(ports)

            #Total = score_os + score_ip + score_port

            #print("Score:",Total,"\n")

            #port_categories(ports)
            
            #Port_ability = port_info(ports)
            
            #print(Port_ability)
            
            #for words in Port_ability:
                #print(words, Port_ability[words])
            
            #monster_name_list = monster_list()

            #monster_name = random.choice(monster_name_list)

            #device_name = device_check(device)

            #print("==================\n",device_name,monster_name,"\n""==================")
            #rarity_classification(A,B,C,D,os,ports)

            
# we want to determine how rare a monster is based on info we collect


main()


# add mac address eventually
# i think i could add sub menus within the menu 

# make a menu for ports that lists each port first. Rather than filling the screen with every bit of info

#class Ports:
    #def __init__(self,ports):

        #self.port_dictionary = port_info(ports)
        #self.name = name
        #self.category = category
        #self.ability = ability
        #self.vulnerability = vulnerability

        #print(self.port_dictionary)