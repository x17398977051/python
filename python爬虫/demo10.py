#selenium提交表单
user = driver.find_element_by_name('username') #找到账号输入框
user.clear #清除输入框内容
user.send_keys('admin') #设置输入框内容

#同理找到密码框

#最后模拟登陆
driver.find_element_by_id('login_btn').click()