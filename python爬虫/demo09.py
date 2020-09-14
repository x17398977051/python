# 导入selenium库
from selenium import webdriver

# 为了解决selenium加载会很慢的问题,我们可以选择性的控制浏览器加载的内容,css,images,javaScript ...
# 控制css加载
fp = webdriver.FirefoxProfile()
#禁止浏览器加载图片(实测有效)
fp.set_preference('permissions.default.image',2)
#实测无效,禁止加载CSS
fp.set_preference('permissions.default.stylesheet',2)
#实测无效 禁止加载js
fp.set_preference('javascript.enabled',False)
# 使用geckodriver是为了防止selenium版本不兼容导致代码报错!
driver = webdriver.Firefox(firefox_profile=fp, executable_path='C:\/Users\Machenike\Documents\gecko\geckodriver.exe')
driver.get('https://www.runoob.com/html/html-tutorial.html');