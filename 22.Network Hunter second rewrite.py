import random

class port:

    def __init__(self,ports):
        
        self.port_dictionary_name = port_dictionary_name(ports)
        self.port_dictionary = port_dictionary(ports)

    def port_return_name(self):
        for number, port in enumerate(self.port_dictionary_name, start=1):
            print(f"{number}. {port}")

    #def port_return_full(self):



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

    ip_address = input("Enter an ip address: ")

    A,B,C,D = ip_address.split(".")

    A = int(A)

    B = int(B)

    C = int(C)

    D = int(D)

    os = input("Enter your operating system: ")

    ports = input("Enter ports: ")

    device = input("Enter your device: ")

    my_port = port(ports)
    port_return = my_port.port_return_name()
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

    os_bank = {}

    os_list = ["windows", 
               "linux", 
               "mac"]

    if os in os_list:

        return os
    
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

            port_list.append(f"Port number: {port} \nport name: {port_dictionary_list[port]['name']} \ncategory: {port_dictionary_list[port]['category']} \nability: {port_dictionary_list[port]['ability']}")
    return port_list



def port_exended_info(ports):

    port_analysis = input("type a number for analysis: ")
    sub = port_dictionary(ports)
    if port_analysis == "1" and len(sub) >= 1:
        sub = port_dictionary(ports)
        print(sub[0])

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

def biome(A,B,C,D):

    def menu(choice):
        
        if choice == "1":

            return "1"
        
        elif choice == "2":

            return "2"
        
        elif choice == "3":

            return "3"
        
    if ip_score(A,B,C,D) == 5:

        print("You have entered")

        print("===============\nHome Network\n==============")

        print("Wi-fi fills the air\nCheap routers hum quietly\nDesktop beasts roam......\n")

        choice = input("type 1 to continue: ")

        return menu(choice)
    
    elif ip_score(A,B,C,D) == 10:

        print("You have entered")
        
        print("==============\nInternet Ocean\n==============")

        print("Countless packets drift through the void\nsignals echo from ever direction\nunknown hosts lurk beneath the surface.....")
        
        menu()
        
    elif ip_score(A,B,C,D) == 15:

        print("You have entered")

        print("================\nMirror Realm\n===============")

        print("Your search for a network\nleads only to yourself.....")

        menu()
        
    elif ip_score(A,B,C,D) == 20:

        print("You have entered")

        print("=============\nLost Network\n==============")

        print("The air is silent\nNo router answers\nOnly abandoned devices remain.....")

        menu()

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

    os_list = {"windows":{"family":"windows NT","Primary Strength":"Broad hardware compatibility","Primary Weakness":"Most commonly targeted desktop OS","Tyical Uses":"Gaming Business General Desktop"}}

    if sub_os_info in os_list:

        print (f"\nOperating System: {sub_os_info}\n\nFamily: {os_list[sub_os_info]['family']}\n\nPrimary Strength: {os_list[sub_os_info]['Primary Strength']}\n\n===================\n")

#found function simply adds the text you found. to the screen
# its meant to emulate pokemon a bit.
#add suspense

def found():

    you_found = input("You found.......")

    if you_found == "1":

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

    biome_result = biome(A,B,C,D)

    if biome_result == "1":
        
        found_text = found()
        if found_text == "1":

            monster_name_list = monster_list()

            monster_name = random.choice(monster_name_list)
  
            device_name = device_check(device)

            print("==================\n",device_name,monster_name,"\n""==================\n")

            #rarity_classification(A,B,C,D,os,ports)
        active = True
        while active:
            message = input("1. Operating system\n2. Ports\n3. Ip address\n")
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
                
                my_port = port(ports)
                my_port.port_return_name()
                #print (port_return)
                
                sub_active_port = True
                while sub_active_port:

                    port_exended_info(ports)


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
