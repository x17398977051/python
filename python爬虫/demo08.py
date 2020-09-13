# 爬一下菜鸟教程
from selenium import webdriver

comments = []

driver = webdriver.Firefox(executable_path='C:/Users/Administrator/Desktop/geckodriver.exe')  # 新版本需要下载 geckodriver
# 菜鸟教程网址
link = 'https://www.runoob.com/js/js-obj-math.html'
driver.get(link)
qa_headline = driver.find_element_by_id('qa_headline')
qa_headline.click()

comment_list = driver.find_element_by_class_name('commentlist')
comment_list_items = comment_list.find_elements_by_css_selector('li.comment')

for node in comment_list_items:
    children_div = node.find_element_by_class_name('comt-main')
    children_div_p = children_div.find_elements_by_css_selector('p')
    for html_p in children_div_p:
        comments.append(html_p.text)


with open('runoob_js_js_object_math.txt','a+') as f:
    for comment in comments:
        f.write(f'{comment}\n')
