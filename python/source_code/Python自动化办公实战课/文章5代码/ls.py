from subprocess import run, Popen, PIPE

cmd1 = ["ls", "."]
returncode = run(cmd1)

print(returncode)
# CompletedProcess(args=['ls', '.'], returncode=0)
# returncode是“ls .”的退出状态码.
# 通常来说, 一个为 0 的退出码表示进程运行正常

# 使用Popen获取程序运行结果
with Popen(cmd1, shell=True, stdout=PIPE, stderr=PIPE, encoding="utf-8") as fs:
    fs.wait(2)
    
    # 从标准输出中读取数据,知道文件结束
    files = fs.communicate()[0]

print(files)
