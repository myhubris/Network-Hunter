# main function we ask the user for a yes or no
# we run the scanner function on said input
def main():
    scan = input("Would you like to intitiate scan?: y/n ")
    scanner(scan)

def scanner(scan): 
    # if the user types y short for yes the host variable is declared
    # and the info is printed to the screen
    if scan == "y":
        host = {"ip_address" : "192.168.1.1",
            "ports" : [443, 5228],
            "os": "Windows",
            "online": True}
        for info, value in host.items():
            if info != "ports":
                print(info, value,sep=" : ")
            
        for number in host["ports"]:
                print(number)
        # so i want to print the list which is within the dictionary
        # specifically the ports list.
        # my first guess is to run an if statement
        # if info in host == "ports"
            #for number in ports
                #print number
    if scan == "n":
        print("leave")

main()