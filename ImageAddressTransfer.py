import time
import requests
import oss2
from itertools import islice

class Oss(object):
    def __init__(self):
        self.Account = {
            'AccessKeyID': '*****',
            'AccessKeySecret': '********',
            'BucketName': 'bpj-webfiles',
            'ImagePath' : 'images/twitter/'
        }
        

        self.auth = oss2.Auth(self.Account['AccessKeyID'], self.Account['AccessKeySecret'])
        self.bucket = oss2.Bucket(self.auth, 'http://oss-cn-hangzhou.aliyuncs.com', self.Account['BucketName'])
    
    def put_to_oss(self, name, link):
        input = requests.get(link)
        self.bucket.put_object(self.Account['ImagePath']+name, input)
        print('上传成功')
        time.sleep(1)

        # # url =  https://bpj-webfiles.oss-cn-hangzhou.aliyuncs.com/example/example.jpg
        # url = 'https://'+ self.Account['BucketName'] + '.oss-cn-hangzhou.aliyuncs.com/' + self.Account['ImagePath'] + name
        
        # https://bpj-webfile.junshangxun.com/images/twitter/example.jpg
        url = 'https://bpj-webfile.junshangxun.com/images/twitter/' + name 
        return url

    def list_from_oss(self):
        # oss2.ObjectIterator用于遍历文件。
        for b in islice(oss2.ObjectIterator(self.bucket), 20):
            print(b.key)

    def delete_from_oss(self, object_name):
        self.bucket.delete_object(object_name)

    def transfer(self, urls):
        
        image_links = []
        for i in range(len(urls)):
            name = urls[i].split('/')[-1]
            image_links.append(self.put_to_oss(name, urls[i]))

        return image_links

oss = Oss()
oss.list_from_oss()

