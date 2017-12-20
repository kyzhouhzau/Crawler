
# Requests 

install

pip install requests

 examples


```python
import requests

response = requests.get('http://www.baidu.com')
print(type(response))
print(response.status_code)
print(response.text)
print(response.cookies)
```

 # 各种请求方式 


```python
import requests
requests.post('http://httpbin.org/post')
requests.put('http://httpbin.org/put')
requests.delete('http://httpbin.org/delete')
requests.head('http://httpbin.org/head')

```


# 请求


#  基本GET请求


```python
import requests
response = requests.get('http://www.baidu.com')
print(response.text)
```

 带参数的GET请求


```python
import requests

response = requests.get('http://httpbin.org/get?name=germey&age=22')
print(response.text)
```


```python
import requests

data = {
    'name':'germey',
    'age':22
}
response = requests.get('http://httpbin.org/get',params=data)
print(response.text)
```

解析JSON


```python
import requests
import json

response = requests.get('http://httpbin.org/get')
print(response.json())
print(json.loads(response.text))
```

获取二进制类型


```python
import requests

response = requests.get('http://seopic.699pic.com/photo/00013/4041.jpg_wh1200.jpg')

with open('祈福.jpg','wb') as f:
    f.write(response.content)
    f.close()
```

添加Headers


```python
import requests

response = requests.get('http://www.zhihu.com/explore')
print(response.text)
```


```python
import requests

headers = {
    
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'
}
response = requests.get('http://www.zhihu.com/explore',headers = headers)
print(response.text)
```

# 基本POST请求


```python
import requests

data = {'name':'germey','age':22}
headers = {
    
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'
}
response = requests.post('http://httpbin.org/post',data = data)
print(response.text)
```

# 响应

response属性


```python
import requests
response = requests.get('http://www.baidu.com')
print(type(response.status_code),response.status_code)
print(type(response.cookies),response.cookies)
print(type(response.headers),response.headers)
print(type(response.url),response.url)
print(type(response.history),response.history)
```

状态码的判断


```python
import requests

response = requests.get('http://www.jianshu.com/hello.html')
exit() 
if response.status_code == requests.codes.not_found:
    print('404 NOTFOUND')
```

高级操作

 文件上传


```python
import requests

files ={"files":open("祈福.jpg",'rb')}
response = requests.post('http://httpbin.org/post',files=files)
print(response.text)
```

 获取Cookie


```python
import requests

response = requests.get('http://www.baidu.com')
print(response.cookies)
for key,value in response.cookies.items():
    print(key + '=' + value)
```

# 会话维持

模拟登陆


```python
import requests 

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
response = s.get('http://httpbin.org/cookies')
print(response.text)

```

证书验证


```python
import requests
from requests.packages import urllib3
urllib3.disable_warnings()#消除警告信息

response = requests.get('https://www.12306.cn',verify=False)#使用verify参数可以避免网站证书不合法问题
print(response.status_code)
```


```python
import requests

response = requests.get('https://www.12306.cn',cert=('/path/server.crt','/path/key'))
#手动添加本地证书
print(response.status_code)
```

# 代理设置


```python
import requests
proxies = {
    "http":"http://127.0.0.1:51507",
    "https":"https://127.0.0.1:51507"
}

response = requests.get("http://www.baidu.com",proxies=proxies)
print(response.status_code)
```

    200
    


```python
import requests

proxies={    
    "http":"socks5://127.0.0.1:51507",
    "https":"socks5://127.0.0.1:51507"
}
response = requests.get("https://www.taobao.com",proxies=proxies)
print(response.status_code)
```

# 超时设置


```python
import requests

response = requests.get("http://www.taobao.com",timeout=1)
print(response.status_code)

```

    200
    

# 认证设置


```python
import requests
from requests.auth import HTTPBasicAuth

response = requests.get('http://www.++++++++++.com'),auth=HTTPBasicAuth('13026156724','zhou3210'))
print(response.text)
```


```python
import requests


response = requests.get('http://www.++++++++++.com'),auth=('13026156724','zhou3210'))
print(response.text)
```

# 异常处理


```python
import requests
from requests.exceptions import HTTPError,ConnectionError,ReadTimeout

try:
    response = requests.get('http://www.baidu.com',timeout=0.01)
except HTTPError:
    print('HTTPError')
except ConnectionError:
    print('ConnectionError')
except ReadTimeout:
    print('ReadTimeout')
```
