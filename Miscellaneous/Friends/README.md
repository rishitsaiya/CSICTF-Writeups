## Friends
The main idea finding the flag is just parsing the input smartly.

#### Step-1:
When we download `namo.py`, we are greeted with:

```python
import math
import sys

def fancy(x):
    a = (1/2) * x
    b = (1/2916) * ((27 * x - 155) ** 2)
    c = 4096 / 729
    d = (b - c) ** (1/2)
    e = (a - d - 155/54) ** (1/3)
    f = (a + d - 155/54) ** (1/3)
    g = e + f + 5/3
    return g

def notfancy(x):
    return x**3 - 5*x**2 + 3*x + 10

def mathStuff(x):
    if (x < 3 or x > 100):
        exit()

    y = fancy(notfancy(x))

    if isinstance(y, complex):
        y = float(y.real)

    y = round(y, 0)
    return y

print("Enter a number: ")
sys.stdout.flush()
x = round(float(input()), 0)
if x == mathStuff(x):
    print('Fail')
    sys.stdout.flush()
else:
    print(open('namo.txt').read())
    sys.stdout.flush()
```

#### Step-2:
So I tried basic numbers and it worked according to the given algorithm but however, we could try a float `nan` and then I ran it along with the remote server to enter the `else` condition at the end.

```bash
echo nan | nc chall.csivit.com 30425
```
Output:

```bash
Enter a number: 
Mitrooon
bhaiyo aur behno "Enter a number"
mann ki baat nambar

agar nambar barabar 1 hai {
	bhaiyo aur behno "s"
}

nahi toh agar nambar barabar 13 hai {
	bhaiyo aur behno "_"
}


nahi toh agar nambar barabar 15 hai {
	bhaiyo aur behno "5"
}


nahi toh agar nambar barabar 22 hai {
	bhaiyo aur behno "4"
}


nahi toh agar nambar barabar 28 hai {
	bhaiyo aur behno "k"
}


nahi toh agar nambar barabar 8 hai {
	bhaiyo aur behno "y"
}


nahi toh agar nambar barabar 17 hai {
	bhaiyo aur behno "4"
}


nahi toh agar nambar barabar 9 hai {
	bhaiyo aur behno "_"
}


nahi toh agar nambar barabar 4 hai {
	bhaiyo aur behno "t"
}


nahi toh agar nambar barabar 3 hai {
	bhaiyo aur behno "c"
}


nahi toh agar nambar barabar 20 hai {
	bhaiyo aur behno "r"
}


nahi toh agar nambar barabar 12 hai {
	bhaiyo aur behno "n"
}


nahi toh agar nambar barabar 0 hai {
	bhaiyo aur behno "c"
}


nahi toh agar nambar barabar 23 hai {
	bhaiyo aur behno "t"
}


nahi toh agar nambar barabar 27 hai {
	bhaiyo aur behno "0"
}


nahi toh agar nambar barabar 10 hai {
	bhaiyo aur behno "n"
}


nahi toh agar nambar barabar 11 hai {
	bhaiyo aur behno "4"
}


nahi toh agar nambar barabar 7 hai {
	bhaiyo aur behno "m"
}


nahi toh agar nambar barabar 25 hai {
	bhaiyo aur behno "c"
}


nahi toh agar nambar barabar 24 hai {
	bhaiyo aur behno "_"
}


nahi toh agar nambar barabar 6 hai {
	bhaiyo aur behno "{"
}


nahi toh agar nambar barabar 16 hai {
	bhaiyo aur behno "_"
}


nahi toh agar nambar barabar 18 hai {
	bhaiyo aur behno "_"
}


nahi toh agar nambar barabar 2 hai {
	bhaiyo aur behno "i"
}


nahi toh agar nambar barabar 5 hai {
	bhaiyo aur behno "f"
}


nahi toh agar nambar barabar 19 hai {
	bhaiyo aur behno "g"
}


nahi toh agar nambar barabar 14 hai {
	bhaiyo aur behno "1"
}


nahi toh agar nambar barabar 21 hai {
	bhaiyo aur behno "3"
}


nahi toh agar nambar barabar 26 hai {
	bhaiyo aur behno "0"
}


nahi toh agar nambar barabar 29 hai {
	bhaiyo aur behno "}"
}

nahi toh {
	bhaiyo aur behno ""
}

achhe din aa gaye
```

#### Step-3:
Simple substitution like 0=c, 1=s, 2=i in the context of flag like `csictf{`, would also work. Instead I got this script to get the flag.

```bash
echo nan | nc chall.csivit.com 30425 | grep -A1 'hai {' | sed 's/agar nambar barabar //' | sed 's/nahi toh //' | sed 's/ hai {$/ =/' | sed 's/^\tbhaiyo aur behno \"//' | sed 's/\"$//' | sed 's/--//' | sed ':a;N;$!ba;s/=\n/ /g' | sort -n | uniq | awk '{print $2}' | tr -d '\n'; echo ''
```
This is a 1 liner and we get the flag after this.

#### Step-5:
Finally the flag becomes:
`csictf{my_n4n_15_4_gr34t_c00k}`