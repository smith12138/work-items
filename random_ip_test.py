
import requests
import MySQLdb
import re

addr_url = 'https://tool.chinaz.com/iframe.ashx?t=port&callback=jQuery111302610836775993395_1595581198586'

header = {
    "Cookie": "qHistory=aHR0cDovL3Rvb2wuY2hpbmF6LmNvbS9wb3J0L1/nq6/lj6Pmiavmj48=",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}

def get_random_ip():
    conn = MySQLdb.connect(host='google.weyey.com', user='root', db='ip_proxy', passwd='tanling', charset='utf8')
    cursor = conn.cursor()
    cursor.execute('''select ip from git_jhao_proxy order by rand() limit 1''')
    for i in cursor.fetchall():
        ip = i[0]
    return ip

def check_prot():
    ip = get_random_ip()
    port = re.findall(':(\d+)', ip)[0]
    ip = re.findall('(.+):', ip)[0]
    data = {
        "host": ip,
        "port": port,
        "encode": "BJc|7gS0UddxJTmdYux9iGYUpTI0BRWl"
    }
    result = requests.post(url=addr_url, headers=header, data=data).text
    if '关闭' in result:
        print('fail')
    if '开启' in result:
        print('success:{}'.format(ip + ':' + port))


while True:
    check_prot()

