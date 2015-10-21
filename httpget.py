import httplib 
conn = httplib.HTTPConnection("view.news.qq.com") 
conn.request("HEAD","/original/intouchtoday/n2606.html") 
res = conn.getresponse() 
print res.status, res.reason 
data = res.read() 
print len(data) 