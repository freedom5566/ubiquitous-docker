import urllib
import gzip
import json

url = "http://data.taipei/youbike"
urllib.urlretrieve(url, "data.gz")
f = gzip.open("data.gz", 'r')
jdata = f.read()
f.close()
data = json.loads(jdata)
for key,value in data["retVal"].iteritems():
    sno = value["sno"]
    sna = value["sna"]
    print "NO." + sno + " " + sna
