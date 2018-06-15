import core
import os
import settings
import sys
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

    if status != "quit":
        if sys.argv.__len__()==1:
            print(strings.no_command)
        else:
            if  sys.argv[1] == 'download' or sys.argv[1] == "-d": core.download_from_list()
            elif sys.argv[1] == '-h': print(strings.help)
            elif sys.argv[1] == '-s': print(settings.paths)
            else:
                print(strings.no_command)




