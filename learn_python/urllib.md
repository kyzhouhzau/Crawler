
# urillb

# urlopen
urllib.request.urlopen(url,data=None,[timeout,]*,cafil=None,capath=None,cadefault=False,context=None)

```python
import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))
```


```python
import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post',data=data)
print(response.read())
```


```python
import urllib.request

response = urllib.request.urlopen('http://httpbin.org/get',timeout=1)
print(response.read())
```


```python
import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://httpbin/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')
```

# 响应

# 响应类型


```python
import urllib 
response = urllib.request.urlopen('http://python.org')
print(type(response))
```

# 状态码，响应头


```python
import urllib
response = urllib.request.urlopen('http://www.python.org')
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))

```


```python
import urllib
response = urllib.request.urlopen('http://www.python.org')
print(response.read().decode('utf-8'))

```

# Request


```python
import urllib.request

request = urllib.request.Request('http://www.python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))

```


```python
from urllib import request,parse

url = 'http://httpbin.org/post'
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'
,'Host': 'httpbin.org'
}
dict = {
    'name':'Germey'
}
data = bytes(parse.urlencode(dict),encoding='utf8')
req = request.Request(url=url,data=data,headers=headers,method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))


```


```python
from urllib import request,parse

url = 'http://httpbin.org/post'
dict = {
    'name':'Germey'
}
data = bytes(parse.urlencode(dict),encoding='utf8')
req = request.Request(url=url,data=data,headers=headers,method='POST')
req.add_header('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'
)
response = request.urlopen(req)
print(response.read().decode('utf-8'))
```

# Handler############################

# 代理


```python
import urllib.request

proxy_handler = urllib.request.ProxyHandler({'http':'http://127.0.0.1:9743'
})
opener = urllib.request.build_opener(proxy_handler)
response = opener.open('http://httpbin.org/get')
print(response.read())

```

# Cookie


```python
import http.cookiejar,urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+"+"+item.value)
```


```python
import http.cookiejar,urllib.request
filename = "cookie.txt"
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)


```


```python
import http.cookiejar,urllib.request

filename = "cookie2.txt"
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)

```


```python
import urllib.request,http.cookiejar
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie2.txt',ignore_discard=True,ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))

```

# 异常处理


```python
from urllib import request,error

try:
    response = request.urlopen('http://www.cuiqingcai.com/index.htm')
except error.URLError as e:
    print(e.reason)
```


```python
from urllib import request,error

try:
    response = request.urlopen('http://www.cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print("Request Successfuly")
```


```python
from urllib import request, error
import socket

try:
    response = request.urlopen('http://www.baidu.com',timeout=0.01)
except error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')
```

# URL解析

# urlparse


urllib.parse.urlparse(urlstring,scheme=",allow_fragments=True)



```python
from urllib.parse import urlparse

result = urlparse('www.baidu.com/index.html;user?id=5#comment',scheme='https')
print(result)
```


```python
from urllib.parse import urlparse

result = urlparse('www.baidu.com/index.html;user?id=5#comment',scheme='https',allow_fragments=False)
print(result)
```

# urlunparse

用于拼接

# urljoin


```python
from urllib.parse import urljoin

print(urljoin('http://www.baidu.com','https://cuiqingcai.com/FAQ.html'))


```

# urlencode


```python
from urllib.parse import urlencode

params = {
    'name':'germey',
    'age':22
}
base_url = 'http://www.baidu.com?'
url = base_url+urlencode(params)
print(url)
```


```python
import urllib.request
import urllib
import re

def get_html(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

def get_img(html):
    reg = r'src="(.*?)"'
    pattern = re.compile(reg)
    imglist = re.findall(pattern,html)
    i = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg'%i)
        i+=1
html = get_html('http://tieba.baidu.com/p/2166231880')
print(html)
print (get_img(html))

```
