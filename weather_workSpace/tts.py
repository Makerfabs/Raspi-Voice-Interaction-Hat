import requests
import base64
import socket
import socks
import json

api_key = "AIzaSyBePoKOzQjLmB2rPJ-d9U-Cb1gDb5ynW5Y"

def SaveToTxt(file, data):
    fout = open(file, 'w')
    fout.write(data)
    fout.close()

def Base64_to_output(txt, output_file):
    fin = open(txt, 'r')
    base64_data = fin.read()
    fin.close()
    ori_image_data = base64.b64decode(base64_data)
    fout = open(output_file, 'wb')
    fout.write(ori_image_data)
    fout.close()

def TTS():
    f_text = open("./response1.txt",'r')
    json_str = f_text.read()
    f_text.close()
    data_text = json.loads(json_str)
    data_wea = data_text['weather'][0]['main']
    #data_wea1 = eval(data_wea)

    f_text_add = open("./address.txt",'r')
    data_add = f_text_add.read()
    f_text_add.close()

    text = "Hello.The weather in "+data_add+"is"+str(data_wea)+", the highest temperature is "+str(data_text['main']['temp_max'])+"degrees Celsius,the lowest is "+ str(data_text['main']['temp_min'])+"degrees Celsius,humidity is "+ str(data_text['main']['humidity'])+"%,wind speed is "+str(data_text['wind']['speed'])+"km/h. the broadcast ends. Good mood a day."
    data = """
        {
            "input": {
                "text": "
                """+ text +"""
                "
            },
            "voice": {
                "languageCode": "en-gb",
                "name": "en-GB-Standard-A",
                "ssmlGender": "FEMALE"
            },
            "audioConfig": {
                "audioEncoding": "MP3",
                "speakingRate": 0.7
            }
        }
    """
    headers = {'content-type': 'application/json'}

    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
    socket.socket = socks.socksocket
    
    r = requests.post(
        'https://texttospeech.googleapis.com/v1/text:synthesize?key='+api_key, data=data, headers=headers)
    #print(r.text)

    r_list = eval(r.text)

    #print(r_list["audioContent"])

    SaveToTxt("./tts_response.txt", str(r_list))
    SaveToTxt("./temp.txt", r_list["audioContent"])
    Base64_to_output("./temp.txt", "./output.mp3")

if __name__ == '__main__':
    TTS()
    # print(__name__)

