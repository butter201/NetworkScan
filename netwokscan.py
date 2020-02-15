import scapy.all as scapy
ipadess=input("enter ip adress without range=>")
arp_packet=scapy.ARP(pdst=ipadess)
#scapy.ls(scapy.ARP())
#scapy.ls(scapy.Ether())
combin_packet=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/arp_packet
(answer,unanswerd)=scapy.srp(combin_packet,timeout=1)
answer.summary()
