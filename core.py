# v 1.000
#
# Luiz Felipe C Salgado
# luizfelipecsalgado@gmail.com
#

import settings
import os
import threading
import dowload_video as d
import strings


def download_from_list():
    with open(os.getcwd() + settings.paths['links_youtube_file'], 'r') as f:
        wtext = f.read()
        print(strings.ll)
        print(wtext)
        print('-' * 40)
        links = wtext.split('\n')
        sucess_downloads = []
        threads = []

        for i in links:
            video, thread = d.download_video(i)
            if video is not None:
                sucess_downloads.append(video)
            if thread is not None:
                threads.append(thread)

        print(strings.fd)

        for _ in threads:
            _.join()

        print(strings.ld)
        for i in sucess_downloads:
            settings.downloaded_list.append(i['title'])
            print(strings.sd.format(
                i["title"], i["subtype"], i["resolution"]))

        save_dlist()


def save_dlist():
    with open('download_list', 'w') as f:
        str = ''
        for _ in settings.downloaded_list:
            str += _ + '\n'
        f.write(str)


def open_dlist():
    with open('download_list', 'r') as f:
        text = f.read()
        list = text.split('\n')
        settings.downloaded_list = list


def set_settings():
    with open('settings', 'r') as s:
        wtext = s.read()
        settings_list = wtext.split("\n")
        list_temp = []
        for _ in settings_list:
            list_temp.append(_.split(" "))
        sdict = {}
        for i in list_temp:
            sdict[i[0]] = i[1]
        settings.paths = sdict
        print("[V] Settings readed.")


def refresh_settings():
    with open("settings", "w") as s:
        str = ''
        for i in settings.paths:
            str += "{} {}\n".format(i, settings.paths[i])
        s.write(str)
        print("[V] Settings created.")


def check_directories():
    if os.path.isdir(os.getcwd() + settings.paths['download_folder']) is False:
        os.mkdir(os.getcwd() + settings.paths['download_folder'])
        print(strings.ddc)

    try:
        t = open(os.getcwd() + settings.paths['links_youtube_file'], 'r')
        if t.read() == '':
            print(strings.le)
            return "quit"
    except FileNotFoundError:
        with open(os.getcwd() + settings.paths['links_youtube_file'], 'w+') as f:
            print(strings.flc)
            return "quit"
