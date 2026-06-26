def main():
    # ask for input from the user for now... eventually id like to scan computers
    print("===========================")
    print ("Network Hunter")
    print("===========================\n")

    ip_address = input("Enter an ip address: ")

    A,B,C,D = ip_address.split(".")
    A = int(A)
    B = int(B)
    C = int(C)
    D = int(D)


    os = input("Enter your operating system: ")

    ports = input("Enter ports")

    device = input("Enter your device")



    host(os,ports,ip_address,A,B,C,D)

    

# this determines if ip is legitimate
def ip_check(ip_address):
    A,B,C,D = ip_address.split(".")

# variable for each octet seperated by .
    A = int(A)
    B = int(B)
    C = int(C)
    D = int(D)


    if bit_check(A,B,C,D) == True:
            
        private_or_public(A,B,C,D)
            
    else:
        return "invalid ip"
    
    #os = input("Enter your operating system: ")
    
    #os_result = os_check(os)
    
    #ort_result = port_check(ports)

    #print (os_result)

    #print (port_result)

# i want bit check to tell me if every variable is true
def bit_check(A,B,C,D):
    if A >= 0 and A <= 255 and B >= 0 and B <= 255 and C >= 0 and C <= 255 and D >= 0 and D <= 255:
        return True
    else:
        return False
# function that tells us if ip is private or public
def private_or_public(A,B,C,D):
    if A == 192 and B == 168:
        return "private"
    elif A == 10:
        return "private"
#function that prints os
# needs to be changed to include odd os

def os_check(os):
    if os == "windows":
        return os
    elif os == "linux":
        return os
    elif os == "mac":
        return os
    else:
        print("invalid os")
    # function that takes ports out of brackets and print them
def port_check(ports):
    #number_list =[]
    port_list = ports.split(",")
    #for number in port_list:
        #number = int(number)
        #print(number)
    return port_list


# device which user is scanning.
#def device_check(device):
    #if device == "laptop":
    
    #elif device == "phone":

    #elif device == "desktop":

    #elif device == "router"
# assign range of ip addresses an amount of points based on how likely you will find them
def rarity_generator_ip(A,B,C,D):
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

def rartity_generator_os(os):
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

#with this function i want to be able to go through the list of numbers and add points
def rarity_generator_port(ports):
    number_list = []
    port_list = ports.split(",")
    score_port = 0
    for number in port_list:
        #score_port = score_port +  5
        if number in ["80","443","22"]:
            score_port = score_port +  5
        elif number not in ["80","443","22"]:
            score_port = score_port + 0

            
    return score_port
    # somehow i want to iterate over each number (that is check each number) and if it is in the list of number score_plus equal 5       
def biome(A,B,C,D):
    if rarity_generator_ip(A,B,C,D) == 5:
        print("You have entered")
        print("##################\nHOME NETWORK\n##################")
        print("Wi-fi fills the air\nCheap routers hum quietly\nDesktop beasts roam......\n")
        choice = input("type 1 to continue: ")
        if choice == "1":
            return "1"
        elif choice == "2":
            return "2"
        elif choice == "3":
            return "3"
        
    elif rarity_generator_ip(A,B,C,D) == 10:
        print("You have entered")
        print("##################\nInternet Ocean\n##################")
        print("Countless packets drift through the void\nsignals echo from ever direction\nunknown hosts lurk beneath the surface.....")
        choice = input("type 1 to continue: ")
        if choice == "1":
            return "1"
        elif choice == "2":
            return "2"
        elif choice == "3":
            return "3"
        
    elif rarity_generator_ip(A,B,C,D) == 15:
        print("You have entered")
        print("##################\nMirror Realm\n##################")
        print("Your search for a network\nleads only to yourself.....")
        choice = input("type 1 to continue: ")
        if choice == "1":
            return "1"
        elif choice == "2":
            return "2"
        elif choice == "3":
            return "3"
        
    elif rarity_generator_ip(A,B,C,D) == 20:
        print("You have entered")
        print("##################\nLost Network\n##################")
        print("The air is silent\nNo router answers\nOnly abandoned devices remain.....")
        choice = input("type 1 to continue: ")
        if choice == "1":
            return "1"
        elif choice == "2":
            return "2"
        elif choice == "3":
            return "3"
    #elif rarity_generator_ip(A,B,C,D) == 
#def species():
    #if 

def rarity_classification(A,B,C,D,os,ports):
    score_ip = rarity_generator_ip(A,B,C,D)

    score_os = rartity_generator_os(os)

    score_port = rarity_generator_port(ports)

    Total = score_os + score_ip + score_port

    if Total <= 20:
        print ("00001 common\n")

# monster generator eventually itll be based on biome as well
def monster(A,B,C,D,os,ports):
    score_ip = rarity_generator_ip(A,B,C,D)

    score_os = rartity_generator_os(os)

    score_port = rarity_generator_port(ports)

    Total = score_os + score_ip + score_port

    if Total <= 15:
        print("===========================")
        print("laptop ooze")
        print("===========================\n")
    elif Total > 15 and Total <= 25:
        print("===========================")
        print("ethernet ghoul")
        print("===========================")
def found():
    you_found = input("You found.......")
    if you_found == "1":
        return you_found

#def os_determination():

#def port_traits(ports):
    #port 80 (HTTP) Hypertext transfer protocol
    #unencrypted(vulnerable to eavesdropping and interception)
    #outdated 
    #port 443 (HTTPS) Hypertext transfer protocol secure
    #routes datat through a secure, scrambled "tunnel"
    #modern, secure
    #port 22 (secure shell) 
    # securely connects to servers and issues commands over the internet
    #port 53 (DNS) Domain name system
    # translator 
    # default network port used by the Domain Name System
    # primary gateway for translating human-readable website domains
    # into machine readable ip addresses
    
# function to print ports from list and give them descriptions(abilities eventually)
# add some statement which counts the number of open ports
def individual_port(ports):
    port_result = port_check(ports)
    for number in port_result:
        print (f"port:" ,number,"\n")
        if number == "80":
            print ("HTTP")
        if number == "443":
            print ("HTTPS")

#def port_categories_v3(ports):
   ##for number in port_result:


# still working on designing a functional table for the data.... Im getting closer but apparently im mixing up data and crap.


def port_categories_v3(ports):
    system_port_list = []
    ability_dictionary = {}
    port_result = port_check(ports)
    for number in port_result:
        #print (f"port:" ,number,"\n")
        if number in system_port_list:
            category = "SYSTEM (core infrasturucture)"
        if number == "135":
            ability_dictionary["Category"] = "SYSTEM"
            ability_dictionary["Ability"] = "Digital Switchboard"
            return ability_dictionary
#def port_categories(ports):
   #port_result = port_check(ports)
    #for number in port_result:
        #print (f"port:" ,number,"\n")
        #if number == "135" or number == "137" or number == "138" or number == "139" or number == "445":
            #Im not 100% on what i will do with the categories yet
            #i do want to retun the data for sure.... Iono 
            #category = "SYSTEM (core infrastructure)"
            #if number == "135":
                #ability_135 = "Ability: Digital Switchboard"
                
                #definition = ("RPC\nRemote Procedure Call")
                
                #weakness = "Something"
                #return ability_135,definition,weakness
            
            #if number == "445":
                #print("SMB")
                #print("Server Message Block")
                #print("ability: domain communication")
                #print("Weakness: when exposed to the internet, it becomes a major attack surface for data breaches and ransomware delivery")

            #print ("HTTP")
       # if number == "443":
            #print ("HTTPS")


# the host function will generate the monster and display stats
def host(os,ports,ip_address,A,B,C,D):
    biome_result = biome(A,B,C,D)
    if biome_result == "1":
        
        found_text = found()
        if found_text == "1":
            #print("===========================")
            #print ("Network Hunter")
            #print("===========================\n")

            monster(A,B,C,D,os,ports)

            rarity_classification(A,B,C,D,os,ports)

            os_result = os_check(os)
            
            #port_result = port_check(ports)

            print (f"os:",os_result,"\n")

            #for number in port_result:
                #print (f"port:" ,number,"\n")

            individual_port(ports)
            #ip_check(ip_address)


            ip_result = ip_check(ip_address)

            print(private_or_public(A,B,C,D),"\n")

            score_ip = rarity_generator_ip(A,B,C,D)

            score_os = rartity_generator_os(os)

            score_port = rarity_generator_port(ports)

            Total = score_os + score_ip + score_port

            print("Score:",Total,"\n")

            #port_categories(ports)
            
            Port_ability = port_categories_v3(ports)
            
            #print(Port_ability)
            for words in Port_ability:
                print(words, Port_ability[words])
            
            
            #rarity_classification(A,B,C,D,os,ports)

            
# we want to determine how rare a monster is based on info we collect


main()