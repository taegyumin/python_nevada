# API/Estimate.py

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
    result = estimate.get_avg_position_bid_json(type='keyword',device='PC',key_and_position_list=[('종이빨대',15),('스테인레스빨대',3)])
    print(result)

    result_list = estimate.get_avg_position_bid_list(type='keyword',device='PC',key_and_position_list=[('종이빨대',15),('스테인레스빨대',3)])
    for result in result_list:
        keyword = result.keyword
        position = result.position
        bid = result.bid
        print(keyword, position, bid)

#### 결과 예시
	[{'bid': 380, 'keyword': '종이빨대', 'position': 15}, {'bid': 310, 'keyword': '스테인레스빨대', 'position': 3}]
	
	종이빨대 15 380
	스테인레스빨대 3 310
    
### exposure minimum bid (광고 노출을 위한 최소 입찰가) 구하기
#### 코드 예시
    result = estimate.get_exposure_mini_bid_json(type='keyword', device='PC',  period='DAY', keys=['종이빨대','스테인레스빨대','옥수수빨대'])
    print(result)
    
	result_list = estimate.get_exposure_mini_bid_list(type='keyword', device='PC',  period='DAY', keys=['종이빨대','스테인레스빨대','옥수수빨대'])
	for result in result_list:
		keyword = result.keyword
		bid = result.bid
		print(keyword, bid)
		
#### 결과 예시
	[{'bid': 420, 'keyword': '종이빨대'}, {'bid': 80, 'keyword': '스테인레스빨대'}, {'bid': 70, 'keyword': '옥수수빨대'}]
	
	종이빨대 420
	스테인레스빨대 80
	옥수수빨대 70

### median bid (입찰가 중앙값) 구하기
#### 코드 예시
    result = estimate.get_median_bid_json(type='keyword', device='MOBILE', period='MONTH', keys=['종이빨대','스테인레스빨대','옥수수빨대'])
    print(result)

    result_list = estimate.get_median_bid_list(type='keyword', device='MOBILE', period='MONTH', keys=['종이빨대','스테인레스빨대','옥수수빨대'])
    for result in result_list:
        keyword = result.keyword
        bid = result.bid
        print(keyword, bid)
    
#### 결과 예시
	[{'bid': 1610, 'keyword': '종이빨대'}, {'bid': 350, 'keyword': '스테인레스빨대'}, {'bid': 440, 'keyword': '옥수수빨대'}]
	
	종이빨대 1610
	스테인레스빨대 350
	옥수수빨대 440
 
    
### performance (예상 노출수, 예상 클릭수, 예상 평균클릭비용, 예상 비용) 구하기
#### 코드 예시
    result = estimate.get_performance_json(type='keyword', device='BOTH', keywordplus=False, key='종이빨대', bids=[100, 200, 300])
    print(result)

    result_list = estimate.get_performance_list(type='keyword', device='BOTH', keywordplus=False, key='종이빨대', bids=[100, 200, 300])
    for result in result_list:
        keyword = '종이빨대'
        bid = result.bid #입찰가
        impressions = result.impressions #예상 노출수
        clicks = result.clicks  # 예상 클릭수
        cost = result.cost  # 예상 비용
        cost_per_click = int(cost / clicks)  # 예상 평균클릭비용
        print(bid, impressions, clicks, cost, cost_per_click)

#### 결과 예시
	[{'bid': 100, 'clicks': 2, 'impressions': 538, 'cost': 200}, {'bid': 200, 'clicks': 2, 'impressions': 1502, 'cost': 400}, {'bid': 300, 'clicks': 3, 'impressions': 2373, 'cost': 893}]
	
	종이빨대 100 538 2 200 100
	종이빨대 200 1502 2 400 200
	종이빨대 300 2373 3 893 297
        