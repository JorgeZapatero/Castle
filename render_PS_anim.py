from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
import os
import sys


def overwrite_PS_def(file_path, symbol, val):
    fh, abs_path = mkstemp()
    with fdopen(fh, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                if symbol in line:
                    new_file.write(symbol + " " + str(val) + " def\n")
                else:
                    new_file.write(line);
    remove(file_path)
    move(abs_path, file_path)


in_file = sys.argv[1]

temp = 'TEMP_'+in_file;

os.system("cp "+in_file+" "+temp);

nFrames = sys.argv[2]

#set the total frames
overwrite_PS_def("./"+temp, "/nFrames", nFrames)

for cFrame in range(0, int(nFrames)):
    overwrite_PS_def("./"+temp, "/cFrame", cFrame)
    num = str(cFrame)
    while len(num) < 3:
        num = "0"+num
    os.system("gs -sDEVICE=png48 -g720x1280 -o ps_frame"+num+".png "+temp)

os.system("rm "+temp)

