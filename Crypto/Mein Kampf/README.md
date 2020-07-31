## Mein Kampf
The main idea finding the flag is knowing Enigma Machine library.

#### Step-1:
After reading the given message:

```
M4 UKW $ Gamma 2 4 $ 5 9 $ 14 3 $ 5 20 fv cd hu ik es op yl wq jm
```
Google searches gave some sense of Enigma Machine.

#### Step-2:
So, I quickly searched for such libraries in python at got it at: https://pypi.org/project/py-enigma/

#### Step-3:
So, I wrote a `exploit.py` script with help from [official documentation](https://pypi.org/project/py-enigma/).

```python
from enigma.machine import EnigmaMachine

ROTORS = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'Beta', 'Gamma']
REFLECTORS = ['B', 'C', 'B-Thin', 'C-Thin']

state = 'M4 UKW $ Gamma 2 4 $ 5 9 $ 14 3 $ 5 20 fv cd hu ik es op yl wq jm'
enc = 'zkrtwvvvnrkulxhoywoj'

rings = '4 9 3 20'
plug = 'fv cd hu ik es op yl wq jm'.upper()
pos = '2 5 14 5'
pos = ''.join(chr(int(x) - 1 + ord('A')) for x in pos.split())

for rf in REFLECTORS:
    for r2 in ROTORS:
        for r3 in ROTORS:
            for r4 in ROTORS:
                rotors = ['Gamma', r2, r3, r4]
                e = EnigmaMachine.from_key_sheet(rotors=rotors, ring_settings=rings, 
                    reflector=rf, plugboard_settings=plug)
                e.set_display(pos)
                txt = e.process_text(enc).lower()
                if 'csictf' in txt:
                    print(txt)
```

#### Step-4:
When I ran the script as `python3 exploit.py`, I got the flag:

```bash
csictfnoshitsherlock
```

#### Step-5:
Finally the flag becomes:
`csictf{no_shit_sherlock}`