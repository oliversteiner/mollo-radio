from getkey import getkey, keys

key = getkey()
if key == keys.UP:
    print('up')  # Handle the UP key
elif key == keys.DOWN:
    print('down') # Handle the DOWN key
elif key == 'a':
    print('a')  # Handle the `a` key
elif key == 'Y':
    print('Y')  # Handle `shift-y`
else:
    # Handle other text characters
    buffer += key
    print(buffer)
