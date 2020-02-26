# API/MasterReport.py
`MasterReport.py`는 `광고시스템 > 보고서 > 대용량 다운로드 보고서 > 광고 정보 일괄 다운로드`의 기능을 담고 있습니다. <br>


### MasterReport 객체 생성하기
	from nevada.API.MasterReport import *
	
	base_url = "https://api.naver.com" #그대로 두세요.
	api_key = "Naver-search_AD_ACCESS_LICCENSE" #변경하세요.
	secret_key = "Naver-search_AD_SECRET_KEY" #변경하세요.
	customer_id = "Naver-search_AD_CUSTOMER_ID" #변경하세요.
	
	mr = MasterReport(base_url=base_url, api_key=api_key, secret_key=secret_key, customer_id=customer_id)

### 전체 보고서 조회하기
#### 코드 예시
    result_list = mr.list(format=True)
    for result in result_list:
        CommonFunctions.print_all_attr(result)
#### 결과 예시
	clientCustomerId : 1810030
	downloadUrl : https://api.naver.com/report-download?authtoken=%2BqBt0DaxMbSCE70atv7huhbX7uVKpcq7YouDZyoGTR1bBZpsHVKhw9sEb8vHbg%2Bu4c%2F6s1ccsBJzoNijefHAxHEW6jv1WoYUqY9ZuXlvZ5k%3D
	fromTime : 2020-01-19T00:00:00Z
	id : C36E0BF666873E000416E1E03DFE0ACA
	item : Adgroup
	managerCustomerId : 1810030
	managerLoginId : 생략:naver
	registTime : 2020-02-18T12:15:58.926Z
	status : BUILT
	updateTime : 2020-02-18T12:14:00Z
	
	clientCustomerId : 1810030
	downloadUrl : https://api.naver.com/report-download?authtoken=%2BqBt0DaxMbSCE70atv7huhbX7uVKpcq7YouDZyoGTR1bBZpsHVKhw5OXBFwoPJdNvTC%2B3SXUIWlHDAFu%2FgV1JSWSRQ2hCONHC31%2FE1V8V1k%3D
	fromTime : 2020-01-18T00:00:00Z
	id : D11B66049497097628086B3F43B25F8F
	item : Adgroup
	managerCustomerId : 1810030
	managerLoginId : 생략:naver
	registTime : 2020-02-18T12:16:01.630Z
	status : BUILT
	updateTime : 2020-02-18T12:15:00Z
	
	clientCustomerId : 1810030
	downloadUrl : https://api.naver.com/report-download?authtoken=%2BqBt0DaxMbSCE70atv7huhbX7uVKpcq7YouDZyoGTR1bBZpsHVKhw9tj%2F3OuQu5aT1ib0jAUVKCFtGUmSmbli2yVdhHMpqLkvTuZ38IePJQ%3D
	fromTime : 2020-01-17T00:00:00Z
	id : 36FCD4BC49A88CB3116506C25396249F
	item : Adgroup
	managerCustomerId : 1810030
	managerLoginId : 생략:naver
	registTime : 2020-02-18T12:16:03.475Z
	status : BUILT
	updateTime : 2020-02-18T12:15:00Z


### 특정 Id에 대한 보고서 조회하기
#### 코드 예시
    result = mr.get_by_id('C36E0BF666873E000416E1E03DFE0ACA', format=True)
    CommonFunctions.print_all_attr(result)
#### 결과 예시
	clientCustomerId : 1810030
	downloadUrl : https://api.naver.com/report-download?authtoken=D9DKMTJIxDK9gFCaHJuB5wgwuc%2F9jpctuWIh24fnBY%2FY2Wh0gKXXdiEWuf7xKJH4Lc9d%2BOh%2FrUMiDnBfEbO8sRNqsA3UnXFheItayEA2wEo%3D
	fromTime : 2020-01-19T00:00:00Z
	id : C36E0BF666873E000416E1E03DFE0ACA
	item : Adgroup
	managerCustomerId : 1810030
	managerLoginId : mtg0821:naver
	registTime : 2020-02-18T12:15:58.926Z
	status : BUILT
	updateTime : 2020-02-18T12:14:00Z


### 보고서 생성하기
#### 코드 예시
    result = mr.create(item='Adgroup', fromTime="2020-01-15", format=True)
    CommonFunctions.print_all_attr(result)
#### 결과 예시
	clientCustomerId : 1810030
	downloadUrl : 
	fromTime : 2020-01-15T00:00:00Z
	id : 8F82155BC132F79B49823E8FBC09A09B
	item : Adgroup
	managerCustomerId : 1810030
	managerLoginId : mtg0821:naver
	registTime : 2020-02-18T13:02:53.569Z
	status : REGIST
	updateTime : 2020-02-18T13:01:00Z


### 특정 Id에 대한 보고서 삭제하기
#### 코드 예시
    mr.delete_by_id('8F82155BC132F79B49823E8FBC09A09B')
#### 결과 예시
생략

### 전체 보고서 삭제하기
#### 코드 예시
    mr.delete_all()
#### 결과 예시
생략


