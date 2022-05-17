from pytwitterscraper import TwitterScraper

class TwitterInfo(object):
    def __init__(self, key, msg, name):
        self.key = key 
        self.channel_id = None 
        self.channel = None 
        self.mesbody = '推特 | ' + key + '：'+ msg
        self.image_url = None 
        self.html_url = None 

        self.image_urls_list = None 
        self.msg = msg 
        self.name = name 

        self.inital()

    def inital(self):
        if self.key in {'Butter','MiniDoge','BabyDoge'}:
            self.channel_id = 16
            self.channel = '项目推特'
        
        if self.key in {'孙宇晨','赵长鹏','马斯克','灰度创始人'}:
            self.channel_id = 2
            self.channel = '名人推特'
        
        if self.key in {'火币','灰度资本','欧易','Coinbase'}:
            self.channel_id = 9
            self.channel = '平台推特'
    
    def inital_oss_image_url(self, image_urls):
        self.image_urls_list = image_urls 
        self.image_url = '' if image_urls==[] else ','.join(image_urls)
        
    def inital_oss_html_url(self, html_url):
        self.html_url = html_url 

class CrawlerTwit(object):

    def __init__(self, twitter_name):
        self.name = twitter_name 
        
        self.id = None 
        self.initial_id()

    def initial_id(self):
        try:
            tw = TwitterScraper()
            
            profile = tw.get_profile(name=self.name)
            self.id = profile.__dict__['id']

        except Exception as r:
            print("出错啦: %s" % r)
            print(r.__traceback__.tb_frame.f_globals["__file__"])
            print(r.__traceback__.tb_lineno)

    
    # 获取十条数据，形如：mesbody, created_time 
    # created_time 有时差
    def get_datas(self):
        data = []
        # data[0]: mesbody, created_time
        # 获取前10条推特
        try:
            tw = TwitterScraper()
            tweets = tw.get_tweets(self.id, count=2)
            
            for line in tweets.contents:
                twinfo = tw.get_tweetinfo(line['id'])
                created_time = twinfo.contents['created_at']
                mesbody = twinfo.contents['text']
                
                media = twinfo.contents['media']
                # media格式如下：
                # [{'url': 'https://t.co/ITY6jyeDLM', 'type': 'photo', 
                # 'image_url': 'https://pbs.twimg.com/media/E5wIZGDXEAEfCGh.jpg', 
                # 'twitter_url': 'https://twitter.com/elonmusk/status/1413013632464662528/photo/1'}]

                image_urls = []
                
                for i in range(len(media)):
                    image_urls.append(media[i]['image_url'])


                #str.find(sub_s): 找到了返回第一个位置索引，没找到返回-1
                
                idx = mesbody.find('http')
                if idx!=-1:
                    mesbody = mesbody[:idx]
        
                if mesbody:
                    data.append([mesbody, created_time, image_urls])
                    
        except Exception as r:
            print("出错啦: %s" % r)
            print(r.__traceback__.tb_frame.f_globals["__file__"])
            print(r.__traceback__.tb_lineno)

        return data


# tweets_infos = tweets.contents 格式如下：
# '''
# {'id': 1400645833150840835, 
# 'created_at': datetime.datetime(2021, 6, 4, 2, 49, 24, tzinfo=datetime.timezone.utc), 
# 'lang': 'und', 
# 'text': 'https://t.co/MLhu6oOwgc', 
# 'hashtags': [], 
# 'media': [{'url': 'https://t.co/MLhu6oOwgc', 'type': 'photo', 'image_url': 'https://pbs.twimg.com/media/E3AX9irWQAI77cW.jpg', 'twitter_url': 'https://twitter.com/elonmusk/status/1400645833150840835/photo/1'}],
# 'urls': [], 
# 'likes': 128942,
# 'relay': 0, 
# 'retweet': 14940}
# '''