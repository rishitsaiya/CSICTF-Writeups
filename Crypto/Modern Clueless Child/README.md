## MODERN CLUELESS CHILD
The main idea finding the flag is decryption using XOR keys.

#### Step-1:
After reading the given message:

```bash
I was surfing the crimson wave and oh my gosh I was totally bugging. I also tried out the lilac hair trend but it didn't work out. That's not to say you are any better, you are a snob and a half. But let's get back to the main question here- Who am I? (You don't know my name)

Ciphertext = "52f41f58f51f47f57f49f48f5df46f6ef53f43f57f6cf50f6df53f53f40f58f51f6ef42f56f43f41f5ef5cf4e" (hex) Key = "12123"
```

#### Step-2:
I quickly removed the `f` from cipher text as looked like it was used for space. So I wrote a script `sub.py` to replace `f` with `''`.

```python
ciphertext = "52f41f58f51f47f57f49f48f5df46f6ef53f43f57f6cf50f6df53f53f40f58f51f6ef42f56f43f41f5ef5cf4e"
sub = ciphertext.replace('f','')
print(sub)
```

On running `python3 sub.py` this, it gave me  `52415851475749485d466e5343576c506d53534058516e425643415e5c4e`.

#### Step-3:
I had to check if I am not missing any cipher text so I cross check the flag by XOR checks. So, I wrote this `xor1.py` script get the `csictf{` code:

```python
from pwn import xor
flag = bytes.fromhex('52415851475749485d466e5343576c506d53534058516e425643415e5c4e')
print(xor(flag, 'csictf{'.encode()))
```
Output:
```bash
b"1212312+./\r'%,\x0f#\x040'&#2\x1d+57'%?="
```

#### Step-4:
Since we got the key `1212312` means we are right path as key has cyclic property key (12123). Now it was just replacement on the key with ASCII.

`exlpoit.py` to get flag:
```python
from pwn import xor
flag = bytes.fromhex('52415851475749485d466e5343576c506d53534058516e425643415e5c4e')
print(xor(flag, '12123'.encode()))
```
On running `python3 exploit.py`, Voila! I got the flag.
```bash
b'csictf{you_are_a_basic_person}'
```

#### Step-5:
Finally the flag becomes:
`csictf{you_are_a_basic_person}`