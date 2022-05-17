import datetime
from time import sleep 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
'''
网页抓取操作类
'''


class PullData(object):

    def __init__(self):
        print("init---PullData---")  
   
    # 币世界-政策
    def getPullBishijiePolicy(self):
        
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        browser = webdriver.Chrome(executable_path=r'C:\Program Files\chromedriver.exe', chrome_options=chrome_options)
        browser.get('https://www.bishijie.com/kuaixun')
        sleep(2)
        
        policy_button = browser.find_element_by_xpath('//*[@id="kuaixun"]/div[2]/div[1]/div/div[1]/div[1]/div/ul/li[3]/a')
        policy_button.click()
        sleep(2)
        
        title_template = '//*[@id="kuaixun"]/div[2]/div[1]/div/div[2]/div[1]/div[2]/ul/li[{}]/div/a/h3'
        mesbody_template = '//*[@id="kuaixun"]/div[2]/div[1]/div/div[2]/div[1]/div[2]/ul/li[{}]/div/div[1]/div[1]'
        url_template = '//*[@id="kuaixun"]/div[2]/div[1]/div/div[2]/div[1]/div[2]/ul/li[{}]/div/a'

        array = []

        # 获取当日的0~5条数据
        for i in range(1,6):
            try:
                title = browser.find_element_by_xpath(title_template.format(i)).text[6:]
                mesbody = browser.find_element_by_xpath(mesbody_template.format(i)).text
                url = browser.find_element_by_xpath(url_template.format(i)).get_attribute('href')
                line = [title, mesbody, url]
                array.append(line)
                sleep(0.1)
            except:
                print('selenium.common.exceptions.NoSuchElementException')
                            
        return array 
        

    # 巴比特-微博
    def getPullBaBiteWeibo(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        browser = webdriver.Chrome(executable_path=r'C:\Program Files\chromedriver.exe', chrome_options=chrome_options)
        browser.get('https://www.8btc.com/flash')
        sleep(2)

        policy_button = browser.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/div[1]/ul/li[3]')
        policy_button.click()
        sleep(2)
        
        name_template = '//*[@id="main"]/div/div/div[2]/div[4]/ul/li[{}]/div[1]/div[2]/p[1]'
        mesbody_template = '//*[@id="main"]/div/div/div[2]/div[4]/ul/li[{}]/div[2]/p'
        url_template = '//*[@id="main"]/div/div/div[2]/div[4]/ul/li[{}]/div[2]/p/a'
        
        array = []

        # 前10条数据
        for i in range(1,11):
            try:
                title = browser.find_element_by_xpath(name_template.format(i)).text
                mesbody = browser.find_element_by_xpath(mesbody_template.format(i)).text
                url = browser.find_element_by_xpath(url_template.format(i)).get_attribute('href')
                line = [title, mesbody, url]
                array.append(line)
                sleep(0.1)
            except:
                print('selenium.common.exceptions.NoSuchElementException')
        return array 

    # 币世界-社区
    def getPullBishijieCommunity(self):
        url = 'https://www.bishijie.com/community/new'
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        browser = webdriver.Chrome(executable_path=r'C:\Program Files\chromedriver.exe', chrome_options=chrome_options)
        browser.get(url)
        sleep(2)

        name_template = '//*[@id="communityNew"]/div/div[1]/div[2]/ul/li[{}]/div[1]/div[2]/div[1]/div[1]/div[1]'
        mesbody_template = '//*[@id="communityNew"]/div/div[1]/div[2]/ul/li[{}]/div[1]/div[2]/div[2]/div/div/span/span[1]'
        url_template = '//*[@id="communityNew"]/div/div[1]/div[2]/ul/li[{}]/div[1]/div[2]/div[2]/div/div/span/span[2]/a'

        array = []

        for i in range(10):
            try:
                title = browser.find_element_by_xpath(name_template.format(i+1)).text
                mesbody = browser.find_element_by_xpath(mesbody_template.format(i+1)).text
                url = browser.find_element_by_xpath(url_template.format(i+1)).get_attribute('href')
                line = [title, mesbody, url]
                array.append(line)
                sleep(0.1)
            except Exception as r:
                print('未知错误 %s' % r)
                print(r.__traceback__.tb_frame.f_globals["__file__"])
                print(r.__traceback__.tb_lineno)
        return array 

S = PullData()
array = S.getPullBishijieCommunity()
for line in array:
    print(line)
