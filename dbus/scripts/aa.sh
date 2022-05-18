#!/bin/bash
while true; do
    title=`dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2
    org.freedesktop.DBus.Properties.Get
    string:'org.mpris.MediaPlayer2.Player' 
    string:'Metadata'|
    egrep -A 1 "title"|
    egrep -v "title"|
    cut -b 44-|
    cut -d '"' -f 1|
    egrep -v ^$`

    artist=`dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:'org.mpris.MediaPlayer2.Player' string:'Metadata'|egrep -A 2 "artist"|egrep -v "artist"|egrep -v "array"|cut -b 27-|cut -d '"' -f 1|egrep -v ^$`
    
    album=`dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.freedesktop.DBus.Properties.Get string:'org.mpris.MediaPlayer2.Player' string:'Metadata'|egrep -A 1 "album"|egrep -v "album"|cut -b 44-|cut -d '"' -f 1|egrep -v ^$`

    vaicaralho=" $title -  $artist ♪♫  ►"
    
    echo -e $vaicaralho > currentPlaying.txt
    sleep 2;
    echo -e $vaicaralho
done