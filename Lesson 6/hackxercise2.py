from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####


DESIRE_INDEX = 3


def show_mac_address():
    packets = rdpcap(recording_path)
    print(packets[DESIRE_INDEX - 1].src)

