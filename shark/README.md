# Shortcuts
Retrieve the interface name 
```bash
$ ifconfig
$ tcpdump -D
```

Then 
```bash
$ tcpdump -s 0 -i <INTERFACE>
```

**Examples**
```bash
$ tcpdump -s 0 -i eth0 -w "file"
$ tcpdump -n -s 0 -i eth0 -w - -U port 8080 | tee port-capture-eth0-cs.pcap | tcpdump -n -r - 
$ tcpdump -n -s 0 -w - -U '( (port 443) or (port 8080) )' | tee port_cap.pcap | tcpdump -n -r -
```

Shows all the Handshake. The latter shows even the encrypted packets.
```bash
tshark -r "sample.pcap" -Y "ssl.handshake"
tshark -r "sample.pcap" -Y "ssl.handshake && tcp.port==443" -d "tcp.port==443,ssl"
tshark -r "sample.pcap" -2R "ssl"
```

Add the following to filter by PORT
```
# -Y tcp.port==443
tshark -r "sample.pcap" -Y "ssl.handshake && tcp.port==443"
```

To print out the details for each line, use the verbose mode 
```
# -V
$ tshark -r "sample.pcap" -d "tcp.port==443,ssl" -2R "ssl" -V
$ tshark -r "sample.pcap" -Y "tcp.port==443" -V
```

# Scripts 
print_ciphers.py : Parse in a PCAP file and outputs a text file, filtered by some hardcoded values related to SSL handshake
