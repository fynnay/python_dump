# python network check
import urllib2

def internet_on():
    try:
    	header = {"pragma" : "no-cache"} # Tells the server to send fresh copy
        req = urllib2.Request("http://google.com",headers=header,)
        response = urllib2.urlopen(req, timeout = 2)
        return True
    except urllib2.URLError as err:
    	print err
    return False
print internet_on()