#!/usr/bin/env python
# -*- coding: cp1251 -*-
import pylast
import vkontakte


API_KEY = ""
API_SECRET = ""
username = ""
password = ""
tokenVK = ""
uidVK = ""
number_appVK = ""
code_appVK = ""


def add_track(network, library, artist, sound):
    track = network.get_track(artist, sound)
    library.add_track(track)


def connection_lastfm():
    password_hash = pylast.md5(password)
    network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET, username=username, password_hash=password_hash)
    library = pylast.Library(user=username, network=network)
    return network, library


def set_info_by_number(network, library, audio, number):
    name_file_new = audio[number]["artist"] + " - " + audio[number]["title"]
    print "Get file: " + name_file_new + "\tWith number: " + str(number)
    try:
        add_track(network, library, audio[number]["artist"], audio[number]["title"])
    except:
        print "Такого трека на Last.fm не нашлось!"


def get_all_music_vk(network, library, audio):
    for i in xrange(len(audio)):
        set_info_by_number(network, library, audio, i)
    print "Действие завершено!"


def connection_vk():
    vk = vkontakte.API(number_appVK, code_appVK)
    vk = vkontakte.API(token=tokenVK)
    return vk


def main():
    network, library = connection_lastfm()
    vk = connection_vk()
    audio = vk.audio.get(uid=uidVK)
    get_all_music_vk(network, library, audio)


if __name__ == '__main__':
    main()
