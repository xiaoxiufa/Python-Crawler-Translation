---
title : python爬虫（一）
data : 2021-8-13
tags : [python,python爬虫]
toc : True
author: xiaojian
---
## 爬虫中英互译
<!--more -->
## 前言
> 很长一段时间就想认真学习python,但前面一段时间由于执行力太差，导致了python荒废了很久，想着还是把他们重新捡起来，这是我第一次有规划的去写一个爬虫，虽然参考很多资料，终归还是出来了，期望小伙伴们能经常看见我博客的更新，监督一下小新哈哈！！
> 这个爬虫可以实现中英文的翻译，这个爬虫和有道翻译紧密相连
```
爬虫的含义：其实爬虫非常简单，就是python像一个正常人一样去访问一个网站，其实这个过程中我们就是要不断伪装自己，让它以为你就是一个正常人，从而获取更多的源代码  

反爬虫：对扫描器中的网络爬虫环节进行反制，通过一些反制策略来阻碍或干扰爬虫的正常爬行，从而间接地起到防御目的  

反反爬虫机制:我们在请求网页时候对自己进行伪装，可以请求头中添加元素，其实这个并不是所有的爬虫都需要使用到反反爬虫，这个得看网站反爬虫机制的干扰力度
```
## 实验环境
python环境
pycharm
chrome(最好使用这个，其他的也可以)
> 你在写爬虫之前一定到先去正常浏览这个网站，在网页源代码中找到请求头，从而获得请求信息。

## python代码
```
vars="""  
**************************  
** 此工具和有道翻译紧密联系 **** 此工具仅仅支持中英文互译 ****状态码显示200，表示翻译成功**  
** 欢迎使用Python翻译工具 **** 需要自己输入翻译内容 **** 输入exit,则突出翻译 ****************************  
"""  
import requests  
print(vars)  
def fanyi(kd):  
    url = "https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"  
  #请求头  
  headers = {  
        "Accept": "application/json, text/javascript, */*; q=0.01",  
        "Accept-Language": "zh-CN,zh;q=0.9",  
        "Connection": "keep-alive",  
        "Content-Type": "keep-alive",  
        "Host": "fanyi.youdao.com"  
  }  
    #POST请求发送的数据  
  data = {  
        "i": kd,  
        "doctype": "json"  
  }  
    responses = requests.post(url, data) #请求网页  
  code = responses.status_code #获得网页状态码  
  print('状态码:',code)  
    if code == 200: #判端网页是否请求成功  
  responsesdata = responses.json()  
        if responsesdata["errorCode"] == 0: #判断返回信息中的errCode和正常访问是否一致  
  print('翻译结果：',responsesdata["translateResult"][0][0]["tgt"])  
    else :  
        print("翻译失败，请联系管理")  
while True :  
    input_js=input('输入翻译内容：')  
    if input_js=='exit':  
        break  
 else :  
        fanyi(input_js)
```
## 代码执行成功
![](/img/python_pc1.jpg)

## 尾言
希望在过两天，各位小伙伴能看见我下一篇爬虫出现，每天都在精进自己技术！！！





