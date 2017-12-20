
# PyQuery

# 安装

pip install pyquery

# 初始化方法

字符串初始化


```python
html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href=\"link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href=\"link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
print(doc('ul'))

```

URL初始化


```python
from pyquery import PyQuery as pq
doc = pq(url='http://www.baidu.com')
print(doc('head'))

```

文件初始化


```python
from pyquery import PyQuery as pq
doc = pq(filename='demo.html')
print(doc('li'))
```

# 基本CSS选择器


```python
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href=\"link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href=\"link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

from pyquery import PyQuery as pq
doc = pq(html)
print(doc('#container .list li'))

```

# 查找元素

子元素


```python
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href=\"link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href=\"link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

from pyquery import PyQuery as pq
doc = pq(html)
items = doc('.list')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)

```


```python
list = items.children()
print(type(list))
print(list)
```


```python
list = items.children('.active')
print(list)
```

父元素


```python
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href=\"link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href=\"link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

from pyquery import PyQuery as pq
doc = pq(html)
items = doc('.list')
container = items.parent()
print(type(container))
print(container)

```


```python
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href=\"link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href=\"link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''


from pyquery import PyQuery as pq
doc = pq(html)
items = doc('.list')
parents = items.parents()#可以在括号里添加CSS选择标志
print(type(parents))
print(parents)

```

兄弟元素


```python
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href=\"link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href=\"link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
items = doc(.list .item-0.activate)#出现空格表示选择内部的条目，，连续无空格表示并列选择关系
print(items.siblings())#获取兄弟元素

```

# 遍历

单个元素


```python
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href=\"link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href=\"link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
item = doc('.item-0.active')
print(item)
```


```python
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href=\"link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href=\"link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
lis = doc('li').items()
print(type(lis))
for li in lis:
    print(li)
```

# 获取信息

获取属性


```python
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href=\"link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href=\"link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

from pyquery import PyQuery as pq
doc = pq(html)
a = doc('.item-1.active a')
print(a)
print(a.attr.href)
print(a.attr('href'))

```

获取文本


```python
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href=\"link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href=\"link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

from pyquery import PyQuery as pq
doc = pq(html)
a = doc('.item-0.active a')
print(a)
print(a.text())
```

    <a href="link3.html"><span class="bold">third item</span></a>
    third item
    


```python
html = '<html><head><meta charset=utf-8><title>浙大美女校花 甜美神似张子萱</title><meta http-equiv=x-dns-prefetch-control content=on>'
from pyquery import PyQuery as pq
doc = pq(html)
a = doc('title')
print(a.text())
```

    浙大美女校花 甜美神似张子萱
    

获取HTML


```python
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href=\"link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href=\"link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
a = doc('.item-0.active')
print(a.html())
```

# DOM操作

addClass、removeClass


```python
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href=\"link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href=\"link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)#初始化
li = doc('.item-1.active')#选中这一标签
print(li)

li.removeClass('active')
print(li)
li.addClass('active')
print(li)

```

attr、css


```python
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href=\"link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href=\"link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.attr('name','link')
print(li)
li.css('font-size','14px')
print(li)

```

remove挺重要


```python
html = '''
<div class="wrap">
Hello, Word!
<p> This is a paragraph.</p>
</div>
'''

from pyquery import PyQuery as pq
doc = pq(html)
a = doc('.wrap')
print(a.text())
a.find('p').remove()
print(a.text())
```

其他DOM方法

# 伪类选择器


```python
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href=\"link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href=\"link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

from pyquery import PyQuery as pq
doc = pq(html)
li = doc('li:first-child')#获取第一个标签
print(li)
li = doc('li:last-child')#获取最后一个
print(li)
li = doc('li:nth-child(2)')#获取第二个
print(li)
li = doc('li:gt(2)')#获取第二个以后的,计数从0开始
print(li)
li = doc('li:nth-child(2n)')#获取偶数的标签
print(li)
li = doc('li:contains(second)')#获取包含“second”的
print(li)
```
