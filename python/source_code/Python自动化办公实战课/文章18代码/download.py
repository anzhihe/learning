from requests_html import HTMLSession

# URL
url = "https://unsplash.com/photos/NLzaiXOELFY/download"

# 启动
session = HTMLSession()

# GET请求
result = session.get(url)

# 结果
print(result.status_code)

# 保存图片
with open("one.jpg", "wb") as f:
    f.write(result.content)

