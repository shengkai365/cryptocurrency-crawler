import time
import requests
import oss2
from itertools import islice

account = {
            'AccessKeyID': '***************',
            'AccessKeySecret': '**********************',
            'BucketName': 'bpj-webfiles',
            'ImagePath' : 'images/twitter/'
        }

class Oss(object):
    def __init__(self,account):
        self.Account = account 
        self.auth = oss2.Auth(self.Account['AccessKeyID'], self.Account['AccessKeySecret'])
        self.bucket = oss2.Bucket(self.auth, 'http://oss-cn-hangzhou.aliyuncs.com', self.Account['BucketName'])
    
    def put_image_to_oss(self, name, link):
        input = requests.get(link)
        self.bucket.put_object(self.Account['ImagePath']+name, input)
        print('上传图片成功')
        time.sleep(1)

        # # url =  https://bpj-webfiles.oss-cn-hangzhou.aliyuncs.com/example/example.jpg
        # url = 'https://'+ self.Account['BucketName'] + '.oss-cn-hangzhou.aliyuncs.com/' + self.Account['ImagePath'] + name
        
        # https://bpj-webfile.junshangxun.com/images/twitter/example.jpg
        url = 'https://bpj-webfile.junshangxun.com/images/twitter/' + name 
        return url
    
    def put_HTML_to_oss(self,GEN_HTML_PATH):

        name = GEN_HTML_PATH.split('/')[-1]
        self.bucket.put_object_from_file(self.Account['ImagePath']+name, GEN_HTML_PATH)
        print('上传HTML成功')
        time.sleep(1)

        HTML_url = 'https://bpj-webfile.junshangxun.com/images/twitter/' + name 
        return HTML_url 

    def list_from_oss(self):
        # oss2.ObjectIterator用于遍历文件。
        for b in islice(oss2.ObjectIterator(self.bucket), 1000):
            print(b.key)

    def delete_from_oss(self, object_name):
        self.bucket.delete_object(object_name)

    def download_form_oss(self,object_name, local_path):
        self.bucket.get_object_to_file(object_name, local_path)

    def transfer(self, urls):
        
        image_links = []
        for i in range(len(urls)):
            name = urls[i].split('/')[-1]
            image_links.append(self.put_image_to_oss(name, urls[i]))

        return image_links



# oss = Oss(account)
# oss.list_from_oss()
# object_name = 'images/twitter/twitter-html马斯克3391476.html'
# local_path = 'C:/Users/shengkai/Desktop/test.html'
# oss.download_form_oss(object_name,local_path)
# oss.delete_from_oss(object_name)

 