from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####

def show_username_password():
    bind_layers(TCP, HTTP, dport=8000)
    packets = rdpcap(recording_path)
    for p in packets:
        a = p.show(dump=True)
        print(a)

    
show_username_password()
# password = 123456
# username = alice
