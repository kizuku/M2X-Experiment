import urllib2
import json

req = urllib2.Request("http://api.open-notify.org/iss-now.json")
response = urllib2.urlopen(req)

obj = json.loads(response.read())

print "Success"
print obj['timestamp']
print obj['iss_position']['latitude'], obj['iss_position']['latitude']
