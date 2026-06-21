def main():
    # ask for input from the user for now... eventually id like to scan computers

    ip_address = input("Enter an ip address: ")

    A,B,C,D = ip_address.split(".")
    A = int(A)
    B = int(B)
    C = int(C)
    D = int(D)


    os = input("Enter your operating system: ")

    ports = input("Enter ports")

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
            
        network_type(A,B,C,D)
            
    else:
        invalid_ip = "invalid ip"
        return invalid_ip
    
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
def network_type(A,B,C,D):
    if A == 192 and B == 168:
        private = "private"
        return private
    elif A == 10:
        private = "private"
        return private
#function that prints os
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

# the host function will generate the monster and display stats
def host(os,ports,ip_address,A,B,C,D):
    os_result = os_check(os)
    
    port_result = port_check(ports)

    print (f"os:",os_result)

    for number in port_result:
        print (f"port:" ,number)

    #ip_check(ip_address)


    ip_result = ip_check(ip_address)

    print(network_type(A,B,C,D))


#def rarity_generator():
    #if 
main()