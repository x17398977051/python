#Selenium库的使用 $pip install selenium
from selenium import webdriver
driver = webdriver.Firefox(executable_path='C:/Users/Administrator/Desktop/geckodriver.exe') #新版本需要下载 geckodriver

driver.get('http://www.santostang.com/2018/07/04/hello-world/')
driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere-comment']")) #如果有iframe的话,需要先解析iframe

comment = driver.find_element_by_css_selector('div.reply-content')
content = comment.find_element_by_tag_name('p')
print(content.text)

