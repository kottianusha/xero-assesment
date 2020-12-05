import json
import http.client
    
def submitpost():

    #Get data from Given Health URL
    conn = http.client.HTTPSConnection("api.nasa.gov")
    payload = ''
    headers = {
      'Content-Type': 'application/json',
      'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    #Submit Get Call to get Data
    conn.request("GET", "/planetary/apod?api_key=DEMO_KEY", payload, headers)
    res = conn.getresponse()
    #String Data of health URL
    jsondata = json.dumps(json.loads(res.read()))
    print(jsondata)
    
    #Post data to hubdoc-xer-monitoring-system.com
    conn = http.client.HTTPSConnection("hubdoc-xer-monitoring-system.com")
    payload = "{\"body\" : \"" + jsondata + "\"}"
    print(payload);
    headers = {
      'Content-Type': 'application/json',
      'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    conn.request("POST", "/", payload, headers)
    res = conn.getresponse()
    #Post Call Repsonse
    data = res.read()
    print(data)

# Submit Http Requests.
# Import Json >> For Json Data Concersion 
        # http.client/Request >> To submit Http Requests
submitpost()