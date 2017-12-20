
# Selenium

自动化测试工具，支持多种浏览器。
爬虫中主要用来解决JavaSript的渲染问题
当通过requests和urllib库无法获得网页内容，这个时候可以用Selenium库来模拟浏览器

# 安装

pip install selenium

# 基本使用


```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


browser = webdriver.Chrome()#声明浏览器对象
try:
    browser.get('http://www.baidu.com')# 传入网址
    input = browser.find_element_by_id('kw')#找出id为kw的元素
    input.send_keys('Python')# 像元素中发送python字符串
    input.send_keys(Keys.ENTER)# 传入Enter键
    wait = WebDriverWait(browser,10)
    wait.until(EC.presence_of_element_located((By.ID,'content_left')))
    print(browser.current_url)#打出此时的url
    print(browser.get_cookies)#打印出cookies
    print(browser.page_source)#打印出源代码
finally:
    browser.close()
    
```

# 声明浏览器对象


```python
        from selenium import webdriver
    
browserser = webdriver.Chrome()
browser = webdriver.Firefox()
browser = webdriver.Edge()
browser = webdriver.PhantomJS()

```

# 访问页面



```python
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
print(browser.page_source())


```

# 查找元素

单个元素


```python
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.taobao.com')
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first,input_second,input_third)


```

    <selenium.webdriver.remote.webelement.WebElement (session="083bed68dcd606e04283a746c7740ae3", element="0.2966710928404561-1")> <selenium.webdriver.remote.webelement.WebElement (session="083bed68dcd606e04283a746c7740ae3", element="0.2966710928404561-1")> <selenium.webdriver.remote.webelement.WebElement (session="083bed68dcd606e04283a746c7740ae3", element="0.2966710928404561-1")>
    

find_element_by_name

find_element_by_xpath

find_element_by_link_text

find_element_by_tag_name

find_element_by_class_name

find_element_by_css_selector


```python
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input_first = browser.find_element(By.ID,'q')
print(input_first)
#browser.close()

```

多个元素


```python
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
lis = browser.find_elements_by_css_selector('.service-bd li')
print(lis)


```


```python
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
lis = browser.find_elements(By.CSS_SELECTOR,'.service-bd li')
print(lis)


```


    --------------------------------------------------------------------

    NoSuchWindowException              Traceback (most recent call last)

    <ipython-input-4-91eda376000c> in <module>()
          3 browser = webdriver.Chrome()
          4 browser.get('https://www.taobao.com')
    ----> 5 lis = browser.find_elements(By.CSS_SELECTOR,'.service-bd li')
          6 print(lis)
          7 
    

    D:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py in find_elements(self, by, value)
        856         return self.execute(Command.FIND_ELEMENTS, {
        857             'using': by,
    --> 858             'value': value})['value']
        859 
        860     @property
    

    D:\Anaconda3\lib\site-packages\selenium\webdriver\remote\webdriver.py in execute(self, driver_command, params)
        295         response = self.command_executor.execute(driver_command, params)
        296         if response:
    --> 297             self.error_handler.check_response(response)
        298             response['value'] = self._unwrap_value(
        299                 response.get('value', None))
    

    D:\Anaconda3\lib\site-packages\selenium\webdriver\remote\errorhandler.py in check_response(self, response)
        192         elif exception_class == UnexpectedAlertPresentException and 'alert' in value:
        193             raise exception_class(message, screen, stacktrace, value['alert'].get('text'))
    --> 194         raise exception_class(message, screen, stacktrace)
        195 
        196     def _value_or_default(self, obj, key, default):
    

    NoSuchWindowException: Message: no such window: target window already closed
    from unknown error: web view not found
      (Session info: chrome=62.0.3202.94)
      (Driver info: chromedriver=2.31.488763 (092de99f48a300323ecf8c2a4e2e7cab51de5ba8),platform=Windows NT 10.0.16299 x86_64)
    


# 元素交互操作


```python
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('ipad')
button = browser.find_element_by_class_name('btn-search')
button.click()
```

# 交互动作

将动作附加到动作链中串行执行


```python
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)#请求一个url
browser.switch_to.frame('iframeResult')#切换到一个frame
source = browser.find_element_by_css_selector('#draggable')#找到要拖拽对象
target = browser.find_element_by_css_selector('#droppable')#找到目标位置
actions = ActionChains(browser)
actions.drag_and_drop(source,target)
actions.perform()
```

更多动作：http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains

# 执行JavaScript


```python
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("to bottom")')
```

# 获取元素信息

获取属性


```python
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))
```

获取文本值


```python
from selenium import webdriver

browser = webdriver.Chrome()
url = ('https://www.zhihu.com/explore')
browser.get(url)
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)

```

    提问
    

获取ID、位置、标签名、大小


```python
from selenium import webdriver

browser = webdriver.Chrome()
url = 'https:/www.zhihu.com/explore'
browser.get(url)
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)
```

# Frame


```python
from selenium import webdriver

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
print(source)
try:
    logo = browser.find_elememt_by_class_name('logo')
except Exception:
    print('NoLogo')
    
browser.switch_to.parent_frame()
    
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)    

```

# 等待

隐式等待

当使用了隐式等待执行测试的时候，如果 WebDriver没有在 DOM中找到元素，将继续等待，超出设定时间后则抛出找不到元素的异常, 换句话说，当查找元素或元素并没有立即出现的时候，隐式等待将等待一段时间再查找 DOM，默认的时间是0


```python
from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)

```

    提问
    

显式等待


```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser,10)
input = wait.until(EC.presence_of_element_located((By.ID,'q'))) 
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))
print(input,button)
```

详细内容：http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions

# 前进后退


```python
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')
browser.back()
time.sleep(9)
browser.forward()
browser.close()

```

# Cookies


```python
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())

```

# 选项卡管理


```python
import time

from selenium import webdriver
browser= webdriver.Chrome()
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(5)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://python.org')
```

# 异常处理


```python
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()

```

详细文档：http://selenium-python.readthedocs.io/api.html#module-selenium.common.exceptions
