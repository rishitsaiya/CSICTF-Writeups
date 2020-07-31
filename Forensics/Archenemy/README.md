## Archenemy
The main idea finding the flag is using simple Steganography techniques.

#### Step-1:
After I downloaded `arched.png`, I wasn't able to open it. So I tried simple strings, binwalk commands. But no results.

#### Step-2:
So, I went for steghide tool this time.

I tried `steghide extract -sf arched.png` and with a empty passphrase and it gave me this:

```
wrote extracted data to "flag.zip".
```
#### Step-3:
So, now I had `flag.zip`, which had an image `meme.jpg`, but the zip was encrypted. So I had to use tool of that.

```
$ zipCracker/zipcracker.py -f flag.zip -w /usr/share/wordlists/rockyou.txt 
    3638 / 14344394 |   0.00% -> masones1lndg456ce

Password cracked: kathmandu

Took 2.379971 seconds to crack the password. That is, 1529 attempts per second.
```

#### Step-4:
Voila! We finally have `meme.jpg` which contains flag.

<img src="meme.jpg">

#### Step-5:
Finally the flag becomes:
`csictf{1_h0pe_y0u_don't_s33_m3_here}`