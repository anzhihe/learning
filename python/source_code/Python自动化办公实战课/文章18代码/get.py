from requests_html import HTMLSession

# URL
name = "猫"
url = f"https://unsplash.com/s/photos/{name}"

# 启动
session = HTMLSession()

# GET请求
result = session.get(url)

# 结果
print(result.status_code)
print(result.html.html)
