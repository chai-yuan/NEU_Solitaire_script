from selenium import webdriver
import json
import time

driver = webdriver.Chrome(r".\chromedriver.exe")

names = {

}
urls = []

#从文件中读取网址
with open("urls.txt","r") as f:
    content = [line.rstrip('\n') for line in f]
    urls=content

#对每一个网址进行操作
for url in urls:
    driver.get(url)
    driver.delete_all_cookies()
    #清空标记
    for name in names:
        names[name]=0

    with open('cookies.txt','r') as f:
        cookies_list = json.load(f)
        #载入cookie
        for cookie in cookies_list:
            if isinstance(cookie.get('expiry'), float):
                cookie['expiry'] = int(cookie['expiry'])
            driver.add_cookie(cookie)
        #刷新并延时，防止因为网络加载缓慢而出错
        driver.refresh()
        time.sleep(5)

        #对每一份名单进行检查
        for i in range(2,34):
            time.sleep(0.15)
            try:
                test = driver.find_element_by_xpath('//*[@id="root"]/div[3]/div/div[2]/div[2]/div/div[1]/div['+str(i)+']/textarea')
                driver.execute_script("arguments[0].scrollIntoView();", test)
                a=test.text
                for name in names:
                    if(a[:2]==name[4:6]):
                        names[name]=1   #找到了！
            except:
                break       #如果没有填完，那么就退出好了
        
        #输出
        print()
        print()
        print("对"+url+"进行检查")
        print()
        for name in names:
            if(names[name]==0):
                print(name+" 未填写")
        
        print()
        print("检查完毕")
