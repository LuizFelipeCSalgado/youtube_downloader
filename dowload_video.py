from datetime import datetime

import strings
import settings
import threading
import pytube
import os

__months__ = {1:"jan",2:"fev",3:"mar",4:"abr",5:"mai",6:"jun",7:"jul",8:"ago",9:"set",
              10:"out",11:"nov",12:"dez"}

def download_video(yt_link):

    DOWLOAD_FOLDER = settings.paths["download_folder"] + "\\{} {} {}".format(datetime.now().year,
                                                                             __months__[datetime.now().month],
                                                                             datetime.now().day)
    if os.path.isdir(os.getcwd()+DOWLOAD_FOLDER) is False:
        os.mkdir(os.getcwd()+DOWLOAD_FOLDER)
        print(strings.ddnf.format(
            DOWLOAD_FOLDER
        ))


    # yt_link = str(input("enter the link of the video: "))
    print(strings.noq.format(yt_link))
    videos_list = pytube.YouTube(yt_link)

    print(strings.vrtd.format(videos_list.title))

    if videos_list.title in settings.downloaded_list:
        print('video already downloaded')
        return None, None

    bq = []

    for i,v in enumerate(videos_list.fmt_streams):
        print(strings.vi.format(i+1,v.subtype,v.resolution))
        if (v.subtype == 'mp4' and v.resolution == '1080p') or (v.subtype == 'mp4' and v.resolution == '720p')\
                or (v.subtype == 'mp4' and v.resolution == '360p') :
            bq.append(i+1)
            print("{} {} added.".format(v.subtype,v.resolution))


    if settings.paths['best_quality'] is False:
        option = int(input(strings.mopt))

        while option not in range(1, videos_list.fmt_streams.__len__()+1) and option != 0:
            option = int(input(strings.mopt))
        if option == 0: exit()
    else:
        if bq is not []:
            # print(bq)
            print('Best quality choice {}'.format(bq[0]))
            option = bq[0]
        else:
            print('Only bad quality of videos found... not going to download.')
            quit()

    video_download = videos_list.fmt_streams[option-1]

    def download():
        video_download.download(os.getcwd()+DOWLOAD_FOLDER)
    t = threading.Thread(target=download)
    t.start()


    print(strings.dwl)
    return {"title":videos_list.title,
            "subtype":videos_list.fmt_streams[option-1].subtype,
            "resolution":videos_list.fmt_streams[option-1].resolution}, t