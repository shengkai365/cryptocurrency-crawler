from pytwitterscraper import TwitterScraper
from time import sleep 
import datetime
from sql_insert import insert
 # 推特
def getPullTwitter():

    #人名：twitter_id
    users = {'马斯克':'elonmusk'}
    while True:
        array = []
        
        for key in users.keys():
            tw = TwitterScraper()
            profile = tw.get_profile(name=users[key])
            # 获取前10条推特
            tweets = tw.get_tweets(profile.__dict__['id'],count=10)
            tweets_infos = tweets.contents
            # 根据时间排序
            tweets_infos.sort(key = lambda item: item['created_at'], reverse=True)

            # array[0]:   name(elonmusk), mesbody, url, image_url
            line = []
            for info in tweets_infos:
                text = info['text']
                media = info['media']

                mesbody = text 
                url = ''
                image_url = ''

                #str.find(sub_s): 找到了返回第一个位置索引，没找到返回-1
                idx = text.find('http')
                if idx!=-1:
                    url = text[idx:]
                    mesbody = text[:idx]
                
                if media!=[] and media[0]['type']=='photo':
                    image_url = media[0]['image_url']
                    if url == '':
                        url = media[0]['url']
                line = ['elonmusk', mesbody, url, image_url]
            insert(url,mesbody)

        print("Waite 5 minutes")
        sleep(300)
    return array 


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



if __name__ == "__main__":
    getPullTwitter()