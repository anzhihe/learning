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
print(result.html.xpath('//figure[@itemprop="image"]//a[@rel="nofollow"]/@href'))

# ['https://unsplash.com/photos/NLzaiXOELFY/download?force=true', 
#  'https://unsplash.com/photos/3JyEfhb8Zgo/download?force=true', 
#  'https://unsplash.com/photos/4Y6UYds0cIo/download?force=true', 
#  ... ...
# ]