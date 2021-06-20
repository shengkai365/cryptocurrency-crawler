import datetime
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import datetime
import json
# from exceptionMessage import ExceptionMessage

'''
网页抓取操作类
'''
#代理服务器
proxyHost = "120.12.70.105"
proxyPort = "4220"

# proxyMeta = "http://%(host)s:%(port)s" % {
#     "host" : proxyHost,
#     "port" : proxyPort,
# }

#pip install -U requests[socks]  socks5 
proxyMeta = "socks5://%(host)s:%(port)s" % {

    "host" : proxyHost,

    "port" : proxyPort,

}

proxies = {
    "http"  : proxyMeta,
    "https"  : proxyMeta
}

class PullData(object):

    def __init__(self):
        print("init---PullData---")  # never prints

    def getHTMLText(self, url):
        try:
            r = requests.get(url, timeout=30,proxies=proxies)
            r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
            r.encoding = r.apparent_encoding
            return r.text
        except:
            print(url + '产生异常')
            return "产生异常"

    def getPullHuoBiData(self, oldTitle):

        insertTimes = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        url1 = 'https://www.huobi.pe/support/zh-cn/list/360000039942?t=' + insertTimes
        array = []
        try:
            session = HTMLSession()
            r1 = session.get(url1,proxies=proxies)
            for i in range(20):
                title = r1.html.find(
                    '#__layout > section > div > div.page > div > div.layout-box > div.main-content > dl > dd:nth-child({}) > div.link-dealpair > a'.format(
                        i + 1), first=True)
                time = r1.html.find(
                    '#__layout > section > div > div.page > div > div.layout-box > div.main-content > dl > dd:nth-child({}) > div.date'.format(
                        i + 1), first=True)

                if title is None:
                    continue
                else:
                    tempTile = title.text.replace(',', '')

                    if oldTitle != '' and oldTitle in tempTile:
                        break

                    line = ('1' , '平台上新', tempTile, 'https://www.huobi.pe' + title.attrs['href'],
                            datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'), '', '3', '火币', 'N', '0')
                    array.append(line)

        except Exception as r:
            print('未知错误 %s' % r)
            print(r.__traceback__.tb_frame.f_globals["__file__"])
            print(r.__traceback__.tb_lineno)
            ExceptionMessage.sendErrorMessage('getPullHuoBiData--火币抓取异常')

        return array

    def getPullBiAnData(self, oldTitle):

        insertTimes = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        url2 = 'https://www.binancezh.co/zh-CN/support/announcement/c-48?navId=48&t=' + insertTimes
        array = []
        try:
            session = HTMLSession()
            r2 = session.get(url2,proxies=proxies)
            for i in range(20):
                title = r2.html.xpath(
                    '//*[@id="__APP"]/div/div/main/div/div[3]/div[1]/div[2]/div[2]/div/a[{}]'.format(i + 1), first=True)
                if title is None:
                    continue
                else:
                    tempTile = title.text.replace(',', '')
                    if oldTitle != '' and oldTitle in tempTile:
                        break

                    line = ('1', '平台上新', tempTile, 'https://www.binancezh.co/' + title.attrs['href'],
                            datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'), '', '3','币安', 'N', '0')
                    array.append(line)

        except Exception as r:
            print('未知错误 %s' % r)
            print(r.__traceback__.tb_frame.f_globals["__file__"])
            print(r.__traceback__.tb_lineno)
            ExceptionMessage.sendErrorMessage('getPullBiAnData--币安抓取异常')

        return array

    def getPullOEXData(self, oldTitle):
        array = []
        insertTimes = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        url3 = 'https://www.ouyi.cc/support/hc/zh-cn/sections/115000447632-%E6%96%B0%E5%B8%81%E4%B8%8A%E7%BA%BF&t=' + insertTimes
        try:
            # i: 为页码
            for i in range(1):
                r3 = self.getHTMLText(url3)
                soup = BeautifulSoup(r3, 'html.parser')
                Tags = soup.find_all('a', class_="article-list-link")
                for tag in Tags:
                    tempTile = tag.string.replace(',', '')
                    if oldTitle != '' and oldTitle in tempTile:
                        break

                    line = ('1', '平台上新', tag.string.replace(',', ''), 'https://www.ouyi.cc/support/' + tag.attrs['href'],
                            datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'), '', '3', 'okex', 'N', '0')
                    array.append(line)

        except Exception as r:
            print('未知错误 %s' % r)
            print(r.__traceback__.tb_frame.f_globals["__file__"])
            print(r.__traceback__.tb_lineno)
            ExceptionMessage.sendErrorMessage('getPullOEXData--okex抓取异常')

        return array

    @property
    def getPullBiShiJieData(self):

        insertTimes = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        url4 = 'https://www.bishijie.com/kuaixun?t='+insertTimes
        array = []
        try:
            session = HTMLSession()
            r4 = session.get(url4,proxies = proxies)
            for i in range(20):
                title = r4.html.find(
                    '#kuaixun > div.nno > div.fl > div > div.home-container > div > div.content-wrap > ul > li:nth-child({}) > div > a > h3'.format(
                        i + 1), first=True)

                content = r4.html.find(
                    '#kuaixun > div.nno > div.fl > div > div.home-container > div > div.content-wrap > ul > li:nth-child({}) > div > div > div'.format(
                        i + 1), first=True)

                addrs = r4.html.find(
                    '#kuaixun > div.nno > div.fl > div > div.home-container > div > div.content-wrap > ul > li:nth-child({}) > div > a'.format(
                        i + 1), first=True)

                titleText = title.text
                titleText = titleText[6:]
                if title is None:
                    continue
                else:
                    if len(title.attrs) > 1:
                        line = (titleText, 'https://www.bishijie.com' + addrs.attrs['href'],
                                datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'),
                                content.text)
                        array.append(line)
        except Exception as r:
            print('未知错误 %s' % r)
            print(r.__traceback__.tb_frame.f_globals["__file__"])
            print(r.__traceback__.tb_lineno)
            ExceptionMessage.sendErrorMessage('getPullBiShiJieData--币世界抓取异常')

        return array
        # 非小号
    
    # 非小号
    def getPullFeiXiaoHao(self):
        url_ = 'https://dncapi.bqrank.net/api/v4/news/news?channelid=24&direction=1&per_page=100&isfxh=0&webp=1'
        try:
            text = self.getHTMLText(url_)
            dic = json.loads(text)
            array = []
            for item in dic['data']['list'][:10]:
                title = item['title']
                mesbody = item['content']
                url = item['avatar']
                line = (title, url, datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'), mesbody)
                array.append(line)
        except Exception as r:
            print('未知错误 %s' % r)
            print(r.__traceback__.tb_frame.f_globals["__file__"])
            print(r.__traceback__.tb_lineno)
            ExceptionMessage.sendErrorMessage('getPullFeiXiaoHao--非小号抓取异常')

        return array

    # 币快报
    def getPullBiKuaiBao(self):
        url_ = 'https://www.beekuaibao.com/newsflashes'
        try:
            session = HTMLSession()
            r = session.get(url_, headers=self.headers)
            array = []
            for i in range(10):
                title_pattem = '#__layout > div > div > div > div > section > div > div > div > div.body > div > div > div.bd > div > div.body > div > a:nth-child({}) > div.title'.format(
                    i + 1)
                mesbody_pattem = '#__layout > div > div > div > div > section > div > div > div > div.body > div > div > div.bd > div > div.body > div > a:nth-child({}) > div.desc > div'.format(
                    i + 1)
                url_pattem = '#__layout > div > div > div > div > section > div > div > div > div.body > div > div > div.bd > div > div.body > div > a:nth-child({})'.format(
                    i + 1)

                title_elem = r.html.find(title_pattem, first=True)
                mesbody_elem = r.html.find(mesbody_pattem, first=True)
                url_elem = r.html.find(url_pattem, first=True)

                title = title_elem.text
                mesbody = mesbody_elem.text
                url = 'https://www.beekuaibao.com' + url_elem.attrs['href']

                line = (title, url, datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'), mesbody)
                array.append(line)
        except Exception as r:
            print('未知错误 %s' % r)
            print(r.__traceback__.tb_frame.f_globals["__file__"])
            print(r.__traceback__.tb_lineno)
            ExceptionMessage.sendErrorMessage('getPullBiKuaiBao--币快报抓取异常')

        return array

    # 巴比特7x24
    def getPullBaBite(self):
        url_ = 'https://www.8btc.com/flash'
        try:
            session = HTMLSession()
            r = session.get(url_, headers=self.headers)
            array = []
            for i in range(10):
                title_pattem = '#main > div > div > div.mid-container.bbt-col-xs-16 > div:nth-child(5) > div.flash-list > div:nth-child({}) > div > h6 > a > p'.format(
                    i + 1)
                mesbody_pattem = '#main > div > div > div.mid-container.bbt-col-xs-16 > div:nth-child(5) > div.flash-list > div:nth-child({}) > div > div.flash-desc > div > p'.format(
                    i + 1)
                url_pattem = '#main > div > div > div.mid-container.bbt-col-xs-16 > div:nth-child(5) > div.flash-list > div:nth-child({}) > div > h6 > a'.format(
                    i + 1)

                title_elem = r.html.find(title_pattem, first=True)
                mesbody_elem = r.html.find(mesbody_pattem, first=True)
                url_elem = r.html.find(url_pattem, first=True)

                title = title_elem.text
                mesbody = mesbody_elem.text
                url = 'https://www.8btc.com' + url_elem.attrs['href']

                line = (title, url, datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'), mesbody)
                array.append(line)
        except Exception as r:
            print('未知错误 %s' % r)
            print(r.__traceback__.tb_frame.f_globals["__file__"])
            print(r.__traceback__.tb_lineno)
            ExceptionMessage.sendErrorMessage('getPullBaBite--巴比特抓取异常')
        return array



# S = PullData()
# array = S.getPullBiAnData('$')
# # array = S.getPullOEXData("#")
# print(array)