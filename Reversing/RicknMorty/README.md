## RickNMorty
The main idea finding the flag is reverse the functions using Ghidhra to understand the code.

#### Step-1:
After I downloaded `RickNMorty`, and decompiled it in Ghidhra, I got the **main()** as follows:
```c
undefined8 main(void)
{
  int iVar1;
  time_t tVar2;
  long lVar3;
  long local_48;
  time_t local_40;
  time_t local_38;
  time_t local_30;
  long local_28;
  long local_20;
  char *local_18;
  int local_10;
  int local_c;
  
  setbuf(stdin,(char *)0x0);
  setbuf(stdout,(char *)0x0);
  setbuf(stderr,(char *)0x0);
  tVar2 = time(&local_30);
  srand((uint)tVar2);
  time(&local_38);
  local_c = 1;
  local_10 = 0;
  while( true ) {
    iVar1 = rand();
    if (iVar1 % 3 + 4 < local_10) break;
    iVar1 = rand();
    local_20 = (long)(iVar1 % 10 + 6);
    iVar1 = rand();
    local_28 = (long)(iVar1 % 10 + 6);
    printf("%d %d\n",local_20,local_28);
    __isoc99_scanf(&DAT_0040200f,&local_48);
    lVar3 = function1(local_20);
    lVar3 = function2(lVar3 + 3);
    if (lVar3 != local_48) {
      local_c = 0;
    }
    local_10 = local_10 + 1;
  }
  time(&local_40);
  local_18 = (char *)(double)(local_40 - local_38);
  printf(local_18,"fun() took %f seconds to execute \n");
  if ((local_c != 1) || (30.00000000 < (double)local_18)) {
    printf("Nahh.");
  }
  else {
    puts("Hey, you got me!");
    system("cat flag.txt");
  }
  return 0;
}
```

#### Step-2:
A pair of random numbers is generated and passed through `function1()` & `function2()` and checked with pair of numbers with given number to get the flag.

```c
long function1(long param_1,long param_2)
{
  int local_10;
  int local_c;
  
  local_c = 0;
  local_10 = 1;
  while ((local_10 <= param_1 || (local_10 <= param_2))) {
    if ((param_1 % (long)local_10 == 0) && (param_2 % (long)local_10 == 0)) {
      local_c = local_10;
    }
    local_10 = local_10 + 1;
  }
  return (long)local_c;
}
```

```c
long function2(long param_1)
{
  long lVar1;
  
  if (param_1 == 0) {
    lVar1 = 1;
  }
  else {
    lVar1 = function2(param_1 + -1);
    lVar1 = lVar1 * param_1;
  }
  return lVar1;
}
```

#### Step-3:
So, I wrote this `exploit.py` to get the flag:

```python
from pwn import *

context.log_level='DEBUG'
p = remote('chall.csivit.com', 30827) #Remote netcat

def fun1(param_1, param_2):
    local_c = 0
    local_10 = 1
    while (local_10 <= param_1) or (local_10 <= param_2):
        if (param_1 % local_10 == 0) and (param_2 % local_10 == 0):
            local_c = local_10
        local_10 += 1
    return local_c

def fun2(param_1):
    lvar1 = 0
    if param_1 == 0:
        lvar1 = 1
    else:
        lvar1 = fun2(param_1 - 1)
        lvar1 = lvar1 * param_1
    return lvar1

while True:
    line = p.recvline()
    if not line or line.decode().startswith('fun() took'):
        break

    nums = line.decode().rstrip().split(' ')
    ans = fun1(int(nums[0]), int(nums[1]))
    ans = fun2(ans + 3)
    p.sendline(str(ans))

p.stream()
```

#### Step-4:
Running the script gave me:

```bash
[DEBUG] PLT 0x40102c puts
[DEBUG] PLT 0x401040 setbuf
[DEBUG] PLT 0x401050 system
[DEBUG] PLT 0x401060 printf
[DEBUG] PLT 0x401070 srand
[DEBUG] PLT 0x401080 time
[DEBUG] PLT 0x401090 __isoc99_scanf
[DEBUG] PLT 0x4010a0 rand
[*] 
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[+] Opening connection to chall.csivit.com on port 30827: Done
[DEBUG] Received 0x6 bytes:
    b'11 15\n'
[DEBUG] Sent 0x3 bytes:
    b'24\n'
[DEBUG] Received 0x5 bytes:
    b'9 12\n'
[DEBUG] Sent 0x4 bytes:
    b'720\n'
[DEBUG] Received 0x5 bytes:
    b'7 10\n'
[DEBUG] Sent 0x3 bytes:
    b'24\n'
[DEBUG] Received 0x5 bytes:
    b'9 11\n'
[DEBUG] Sent 0x3 bytes:
    b'24\n'
[DEBUG] Received 0x5 bytes:
    b'8 10\n'
[DEBUG] Sent 0x4 bytes:
    b'120\n'
[DEBUG] Received 0x5 bytes:
    b'6 13\n'
[DEBUG] Sent 0x3 bytes:
    b'24\n'
[DEBUG] Received 0x28 bytes:
    b'fun() took 0.000000 seconds to execute \n'
[DEBUG] Received 0x11 bytes:
    b'Hey, you got me!\n'
Hey, you got me!
[DEBUG] Received 0x28 bytes:
    b'csictf{h3_7u2n3d_h1m531f_1n70_4_p1ck13}\n'
csictf{h3_7u2n3d_h1m531f_1n70_4_p1ck13}
```
Voila! We got the flag.

#### Step-5:
Finally the flag becomes: 
`csictf{h3_7u2n3d_h1m531f_1n70_4_p1ck13}`