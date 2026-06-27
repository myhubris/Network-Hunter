import random

def main():

#this main loop
# its jobs right now are as listed
#print Network Hunter title
#ask for user input for each specified category
#ipaddress
#os
#ports
#device
#at the end we pass everything to the host function.

    #[print network hunter title]
    print("===========================")

    print ("Network Hunter")

    print("===========================\n")

    #user input ip address
    #ip address is split into 4 seperate variable for each octet
    # i feel like i could do this in a seperate function
    # the only thing stopping me is host requires A,B,C,D
    # need to consider dhcp when im making these functions
    #that is to say the ip is most likely not permanent
    ip_address = input("Enter an ip address: ")

    A,B,C,D = ip_address.split(".")

    A = int(A)

    B = int(B)

    C = int(C)

    D = int(D)

    os = input("Enter your operating system: ")

    ports = input("Enter ports")

    device = input("Enter your device")

    host(os,ports,ip_address,A,B,C,D,device)

#this first function checks our split ip address and asks if each octet is in the range 0-250
#i may need to use a length function to stop addressess that do not use 4 octets
def bit_check(A,B,C,D):

    if A >= 0 and A <= 255 and B >= 0 and B <= 255 and C >= 0 and C <= 255 and D >= 0 and D <= 255:

        return True
    
    else:

        return "invalid ip"
    
#ip check only runs if bit check is true else it return an invalid ip
# we may not need this function.
# i think bit_check does this on its own
def ip_check(A,B,C,D):
    
    if bit_check(A,B,C,D) == True:

        ip_info(A,B,C,D)

    else:
        return "invalid ip"

#this function takes the user ip adress and gives information based on the address

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

#this function takes user os and gives info

def os_info(os):

    os_list = ["windows", "linux", "mac"]

    if os in os_list:

        return os

#so all this funcion does is split the ports 
#im not sure how necessary it is?.....

def port_check(ports):

    port_list = ports.split(",")

    return port_list

#there is quite a bit to add in here. More ports. More abilities. this list could be quite extensive
# the idea though is to make a list of ports for each category/affinity

def port_info(ports):
    system_port_list = ["135","137","138","139","445"]

    web_port_list = ["80","443","8080","8443"]

    remote_port_list = ["22","23","3389","5900"]

    network_services_port_list = ["53","67","68","123","1900","5353"]

    data_base_port_list = ["1433","3306","5432","27017"]

    mail_port_list = ["25","110","143","465","587","993"]

    directory_port_list = ["389","636","88"]

    device_port_list = ["515","631","9100"]

    media_port_list = ["554","1935"]

    ability_dictionary = {}

    port_result = port_check(ports)

    for number in port_result:
        #print (f"port:" ,number,"\n")
        if number in system_port_list:

            category = "SYSTEM (core infrasturucture)"

            if number == "135":

                ability_dictionary["Category"] = category

                ability_dictionary["Ability"] = "Digital Switchboard"

                return ability_dictionary
    

# this function returns the device if the user input is in the list.
# i think some more infor could be produced from this instead of just returning the device
# maybe device name can go along with it. I have seen commands which can get that.

def device_check(device):

    device_list = ["laptop","desktop","phone"]

    if device in device_list:

        return device

#i have some rarity generators that im just not sure i want to put back in yet. several different functions whihc generate rarity based on what the use has input
# i think i will keep them and call them score rather than generator

def ip_score(A,B,C,D):
# id have to got thorugh here to really understand why and if these scores are accurate.
# i think incorporating a score system is good long term but may require a significant over haul
# scores may need to be added into original info table (i.e. ip score of 5 goes into ip table)

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

#another score calculator for os. again these arent doing much but at the very least data is being returned     
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
    
# score calculator for ports. I have no idea what i intended number list to do. Ill leave it for now in case it comes to me
# alright im thinking we drop the score from ports. These need to be strictly attribute/skills moves whatever

#def port_score(ports):

    #number_list = []

    #port_list = ports.split(",")

    #score_port = 0

    #for number in port_list:

        #score_port = score_port +  5

        #if number in ["80","443","22"]:

            #score_port +=  5

        #elif number not in ["80","443","22"]:

            #score_port = score_port + 0

#this guy is chunky and cluttered as of now
# alright cleaned up a bit
# it determines bio based on the ip score.
# for now i think its the best way to generate. It only takes a little info to figure out
# but further down the line we may want to figure something else out
# i added a function called choice within the biome function
# i think it works?....

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

    

    
    
#give rarity a name (common,uncommon,etc) I took out port rarity it didnt make sense
# we will have to readjust this number of orts could be an option
# the biome could contribute

def rarity_classification(A,B,C,D,os,ports):

    score_ip = (A,B,C,D)

    score_os = (os)

    score_port = (ports)

    Total = score_os + score_ip + score_port

    if Total <= 20:

        print ("00001 common\n")

#list of monsters the game can randomly select from
# im on the fence about hardcoded select monsters
#or generating them based on desktop name
# and other variables.
# I do think getting the code to determine what device your using is cool tho

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

def found():

    you_found = input("You found.......")

    if you_found == "1":

        return you_found

#this is where most info gets printed to the screen

def host(os,ports,ip_address,A,B,C,D,device):

    biome_result = biome(A,B,C,D)

    if biome_result == "1":
        
        found_text = found()
        if found_text == "1":
            

            monster_name_list = monster_list()

            monster_name = random.choice(monster_name_list)

            device_name = device_check(device)

            print("==================\n",device_name,monster_name,"\n""==================")

            #rarity_classification(A,B,C,D,os,ports)

            os_result = os_info(os)
            
            print (f"os:",os_result,"\n")

            #individual_port(ports)
            
            #ip_result = ip_check(ip_address)

            #print(private_or_public(A,B,C,D),"\n")

            #score_ip = rarity_generator_ip(A,B,C,D)

            #score_os = rartity_generator_os(os)

            #score_port = rarity_generator_port(ports)

            #Total = score_os + score_ip + score_port

            #print("Score:",Total,"\n")

            #port_categories(ports)
            
            Port_ability = port_info(ports)
            
            #print(Port_ability)
            for words in Port_ability:
                print(words, Port_ability[words])
            
            #monster_name_list = monster_list()

            #monster_name = random.choice(monster_name_list)

            #device_name = device_check(device)

            #print("==================\n",device_name,monster_name,"\n""==================")
            #rarity_classification(A,B,C,D,os,ports)

            
# we want to determine how rare a monster is based on info we collect


main()