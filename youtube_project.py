# v 1.000
#
# Luiz Felipe C Salgado
# luizfelipecsalgado@gmail.com
#

import core
import settings
import sys
from optparse import OptionParser
import strings

from io import TextIOWrapper

if __name__ == "__main__":
    print("YouTube project")
    try:
        core.set_settings()
    except:
        core.refresh_settings()

    status = core.check_directories()
    core.open_dlist()

    parser = OptionParser()

    parser.add_option("-d","--download",action='store_true',default=False,dest="download",help="Download videos from link list.")
    parser.add_option("-s","--settings",action='store_true',default=False,dest="settings",help="Show file's paths and settings.")

    options, args = parser.parse_args()
    # print(options)
    # print(args)
    # print(options.download)
    if options.download:
        core.download_from_list()
    elif settings:
        print(settings.paths)

    # if status != "quit":
    #     if sys.argv.__len__()==1:
    #         print(strings.no_command)
    #     else:
    #         if  sys.argv[1] == 'download' or sys.argv[1] == "-d": core.download_from_list()
    #         elif sys.argv[1] == '-h': print(strings.help)
    #         elif sys.argv[1] == '-s': print(settings.paths)
    #         else:
    #             print(strings.no_command)




