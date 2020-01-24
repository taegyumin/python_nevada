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
	result = bizmoney.get_biz_money_json()
	print(result)
	
	result = bizmoney.get_biz_money_list()
	print('customerId: ', result.customerId)
	print('bizmoney: ', result.bizmoney)
	print('budgetLock: ', result.budgetLock)
	print('refundLock: ', result.refundLock)
	
#### 결과 예시
	{'customerId': 1810030, 'bizmoney': 1000, 'budgetLock': False, 'refundLock': False}
	
	customerId:  1810030
	bizmoney:  1000
	budgetLock:  False
	refundLock:  False
	
### 비즈머니 소진 내역 조회하기
#### 코드 예시
    result = bizmoney.get_biz_money_cost_json(statDt='20200118') # 'yyyymmdd'
    print(result)

    result_list = bizmoney.get_biz_money_cost_list(statDt='20191219') #'yyyymmdd'
    for result in result_list:
        print(result.adjustedNonRefundableAmt)
        print(result.adjustedRefundableAmt)
        print(result.customer_id)
        print(result.date)
        print(result.device)
        print(result.networkType)
        print(result.nonRefundableAmt)
        print(result.productCode)
        print(result.refundableAmt)
        
#### 결과 예시
	생략
