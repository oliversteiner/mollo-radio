import json
import mpd


def load_radio_stations():
    # add Streams to playlist
    f = open('assets/data/radio_stations.json', 'r')
    stations = json.loads(f.read())
    f.close()
    return stations


class Radio:
    def __init__(self, ip, port):
        self.radio_stations = []
        self.playing = False
        self.ip = ip
        self.port = port

        # MPD Connect
        client = mpd.MPDClient()
        client.connect(ip, port)
        self.client = client

        # Set default Vol
        self.client.setvol(10)

        # load_radio_stations()
        # self.clear_and_load_playlist()
        commands = client.commands()
        print(commands)

        status = client.status()
        vol = status.get('volume')
        print('Volume: ' + vol)
        state = status.get('state')
        if state == "play":
            self.playing = True

    def clear_and_load_playlist(self):
        # Clears the current playlist
        self.client.clear()

        # load stored playlist 'radio' in current playlist
        self.client.load('radio')

        # list of songs in current playlist
        playlist = self.client.playlist()
        # print(radio_stations)
        for station in self.radio_stations:
            print("%s" % station['name'])

    def play_song(self, station_nr):
        print("playing Station Nr %s" % station_nr)
        index = int(station_nr) - 1
        self.client.play(index)
        self.playing = True
        pass

    def play_pause(self):
        if self.playing:
            print("paused")
            self.client.pause()
            self.playing = False
        else:
            print("playing")
            self.client.play()
            self.playing = True
        return self.playing

    def stop(self):
        print("stop")
        pass

    def volume_up(self):
        print("Volume Up")
        status = self.client.status()
        vol = int(status.get('volume'))
        if vol < 99:
            new_vol = vol + 5
            self.client.setvol(new_vol)
            print('Volume: %i > %i' % (vol, new_vol))
        else:
            print('Max Volume')

        pass

    def volume_down(self):
        print("Volume Down")
        status = self.client.status()
        vol = int(status.get('volume'))
        if vol > 0:
            new_vol = vol - 5
            self.client.setvol(new_vol)
            print('Volume: %i > %i' % (vol, new_vol))
        else:
            print("Min Volume")

        pass

    def show_info(self):
        print("----- Info -----")
        for entry in self.client.lsinfo("/"):
            print("%s" % entry)
        for key, value in self.client.status().items():
            print("%s: %s" % (key, value))
        print("")
        print("----- Playlist -----")
        print(self.client.playlist)
        print("")
        print("----- Current Song -----")
        print(self.client.currentsong())
        pass
