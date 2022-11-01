import ipaddress
from ipaddress import IPv4Network

print("IP Address Validation Tool")


def ipValidate(ip, subnet):
    # CHECK IF IP ADDRESS IS VALID
    flag = 0
    for x in ip.split("."):
        # If the IP address is less than 0 or more than 255, it is invalid
            if int(x) < 0 or int(x) > 255:
                    print("IP address entered is invalid!")
                    flag = 1
                    break
    if flag == 0:
        print("IP address entered is valid!")
    """                
    # Check if IP is in subnet
    if (ipaddress.ip_address(ip) in ipaddress.ip_network(subnet)):
            print("IP is in subnet")
    else:
            print("IP is not in subnet")
    """

def sizeOfBlock(ip, subnet):
        # Find size of block
        count = 0
        subnet_list = subnet.split(sep = ".")
        snet = ""

        # Convert subnet mask to binary and make it a string
        for x in subnet_list:
            x = bin(int(x)).replace("0b", "")
            
            snet = snet + x

        # Count the number of 1's in the string and increment count
        for i in snet:
            if i == "1":
                count = count+1

        # Subtract the number of 1's from 32 to get the number of 0's
        print("Number of addresses in the block: ", 2**(32-count))

def FirstandLast(ip, subnet):

    #Splitting the string ip address into a list
    ip_list = ip.split(sep = ".")
    mask_list = subnet.split(sep = ".")
    first = ""
    last = ""

    for i in range(4):
        
        #First address is the ip address with the subnet mask applied
        first = first + str(int(ip_list[i]) & int(mask_list[i])) + "."

        #Last address is the ip address with the subnet mask applied and the inverse of the subnet mask applied
        last = last + str(int(ip_list[i]) | (255 - int(mask_list[i]))) + "."

    return first[:-1], last[:-1]




def main():
        # Defining variables
        """
        ip = input("Enter IP address: ")
        subnet = input("Enter subnet address with / mask: ")
        # print(ip.split("."))
        """
        ip = "167.199.170.82"
        subnet = "255.255.255.224"
        
        ipValidate(ip, subnet)
        sizeOfBlock(ip, subnet)
        
        lst = FirstandLast(ip, subnet)
        print("First IP address: ", lst[0])
        print("Last IP address: ", lst[1])

        # print(ipaddress.ip_address(ip))
        # ip.split()
        # n = IPv4Network(subnet)

        # first, last = n[0], n[-1]
        # print(first)
        # print(last)
        """
        net4 = ipaddress.ip_network(subnet)
        for x in net4.hosts():
            print(x) 
        """
        


if __name__=="__main__":
    main()