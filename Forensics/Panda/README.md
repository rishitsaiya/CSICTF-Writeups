## Panda
The main idea finding the flag is using zip2john.

#### Step-1:
After I downloaded `panda.zip`, I got 2 files in it, `panda.jpg` & `panda1.jpg`.

#### Step-2:
It was encrypted. So I used `zip2john` tool to crack the zip.

```bash
zip2john panda.zip > hash.txt
john.exe --wordlist=real_human hash.txt
```
<img src="panda.jpg">

<img src="panda1.jpg">

#### Step-3:

This simple `flag.py` python script helps us to get the flag.

```python
print(''.join([chr(i) for i, j in zip(open('panda1.jpg', 'rb').read(), open('panda.jpg', 'rb').read()) if i!= j]))
```

#### Step-4:
Finally the flag becomes:
`csictf{kung_fu_p4nd4}`