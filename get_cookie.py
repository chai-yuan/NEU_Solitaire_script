from selenium import webdriver
import time
import json

#这份代码的作用是获取cookie
#运行这份代码后进行登录操作，随后cookie便会存放到当前目录下

driver = webdriver.Chrome(r".\chromedriver.exe")

# 记得写完整的url 包括http和https
driver.get('')

# 程序打开网页后20秒内 “手动登陆账户” 
time.sleep(20)

with open('cookies.txt','w') as f:
    # 将cookies保存为json格式
    f.write(json.dumps(driver.get_cookies()))

driver.close()