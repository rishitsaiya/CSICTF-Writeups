## little RSA
The main idea finding the flag is getting the cipher text from RSA algorithm.

#### Step-1:
After I downloaded `a.txt` & `flag.zip`, I checked out the contents in them.

`a.txt` gave `c`, `n`, `e` as follows:

```
c=32949
n=64741
e=42667
```
`flag.zip` contains `flag.txt` which is encrypted by a pin which is key from RSA implementation.

#### Step-2:
So, I used again the [RsaCtf Tool](https://github.com/Ganapati/RsaCtfTool) and implemented by a `flag.py`:

`n` was factorized online at http://factordb.com/index.php?query=64741 to get `p` & `q`.
```python
from Crypto.Util.number import inverse
import binascii

e = 42667
c = 32949
n = 64741

# From factordb

p = 101
q = 641

phi = (p-1) * (q-1)

d = inverse(e,phi)
m = pow(c,d,n)

print (m)
```

#### Step-3:
After running above script as `python3 flag.py`, I got this output as `18429`. I used this key to unlock the zip to get access to `flag.txt`.

Voila! I got the flag!

#### Step-4:
Finally the flag becomes:
`csictf{gr34t_m1nds_th1nk_4l1ke}`