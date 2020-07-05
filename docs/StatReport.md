# API/StatReport.py
`StatReport.py`는 `광고시스템 > 보고서 > 대용량 다운로드 보고서 > 대용량 보고서 다운로드`의 기능을 담고 있습니다. <br>


### StatReport 객체 생성하기
	from nevada.API.StatReport import *
	
	base_url = "https://api.naver.com" #그대로 두세요.
	api_key = "Naver-search_AD_ACCESS_LICCENSE" #변경하세요.
	secret_key = "Naver-search_AD_SECRET_KEY" #변경하세요.
	customer_id = "Naver-search_AD_CUSTOMER_ID" #변경하세요.
	
	sr = StatReport(base_url=base_url, api_key=api_key, secret_key=secret_key, customer_id=customer_id)


### 보고서 생성하기
#### 코드 예시
    result_json = sr.create(reportTp='AD',statDt='2020-01-23T02:00:00Z')
    result_obj = CommonFunctions.json_to_object(result_json, StatReportObject)
    CommonFunctions.print_all_attr(result_obj)
    
    result_json = sr.create(reportTp='AD', statDt='20200123')
    result_obj = CommonFunctions.json_to_object(result_json, StatReportObject)
    CommonFunctions.print_all_attr(result_obj)
    
#### 결과 예시
	downloadUrl : 
	loginId : mtg0821:naver
	regTm : 
	reportJobId : 803874623
	reportTp : AD
	statDt : 2020-01-23T02:00:00Z
	status : REGIST
	updateTm : 
	
	downloadUrl : 
	loginId : mtg0821:naver
	regTm : 
	reportJobId : 803874623
	reportTp : AD
	statDt : 2020-01-23T02:00:00Z
	status : REGIST
	updateTm : 


### 전체 보고서 조회하기
#### 코드 예시
    result_json = sr.list()
    result_obj = CommonFunctions.json_to_object(result_json, StatReportObject)
    
    for i in result_obj:
        CommonFunctions.print_all_attr(i)
        
#### 결과 예시
	downloadUrl : 
	loginId : mtg0821:naver
	regTm : 2020-02-18T13:16:44Z
	reportJobId : 803874623
	reportTp : AD
	statDt : 2020-01-22T15:00:00Z
	status : NONE
	updateTm : 2020-01-22T15:00:00Z
	
	downloadUrl : 
	loginId : mtg0821:naver
	regTm : 2020-02-18T13:16:44Z
	reportJobId : 803874624
	reportTp : AD
	statDt : 2020-01-22T15:00:00Z
	status : NONE
	updateTm : 2020-01-22T15:00:00Z


### 특정 Id에 대한 보고서 조회하기
#### 코드 예시
    result_json = sr.get(reportJobId='803874623')
    result_obj = CommonFunctions.json_to_object(result_json, StatReportObject)
    CommonFunctions.print_all_attr(result_obj) // ?

#### 결과 예시
	downloadUrl : 
	loginId : mtg0821:naver
	regTm : 2020-02-18T13:16:44Z
	reportJobId : 803874623
	reportTp : AD
	statDt : 2020-01-22T15:00:00Z
	status : NONE
	updateTm : 2020-01-22T15:00:00Z

### 특정 Id에 대한 보고서 삭제하기
#### 코드 예시
    sr.delete_by_id('803874623')
#### 결과 예시
생략

### 전체 보고서 삭제하기
#### 코드 예시
	sr.delete_all()
#### 결과 예시
생략

