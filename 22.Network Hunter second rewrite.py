import curses

import network_curses

import os

import time

import random

#class os:

    #def __init__(self,os):
        #self.os_info = os_info(os)

    #def 

#these classes will be for the most part static for now,
#eventually id like them to be automatically found

#alright so the source will eventually be the users device

class subnet:
    def __init__(self,subnet):
        self.subnet = subnet
    

class source:
    def __init__(self,source_ip):
        self.source_ip = source_ip



#the packet will be the user
# i want the user to move through a "dungeon" i.e packet route
# then the user finds the "monster" i.e the target device
#class packet:

#the target for our packet
class Target:

    def __init__(self,ip):
        self.ip = ip
        #self.name = Name
        #self.network = Network


#for now this will just have to be static 
class mac_address:

    def __init__(self,mac):
        self.mac = mac

class packet:
    def __init__(self,source_ip,destination_ip):
        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.protocol = "ICMP"
        self.type = "8"
        self.status = "outbound"


    

class port:

    port_database = {"135":{"name":"RPC",
                                       "category": "SYSTEM (core infrastructure)",
                                       "ability": "Digital Switchboard",
                                       "vulnerabilities":"internet exposure"},
                                "137":{"name":"NBNS",
                                       "category": "SYSTEM (core infrastructure)",
                                       "ability": "Name Resolution",
                                       "vulnerabilities":"info leak"},
                                "445":{"name":"SMB",
                                       "category": "SYSTEM (core infrastructure)",
                                       "ability": "Resource Sharing",
                                       "vulnerabilities":"remote execution"},}


    def __init__(self,ports):
        
        #self.port_dictionary_name = port_dictionary_name(ports)
        #self.port_dictionary = port_dictionary(ports)


        port_result = port_check(ports)
            #return port_result
        self.port_list = []
        for port in port_result:
            if port in self.port_database:
                self.port_list.append(port)
                    #port, port_info in port_dictionary_list.items():
                #self.port_list.append({port})
                #self.port_list.append(f"Port number: {port} \n\nport name: {self.port_database[port]['name']} \n\ncategory: {self.port_database[port]['category']} \n\nability: {self.port_database[port]['ability']} \n\nvulnerability: {self.port_database[port]['vulnerabilities']}\n")
                        #return port_list


    def port_return_name(self):
        for number, port in enumerate(self.port_database.keys(), start=1):
            if port in self.port_list:
                print(f"{number}. {port}")

    #def port_return_full(self):
#the plan is to shift the nested dictionary approach to classes

#supposedly itll be more organized yadayada
"""class PortPort:

    port_database = {"135":{"name":"RPC",
                                   "category": "SYSTEM (core infrastructure)",
                                   "ability": "Digital Switchboard",
                                   "vulnerabilities":"internet exposure"},
                            "137":{"name":"NBNS",
                                   "category": "SYSTEM (core infrastructure)",
                                   "ability": "Name Resolution",
                                   "vulnerabilities":"info leak"},
                            "445":{"name":"SMB",
                                   "category": "SYSTEM (core infrastructure)",
                                   "ability": "Resource Sharing",
                                   "vulnerabilities":"remote execution"},}
    
    def port_return_name(self):
            for number, port in enumerate(self.port_dictionary_name, start=1):
                print(f"{number}. {port}")"""

def clear_delay(seconds):

    time.sleep(seconds)

    

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

#this is rewrite number 2 of network hunter
# for this code id like to implement classes
# at least the beginning of classes
# i want the ports to be a class

def main():

#per usual we start by printing the title
#would love to do some better word art

# NET HUNTER could potentially be turned into word art
# like overthewire

    print("===========================")

    print ("Network Hunter")

    print("===========================\n")

#we have the inputs
    while True:
        try:
            ip_address = input("Enter an ip address: ")

            A,B,C,D = ip_address.split(".")
            
            A = int(A)
            
            B = int(B)
            
            C = int(C)
            
            D = int(D)
        except Exception:
            print("try again")
        else:

        

            #A,B,C,D = ip_address.split(".")

            #A = int(A)

            #B = int(B)

            #C = int(C)

            #D = int(D)

            os = input("Enter your operating system: ")

            ports = input("Enter ports: ")

            device = input("Enter your device: ")

            my_port = port(ports)
            port_return = my_port.port_return_name()

        #def static_target():


        # host function which pretty much runns everything
            host(os,ports,ip_address,A,B,C,D,device)

    #this function takes our ip address (broken into octets)
    # returns true or false

def bit_check(A,B,C,D):

    if A >= 0 and A <= 255 and B >= 0 and B <= 255 and C >= 0 and C <= 255 and D >= 0 and D <= 255:

        return True
    
    else:

        return False
    
#checks ports
#im still not sure if this is necessary lol
#but maybe...
#some other functions currently use it

def port_check(ports):

    port_list = ports.split(",")

    return port_list

#checks if you input an actual device then returns said device
#used for generating the monster names

def device_check(device):

    device_list = ["laptop","desktop","phone"]

    if device in device_list:

        return device

# ip info

def ip_info(A,B,C,D):

    ip_table = {}

    if A == 10:

        ip_table["Class"] = "A"

        ip_table["Type"] = "Private"

        return ip_table
    
    elif A == 172 and B >= 16 and B <= 31:

        ip_table["Class"] = "B"

        ip_table["Type"] = "Private"

        return ip_table
    
    elif A == 192 and B == 168:

        ip_table["Class"] = "C"

        ip_table["Type"] = "Private"

        return ip_table
    
    else:

        ip_table["Class"] = "Unknown"

        ip_table["Type"] = "Public"

        return ip_table   
    
    #os info

def os_info(os):

    os_list = ["windows", 
               "linux", 
               "mac"]

    if os in os_list:

        return os

def os_bank(os):
    os_dictionary = {"windows":{
            "os_name":"Microsoft Windows",
            "vendor":"Microsoft",
            "family":"Windows NT",
            "kernel":"Windows NT kernel",
            "common_devices": [
                "desktop",
                "laptop",
                "workstation",
                "server"
            ],
            "common_uses":[
                "general home computer",
                "business",
                "gaming",
                "enterprise",
            ],
            "file_systems":[
                "NTFS",
                "ReFS",
                "FAT32",
                "exFAT",
            ],
            "shells": [
                "Powershell",
                "Command Prompt",
            ],
            "Package_tools":[
                "winget",
                "Microsoft Store",
            ],
            "Strengths": [
                "broad hardware and software support",
                "Everyday consumer",
                "Large enterprise presence",
            ],
            "security_notes":[
                "easy target because of widespread",
                "Uses Microsoft Defender and Windows Firewall",
                "security can vary drastically depending on version, config, and patch level",
            ]
    
            }}
    
    
def port_dictionary_name(ports):
    port_dictionary_name_list = {"135":{"name":"RPC"},
                                 "137":{"name":"NBNS"},
                                 "445":{"name":"SMB"}}
    
    port_result = port_check(ports)
    port_list = []
    for port in port_result:
        if port in port_dictionary_name_list:
            
            port_list.append(f"{port} - {port_dictionary_name_list[port]['name']}")
    return port_list

# this function is a work in progress in may become consolidated or it may end up being seperate
# my goal is to get user input "player inputs a number for a port on the port list"
# then the port provides more complex information
# im trying to think of ways i could use the key(port) to access the values

#def port_information_submenu():


#changed title from port info to port dictionary. Im going to try to put everything in on big dictionary rather than have it all split up 
# we shall see..

def port_dictionary(ports):
    port_dictionary_list = {"135":{"name":"RPC","category": "SYSTEM (core infrastructure)","ability": "Digital Switchboard","vulnerabilities":"internet exposure"},
                        "137":{"name":"NBNS","category": "SYSTEM (core infrastructure)","ability": "Name Resolution","vulnerabilities":"info leak"},
                        "445":{"name":"SMB","category": "SYSTEM (core infrastructure)","ability": "Resource Sharing","vulnerabilities":"remote execution"},}

    port_result = port_check(ports)
    #return port_result
    port_list = []
    for port in port_result:
        if port in port_dictionary_list:
            #port, port_info in port_dictionary_list.items():

            port_list.append(f"Port number: {port} \n\nport name: {port_dictionary_list[port]['name']} \n\ncategory: {port_dictionary_list[port]['category']} \n\nability: {port_dictionary_list[port]['ability']} \n\nvulnerability: {port_dictionary_list[port]['vulnerabilities']}\n")
    return port_list



#im doing this over and over again/
#probably a way to shorten it up
# proly a for loop if i had to guess

def port_exended_info(ports):

    port_loop = True
    while port_loop:
    

        port_analysis = int(input("type a number: "))
        sub = port_dictionary(ports)
        if port_analysis >= 1:
        #for definition in sub:
            return (sub[port_analysis-1])
        else:
            return False
    
    #if port_analysis == "1" and len(sub) >= 1:
        #sub = port_dictionary(ports)
        #return(sub[0])

    #if port_analysis == "2" and len(sub) >= 2:
        #sub = port_dictionary(ports)
        #return(sub[1])

    #if port_analysis == "3" and len(sub) >= 3:
        #sub = port_dictionary(ports)
        #return(sub[2])

    #if port_analysis == "4" and len(sub) >= 4:
        #sub = port_dictionary(ports)
        #return(sub[3])


    #port_result = port_check(ports)
    
    #or port in port_result:
        #return port


#alright i created this class so i could make life easier
# but the way im using it
#pretty sure its just redundant lol
# i do have some ideas on how to make it work though so ill leave it for now

#class port:

    #def __init__(self,ports):
        
        #self.port_dictionary = port_dictionary(ports)

    #def port_return(self):
        #for number, port in enumerate(self.port_dictionary, start=1):
#            print(f"{number}. {port}")



#my_port = port(ports)
#my_port.port_return()

# id have to got thorugh here to really understand why and if these scores are accurate.
# i think incorporating a score system is good long term but may require a significant over haul
# scores may need to be added into original info table (i.e. ip score of 5 goes into ip table)
# still not sure if i like this or not, but ya know thats how life goes
# Right now we are going to leave it
# will work on it next rewrite

def ip_score(A,B,C,D):

    score = 0
    
    if A == 192 and B == 168:

        score = score + 5

        return score
       
    elif A == 10:

        score = score + 5

        return score
    
    elif A == 172 and B >= 16 and B <= 31:
        
        score = score + 5
        
        return score
    
    elif A == 127:
        
        score = score + 15
        
        return score
    
    elif A == 169 and B == 254:
        
        score = score + 20
        
        return score
    
    else:
        
        score = score + 10
        
        return score

#again another score counter

def os_score(os):

    score_os = 0

    if os == "windows":

        score_os = score_os + 5

        return score_os
    
    elif os == "mac":

        score_os = score_os + 10

        return score_os
    
    elif os == "linux":

        score_os = score_os + 15

        return score_os
    
    else:

        score_os = score_os + 20

        return score_os

#this thing is not my favorite
# its clunky right now and needs to be..... changed
# the biome should also be more readily available to user
#not just shown on screen once

#im scratching my head at the way i have this biome thing set up
# anyways we need to make this more tidy. At the moment it looks janky 
# i replace typing 1 as input to the next screen with pressing enter
# feels better looks cleaner

def biome(A,B,C,D):


    #def menu(choice):
        
        #if choice == "1":

            #return "1"
        
        #elif choice == "2":

            #return "2"
        
        #elif choice == "3":

            #return "3"
        
    if ip_score(A,B,C,D) == 5:

        print("You have entered")

        clear_screen()

        print("===============\nHome Network\n==============")

        print("Wi-fi fills the air\nCheap routers hum quietly\nDesktop beasts roam......\n")

        choice = input("press enter to continue: ")
        if choice == "":
            return choice
    
    elif ip_score(A,B,C,D) == 10:

        print("You have entered")
        
        print("==============\nInternet Ocean\n==============")

        print("Countless packets drift through the void\nsignals echo from ever direction\nunknown hosts lurk beneath the surface.....")
        
        
        
    elif ip_score(A,B,C,D) == 15:

        print("You have entered")

        print("================\nMirror Realm\n===============")

        print("Your search for a network\nleads only to yourself.....")
        
    elif ip_score(A,B,C,D) == 20:

        print("You have entered")

        print("=============\nLost Network\n==============")

        print("The air is silent\nNo router answers\nOnly abandoned devices remain.....")

#right now this thing is essentially useless
# i took away the port score function
# again it would need a massive overhaul to function
# for now im more worries about getting the menus organized

def rarity_classification(A,B,C,D,os,ports):

    score_ip = (A,B,C,D)

    score_os = (os)

    score_port = (ports)

    Total = score_os + score_ip + score_port

    if Total <= 20:

        print ("00001 common\n")

#this guy does something??? haha
#im not sure if it does anything at all right this second
# i may have been making it to just start it idk

def submenu_ip_address(A,B,C,D):

    sub_ip_info = ip_info(A,B,C,D)

    for info,value in sub_ip_info.items():

        print (f"",info,":",value)

#i dont think im calling either of these functions yet
# It feels like a game sometimes.
# a made up place in a made up world.
# what am i supposed to do about it?


def sub_menu_os(os):

    sub_os_info = os_info(os)

    os_dictionary = {"windows":{
            "os_name":"Microsoft Windows",
            "vendor":"Microsoft",
            "family":"Windows NT",
            "kernel":"Windows NT kernel",
            "common_devices": [
                "desktop",
                "laptop",
                "workstation",
                "server"
            ],
            "common_uses":[
                "general home computer",
                "business",
                "gaming",
                "enterprise",
            ],
            "file_systems":[
                "NTFS",
                "ReFS",
                "FAT32",
                "exFAT",
            ],
            "shells": [
                "Powershell",
                "Command Prompt",
            ],
            "Package_tools":[
                "winget",
                "Microsoft Store",
            ],
            "Strengths": [
                "broad hardware and software support",
                "Everyday consumer",
                "Large enterprise presence",
            ],
            "security_notes":[
                "easy target because of widespread",
                "Uses Microsoft Defender and Windows Firewall",
                "security can vary drastically depending on version, config, and patch level",
            ]
    
            }}

    if sub_os_info in os_dictionary:
        os_short = os_dictionary[sub_os_info]

        return(f"Os Name: {os_short['os_name']}\n\nVendor: {os_short['vendor']}\n")
              

#found function simply adds the text you found. to the screen
# its meant to emulate pokemon a bit.
#add suspense

def found():

    you_found = input("You found.......")

    if you_found == "":

        return you_found

# list of monsters right now it just returns these creatures regardless of biome
#will eventually make them biome specific

def monster_list():

    home = ["ooze",
            
            "ghoul",

            "skeleton",

            "pest",

            "dwarf",

            "bat",

            "critter",

            "beast"]
    
    return home

def host(os,ports,ip_address,A,B,C,D,device):
    my_device = source("192.168.0.0")
    my_target = Target('192.168.0.1')
    mac_target_address = mac_address("00:1A:2B:3C:4D:5E")
    my_subnet = subnet("255.255.255.0")

    biome_result = biome(A,B,C,D)

    if biome_result == "":
        clear_screen()

        found_text = found()
        if found_text == "":

            clear_screen()

            monster_name_list = monster_list()

            monster_name = random.choice(monster_name_list)
  
            device_name = device_check(device)

            print("==================\n",device_name,monster_name,"\n""==================\n")

            #rarity_classification(A,B,C,D,os,ports)
        active = True
        while active:

            clear_screen()

            print("==================\n",device_name,monster_name,"\n""==================\n")

            message = input("1. Operating system\n2. Ports\n3. Packet Dungeon\n4. Target\n")
            if message == "1":

                clear_screen()

                print("==================\n",device_name,monster_name,"\n""==================\n")

                #print("\n=========operating system=========\n")

                os_result = os_info(os)
            
                print (f"os:",os_result,"\n")
        
                #submenu = input("type the value of any category for detailed analysis")

                sub_active = True

                while sub_active:

                    submenu = input("press enter for analysis: ")

                    if submenu == "":

                       clear_screen()

                       print("==================\n",device_name,monster_name,"\n""==================\n")
                       
                       print(sub_menu_os(os))

                       #submenu_ip_address(A,B,C,D)
                    elif submenu == "0":

                        break

            elif message == "2":

                clear_screen()

                print("\n=========Ports=========\n")
                
                clear_screen()

                print("==================\n",device_name,monster_name,"\n""==================\n")

                my_port = port(ports)
                my_port.port_return_name()
                #print (port_return)
                
                sub_active_port = True
                while sub_active_port:

                    #print("==================\n",device_name,monster_name,"\n""==================\n")
                    port_e_i = port_exended_info(ports)
                    if port_e_i == False:
                        break
                    else:

                        #port_e_i = port_exended_info(ports)
                        clear_screen()
                        print("==================\n",device_name,monster_name,"\n""==================\n")
                        print (port_e_i)

                    #if port_e_i == False:
                        #break
            #elif message == 3:
                #pass

            #elif message == "4":
                #clear_screen()
                #print("==================\n",device_name,monster_name,"\n""==================\n")
                

                #print(input("123"))

                #my_target = Target('123')
                #print(my_target.ip)

                    
            #elif message == "5":
                #clear_screen()
                #print("==================\n",device_name,monster_name,"\n""==================\n")


                #my_device = source("192.168.0.0")
                #print(my_device.source_ip)

                ##break_message = input("type 0 to break ")
                #if break_message == "0":
                    #break

            #elif message == "6":
                
                #clear_screen()
                #print("You have entered packet dungeon")
                #select_dungeon = True
                #while select_dungeon:
                    ##print("1.ping\n")
                    #select = input("select your dungeon: ")

                    #dungeon_enter = input("hit enter to initiate ping ")
                    #if select == "1":
                        #print (my_device.source_ip)

                        #print ("target", my_target.ip)

                        #F,G,H,I = my_device.source_ip.split(".")
                        #F = int(F)
                        #G = int(G)
                        #H = int(H)
                        #I = int(I)

                        #W,X,Y,Z = my_target.ip.split(".")
                        ##W = int(W)
                        #X = int(X)
                        #Y = int(Y)
                        #Z = int(Z)
                        #print("subnet:", my_subnet.subnet)

                        #if  Y == H:
                        #    print('local network')
                        ##elif Y > H:
                        #    print("remote")
                                                
                        
                        #send_arp = input("hit enter to send arp request")
                        #if send_arp == "":
                        #    print("sending.")
                        #    clear_screen_with_delay(1.5)
                        #    print("sending..")
                        #    clear_screen_with_delay(1.5)
                        #    print("sending...")
                        #    clear_screen_with_delay(1.5)
                        #    print("sending....")

                        #mac_target = input("enter target MAC ")
                        #if mac_target == mac_target_address.mac:
                            #while True:
                        #    print (my_target.ip)
                        #    congrats = input("congrats you made it ")
                        #    if congrats == "0":
                                


                        #        break
            elif message == "3":

                target = input("what is the target: ")

                user = input("who is the user")


                my_target = Target('123')

                user_packet = packet(user,target)
                if user_packet.destination_ip == my_target.ip:

                #my_target = Target('123')
                #if target == my_target.ip:

                    curses.wrapper(network_curses.main)

                else:
                    print ("try again")







            elif message == "0":
                break



#this idea feels complex at the moment.
#somehow i need the list of ports to be accessible if user inputs 1-9 
# and then i need the port to expand its info giving all of the nested dictionary info
# essentialy
# 1.135
# user types 1 and info is shown

# im considering breaking ports down even further.

# one function contains the ports then the next shows name the last is all info. That may work


main()
