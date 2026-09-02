# a library for my module network curses
import curses

#a module specifically for network hunter
import network_curses

#this library has a clear_screen function which clears the screen before more text is added to screen
import os

#Im ot sure if im using this right now...
#but its orignal use was to delay text printed to screen
import time

#right now this is mostly used for generating the monster name
#this could be useful for ip addresses eventually
import random

# i originally had lots of classes.
#but my understanding of how useful a class can  be is still shaky
# were going to do 2 classes for now
#port and packet

#alright we define a class called packet
class packet:
    #we add some parameters "source_ip and destination_ip"
    def __init__(self,source_ip,destination_ip):
        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.protocol = "ICMP"
        self.type = "8"
        self.status = "outbound"


#this function clears the screen
def clear_screen():

# im not entirely familiar with what this line does.
#i believe it translates roughly
# if system is windows clear screen. Not sure why that line needs all that 
# i have not deep dived into this library
    os.system("cls" if os.name == "nt" else "clear")

# my main function the meat of this program.... kind of
# it just runs everything
def main():

    #print some fancy string to the screen
    print("===========================")

    print ("Network Hunter")

    print("===========================\n")

    main_menu = input("hit enter to continue: ")

    host()

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

def device_list():

    device = ["Laptop",

              "Phone",

              "Desktop"]

    return device
#im thinking of moving most of these inputs
# I dont think they should be the first thing that runs when you open
def input_comments():
    """"""
    #the game.
    #while True:
        #try:
            #ip_address = input("Enter an ip address: ")
    
            #A,B,C,D = ip_address.split(".")
                
            #A = int(A)
                
            #B = int(B)
                
            #C = int(C)
                
            #D = int(D)
        #except Exception:
            #print("try again")
        #else:
    
            #os = input("Enter your operating system: ")
    
            #ports = input("Enter ports: ")
    
            #device = input("Enter your device: ")
    
            # im thinking this host function will need a lot less soon

    #host(os,ports,ip_address,A,B,C,D,device)
    
        #this function takes our ip address (broken into octets)
        # returns true or false
    

def host():
    
    #biome_result = biome(A,B,C,D)

    #if biome_result == "":
        #clear_screen()

        #found_text = found()
        #if found_text == "":

            #clear_screen()

    monster_name_list = monster_list()

    monster_name = random.choice(monster_name_list)

    device_name_list = device_list()
  
    device_name = random.choice(device_name_list)

    def monster_generator():
        name = device_name + " " + monster_name
        return name
    
        

            #print("==================\n",device_name,monster_name,"\n""==================\n")

            #rarity_classification(A,B,C,D,os,ports)

    mg = monster_generator()
    active = True
    while active:

        clear_screen()

        #print("==================\n",device_name,monster_name,"\n""==================\n")

        print("===========================")
        
        print ("Network Hunter")
        
        print("===========================\n")

        message = input("1. Packet Dungeon\n")

        if message == "1":

            target = input("what is the target: ")

            user = input("who is the user")

            my_target = '123'

            user_packet = packet(user,target)
            if user_packet.destination_ip == my_target:

                #my_target = Target('123')
                #if target == my_target.ip:

                curses.wrapper(network_curses.main,mg)

            else:
                print ("try again")

        elif message == "0":
            break



    def comment():
        """"""
        #if message == "1":

            #clear_screen()

            #print("==================\n",device_name,monster_name,"\n""==================\n")

                #print("\n=========operating system=========\n")

           # os_result = os_info(os)
            
            #print (f"os:",os_result,"\n")
        
                #submenu = input("type the value of any category for detailed analysis")

            #sub_active = True

            #while sub_active:

                #submenu = input("press enter for analysis: ")

                #if submenu == "":

                    #clear_screen()

                    #print("==================\n",device_name,monster_name,"\n""==================\n")
                       
                    #print(sub_menu_os(os))

                       #submenu_ip_address(A,B,C,D)
                #elif submenu == "0":

                    #break

        #elif message == "2":

            #clear_screen()

            #print("\n=========Ports=========\n")
                
            #clear_screen()

            #print("==================\n",device_name,monster_name,"\n""==================\n")

            #my_port = port(ports)
            #my_port.port_return_name()
                #print (port_return)
                
            #sub_active_port = True
            #while sub_active_port:

                #print("==================\n",device_name,monster_name,"\n""==================\n")
                #port_e_i = port_exended_info(ports)
                #if port_e_i == False:
                    #break
                #else:

                    #port_e_i = port_exended_info(ports)
                    #clear_screen()
                    #print("==================\n",device_name,monster_name,"\n""==================\n")
                    #print (port_e_i)

        
        #if message == "1":

            #target = input("what is the target: ")

            #user = input("who is the user")


            #my_target = Target('123')

            ##user_packet = packet(user,target)
            #if user_packet.destination_ip == my_target.ip:

                #my_target = Target('123')
                #if target == my_target.ip:

             #   curses.wrapper(network_curses.main)

            #else:
             #   print ("try again")







        #elif message == "0":
         #   break



#this idea feels complex at the moment.
#somehow i need the list of ports to be accessible if user inputs 1-9 
# and then i need the port to expand its info giving all of the nested dictionary info
# essentialy
# 1.135
# user types 1 and info is shown

# im considering breaking ports down even further.

# one function contains the ports then the next shows name the last is all info. That may work


main()
