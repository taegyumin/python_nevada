# API/Bizmoney.py
`Bizmoney.py`는 `광고시스템 > 비즈머니`의 기능들을 담고 있습니다.

### Bizmoney 객체 생성하기
	from nevada.API.Bizmoney import *
	
	base_url = 'https://api.naver.com' #그대로 두세요.
	    
	api_key = "Naver-search_AD_ACCESS_LICCENSE" #변경하세요.
	secret_key = "Naver-search_AD_SECRET_KEY" #변경하세요.
	customer_id = "Naver-search_AD_CUSTOMER_ID" #변경하세요.
	    
	bizmoney = Bizmoney(base_url=base_url, api_key=api_key, secret_key=secret_key, customer_id=customer_id)
    
### 비즈머니 잔액 조회하기
#### 코드 예시
	result = bizmoney.get()
    result_obj = CommonFunctions.json_to_object(result, BizmoneyObject)

    CommonFunctions.print_all_attr(result_obj)
	
#### 결과 예시
	bizmoney : 1000
    budgetLock : False
    customerId : 1839303
    refundLock : False
	

#### 변수 설명
    customerId : 고객의 고유 ID, bizmoney : 가지고 있는 비즈머니 잔액
    budgetLock : 예산 잠금 여부, refundLock : 환불 잠금 여부 
    