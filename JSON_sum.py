import urllib.request, urllib.parse, urllib.error
import json

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break
    print('Retrieving', address)
    uh = urllib.request.urlopen(address)
    data = uh.read()
    print( 'Retrieved',len(data),'characters')

    info = json.loads(data)
    #print(info)
    #print('User count:', len(info))
    sum=0
    for item in range(0,len(info['comments'])):
        num=info['comments'][item]['count']
        #print(num)
        sum+=(num)

    print(sum)
