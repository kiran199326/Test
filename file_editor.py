import os
import sys
os.remove("kickass1.txt")
def line_del():
    flag = 1
    linelist1 = open("kickass1.txt", 'a+', encoding="utf-8")
    with open('kickass.txt', 'r', encoding="utf-8")as f:
        for line in f.readlines():
            if line.startswith("Download Tutorials Other Torrents - Kickass Torrents") or " << " in line:
                flag = 0
            if line.startswith("leech") or line.startswith("Kickass Torrents"):
                flag = 1
            if line and flag and not line.startswith("leech") and not line.startswith("Kickass Torrents"):
                    linelist1.write(line)
    f.close()
    linelist1.close()
line_del()
