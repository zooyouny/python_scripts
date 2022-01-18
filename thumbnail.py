#!/usr/bin/env python
import subprocess
import sys


def _make_thumbnail(input_m3u8, output):
    out_vcodec = "h264_nvenc"
    w = 146
    h = 82
    bitrate = "500k"
    command = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel error",
        "-y",
        "-threads 0",
        f"-i {input_m3u8}",
        "-g 1",
        "-keyint_min 1",
        f"-c:v {out_vcodec}",
        "-profile:v high",
        f"-s {w}x{h}",
        f"-b:v {bitrate}",
        f"-maxrate {bitrate}",
        f"-bufsize {bitrate}",
        "-movflags +faststart",
        "-f mp4",
        f"{output}",
    ]

    command = " ".join(command)
    print(command)
    proc = subprocess.Popen(command, shell=True)
    proc.communicate()


def make_thumbnails(folder, channel_count):
    for channel in range(channel_count):
        input_m3u8 = f"{folder}/{channel + 1:03d}/1080p/media.m3u8"
        output = f"{folder}/{channel + 1:03d}/thumbnail.mp4"
        _make_thumbnail(input_m3u8, output)


if __name__ == "__main__":
    folder = sys.argv[1]
    channel_count = int(sys.argv[2])
    make_thumbnails(folder, channel_count)
