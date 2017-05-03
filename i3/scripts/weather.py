#!/usr/bin/python3
import requests
import json

city = '湘潭'


if __name__ == '__main__':
    try:
        try_count = 3
        while try_count:
            r = requests.get(
                'http://api.map.baidu.com/telematics/v3/weather?location={}&output=json&ak=SsZtFOraSSNdSkO1neEQZ3bH'.format(city))
            r.encoding = 'utf-8'
            j = json.loads(r.text)
            if j.get('error') == 0:
                for index, weather_data in enumerate(j.get('results')[0].get('weather_data')):
                    if index > 2:
                        break
                    weather=weather_data.get('weather')
                    icon=''
                    if '云' in weather:
                        icon=''
                    elif '雨' in weather:
                        icon=''
                    elif '雷' in weather:
                        icon=''
                    elif '雪' in weather:
                        icon=''
                    if index == 0:
                        print(icon, weather, weather_data.get('temperature'), end='　')
                    else:
                        print(icon, weather_data.get('temperature'), end='　')
                break
            try_count -= 1
    except Exception:
        print('获取天气失败')
