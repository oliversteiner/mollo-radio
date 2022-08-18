
client = mpd.MPDClient()
client.connect("10.0.1.99", 6610)

for entry in client.lsinfo("/"):
    print("%s" % entry)
for key, value in client.status().items():
    print("%s: %s" % (key, value))
# client.play()
# client.setvol(10)
# client.pause()
# client.play()


# content of stored playlist with name 'radio
playlist = client.listplaylist('radio')

# Clears the current playlist
client.clear()

# load stored playlist 'radio' in current playlist
client.load('radio')

# list of songs in current playlist
playlist = client.playlist()

# play song number 1 from current playlist
client.play(0)

# load info of current Song
song = client.currentsong()
song_title = (song['title'])

# list of available npm radio.py from backend
commands = client.commands()

# Volume
client.setvol()
client.volume()

