from pwn import xor
flag = bytes.fromhex('52415851475749485d466e5343576c506d53534058516e425643415e5c4e')
print(xor(flag, 'csictf{'.encode()))