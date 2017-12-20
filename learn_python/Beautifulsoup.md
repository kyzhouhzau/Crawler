
# BeautifulSoup

很多时候能代替正则表达式完成网页信息的提取

# 安装

pip install beautifulsoup4

# 基本使用方法


```python
html="""
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class=\"title\" name=\"dromouse\"><b>The Dormouse's story</b></p>
    <p class=\"story\">Once upon a time there were three little sisters; and their names were
    <a href=\"http://example.com/elsie\" class=\"sister\" id=\"link1\"><!-- Elsie --></a>,
    <a href=\"http://example.com/lacie\" class=\"sister\" id=\"link2\">Lacie</a> and
    <a href=\"http://example.com/tillie\" class=\"sister\" id=\"link3\">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class=\"story\">...</p>"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,"html")
print(soup.prettify())#格式化代码
print(soup.title.string)#选择title标签，并将里面的内容打印出来

```

# 常用标签选择器

选择元素


```python
html="""
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class=\"title\" name=\"dromouse\"><b>The Dormouse's story</b></p>
    <p class=\"story\">Once upon a time there were three little sisters; and their names were
    <a href=\"http://example.com/elsie\" class=\"sister\" id=\"link1\"><!-- Elsie --></a>,
    <a href=\"http://example.com/lacie\" class=\"sister\" id=\"link2\">Lacie</a> and
    <a href=\"http://example.com/tillie\" class=\"sister\" id=\"link3\">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class=\"story\">...</p>"""


from bs4 import BeautifulSoup

soup = BeautifulSoup(html,'lxml')
print(soup.title.string)
print(type(soup.title))
print(soup.head)
print(soup.p)#仅返回第一个找到的对象
```

 获取名称


```python
html="""
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class=\"title\" name=\"dromouse\"><b>The Dormouse's story</b></p>
    <p class=\"story\">Once upon a time there were three little sisters; and their names were
    <a href=\"http://example.com/elsie\" class=\"sister\" id=\"link1\"><!-- Elsie --></a>,
    <a href=\"http://example.com/lacie\" class=\"sister\" id=\"link2\">Lacie</a> and
    <a href=\"http://example.com/tillie\" class=\"sister\" id=\"link3\">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class=\"story\">...</p>"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.title.name)

```

获取属性


```python
html="""
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class=\"title\" name=\"dromouse\"><b>The Dormouse's story</b></p>
    <p class=\"story\">Once upon a time there were three little sisters; and their names were
    <a href=\"http://example.com/elsie\" class=\"sister\" id=\"link1\"><!-- Elsie --></a>,
    <a href=\"http://example.com/lacie\" class=\"sister\" id=\"link2\">Lacie</a> and
    <a href=\"http://example.com/tillie\" class=\"sister\" id=\"link3\">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class=\"story\">...</p>"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.p['name'])
print(soup.p.attrs['name'])

```

获取内容


```python
html="""
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class=\"title\" name=\"dromouse\"><b>The Dormouse's story</b></p>
    <p class=\"story\">Once upon a time there were three little sisters; and their names were
    <a href=\"http://example.com/elsie\" class=\"sister\" id=\"link1\"><!-- Elsie --></a>,
    <a href=\"http://example.com/lacie\" class=\"sister\" id=\"link2\">Lacie</a> and
    <a href=\"http://example.com/tillie\" class=\"sister\" id=\"link3\">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class=\"story\">...</p>"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.p.string)

```

    The Dormouse's story
    

 嵌套选择


```python
html="""
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class=\"title\" name=\"dromouse\"><b>The Dormouse's story</b></p>
    <p class=\"story\">Once upon a time there were three little sisters; and their names were
    <a href=\"http://example.com/elsie\" class=\"sister\" id=\"link1\"><!-- Elsie --></a>,
    <a href=\"http://example.com/lacie\" class=\"sister\" id=\"link2\">Lacie</a> and
    <a href=\"http://example.com/tillie\" class=\"sister\" id=\"link3\">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class=\"story\">...</p>"""


from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.head.title.string)

```

子节点和子节点


```python
html="""
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link33">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.p.contents)


```


```python
html="""
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class=\"title\" name=\"dromouse\"><b>The Dormouse's story</b></p>
    <p class=\"story\">Once upon a time there were three little sisters; and their names were
    <a href=\"http://example.com/elsie\" class=\"sister\" id=\"link1\"><!-- Elsie --></a>,
    <a href=\"http://example.com/lacie\" class=\"sister\" id=\"link2\">Lacie</a> and
    <a href=\"http://example.com/tillie\" class=\"sister\" id=\"link3\">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class=\"story\">...</p>"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.p.children)
for i,child in enumerate(soup.p.children):
    print(i,child)
#获取所有子节点。


```


```python
html="""
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class=\"title\" name=\"dromouse\"><b>The Dormouse's story</b></p>
    <p class=\"story\">Once upon a time there were three little sisters; and their names were
    <a href=\"http://example.com/elsie\" class=\"sister\" id=\"link1\"><!-- Elsie --></a>,
    <a href=\"http://example.com/lacie\" class=\"sister\" id=\"link2\">Lacie</a> and
    <a href=\"http://example.com/tillie\" class=\"sister\" id=\"link3\">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class=\"story\">...</p>"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.p.descendants)#子孙节点
for i,child in enumerate(soup.p.descendants):
    print(i,child)
    
```

父节点和祖先节点


```python
html = """
    <html>
        <head>
            <title>The Dormouse's story</title>
        </head>
        <body>
            <p class="story\>
                Once upon a time there were three little sisters; and their names were
                <a href="http://example.com/elsie" class="sister" id="link1">
                    <span>Elsie</span>
                </a>
                <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
                and
                <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
                and they lived at the bottom of a well.
            </p>
            <p class="story">...</p>
      """

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.a.parent)
```


```python
html = """
    <html>
        <head>
            <title>The Dormouse's story</title>
        </head>
        <body>
            <p class="story\>
                Once upon a time there were three little sisters; and their names were
                <a href="http://example.com/elsie" class="sister" id="link1">
                    <span>Elsie</span>
                </a>
                <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
                and
                <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
                and they lived at the bottom of a well.
            </p>
            <p class="story">...</p>
      """

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.a.parents)
```

兄弟节点


```python
html = """
    <html>
        <head>
            <title>The Dormouse's story</title>
        </head>
        <body>
            <p class="story\>
                Once upon a time there were three little sisters; and their names were
                <a href="http://example.com/elsie" class="sister" id="link1">
                    <span>Elsie</span>
                </a>
                <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
                and
                <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
                and they lived at the bottom of a well.
            </p>
            <p class="story">...</p>
      """

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(list(enumerate(soup.a.next_siblings)))
print(list(enumerate(soup.a.previous_siblings)))
```

# 标准选择器

find_all(name,attrs,recursive,text,**kwargs)

可以根据标签名、属性，内容查找文档

name(标签的名字)


```python
 html='''
    <div class=\"panel\">
        <div class="panel-heading">
            <h4>Hello</h4>
        </div>
        <div class="panel-body">
            <ul class="list" id="list-1">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
                <li class="element">Jay</li>
            </ul>
            <ul class="list list-small" id="list-2">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
            </ul>
        </div>
    </div>
    '''
from bs4 import BeautifulSoup 
soup = BeautifulSoup(html,'lxml')

print(soup.find_all('ul'))
print(type(soup.find_all('ul')))
```


```python
 html='''
    <div class=\"panel\">
        <div class="panel-heading">
            <h4>Hello</h4>
        </div>
        <div class="panel-body">
            <ul class="list" id="list-1">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
                <li class="element">Jay</li>
            </ul>
            <ul class="list list-small" id="list-2">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
            </ul>
        </div>
    </div>
    '''
from bs4 import BeautifulSoup 
soup = BeautifulSoup(html,'lxml')

for ul in soup.find_all('ul'):
    for li in ul.find_all('li'):
        print(li)
```

attrs


```python
 html='''
    <div class=\"panel\">
        <div class="panel-heading">
            <h4>Hello</h4>
        </div>
        <div class="panel-body">
            <ul class="list" id="list-1" name="elements">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
                <li class="element">Jay</li>
            </ul>
            <ul class="list list-small" id="list-2" name="elements">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
            </ul>
        </div>
    </div>
    '''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.find_all(attrs={'name':'elements'}))
print(soup.find_all(attrs={'id':'list-1'}))
```


```python
 html='''
    <div class=\"panel\">
        <div class="panel-heading">
            <h4>Hello</h4>
        </div>
        <div class="panel-body">
            <ul class="list" id="list-1" name="elements">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
                <li class="element">Jay</li>
            </ul>
            <ul class="list list-small" id="list-2" name="elements">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
            </ul>
        </div>
    </div>
    '''
    
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.find_all(id="list-1"))
print(soup.find_all(class_="element"))
```

text


```python
 html='''
    <div class=\"panel\">
        <div class="panel-heading">
            <h4>Hello</h4>
        </div>
        <div class="panel-body">
            <ul class="list" id="list-1" name="elements">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
                <li class="element">Jay</li>
            </ul>
            <ul class="list list-small" id="list-2" name="elements">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
            </ul>
        </div>
    </div>
    '''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.find_all(text="Foo"))
```

find(name,attrs,recursive,text,**kwargs)


```python
 html='''
    <div class=\"panel\">
        <div class="panel-heading">
            <h4>Hello</h4>
        </div>
        <div class="panel-body">
            <ul class="list" id="list-1" name="elements">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
                <li class="element">Jay</li>
            </ul>
            <ul class="list list-small" id="list-2" name="elements">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
            </ul>
        </div>
    </div>
    '''
    
    
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')

print(soup.find('ul'))
print(type(soup.find('ul')))
print(soup.find('page'))
```

find_parents() ;  find_parent()

find_next_sibling()  ;  find_next_sibling()

find_previous_sibling()  ;     find_previous_sibling()

find_all_previous();find_previous()

# CSS选择器

通过select()直接传入CSS选择器即可完成选择


```python
 html='''
    <div class="panel">
        <div class="panel-heading">
            <h4>Hello</h4>
        </div>
        <div class="panel-body">
            <ul class="list" id="list-1" name="elements">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
                <li class="element">Jay</li>
            </ul>
            <ul class="list list-small" id="list-2" name="elements">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
            </ul>
        </div>
    </div>
    '''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.select('.panel .panel-heading'))#'.'表示class
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))#'#'表示id
```


```python
 html='''
    <div class="panel">
        <div class="panel-heading">
            <h4>Hello</h4>
        </div>
        <div class="panel-body">
            <ul class="list" id="list-1" name="elements">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
                <li class="element">Jay</li>
            </ul>
            <ul class="list list-small" id="list-2" name="elements">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
            </ul>
        </div>
    </div>
    '''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')

uls=soup.select('ul')
for ul in uls:
    print(ul.select('li'))
```

# 获取属性


```python
 html='''
    <div class="panel">
        <div class="panel-heading">
            <h4>Hello</h4>
        </div>
        <div class="panel-body">
            <ul class="list" id="list-1" name="elements">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
                <li class="element">Jay</li>
            </ul>
            <ul class="list list-small" id="list-2" name="elements">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
            </ul>
        </div>
    </div>
    '''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
uls =soup.select('ul')
for ul in uls:
    print(ul['id'])
```


```python
 html='''
    <div class="panel">
        <div class="panel-heading">
            <h4>Hello</h4>
        </div>
        <div class="panel-body">
            <ul class="list" id="list-1" name="elements">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
                <li class="element">Jay</li>
            </ul>
            <ul class="list list-small" id="list-2" name="elements">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
            </ul>
        </div>
    </div>
    '''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
for li in soup.select('li'):
    print(li.get_text())
```

# 总结

1、推荐使用lxml解析库，必要时使用html.parser
2、标签选择功能弱，但速度快
3、建议使用find()、find_all()查询匹配单个结果或者多个结果
4、如果对CSS选择器熟悉建议使用select()
5、记住常用的获取属性和文本的方法


```python
from jupyterthemes import jtplot
jtplot.style(context='talk', fscale=1.4, spines=False, gridlines='--')
jtplot.reset()
```
