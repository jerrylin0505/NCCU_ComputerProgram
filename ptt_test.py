import requests
from pyquery import PyQuery as pq

cookies = {"over18":"1"}
res = requests.get("https://www.ptt.cc/bbs/Gossiping/index.html", cookies=cookies)
mainPageDoc = pq(res.text)


for i in range(10):
  for eachTitle in mainPageDoc(".bbs-screen > div > div.title > a").items():
    print(eachTitle.text(), eachTitle.parent().siblings(".meta > .author").text())

  mainPageDoc.make_links_absolute(base_url=res.url)
  res = requests.get(mainPageDoc("#action-bar-container > div > div.btn-group.btn-group-paging \
  > a:nth-child(2)").attr("href"), cookies=cookies)
  mainPageDoc = pq(res.text)
