**# API/Estimate.py

`Estimate.py`는 `광고시스템 > 도구 > 키워드 도구 > 월간 예상 실적 보기`의 기능들을 담고 있습니다.

## Example

### Estimate 객체 생성하기
    from nevada.API.Estimate import *
    
    base_url = 'https://api.naver.com' #그대로 두세요.
    
    api_key = "Naver-search_AD_ACCESS_LICCENSE" #변경하세요.
    secret_key = "Naver-search_AD_SECRET_KEY" #변경하세요.
    customer_id = "Naver-search_AD_CUSTOMER_ID" #변경하세요.

    estimate = Estimate(base_url=base_url, api_key=api_key, secret_key=secret_key, customer_id=customer_id)
    
   
    
### average position bid (입찰가 평균) 구하기
#### 코드 예시
    result_list = estimate.get_avg_position_bid(type='keyword',device='PC',key_and_position_list=[('종이빨대',15),('스테인레스빨대',3)], format=True)
    for i in result_list:
        CommonFunctions.print_all_attr(i)  # from nevada.Common.Connector import * 를 해줘야 함.


#### 결과 예시

    bid : 330
    keyword : 종이빨대
    position : 15
    
    bid : 310
    keyword : 스테인레스빨대
    position : 3
    
### exposure minimum bid (광고 노출을 위한 최소 입찰가) 구하기
#### 코드 예시
    result_list = estimate.get_exposure_mini_bid(type='keyword', device='PC', period='DAY', keys=['종이빨대', '스테인레스빨대', '옥수수빨대'], format=True)
    for i in result_list:
        CommonFunctions.print_all_attr(i)  # from nevada.Common.Connector import * 를 해줘야 함.
		
#### 결과 예시
    
    bid : 370
    keyword : 종이빨대
    
    bid : 70
    keyword : 스테인레스빨대
    
    bid : 70
    keyword : 옥수수빨대

### median bid (입찰가 중앙값) 구하기
#### 코드 예시
    result_list = estimate.get_median_bid(type='keyword', device='MOBILE', period='MONTH', keys=['종이빨대','스테인레스빨대','옥수수빨대'], format=True)
    for i in result_list:
        CommonFunctions.print_all_attr(i)  # from nevada.Common.Connector import * 를 해줘야 함.
    
#### 결과 예시
    [{'bid': 1690, 'keyword': '종이빨대'}, {'bid': 360, 'keyword': '스테인레스빨대'}, {'bid': 300, 'keyword': '옥수수빨대'}] 
    
    bid : 1690
    keyword : 종이빨대
    
    bid : 360
    keyword : 스테인레스빨대
    
    bid : 300
    keyword : 옥수수빨대
 
    
### performance (예상 노출수, 예상 클릭수, 예상 평균클릭비용, 예상 비용) 구하기
#### 코드 예시
    
    result_list = estimate.get_performance(type='keyword', device='BOTH', keywordplus=False, key='종이빨대', bids=[100, 200, 300], format=True)
    for i in result_list:
        print("종이빨대")
        CommonFunctions.print_all_attr(i)  # from nevada.Common.Connector import * 를 해줘야 함.

#### 결과 예시

	종이빨대
	bid : 100
	clicks : 1
	cost : 88
	impressions : 642
	cost_per_click : 88
	
	종이빨대
	bid : 200
	clicks : 1
	cost : 172
	impressions : 1815
	cost_per_click : 172
	
	종이빨대
	bid : 300
	clicks : 2
	cost : 512
	impressions : 2803
	cost_per_click : 256
    
#### 변수 설명
    bid : 입찰가
    impressions : 예상 노출수
    clicks : 예상 클릭수
    cost : 예상 비용
    cost_per_click: 예상 평균클릭비용