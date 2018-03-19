#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import gzip
import json
import MySQLdb
from datetime import datetime

url = "http://data.taipei/youbike"
#print "downloading with urllib"
urllib.urlretrieve(url, "data.gz")
f = gzip.open('data.gz', 'r')
jdata = f.read()
f.close()
data = json.loads(jdata)
conn = MySQLdb.connect(host="db", user="root", passwd="123", db="HelloTest")
c = conn.cursor()
conn.set_character_set('utf8')

for key,value in data["retVal"].iteritems():
    sno = value["sno"]
    tot = value["tot"]
    sbi = value["sbi"]
    bemp = value["bemp"]
    act = value["act"]

    sql = "INSERT INTO data(sno,tot,sbi,bemp,act,utime) VALUES(%s,%s,%s,%s,%s,%s)"
    try:
        c.execute(sql,(sno,tot,sbi,bemp,act,datetime.now()))
        conn.commit()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

sql = "DELETE  FROM data WHERE utime < CONVERT_TZ(NOW(),'+00:00','+08:00') - INTERVAL 1 DAY"
try:
    c.execute(sql)
    conn.commit()
except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
conn.close()