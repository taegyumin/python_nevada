# API/Campaign.py

`Campaign.py`는 `광고시스템 > 광고관리 > 캠페인`의 기능을 담고 있습니다. <br>


### Campaign 객체 생성하기
	from nevada.API.ManagedKeyword import *
	
	base_url = 'https://api.naver.com' #그대로 두세요.
	api_key = "Naver-search_AD_ACCESS_LICCENSE" #변경하세요.
	secret_key = "Naver-search_AD_SECRET_KEY" #변경하세요.
	customer_id = "Naver-search_AD_CUSTOMER_ID" #변경하세요.
	
	campaign = Campaign(base_url=base_url, api_key=api_key, secret_key=secret_key, customer_id=customer_id)

### nccCampaignId로 캠페인 정보 조회하기
#### 코드 예시
	CommonFunctions.print_all_attr(campaign.get('cmp-a001-01-000000002696103', format=True))

#### 결과 예시
	campaignTp : WEB_SITE
	customerId : 1810030
	dailyBudget : 100
	delFlag : False
	deliveryMethod : STANDARD
	editTm : 2020-02-16T10:01:36.000Z
	expectCost : 0
	migType : 0
	name : python_nevada
	nccCampaignId : cmp-a001-01-000000002696103
	periodEndDt : 2020-02-22T15:00:00.000Z
	periodStartDt : 2020-02-15T15:00:00.000Z
	regTm : 2020-02-16T10:01:25.000Z
	status : ELIGIBLE
	statusReason : ELIGIBLE
	trackingMode : TRACKING_DISABLED
	trackingUrl : None
	useDailyBudget : True
	usePeriod : True
	userLock : False
	
### nccCampaignId의 list로 여러 캠페인 정보 조회하기
#### 코드 예시
    result_list = campaign.list_by_ids(['cmp-a001-01-000000002696103','cmp-a001-03-000000002696246'], format=True)
    for result in result_list:
        CommonFunctions.print_all_attr(result)
      
#### 결과 예시
	campaignTp : WEB_SITE
	customerId : 1810030
	dailyBudget : 100
	delFlag : False
	deliveryMethod : STANDARD
	editTm : 2020-02-16T10:01:36.000Z
	expectCost : 0
	migType : 0
	name : python_nevada
	nccCampaignId : cmp-a001-01-000000002696103
	periodEndDt : 2020-02-22T15:00:00.000Z
	periodStartDt : 2020-02-15T15:00:00.000Z
	regTm : 2020-02-16T10:01:25.000Z
	status : ELIGIBLE
	statusReason : ELIGIBLE
	trackingMode : TRACKING_DISABLED
	trackingUrl : None
	useDailyBudget : True
	usePeriod : True
	userLock : False
	
	campaignTp : POWER_CONTENTS
	customerId : 1810030
	dailyBudget : 100
	delFlag : False
	deliveryMethod : ACCELERATED
	editTm : 2020-02-16T11:41:27.000Z
	expectCost : 0
	migType : 0
	name : 파워컨텐츠#2
	nccCampaignId : cmp-a001-03-000000002696246
	periodEndDt : 2020-02-19T15:00:00.000Z
	periodStartDt : 2020-02-15T15:00:00.000Z
	regTm : 2020-02-16T11:41:27.000Z
	status : ELIGIBLE
	statusReason : ELIGIBLE
	trackingMode : TRACKING_DISABLED
	trackingUrl : None
	useDailyBudget : True
	usePeriod : True
	userLock : False
