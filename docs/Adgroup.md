# API/Adgroup.py
`Adgroup.py`는 `광고시스템 > 광고관리 > 광고그룹`의 기능을 담고 있습니다. <br>

### Adgroup 객체 생성하기
	from nevada.API.Adgroup import *
	
	base_url = 'https://api.naver.com' #그대로 두세요.
	api_key = "Naver-search_AD_ACCESS_LICCENSE" #변경하세요.
	secret_key = "Naver-search_AD_SECRET_KEY" #변경하세요.
	customer_id = "Naver-search_AD_CUSTOMER_ID" #변경하세요.
	
	adgroup = Adgroup(base_url=base_url, api_key=api_key, secret_key=secret_key, customer_id=customer_id)

### nccAdgroupId로 광고그룹 정보 조회하기
#### 코드 예시
    result = adgroup.get('grp-a001-01-000000014208744')
    result_obj = CommonFunctions.json_to_object(result, AdgroupObject)
    CommonFunctions.print_all_attr(result_obj)

    targets = result.targets
    for target in targets:
        CommonFunctions.print_all_attr(target)

#### 결과 예시
	adgroupAttrJson : 
	 L  campaignTp : 1
	bidAmt : 70
	budgetLock : False
	contentsNetworkBidAmt : 70
	customerId : 1810030
	dailyBudget : 100
	delFlag : False
	editTm : 2020-02-16T12:45:40.000Z
	expectCost : 0
	keywordPlusWeight : 100
	migType : 0
	mobileChannelId : bsn-a001-00-000000003334825
	mobileChannelKey : https://github.com/taegyumin/python_nevada
	mobileNetworkBidWeight : 50
	name : python_nevada_광고그룹#1
	nccAdgroupId : grp-a001-01-000000014208744
	nccCampaignId : cmp-a001-01-000000002696103
	pcChannelId : bsn-a001-00-000000003334825
	pcChannelKey : https://github.com/taegyumin/python_nevada
	pcNetworkBidWeight : 100
	regTm : 2020-02-16T10:03:34.000Z
	status : PAUSED
	statusReason : BUSINESS_CHANNEL_UNDER_REVIEW
	targets : [<nevada.API.Adgroup.target object at 0x1075c4f10>, <nevada.API.Adgroup.target object at 0x10766eb50>, <nevada.API.Adgroup.target object at 0x10680f850>, <nevada.API.Adgroup.target object at 0x1075beed0>]
	targetSummary : 
	 L  media : all
	 L  pcMobile : all
	 L  region : all
	 L  time : all
	 L  week : all
	useCntsNetworkBidAmt : False
	useDailyBudget : True
	useKeywordPlus : False
	userLock : False
	
	delFlag : False
	editTm : 2020-02-16T10:03:34.000Z
	nccTargetId : tgt-a001-01-000000135368673
	ownerId : grp-a001-01-000000014208744
	regTm : 2020-02-16T10:03:34.000Z
	target : None
	targetTp : TIME_WEEKLY_TARGET
	
	delFlag : False
	editTm : 2020-02-16T10:03:34.000Z
	nccTargetId : tgt-a001-01-000000135368674
	ownerId : grp-a001-01-000000014208744
	regTm : 2020-02-16T10:03:34.000Z
	target : None
	targetTp : REGIONAL_TARGET
	
	delFlag : False
	editTm : 2020-02-16T10:03:34.000Z
	nccTargetId : tgt-a001-01-000000135368675
	ownerId : grp-a001-01-000000014208744
	regTm : 2020-02-16T10:03:34.000Z
	target : {'type': 1, 'search': [], 'contents': [], 'white': {'media': None, 'mediaGroup': None}, 'black': {'media': None, 'mediaGroup': None}}
	targetTp : MEDIA_TARGET
	
	delFlag : False
	editTm : 2020-02-16T10:03:34.000Z
	nccTargetId : tgt-a001-01-000000135368676
	ownerId : grp-a001-01-000000014208744
	regTm : 2020-02-16T10:03:34.000Z
	target : {'pc': True, 'mobile': True}
	targetTp : PC_MOBILE_TARGET
	
### nccAdgroupId의 list로 여러 광고그룹 정보 조회하기
#### 코드 예시
    result_json = adgroup.list_by_ids(['grp-a001-01-000000014208744','grp-a001-03-000000014209115'])
    result_obj = CommonFunctions.json_to_object(result_json, AdgroupObject)
    for i in result_obj:
        CommonFunctions.print_all_attr(i)
	
#### 결과 예시
	adgroupAttrJson : 
	 L  campaignTp : 1
	bidAmt : 70
	budgetLock : False
	contentsNetworkBidAmt : 70
	customerId : 1810030
	dailyBudget : 100
	delFlag : False
	editTm : 2020-02-16T12:45:40.000Z
	expectCost : 0
	keywordPlusWeight : 100
	migType : 0
	mobileChannelId : bsn-a001-00-000000003334825
	mobileChannelKey : https://github.com/taegyumin/python_nevada
	mobileNetworkBidWeight : 50
	name : python_nevada_광고그룹#1
	nccAdgroupId : grp-a001-01-000000014208744
	nccCampaignId : cmp-a001-01-000000002696103
	pcChannelId : bsn-a001-00-000000003334825
	pcChannelKey : https://github.com/taegyumin/python_nevada
	pcNetworkBidWeight : 100
	regTm : 2020-02-16T10:03:34.000Z
	status : PAUSED
	statusReason : BUSINESS_CHANNEL_UNDER_REVIEW
	targets : None
	targetSummary : 
	 L  media : all
	 L  pcMobile : all
	 L  region : all
	 L  time : all
	 L  week : all
	useCntsNetworkBidAmt : False
	useDailyBudget : True
	useKeywordPlus : False
	userLock : False
	
	adgroupAttrJson : 
	 L  campaignTp : 3
	bidAmt : 70
	budgetLock : False
	contentsNetworkBidAmt : 70
	customerId : 1810030
	dailyBudget : 100
	delFlag : False
	editTm : 2020-02-16T11:42:14.000Z
	expectCost : 0
	keywordPlusWeight : 100
	migType : 0
	mobileChannelId : bsn-a001-00-000000003334963
	mobileChannelKey : https://blog.naver.com/wawcast
	mobileNetworkBidWeight : 60
	name : 파워컨텐츠#2_광고그룹#1
	nccAdgroupId : grp-a001-03-000000014209115
	nccCampaignId : cmp-a001-03-000000002696246
	pcChannelId : bsn-a001-00-000000003334963
	pcChannelKey : https://blog.naver.com/wawcast
	pcNetworkBidWeight : 100
	regTm : 2020-02-16T11:42:14.000Z
	status : PAUSED
	statusReason : BUSINESS_CHANNEL_UNDER_REVIEW
	targets : None
	targetSummary : 
	 L  media : all
	 L  pcMobile : all
	 L  region : partially
	 L  time : all
	 L  week : all
	useCntsNetworkBidAmt : False
	useDailyBudget : True
	useKeywordPlus : False
	userLock : False
