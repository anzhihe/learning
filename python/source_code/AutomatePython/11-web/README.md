# web moduels
* webbrowser: 是Python自带的，打开浏览器获取指定页面。
* requests: 从因特网上下载文件和网页
* Beautiful Soup: 解析HTML，即网页编写的格式
* selenium: 启动并控制一个Web浏览器。selenium能够填写表单，并模拟鼠标在这个浏览器中点击。

# webbrowser
<pre>
import webbrowser
webbrowser.open(https://cn.bing.com/ditu/Default.aspx?q=' + address)
</pre>

# requests
`pip install requests`
<pre>
import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
try:
    res.raise_for_status()
    print(res.text[:250])
except Exception as exc:
	print('There was a problem: %s' % (exc))
</pre>

# BeautifulSoup
`pip install beautifulsoup4`
<pre>
import bs4
</pre>

# selenium
install geckodriver
https://github.com/mozilla/geckodriver
