import requests
import json

url = 'https://wanandroid.com/article/list/1/json'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
try:
    result = requests.get(url=url, headers=headers).json()

    with open('result.json', 'w') as f:
        f.write(json.dumps(result, ensure_ascii=False))

except Exception as e:
    print('出现异常了', e)
