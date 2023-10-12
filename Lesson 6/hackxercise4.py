from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####

DESIRE_INDEX = 4


def show_source_destination_ip_address():
    packets = rdpcap(recording_path)
    print("source: " + packets[DESIRE_INDEX - 1][IP].src)
    print("destination: " + packets[DESIRE_INDEX - 1][IP].dst)


show_source_destination_ip_address()
