def main():
    ip_address = input("Enter an ip address: ")

    os = input("Enter your operating system: ")

    ports = input("Enter ports")

    
    A,B,C,D = ip_address.split(".")

    A = int(A)
    B = int(B)
    C = int(C)
    D = int(D)


    if bit_check(A,B,C,D) == True:
            
        network_type(A,B,C,D)
            
    else:
        print("Invalid Ip")
    
    #os = input("Enter your operating system: ")

    os_check(os)

    port_check(ports)
# i want bit check to tell me if every variable is true
def bit_check(A,B,C,D):
    if A >= 0 and A <= 255 and B >= 0 and B <= 255 and C >= 0 and C <= 255 and D >= 0 and D <= 255:
        return True
    else:
        return False
# function that tells us if ip is private or public
def network_type(A,B,C,D):
    if A == 192 and B == 168:
        print("Private")
    elif A == 10:
        print("Private")
#function that prints os
def os_check(os):
    if os == "windows":
        print (os)
    elif os == "linux":
        print (os)
    elif os == "mac":
        print (os)
    else:
        print("invalid os")
    # function that takes ports out of brackets and print them
def port_check(ports):
    port_list = ports.split(",")
    for number in port_list:
        number = int(number)
        print(number)

main()