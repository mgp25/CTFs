from scapy.all import *
import base64

p = rdpcap('dns.pcapng')

b64 = []
for i in range(7030):
    if not p[i].haslayer(DNS):
        continue
    if DNSQR in p[i]:
        if DNSRR in p[i] and len(p[i][DNSRR].rdata)>0: # downstream/server
            print("S[%i]: %r" % (i,p[i][DNSRR].rdata))
        else: # upstream/client
            b64.append((p[i][DNSQR].qname).decode('utf-8').replace('000.', '').replace('-.','-').replace('*','+'))


def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

b64_str = (''.join(Remove(b64))).strip('-')


file = open("b64bin", "wb")
file.write(base64.b64decode(b64_str))
file.close()
