ip_address = input("Enter the IP Address")

if len(ip_address) == 11:
    ip_address += "00"
elif len(ip_address) == 12:
    ip_address += "0"
#os = input("enter the operating system")

#ports = input("enter open ports")

ip_address_change = ip_address.replace(".","")

ip_address_change = int(ip_address_change)

if ip_address_change >= 1921681100 and ip_address_change <= 1921681254:
    print("common")