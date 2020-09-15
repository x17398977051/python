#selenium爬虫实践;(爬短租网站数据)
from  selenium import webdriver
fp = webdriver.FirefoxProfile()
#禁止浏览器加载图片(实测有效)
fp.set_preference('permissions.default.image',2)
driver = webdriver.Firefox(firefox_profile=fp,executable_path='C:\/Users\Machenike\Documents\gecko\geckodriver.exe')

offset = 0;

url = f'https://zh.airbnb.com/s/Shenzhen--China/homes?items_offset={offset}'
driver.get(url=url)

home_names = driver.find_elements_by_css_selector('div._qrfr9x5')
for n in home_names:
    print(f'客栈名称:{n.text}')

price_box_list = driver.find_elements_by_css_selector('div._1ixtnfc')
for p in price_box_list:
    price_strings = p.find_elements_by_css_selector('span')
    format_str = ''
    for ps in price_strings:
        format_str += ps.text;
    print(f'价格<--->{format_str}')

