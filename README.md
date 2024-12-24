# Sliver_C2_Decrypt
##### This tool is developed from the [SliverC2-Forensics](https://github.com/Immersive-Labs-Sec/SliverC2-Forensics) tool, with some decryption features fixed to address issues encountered during the operation of the HTTP protocol.
##### The upgraded version includes several enhancements such as:  
- Modifying data extracted from pcap files (hex -> utf-8).  
- Handling data not in utf-8 format during the recording process (saving it as a binary file).  
- Automatically identifying PNG files based on magic bytes and saving them to disk.  
- Highlighting error locations or successfully decrypted positions.  
## Rules

### Sliver.yar
This yara file contains two rules, one rule to detect unpacked Sliver implants and another to detect Sliver implants in memory

### Sliver.snort
A collection of Snort rules to identify Sliver HTTP traffic. Due to the designed of the C2 it is possible these patterns will match on legitimate traffic. 


### Sliver-http.yml
A sigma rule to detect sliver HTTP traffic in event logs like Zeek or PacketBeat. 

## Pcap Parser

Given a domain name or IP address extract HTTP and DNS payloads for decryption. 

### requirements

- tshark
- pyshark

### Usage

```
> python3 sliver_pcap_parser.py -h 

usage: sliver_pcap_parser.py [-h] --pcap PCAP --filter {http,dns} [--domain_name DOMAIN_NAME]

Sliver C2 Decryptor

optional arguments:
  -h, --help            show this help message and exit
  --pcap PCAP           Path to pcap file
  --filter {http,dns}   Filter for HTTP, or DNS
  --domain_name DOMAIN_NAME
                        DNS Filter requires the C2 domain name
```

## Decrypter

### Requirements

There are a number of python libraries that are required 

- requirements.txt

### usage

```
> python3 sliver_decrypt.py -h

usage: sliver_decrypt.py [-h] [--key KEY] --transport {dns,http} --file_path FILE_PATH [--force FORCE]

Sliver C2 Decryptor

optional arguments:
  -h, --help            show this help message and exit
  --key KEY             Session Key extracted from memory as hex
  --transport {dns,http}
                        Transport Mode
  --file_path FILE_PATH
                        path to file with encoded data
  --force FORCE         Brute Force Key given a procdump file
```
