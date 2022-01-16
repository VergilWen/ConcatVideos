import os
import sys
import re
parentDir = str.replace(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "\\", "/")
curDir = str.replace(os.path.dirname(__file__), "\\", "/")


def GenFileList():
    ftxtfile = open(str.format("{0}/filelist.txt", curDir), 'w')
    list_dirs = os.walk(str.format("{0}/videos", parentDir))
    for _, _, files in list_dirs:
        for f in files:
            if f.endswith(".mp4") or f.endswith(".ts"):
                fileStr = str.format("file \'{0}/videos/{1}\'\n", parentDir, f)
                ftxtfile.write(fileStr)

def ConcatVideos():
    cmd = str.format("{0}/ffmpeg.exe -y -f concat -safe 0 -i {0}/filelist.txt -vcodec h264 -c copy {1}/{2}.mp4", curDir, parentDir, GenOutputName())
    cmd = str.replace(cmd, "/", "\\")
    print(cmd)
    os.system(cmd)

def GenOutputName():
    list_dirs = os.walk(str.format("{0}/videos", parentDir))
    name = "output"
    for _, _, files in list_dirs:
        if len(files) > 1:
            fileName = files[0]
            match = re.search(".*\d{4}\d{2}\d{2}", fileName)
            if match:
                name = match.group(0)
                break;
    name = name.replace("y2mate.com - ", "")
    name = name.replace(" ", "")
    return name

GenFileList()
ConcatVideos()