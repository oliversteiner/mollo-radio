# Mollo Radio 2

sudo conf

http://blog.scphillips.com/posts/2013/01/sound-configuration-on-raspberry-pi-with-alsa/
https://rpi-jukebox-rfid.readthedocs.io/en/latest/coreapps.html
https://docs.mopidy.com/en/latest/api/#audio
https://github.com/mikebrady/shairport-sync
https://github.com/pimusicbox/mopidy-musicbox-webclient

### Service management with systemd

On systems using systemd you can enable the Mopidy service by running:

    sudo systemctl enable mopidy
This will make Mopidy automatically start when the system starts.

Mopidy is started, stopped, and restarted just like any other systemd service:

    sudo systemctl start mopidy
    sudo systemctl stop mopidy
    sudo systemctl restart mopidy
You can check if Mopidy is currently running as a service by running:

sudo systemctl status mopidy
You can use journalctl to view Mopidy’s log, including important error messages:

    sudo journalctl -u mopidy


## If you run Mopidy as a system service, run:

sudo mopidyctl config

## Edit config
sudo vim /etc/mopidy/mopidy.conf 

### Test Config:
sudo mopidyctl local scan

install Extensions with sudo if you are running Mopidy as Service

sudo -u mopidy pip3 install mopidy-musicbox-webclient
sudo pip3 install mopidy-musicbox-webclient
python3 -m pip install 


To Loud:

alsamixer
sudo alsactl store

/etc/shairport-sync.conf

general = {
name = "Küchen-Radio";
output_backend = "alsa";
};
alsa = {
output_device = "hw:0";
mixer_control_name = "Master";
};

sudo gpasswd -a mopidy audio

https://stream.srg-ssr.ch/drsmw/regio-ag-so_room2.aac
http://stream.srg-ssr.ch/m/drsmw/aacp_96

https://stream.srg-ssr.ch/drsmw/aacp_96.m3u
https://www.broadcast.ch/fileadmin/kundendaten/Dokumente/Internet_Streaming/2021_08_links_for_streaminginternet_radio_de_fr_it.pdf