# nevada

##### Its English Documentation is [here](https://github.com/taegyumin/python_nevada/blob/master/README(english).md).

[<img src="https://img.shields.io/pypi/v/nevada">](https://pypi.org/project/nevada/)
[<img src="https://img.shields.io/pypi/pyversions/nevada">](https://pypi.org/project/nevada/)
[<img src="https://img.shields.io/github/license/taegyumin/python_nevada">](https://github.com/taegyumin/python_nevada/blob/master/LICENSE)

## nevada는?
nevada는 [네이버의 검색광고 API](https://github.com/naver/searchad-apidoc)를 좀 더 쉽게 사용할 수 있도록 해주는 Python 라이브러리입니다.

## 준비하기 (nevada 설치 전)
- [Python](https://www.python.org/) <br>
- [Git client](https://git-scm.com/downloads) <br>

## 설치하기
- `pip3 install nevada` <br>
- `git clone https://github.com/taegyumin/python_nevada.git` <br>

## 네이버에서 API Licnese 발급하기
nevada를 이용하기 위해서는 네이버 검색광고시스템에서 API_KEY를 발급 받아야 합니다. <br>

1. [네이버 검색광고 시스템 메인 탭](http://searchad.naver.com)에서 회원가입을 합니다.
2. [네이버 검색광고 관리 탭](http://manage.searchad.naver.com) 으로 이동합니다.
3. 사이트 내에서 도구 > API 관리 로 이동합니다.
4. API license를 발급합니다.


## 잘 설치 됐는지 확인하기
Python 파일을 만들고, 아래 코드를 실행하십시오. <br>
현재 시간이 출력되면 코드가 정상적으로 실행된 겁니다. <br>
이때, 코드에서 `api_key`, `secret_key`, `customer_id`의 값은 네이버 검색광고 시스템에서 발급 받은 값으로 변경하십시오.

	from nevada.Common.Connector import *
	
	base_url = 'https://api.naver.com'
	api_key = "Naver-search-AD_ACCESS_LICCENSE"
	secret_key = "Naver-search-AD_SECRET_KEY"
	customer_id = "Naver-search-AD_CUSTOMER_ID"

	conn = Connector(base_url, api_key, secret_key, customer_id)
	print(conn.get_datetime())
	
### 자세한 사용 방법은 [docs](https://github.com/taegyumin/python_nevada/tree/master/docs)의 설명서를 참고해주시기 바랍니다.

## update info.
### 0.x.y
- beta

### 1.0.0
- launch

### 1.0.1
- docs/BusinessChannel.md 추가
- Common/Connector.CommonFunctions.print_all_attr() 추가
- API/Estimate.get_performance_bulk_json 수정
- API/Estimate.get_performance_bulk_list 수정
