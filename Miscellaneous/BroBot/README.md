## BroBot
The main idea finding the flag is just using Bot to get the flag.

#### Step-1:
I tried `/about` to get information about the bot and got this:

```python
CTF - https://ctf.csivit.com/
Our Team - https://ctftime.org/team/77170/
Homepage - https://csivit.com/
Contribute - https://github.com/alias-rahil/speakingbot.git/
CTF Support - https://discord.com/invite/9wHPB2B/
BoT Support - @alias_rahil
```
#### Step-2:
I used `/text2voice`. I linked to the source of the bot. It writes our text as `arg` for `echo` in a bash script. Then pipes the script's output to `espeak` to get the sound.

#### Step-3:
I got this from [writeup](https://github.com/goswami-rahul/ctf/tree/master/csictf2020/brobot) to execute. 

```bash
fs = open(f"/home/ctf/{update.message.from_user.id}", "w")
    fs.write(f"echo '{text}'")
    fs.close()
    os.system(
        f"su ctf -c 'sh /home/ctf/{update.message.from_user.id} | espeak -w /home/ctf/{update.message.from_user.id}.wav --stdin'"
)
```

Then a simple `';cat flag.txt;'` gives us the answer.

#### Step-4:
Finally the flag becomes:
`csictf{ai_will_take_over_the_world}`