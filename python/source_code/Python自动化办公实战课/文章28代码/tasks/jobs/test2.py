from tasks import app

@app.task
def run1():
    print("开始备份data2文件夹")

if __name__ == '__main__':
    tasks()
