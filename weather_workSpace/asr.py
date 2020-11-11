import requests
import base64
#import socket
#import socks

api_key = "AIzaSyBePoKOzQjLmB2rPJ-d9U-Cb1gDb5ynW5Y"

wav_data = "//NExAAR8CIEABjGADQIAIHA3BwBg+OOMBCD8EIIOg/B+IAx/UGKj6wfeJAxE78PiDGg+8PiAEHA4Az5Q5B/BPnLxAcLn1g+fOKrDwPjgQE4Y4Z4fWyJkYZXhgEbIeaC//NExAsQkEYgAHvSJB7McDYIHT64egEXsQsH40QHS4QQjfpvqc/YhpLkwaw45LBSL0DNKBSHfxSMxcUtRaGlPKr7APoVgQKgLloRmsZx+3geY4GEAIOIxEIGhLRkBGEt//NExBsXIOI4AN5ScKajd4ah136G/GKt+xXv4VLGfzd8kUhYrRtpDiOTBGTpRnc/ZJB4nEI8CFHBGXfy5/pD8mhu727Knf/W+qD7/82ulXdRSL+mAYDBAEHg5cGLgLNd//NExBEW2RpYAO4ecE5gqChhKPpi4KQ2hv+SNKzlFT/Xsc7vV/LHLkFEsVF35LDLQ4hERlQoegm8lnrUdDqNWCr70pK3KBkxT6gTbsb89yHqZ9NH//o9St/QwVZPJvDh//NExAgUaS6MANPScPG4bZgYxAeREBxQbIbgD4F4Th7HY7METX1l/ukDZzSg4I6QAgAQUGy4Bzc1hQmT3PCAkubdCuTEEBIu+E0cgxDHg5BAEAwAwfEF/evjwhKf69na//NExA"


def ToBase64(file):
    fin = open(file, 'rb')
    wav_data = fin.read()
    base64_data = base64.b64encode(wav_data)
    fin.close()
    return str(base64_data, encoding='UTF-8')
    #return base64_data


def SaveToTxt(file, data):
    fout = open(file, 'w')
    fout.write(data)
    fout.close()

def Read_file(file):
    fout = open(file, 'r')
    data = fout.read()
    fout.close()
    return data


# ToBase64("./speak.wav")

def ASR():
    wav_data = ToBase64("./record_test1.wav")
    SaveToTxt("./base64.txt", wav_data)
    #wav_data = Read_file("./record_text.txt")

    #\"sampleRateHertz\": 16000,
    data = "{\"config\": {\"encoding\":\"LINEAR16\",\"languageCode\": \"en-US\",\"enableWordTimeOffsets\": false},\"audio\": {\"content\": \""
    data += wav_data
    data += "\"}}"
    
    SaveToTxt("./request.txt", data)
    headers = {'content-type': 'application/json'}
        
    #socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
    #socket.socket = socks.socksocket
    r = requests.post( 
        'https://speech.googleapis.com/v1/speech:recognize?key='+api_key, data=data, headers=headers)

    SaveToTxt("./response.txt", r.text)
    # print(r.text)

    #r_list = eval(r.text)

    # print(r_list["results"][0]["alternatives"][0]["transcript"])


if __name__ == '__main__':
    ASR()
    # print(__name__)
