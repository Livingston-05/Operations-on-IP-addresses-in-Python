import ipaddress
from ipaddress import IPv4Network
import math


print("IP Address Validation Tool")

def ipValidate(ip):
    # CHECK IF IP ADDRESS IS VALID
    flag = 0
    ip_list = ip.split(sep = ".")
    if len(ip_list) != 4:
        print("Invalid IP address")
        flag = 1
        exit()
    else:
        for i in ip_list:
            if int(i) < 0 or int(i) > 255:
                print("Invalid IP address")
                flag = 1
                break
    if flag == 0:
        print("Valid IP address")
    else:
        exit()
   
    

def sizeOfBlock(ip, subnet):
        # Find size of block
        global count 
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
        #Mask
        print("Given mask is: ", count)
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


def subnetting():
    n=count
    subnetaddr=""
    print("Enter the number of subnets in power of 2")
    s=int(input())
    if(s%2==0):
        nsub=n+math.log(s,2)
        nsub=int(nsub)
        print("Number of bits in netid",nsub)
        for i in range(0,nsub):
            subnetaddr=subnetaddr+"1"
        for i in range(nsub,32):
            subnetaddr=subnetaddr+"0"
        
        h=32-nsub
        noOfhosts=(2**h)-2
        print("Number of hosts:",noOfhosts)

        subnetaddr=bin(int(subnetaddr,2)).replace("0b","")
        subnetmask=""
        subnetmask=str(int(subnetaddr[0:8],2))+"."+str(int(subnetaddr[8:16],2))+"."+str(int(subnetaddr[16:24],2))+"."+str(int(subnetaddr[24:32],2))
        print("Subnet mask:",subnetmask)

    else:
        print("Invalid number of subnets")
    


def main():
        # Defining variables
        ip = input("Enter IP address: ")
        ipValidate(ip)
        subnet = input("Enter subnet mask address: ")
      
        # ipValidate(ip, subnet)
        sizeOfBlock(ip, subnet)
        
        lst = FirstandLast(ip, subnet)
        print("First IP address: ", lst[0])
        print("Last IP address: ", lst[1])
        subnetting()

        
if __name__=="__main__":
    main()