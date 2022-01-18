#!/usr/bin/env python
import subprocess
import sys
from pathlib import Path


def _capture(input, time):
    name = Path(input).stem
    output = f"{name}_{time}.png"
    command = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel error",        
        "-y",
        f"-ss {time}",
        f"-i {input}",
        "-vframes 1",
        "-q:v 2",
        f"{output}",
    ]

    command = " ".join(command)
    print(command)
    proc = subprocess.Popen(command, shell=True)
    proc.communicate()


def captures(folder, time, channel_count):
    for channel in range(channel_count):
        input = f"{folder}{channel + 1}.mp4"
        _capture(input, time)


if __name__ == "__main__":
    folder = sys.argv[1]
    time = int(sys.argv[2])
    channel_count = int(sys.argv[3])
    captures(folder, time, channel_count)
