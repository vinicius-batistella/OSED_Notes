import ctypes, struct
from keystone import *

# Assembly code inside
CODE = (
    " start:                             "
    "   int3                            ;"
    "   xor ecx, ecx                    ;"
    "   inc ecx                         ;"
    "   push [ecx]                      ;"
    "   ret                             ;"
)

# Initialize engine in X86-32bit mode
ks = Ks(KS_ARCH_X86, KS_MODE_32)
encoding, count = ks.asm(CODE)

scode = ""

for dec in encoding:
    scode += "\\x" + "{0:02x}".format(int(dec)).rstrip("\n")

print(scode)