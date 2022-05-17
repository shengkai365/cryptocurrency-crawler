## Cryptocurrency Crawler

This is a crawler system for cryptocurrency information, so that users can get useful information to make trading decisions in time.



### requirement

```bash
pytwitterscraper
pymysql
python-Levenshtein
fuzzywuzzy
requests
oss2
requests_html
BeautifulSoup4
selenium
```



### How to run

```bash
# clone the repository
git clone https://github.com/shengkai365/cryptocurrency-crawler.git

#
cd cryptocurrency-crawler

# install third-party libraries
pip install -r requirements.txt

#
cd src

# run the crawler of Twitter
python3 crawlerTwitter.py

# test
python3 test.py
```