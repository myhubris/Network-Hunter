# Network Hunter combines basic networking concepts with game elements.
# Users enter an IPv4 address, operating system, device type, and three ports
# to generate a monster and explore its network information and stats.


# Use time.sleep() to pause between animation frames.
import time

# Import os as terminal because os stores the user's operating system
import os as terminal

#choose a monster from the list for its IP category
import random

#main function responsible for handling the inputs and opening the monster interface
def main():

    #outer while loop
    #repeat setup when the user chooses to generate another monster
    while True:
        
        #clear the screen before displaying the next setup
        # this is useful if the player decides to generate another monster
        terminal.system("cls" if terminal.name == "nt" else "clear")

        draw_title()

        draw_terminal_header()

        print("""
Network Hunter combines networking concepts with game elements.
Enter an IPv4 address, then select an operating system, a device,
and three different ports from the provided lists.
Use the monster's menu to view network information and stats.
---------------------------------------
""")

        
        #keep asking until the address is correct
        while True:
            
            try:
            
                #Ask for an address and remove leading and trailing whitespace
                ip_address = input("Enter an ipv4 address(ex. 192.168.0.1)\nor\nEnter ? to view IP ranges\n> ").strip()

                #pulls up a reference for ip address ranges
                if ip_address == "?":
                    print("""
=========Ip ranges=========

Private:
10.0.0.0 - 10.255.255.255
172.16.0.0 - 172.31.255.255
192.168.0.0 - 192.168.255.255
---------------------------
Loopback:
127.0.0.0 - 127.255.255.255
---------------------------
Addresses outside of these ranges are labeled as "not private"
---------------------------
                        """)
                    #go back to while loop asking user for ip address
                    continue

                #split into 4 different variables.
                #the wrong number raises value error
                octet_one,octet_two,octet_three,octet_four = ip_address.split(".")

                #convert each octet into an integer
                octet_one = int(octet_one)

                octet_two = int(octet_two)

                octet_three = int(octet_three)

                octet_four = int(octet_four)

                #Raise ValueError if any octet is outside 0–255
                if not 0 <= octet_one <= 255 or not 0 <= octet_two <= 255 or not 0 <= octet_three <= 255 or not 0 <= octet_four <= 255:
                    raise ValueError

            #handle the ValueError
            except ValueError:

                
                print("\ninvalid ip address try again\n")

            #if user input is valid break out of the while loop
            else:
                break

        #clear the terminal after a successful ip attempt
        terminal.system("cls" if terminal.name == "nt" else "clear")
        draw_title()   
        draw_terminal_header()
        print("Enter the information below to discover and interact with a networking monster!\n---------------------------------------\n")
        print("""
select from operating systems:
windows
linux
mac
""")

        #ask user for an operating system name. Strip and lowercase the result    
        os = input("\nEnter your operating system: \n> ").strip().lower()

        #clear the terminal screen
        #redraw and ask for device
        terminal.system("cls" if terminal.name == "nt" else "clear") 
        draw_title()        
        draw_terminal_header()
        print("Enter the information below to discover and interact with a networking monster!\n---------------------------------------\n")
        print("""
select from devices:
laptop
phone
desktop
""")
        
        #ask user to enter a device remove whitespace and lower
        device = input("\nEnter your device: \n> ").strip().lower()

        #clear the terminal screen
        terminal.system("cls" if terminal.name == "nt" else "clear")        
        draw_title()
        draw_terminal_header()
        print("Enter the information below to discover a monster!")
        print("""
select from the available ports:
21
22
25
53
80
443                    
""")
        print("choose 3 different ports from the list. enter them one at a time. ")

        #store the list returned by collect_ports() for use in the interface
        selected_ports = collect_ports()

        ## Classify the address as private, loopback, or not private
        ip_category = ip_info(octet_one,octet_two)

        #Pass the collected inputs and ip category into the monster interface.
        monster_interface(os,ip_address,octet_one,octet_two,device,ip_category,selected_ports)

#print the programs title
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

#print the Network hunter heading
def draw_terminal_header():

    print("===========================")    
    print ("Network Hunter")
    print("===========================\n")

# classify the address based on the first two octets.. those are enough for the program to determine the type
def ip_info(octet_one,octet_two):

    #private range: 10.0.0.0 through 10.255.255.255
    if octet_one == 10:
        return "private"

    #private range: 172.16.0.0 through 172.31.255.255
    elif octet_one == 172 and 16 <= octet_two <= 31:
        return "private"

    #private range 192.168.0.0 through 192.168.255.255
    elif octet_one == 192 and octet_two == 168:
        return "private"

    #loopback range: 127.0.0.0 through 127.255.255.255
    elif octet_one == 127:
        return "loopback"

    #else statement catch all for all other addresses
    else:
        return "not private"

#collect three port numbers and return them in a list
def collect_ports():

    #create an empty list
    port_list = []

    #range(1, 4) is 1,2,3 so the prompt runs 3 times
    for num in range(1,4):

        # ask for a port number and convert it to an integer
        port_number = int(input(f"enter port {num}: "))

        #append the current number to the list
        port_list.append(port_number)

    #return all three collected port numbers in a list
    return port_list

#return an explanation for the address's IP category
def submenu_ip_address(octet_one,octet_two):

    # Use the ip classification to choose the matching explanation
    sub_ip_info = ip_info(octet_one,octet_two)
    if sub_ip_info == "private":
        return "A private address commonly used within local networks, such as homes, schools, and businesses."
    elif sub_ip_info == "loopback":
        return "A loopback address Refers back to the same device; commonly used for testing local services."
    else:
        return "Outside the private ranges. May be public or belong to another special-use range."

        

#look up the information dictionary for the selected operating system
def sub_menu_os(os):

    #Each os name maps to a dictionary containing some information.
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




    #if the os is in the os_dict return the dictionary for that os
    if os in os_dict:
        return os_dict[os] 

# information dictionaries for the ports
def port_info(selected_ports):

    #collect all of the information for the chosen ports
    port_container = []

    #port numbers map to some info
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

    #for each selected port number
    for port in selected_ports:

        # if that port is in port dictionary
        if port in port_dict:

            #append that port's info to the empty list we created earlier
            port_container.append(port_dict[port])

    #return the list after checking all selected ports
    return port_container

#calculate total attack and defense from the selected port numbers
def attack_defense(selected_ports):

    #variable to store attack power
    attack = 0

    #variable to store defense power
    defense = 0

    # for port in selected ports
    for port in selected_ports:

        # add or subtract the fixed points associated with each selected port
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

    #return the attack and defense total for the menu to display
    return(f"TOTAL ATTACK: {attack}\nTOTAL DEFENSE: {defense}")


# return the list of possible monster for the ip category
def monster_list(ip_category):

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

    # Each category uses a list so random.choice() can select a monster consistently.
    #loopback monster
    loopback = ["mimic"]

    #not private monsters
    not_private = ["unknown"]

    if ip_category == "private":
        return private
    elif ip_category == "loopback":
        return loopback
    else:
        return not_private

# choose and animate a monster, then run its information menus
def monster_interface(os,ip_address,octet_one,octet_two,device,ip_category,selected_ports):

    #Each monster has three ASCII frames stored in a list
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

    #get the possible monsters for this ip category
    monster_name_list = monster_list(ip_category)

    #select one random monster from that list
    monster_name = random.choice(monster_name_list)

    #Use the entered device as a display label.
    #device_name = device

    #select the frame list that matches the chosen monster.
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
            
    #repeat the animation sequence three times.
    for repeat in range(3):

        #play the frames in this order, using their list indexes.
        for frame_number in [0, 1, 0, 2]:
            terminal.system("cls" if terminal.name == "nt" else "clear")
            print("==================\n",device,monster_name,"\n==================\n")

            #Display the frame at the current index
            print(frames[frame_number])

            #pause for .3 seconds between each frame
            time.sleep(0.3)
                    
    #display the main menu and redisplay after returning from a submenu
    while True:
        terminal.system("cls" if terminal.name == "nt" else "clear")
        print("==================\n",device,monster_name,"\n==================\n")
        print(frames[2])
        print("-------MENU-------")
        print("1. Operating system\n2. Ports\n3. Ip address\n0. Generate a new monster")
        print("------------------")
        print("enter a number (1-3) to investigate further")
        print("or")
        print("enter 0 to generate a new monster")

        #read the menu choice
        menu_choice = input("> ").strip()

        # if the menu choice is one open the operating system information
        if menu_choice == "1":
            terminal.system("cls" if terminal.name == "nt" else "clear")
            print(frames[2])
            print("\n=========operating system=========\n")

            # get the selected os's information dictionary
            os_display = sub_menu_os(os)
            while True:
                print (f"Family: {os_display['family']}\n")
                print (f"Primary Strength: {os_display['Primary Strength']}\n")
                print (f"Primary Weakness: {os_display['Primary Weakness']}\n")
                print (f"Typical Uses: {os_display['Typical Uses']}\n------------------------")
                submenu_choice = input("enter 0 to go back to menu: ").strip()

                #Leave this submenu and return to the main menu if user enters 0
                if submenu_choice == "0":
                    break

        #open the selected ports and their monster abilities.
        elif menu_choice == "2":
            terminal.system("cls" if terminal.name == "nt" else "clear")
            print(frames[2])
            print("\n=========ports=========\n")

            #get a list containing each selected port's information dictionary
            port_display = port_info(selected_ports)

            while True:

                #print the details stored under each dictionary key.
                for port in port_display:
                    print(f"port number: {port['port_number']}\n")
                    print(f"service: {port['service']}\n")
                    print(f"description: {port['description']}\n")
                    print(f"ability: {port['ability']}\n")
                    print(f"effect: {port['effect']}\n")
                    print(f"attack: {port['attack']}\n\ndefense: {port['defense']}\n------------------------")

                #calculate the combined attack and defense from the selected ports
                port_attack_defense_display = attack_defense(selected_ports)
                print(f"{port_attack_defense_display}\n------------------------\n")
                submenu_choice = input("enter 0 to go back to menu: ").strip()

                #leave this submenu and return to the main menu if user enters 0
                if submenu_choice == "0":
                    break

        #open the original ip address and its explanation
        elif menu_choice == "3":
            terminal.system("cls" if terminal.name == "nt" else "clear")
            print(frames[2])
            print("\n=========ip address=========\n")

            #get the description for this address's category.
            ip_display = submenu_ip_address(octet_one,octet_two)

            while True:
                print(ip_category,":",ip_address,"\n")
                print(ip_display)
                print("------------------------")
                submenu_choice = input("enter 0 to go back to menu: ").strip()

                #leave this submenu and return to the main menu if user enters 0
                if submenu_choice == "0":
                    break

        #leave this interface so main starts setup for a new monster.
        elif menu_choice == "0":
            break

#start the program
main()