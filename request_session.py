import json
import re
import requests
import time


url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
url1 = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
data = {'first': 'true', 'pn': 1, 'kd': 'python'}
header = {'authority': 'www.lagou.com',
            'method': 'POST',
            'path': '/jobs/positionAjax.json?needAddtionalResult=false',
            'scheme': 'https',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'content-length': '25',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': 'JSESSIONID=ABAAAECABFAACEA3E8EC7B5E16EEF7C13D1AA3686C26505; WEBTJ-ID={}-172bc6409a55b9-031535782204aa-f7d123e-2073600-172bc6409a69d5; RECOMMEND_TIP=true; _ga=GA1.2.37138248.{}; user_trace_token=20200617154603-3d0f7689-9636-42c6-81fa-555347618c04; LGUID=20200617154603-82c45910-08a5-4a12-a52a-1004b536f412; _gid=GA1.2.1489739513.{}; index_location_city=%E5%85%A8%E5%9B%BD; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22172bc6722f1119-0f52d008627ac5-f7d123e-2073600-172bc6722f29bd%22%2C%22%24device_id%22%3A%22172bc6722f1119-0f52d008627ac5-f7d123e-2073600-172bc6722f29bd%22%7D; X_MIDDLE_TOKEN=64677523a0189c91078b75eeeeb7d505; _gat=1; PRE_UTM=; PRE_HOST=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; PRE_SITE=https%3A%2F%2Fwww.lagou.com; LGSID={}-f577ca76-fb3d-45e1-8d17-9bd40fed64bc; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=64c6af6801f49c1380488329518b29a2476fb71f29; LGRID={}-68af1cff-967d-4849-be26-4e662cb5ffc0; SEARCH_ID=ebfcacda44984965bbd794309551f370',
            'origin': 'https://www.lagou.com',
            'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
            'x-anit-forge-code': '0',
            'x-anit-forge-token': 'None',
            'x-requested-with': 'XMLHttpRequest'}

req = requests.Session()
req.get(url=url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}, timeout=3)
cookie = req.cookies
time_stamp = int(time.time())
time_convert = time.strftime('%Y%m%d%H%M%S', time.localtime(time_stamp))
header['cookie'] = header['cookie'].format(time_convert, time_stamp, time_stamp, time_convert, time_convert)
src_data = req.post(url=url1, data=json.dumps(data), headers=header, cookies=cookie, timeout=3).text



print(src_data)