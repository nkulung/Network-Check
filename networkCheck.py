import urllib3


def internetCheck():
    http = urllib3.PoolManager()
    try:
        response = http.request('GET','http://72.14.192.0/')
        return True
    except urllib3.exceptions.ConnectionError:
        return False

def main():
    online = internetCheck()
    if online == True:
        print('*Online*')
    else:
        print('**Offline**')
main()
