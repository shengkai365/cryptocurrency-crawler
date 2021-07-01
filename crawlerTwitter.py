from pytwitterscraper import TwitterScraper


class CrawlerTwit(object):

    def __init__(self,twitter_name):
        self.name = twitter_name 
        
        self.id = None 
        self.initial_id()

    def initial_id(self):
        try:
            tw = TwitterScraper()
            profile = tw.get_profile(name=self.name)
            self.id = profile.__dict__['id']
            print("---initial id: %s" % self.id)

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
            tweets = tw.get_tweets(self.id, count=10)
            tweets_infos = tweets.contents

            # 根据时间排序
            tweets_infos.sort(key = lambda item: item['created_at'], reverse=True)
            
            for info in tweets_infos:
                mesbody = info['text']
                created_time = info['created_at']

                #str.find(sub_s): 找到了返回第一个位置索引，没找到返回-1
                idx = mesbody.find('http')
                if idx!=-1:
                    mesbody = mesbody[:idx]

                if mesbody:
                    data.append([mesbody, created_time])
                    
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