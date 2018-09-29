from scapy.all import *

# 関数を作る練習をする ファイル名からファイルを開いてauthorizationタグを取り出す関数を作る

file_directory = input("PLEASE INPUT FILE DIRECTORY : ")
packets = rdpcap(file_directory)

print(packets)