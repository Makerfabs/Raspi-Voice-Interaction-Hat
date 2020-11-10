import requests
import socket
import socks
import json

address = ["Beijing","Moscow","London","Chicago","Rome","Singapore","Hong Kong","Taiwan","Tokyo","Seoul","Paris","New York","Washington","Sydney"]

file1 = open("./response.txt",'r')
res_data = file1.read()
file1.close()
for str1 in address :
    if res_data.find(str1)>0 :
        wea_add = str1
        break
    else :
        wea_add = "London"

file2 = open("./address.txt",'w')
file2.write(wea_add)
file2.close()

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"lang":"en","units":"metric","q":wea_add}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "47313e7efamshc596ab4201dc763p1c4275jsn3cdf6312f886"
    }

socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
socket.socket = socks.socksocket

response = requests.request("GET", url, headers=headers, params=querystring)

#print(response1.text)



fout = open("./response1.txt","w")
fout.write(response.text)
fout.close()

