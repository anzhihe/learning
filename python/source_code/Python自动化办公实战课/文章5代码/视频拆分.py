from subprocess import run
# 拆分文件的路径
input_video = "/Users/edz/Desktop/05/xxx.mp4"

# 10秒分为一个文件
segment_time = 10

# m3u8文件保存位置
# m3u8_list = "/Users/edz/Desktop/05/xxx.m3u8"

# ts文件保存位置
output_video = "/Users/edz/Desktop/05/video-%04d.ts"

cmd1 = ["ffmpeg", "-i", input_video, "-f", "segment", "-segment_time", str(segment_time), "-segment_format",
    "mpegts", "-segment_list", m3u8_list, "-c", "copy", "-bsf:v", "h264_mp4toannexb", "-map", "0", output_video]

run(cmd1)

# 合并
# ffmpeg -allowed_extensions ALL -protocol_whitelist "file,http,crypto,tcp,https" -i index.m3u8 -c copy out.mp4