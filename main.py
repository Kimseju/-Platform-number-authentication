import requests

api_key = ''  # SMSActivate에서 발급받은 API 키를 입력하세요
service = '' # 원하는 플랫폼을 입력하세요 ( 개발자 문서 참조 )
country = '' # 원하는 국적을 입력하세요 ( 개발자 문서 참조 )
operator = 'any' # 수정해도되고 안해도됩니다.

response = requests.post(f'https://sms-activate.org/stubs/handler_api.php?api_key={api_key}&action=getNumber&service={service}&forward=0&operator={operator}&ref=8402794&country={country}&maxPrice=maxPrice&verification=False&useCashBack=True')
id = response.text.split(':')[1]
number = response.text.split(':')[2]
print(number, id)

b = requests.get(f'https://api.sms-activate.io/stubs/handler_api.php?api_key={api_key}&action=getStatus&id={id}').text
if 'STATUS_WAIT_CODE' in b:
    print('인증코드를 기다리는중입니다.')
elif 'STATUS_CANCEL' in b:
    print('취소된 번호입니다')
elif 'STATUS_OK' in b:
    sms = b.split(':')[1]
    print(sms)
