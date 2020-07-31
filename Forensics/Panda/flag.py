print(''.join([chr(i) for i, j in zip(open('panda1.jpg', 'rb').read(), open('panda.jpg', 'rb').read()) if i!= j]))
