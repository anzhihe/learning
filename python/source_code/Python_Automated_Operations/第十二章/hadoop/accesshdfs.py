import subprocess
cat = subprocess.Popen(["/usr/local/hadoop-1.2.1/bin/hadoop", "fs", "-cat", "/output/006/part-00000"], stdout=subprocess.PIPE)
for line in cat.stdout:
    print line
