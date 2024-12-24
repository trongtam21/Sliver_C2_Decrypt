# Sliver_C2_Decrypt
##### This tool is developed from the [SliverC2-Forensics](https://github.com/Immersive-Labs-Sec/SliverC2-Forensics) tool, with some decryption features fixed to address issues encountered during the operation of the HTTP protocol.
##### The upgraded version includes several enhancements such as:  
- Modifying data extracted from pcap files (hex -> utf-8).  
- Handling data not in utf-8 format during the recording process (saving it as a binary file).  
- Automatically identifying PNG files based on magic bytes and saving them to disk.  
- Highlighting error locations or successfully decrypted positions.  
