Installieren des Raspy OS:

https://www.raspberrypi.com/software/



sudo raspi-config

- SSH einschalten
- Audio-Card wählen
- I2C einschalten
- Remote GPIO einschalten
- Root partition ausweiten
- 

Eigenheiten vom Raspberry Pi beachten:

https://docs.mopidy.com/en/latest/installation/raspberrypi/

## Install from apt.mopidy.com

1.  Add the archive’s GPG key:
```sh
sudo mkdir -p /usr/local/share/keyrings
sudo wget -q -O /usr/local/share/keyrings/mopidy-archive-keyring.gpg \
https://apt.mopidy.com/mopidy.gpg
```
    
   
2.  Add the APT repo to your package sources:
```sh
sudo wget -q -O /etc/apt/sources.list.d/mopidy.list https://apt.mopidy.com/buster.list
```
    
    
3.  Install Mopidy and all dependencies:
    
   ``sudo apt update
    ``sudo apt install mopidy


Aus Terminal lokal starten:

``mopidy

``sudo mopidyctl config




Config File ist hier:
/home/ost/.config/mopidy/mopidy.conf


Erweiterungen installieren:
```sh
sudo python3 -m pip install Mopidy-Local
# sudo python3 -m pip install Mopidy-Headless
sudo python3 -m pip install Mopidy-MPD
sudo python3 -m pip install Mopidy-Raspberry-GPIO
# sudo python3 -m pip install Mopidy-MPRIS

sudo python3 -m pip install Mopidy-Iris
sudo python3 -m pip install Mopidy-Muse
sudo python3 -m pip install Mopidy-ORFRadio

sudo python3 -m pip install mopidy-alsamixer

```


### UPNP (rygel)


```sh
sudo apt install rygel -y
sudo nano /etc/rygel.conf
# Suche nach **[MPRIS]** und editiere den Eintrag **enabled=false** zu **enabled=true**.


#/home/NUTZERNAME/.config/rygel.conf
```
Neue Config anlegen:
``nano /home/ost/.config/rygel.conf

Rygel testen:
``rygel

## Airplay  (Sharepoint)
```sh
sudo apt install autoconf
sudo apt install automake avahi-daemon build-essential git libasound2-dev libavahi-client-dev libconfig-dev libdaemon-dev libpopt-dev libssl-dev libtool xmltoman -y

# Download the Source
git clone https://github.com/mikebrady/shairport-sync.git

# Install
cd shairport-sync
autoreconf -i -f

./configure --sysconfdir=/etc --with-stdout --with-alsa --with-avahi --with-ssl=openssl --with-systemd --with-metadata

make
sudo make install

# start as a service:
sudo systemctl enable shairport-sync

# Now reboot

# Check if running:
service shareport-sync status

# Logs
# change log_verbosity to 1 or 2 in /etc/shairport-sync.conf
 sudo journalctl -n100

```

```sh
## Configuring Shairport Sync
/etc/shairport-sync.conf

```json
general =
{
  name = "Front Room";
  password = "secret";
  // ... other general settings
};
```

Test and Logs:


###  UPnP / DLNA
```sh
sudo apt install mpd -y
sudo nano /etc/mpd.conf
```
Config anpassen:
```json

audio_output {
    type            "fifo"
    name            "UPnP-DLNA"
    path            "/tmp/snapdlna"
    format          "48000:16:2"
    mixer_type      "software"
}
```
Config verlinken:
``sudo ln /etc/mpd.conf /usr/local/etc

Dienst neu starten:
``sudo service mpd restart

## 4. Mopidy konfigurieren

``sudo mopidyctl config


/etc/mopidy/mopidy.conf


### Service management with systemd

On systems using systemd you can enable the Mopidy service by running:

    sudo systemctl enable mopidy
This will make Mopidy automatically start when the system starts.

Mopidy is started, stopped, and restarted just like any other systemd service:

    sudo systemctl start mopidy
    sudo systemctl stop mopidy
    sudo systemctl restart mopidy
You can check if Mopidy is currently running as a service by running:

``sudo systemctl status mopidy
You can use journalctl to view Mopidy’s log, including important error messages:

    sudo journalctl -u mopidy


## If you run Mopidy as a system service, run:

sudo mopidyctl config

## Edit config
sudo vim /etc/mopidy/mopidy.conf 

### Test Config:
sudo mopidyctl local scan





Mopidy und Snapcast installieren:

https://hoerli.net/mopidy-snapcast-multi-room-music-setup/


## HiFiBerry Config

test:
aplay -l
aplay /usr/share/sounds/alsa/Front_Center.wav


Add User to Group Audio
```
usermod -a -G audio USERNAME
```


https://www.hifiberry.com/docs/software/configuring-linux-3-18-x/

Multi Audio Source - Not working?
https://www.hifiberry.com/docs/software/mixing-different-audio-sources/




## Radio Streams
https://www.srf.ch/hilfe/hilfe-sendetechnik/sendetechnik-live-radio-im-internet

``/var/lib/mopidy/m3u/Radio.m3u8

https://stream2.kanalk.ch/kanalk.mp3
http://stream.srg-ssr.ch/drs1/mp3_128.m3u

## Mopidy-Raspberry-GPIO
``sudo usermod -a -G gpio mopidy



Zu laut, zu Leise?

``alsamixer
dann F6 drücken


## MPD Commands

add
addid
addtagid
channels
clear
clearerror
cleartagid
close
commands
consume
count
crossfade
currentsong
decoders
delete
deleteid
disableoutput
enableoutput
find
findadd
idle
list
listall
listallinfo
listfiles
listmounts
listneighbors
listplaylist
listplaylistinfo
listplaylists
load
lsinfo
mixrampdb
mixrampdelay
mount
move
moveid
next
notcommands
outputs
password
pause
ping
play
playid
playlist
playlistadd
playlistclear
playlistdelete
playlistfind
playlistid
playlistinfo
playlistmove
playlistsearch
plchanges
plchangesposid
previous
prio
prioid
random
rangeid
readmessages
rename
repeat
replay_gain_mode
replay_gain_status
rescan
rm
save
search
searchadd
searchaddpl
seek
seekcur
seekid
sendmessage
setvol
shuffle
single
stats
status
stop
subscribe
swap
swapid
tagtypes
toggleoutput
unmount
unsubscribe
update
urlhandlers
volume

