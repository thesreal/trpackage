import zipfile
import os
import sys
import random
import shutil
import string
class FileProblemError(Exception):
    def __init__(self, message):
        super().__init__(message)
print("TR Package v1;ab") 
try:
    try:
        zipfi = input("Path to package (it's gotta be a TRP file): ")
        if os.path.exists(zipfi) and zipfi.lower().endswith(".trp"):
            print("The file exists and seems to be a TR Package file. Good start. We've just looked at the filename, though. It might be broken so I'll check.")
            tempstr = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        else:
            raise FileProblemError("You didn't input a valid path to an actual .trp file")
    except FileProblemError as ce:
        print(f"Error: {ce}")
        sys.exit(1)
    try:
        os.makedirs("/tmp/" + tempstr)
        os.makedirs("/tmp/" + tempstr + "/extzip")
        print("Temporary Directory: /tmp/" + tempstr + "/")
    except:
        print("An error occured but I dunno what it is. *shrug*")
        sys.exit(1)
    try:
        if not os.path.exists("/etc/trpack"):
            os.makedirs("/etc/trpack")
        if not os.path.exists("/etc/trpack/pklst"):
            with open("/etc/trpack/pklist", 'w'):
                pass
    except:
        print("Come on! We can't check if you have our beautiful list of installed packages and make it if it doesn't exist. Goodbye.")
        sys.exit(1)
    try:
        shutil.copy(zipfi, "/tmp/" + tempstr + "/IGNSOURCE.zip")
    except:
        print("We tried to copy your package to a place we can easily work in but we failed.")
        sys.exit(1)
    try:
        with zipfile.ZipFile("/tmp/" + tempstr + "/IGNSOURCE.zip", 'r') as zip_ref:
            zip_ref.extractall("/tmp/" + tempstr + "/extzip")
        print("Okay. We've extracted all the stuff that matters to us from your package. Thank God it's not broken (so far).")
    except:
        print("We tried to extract the package you gave us but either it's me or the package was broken after all. I told you I would check.")
        sys.exit(1)
    try:
        if os.path.isfile(file_path):
            print("Good. The CONFIG in the package exists. Now we can get some goddamn info about your package.")
            config_data = []
            with open("/tmp/" + tempstr + "/extzip/CONFIG", 'r') as config_file:
                config_data = config_file.read().splitlines()
                if len(config_files) == 11:
                    print("CONFIG has the right amount of lines")
                else:
                    raise FileProblemError("The CONFIG is broken so I can't tell what did you just give me. Goodbye and FIX YOUR PACKAGE.")
        else:
            raise FileProblemError("The CONFIG does not exist so I can't tell what did you just give me. Goodbye and FIX YOUR PACKAGE.")
    except FileProblemError as ce:
        print (f"Error: {ce}")
        sys.exit(1)
except KeyboardInterrupt:
    print("I see you wanted to end this abomination so I will obey. Goodbye.")
#try:
#        os.rmdir("/tmp/" + tempstr)
#except:
#    print("We tried to remove the temp directory but I couldn't. Try remove it yourself, here's the path: /tmp/" + tempstr + "/. Deal with it.")
#    sys.exit(1)
