# API/Stat.py
`Stat.py`는 `광고시스템 > 보고서 > 다차원 보고서`에서 보고서를 조회하는 기능을 담고 있습니다. <br>

### Stat 객체 생성하기
	from nevada.API.Stat import *
	
	base_url = "https://api.naver.com" #그대로 두세요.
	api_key = "Naver-search_AD_ACCESS_LICCENSE" #변경하세요.
	secret_key = "Naver-search_AD_SECRET_KEY" #변경하세요.
	customer_id = "Naver-search_AD_CUSTOMER_ID" #변경하세요.
	
	stat = Stat(base_url=base_url, api_key=api_key, secret_key=secret_key, customer_id=customer_id)

### Id로 특정 보고서 조회하기
#### 코드 예시

#### 결과 예시
생략

### Id의 list로 여러 보고서 조회하기
#### 코드 예시

#### 결과 예시
생략

### 보고서 종류(광고 정보)에 따른 보고서 조회하기
#### 코드 예시

#### 결과 예시
생략
