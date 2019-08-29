import sys
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime


# your personal codes goes here:
visaCodes = ({
    'number': 1111,
    'code': 'ZM',
    'desc': 'Residency permit'
}, {
    'number': 1111,
    'code': 'ZM',
    'desc': 'Change of employer'
}, {
    'number': 1111,
    'code': 'DP',
    'desc': 'Familiar reunion'
})

cookies = {
    'has_js': '1',
    '_ga': 'GA1.2.1238708695.1565628710',
    '_gid': 'GA1.2.1827596386.1566819042',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'https://frs.gov.cz',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Sec-Fetch-Site': 'same-origin',
    'Referer': 'https://frs.gov.cz/en/ioff/application-status',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'es,en-US;q=0.9,en;q=0.8',
}

data = {
    'ioff_application_number': '',
    'ioff_application_code': '',
    'ioff_application_year': '2019',
    'ioff_zov': '',
    'op': 'Verify',
    'form_build_id': 'form-2ZPcQLOxOV0Eg4RqwLOHdSOXUccYNre-lZ8Lkdt4WOc',
    'form_id': 'ioff_application_status_form'
}

for code in visaCodes:
    data['ioff_application_number'] = code['number']
    data['ioff_application_code'] = code['code']
    response = requests.post('https://frs.gov.cz/en/ioff/application-status', headers = headers, cookies = cookies, data = data)
    soup = BeautifulSoup(response.content, features = "html.parser")
    cssSelector = "body > div.main-container.container > div > section > div.alert.alert-block.alert-success.messages.status > ul > li:nth-child(1) > p > span > strong"

    res = soup.select(cssSelector)[0]
    code['status'] = res.text
    code['datetime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    print(json.dumps(code))

sys.exit(1)
