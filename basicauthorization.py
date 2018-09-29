from scapy.all import *

file_directory = input("PLEASE INPUT FILE DIRECTORY : ")
packets = rdpcap(file_directory)

print(packets)