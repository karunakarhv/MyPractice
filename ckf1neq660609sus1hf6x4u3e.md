---
title: "TCPDUMP"
datePublished: Sun Sep 13 2020 22:06:41 GMT+0000 (Coordinated Universal Time)
cuid: ckf1neq660609sus1hf6x4u3e
slug: tcpdump
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1600647099807/HhKMTkktM.jpeg

---

Filter ARP Traffic

```
tcpdump -i any arp

``` 
Filter FTP Traffic

```
tcpdump -i any port ftp

``` 

Write Packets to file
```
tcpdump -w test.pcap -i any 
```

Packet Capturing Options:
![Packet-Capturing-Options.JPG](https://cdn.hashnode.com/res/hashnode/image/upload/v1600035315403/i6YdsPX60.jpeg)

Logical Operators:
![Logical-Operators.JPG](https://cdn.hashnode.com/res/hashnode/image/upload/v1600035409729/BlH_MiLZS.jpeg)

Display Output Options:
![Display-Output-Options.JPG](https://cdn.hashnode.com/res/hashnode/image/upload/v1600035946153/6z7MXZelT.jpeg)

References:
[TCPDUMP Cheat Sheet](https://www.comparitech.com/net-admin/tcpdump-cheat-sheet/)
