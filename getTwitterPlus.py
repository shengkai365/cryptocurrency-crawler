from pytwitterscraper import TwitterScraper


tw = TwitterScraper()
profile = tw.get_profile(name="elonmusk")
tweets = tw.get_tweets(profile.__dict__['id'],count=10)

array = []
for item in tweets.contents:
    # 1.发表时间 2.内容 3.媒体文件
    array.append([item['created_at'],item['text'],item['media']])

array.sort(key= lambda item: item[0])
for item in array: 
    print(item)
    print('-----------------')
    print(type(item[0]))

'''
{'id': 1400645833150840835, 
'created_at': datetime.datetime(2021, 6, 4, 2, 49, 24, tzinfo=datetime.timezone.utc), 
'lang': 'und', 
'text': 'https://t.co/MLhu6oOwgc', 
'hashtags': [], 
'media': [{'url': 'https://t.co/MLhu6oOwgc', 'type': 'photo', 'image_url': 'https://pbs.twimg.com/media/E3AX9irWQAI77cW.jpg', 'twitter_url': 'https://twitter.com/elonmusk/status/1400645833150840835/photo/1'}],
'urls': [], 
'likes': 128942,
'relay': 0, 
'retweet': 14940}
'''

 # # 推特
    # def getPullTwitter(self):
    #     socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 8080)
    #     socket.socket = socks.socksocket
    #     #人名：twitter_id
    #     users = {'马斯克':'elonmusk'}

    #     #array[0]: 推特, text， url, time, media
    #     ret = []
    #     for key in users.keys():
    #         tw = TwitterScraper()
    #         profile = tw.get_profile(name=users[key])
    #         tweets = tw.get_tweets(profile.__dict__['id'],count=10)
            
    #         for i in range(10):
    #             array = []
    #             media = tweets.contents[i]['media']
    #             title = key+':  '+ tweets.contents[i]['text']
                
    #             array.append('推特')
    #             array.append(title)
    #             array.append(media[0].get('url','') if len(media) else '')
    #             array.append(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'))
    #             array.append(media[0].get('image_url','') if len(media) else '')
    #             ret.append(array[:]) 

    #     return ret 