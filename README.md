# my_crawler

###  Twitter 爬取需求

| 推特名账号 | channel  | channel_id | name          |
| ---------- | -------- | ---------- | ------------- |
| Butter     | 项目推特 | 16         | butterswap    |
| MiniDoge   | 项目推特 | 16         | MiniDOGEToken |
| BabyDoge   | 项目推特 | 16         | BabyDogeCoin  |
| 孙宇晨     | 名人推特 | 2          | justinsuntron |
| 赵长鹏     | 名人推特 | 2          | cz_binance    |
| 马斯克     | 名人推特 | 2          | elonmusk      |
| 灰度创始人 | 名人推特 | 2          | BarrySilbert  |
| 火币       | 平台推特 | 9          | HuobiGlobal   |
| 灰度资本   | 平台推特 | 9          | Grayscale     |
| 欧易       | 平台推特 | 9          | OKEx          |
| Coinbase   | 平台推特 | 9          | CoinbasePro   |

### 币世界名人

| name     | url                                           |            |
| -------- | --------------------------------------------- | ---------- |
| 忠本聪   | https://i.bishijie.com/home/310341176/dynamic |            |
| 陈楚初   | https://i.bishijie.com/home/825196401/dynamic |            |
| 于集鑫   | https://i.bishijie.com/home/224934581/dynamic |            |
| 紫狮财经 | https://i.bishijie.com/home/810652218/dynamic |            |
| 丁佳永   | https://i.bishijie.com/home/624941048/dynamic |            |
| 海宇谈币 | https://i.bishijie.com/home/137715106/dynamic | 过滤祝福语 |
| 阿星论币 | https://i.bishijie.com/home/111835487/dynamic |            |
| 时时解币 | https://i.bishijie.com/home/124119401/dynamic |            |

### 芝麻开门投票

原始投票页面: https://www.gateio.ch/cn/poll

中间页面： https://www.gateio.ch/poll/votelist/173

详情页面：https://www.gateio.ch/cn/article/21408

抓取详情页面的：标题，项目介绍

### Twitter-HTML-demo

```html
<!DOCTYPE html>
<html>
  <head lang="en">
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1.0, user-scalable=0"
    />
    <meta content="yes" name="apple-mobile-web-app-capable" />
    <meta content="black" name="apple-mobile-web-app-status-bar-style" />
    <meta content="telephone=no" name="format-detection" />
    <title>html模板</title>
  </head>
  <body>
    <div class="box-warp">
      <div class="top-box">
        <div class="title">
          <p>推特｜MidiDoge:MiniDOGE fadsfasdfasadfasdfasdfad</p>
        </div>
        <div class="time">2020-01-01 12:11:22</div>
      </div>
      <div class="content">
        To celebrate the #Tokyo2020 starting today, this #OKExWeekendQuiz we are bringing the #Olympics quiz!What are the 5 sports on the logo?1⃣️ Follow+ Like+ Retweet2⃣️ Comment with the right hashtags (e.g. #football )3⃣️ Fill 
      </div>
      <div class="image-box">
        <div class="image-item">
          <img src="https://bpj-webfile.junshangxun.com/images/twitter/E7C-pdyX0AUCzin.jpg" alt="" srcset="">
        </div>
        <div class="image-item">
          <img src="https://bpj-webfile.junshangxun.com/images/twitter/E7C-pdyX0AUCzin.jpg" alt="" srcset="">
        </div>
        
      </div>
    </div>
    <script>
      $(function () {});
    </script>
  </body>
  <style>
    *{padding:0;margin:0}body{background-color:#e2e2e2}.box-warp{background-color:white;margin:10px 8px 0 8px;border-radius:5px}.box-warp .top-box{border-bottom:1px solid #d8d5d5;padding:10px}.box-warp .top-box .title{font-weight:bold;font-size:1.2rem;width:100%}.box-warp .top-box .title p{word-break:normal;word-break:break-all}.box-warp .top-box .time{font-size:.89rem;color:#9e9e9e;margin-top:5px}.box-warp .content{padding:20px 10px 0 10px;font-size:1rem}.box-warp .content p{word-break:normal;word-break:break-all}.image-box{margin-top:20px}.image-box .image-item{margin-top:5px;padding:0 10px}.image-box .image-item img{width:100%;border-radius:5px}
  </style>
</html>

```
