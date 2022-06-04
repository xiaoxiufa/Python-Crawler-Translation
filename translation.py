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