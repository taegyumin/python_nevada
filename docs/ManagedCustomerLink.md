# API/ManagedCustomerLink.py
`ManagedCustomerLink.py`는 광고와 연동된 고객(Client)와 매니저(Manager)에 대한 정보를 조회하는 기능을 담고 있습니다. <br>


### ManagedCustomerLink 객체 생성하기
	from nevada.API.ManagedCustomerLink import *
	
	base_url = "https://api.naver.com" #그대로 두세요.
	api_key = "Naver-search_AD_ACCESS_LICCENSE" #변경하세요.
	secret_key = "Naver-search_AD_SECRET_KEY" #변경하세요.
	customer_id = "Naver-search_AD_CUSTOMER_ID" #변경하세요.
	
	mcl = ManagedCustomerLink(base_url=base_url, api_key=api_key, secret_key=secret_key, customer_id=customer_id)

### Customer 정보 조회하기: Clients
#### 코드 예시
    result_json = mcl.list(rel_type='MYCLIENTS')
    result_obj = CommonFunctions.json_to_object(result_json, ManagedCustomerLinkObject)
    for i in result_obj:
        CommonFunctions.print_all_attr(result_obj)

#### 결과 예시
	생략
	
### Customer 정보 조회하기: Managers
#### 코드 예시
    result_json = mcl.list(rel_type='MYMANAGERS')
    result_obj = CommonFunctions.json_to_object(result_json, ManagedCustomerLinkObject)
    for i in result_obj:
        CommonFunctions.print_all_attr(result_obj)

#### 결과 예시
	생략