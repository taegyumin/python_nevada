# API/BusinessChannel.py
`BusinessChannel.py`는 `광고시스템 > 도구 > 비즈채널 관리`의 기능들을 담고 있습니다. <br>

### BusinessChannel 객체 생성하기
	from nevada.API.BusinessChannel import *
	
	base_url = 'https://api.naver.com' #그대로 두세요.
	api_key = "Naver-search_AD_ACCESS_LICCENSE" #변경하세요.
	secret_key = "Naver-search_AD_SECRET_KEY" #변경하세요.
	customer_id = "Naver-search_AD_CUSTOMER_ID" #변경하세요.
	
	bc = BusinessChannel(base_url=base_url, api_key=api_key, secret_key=secret_key, customer_id=customer_id)
	
### 비즈니스 채널 아이디로 조회하기
#### 코드 예시
    result_json = bc.get('bsn-a001-00-000000003298108')
    result_obj = CommonFunctions.json_to_object(result_json, BusinessChannelObject)
    for i in result_obj:
        CommonFunctions.print_all_attr(i)

       
#### 결과 예시

    adultStatus : NOT_ADULT_URL
    blackStatus : WHITE_URL
    businessInfo : 
      L isMobileNaverLogin : 0
      L isMobileNaverPay : 0
      L isMobileNaverTalkTalk : 0
      L isNaverLogin : 0
      L isNaverPay : 0
      L isNaverTalkTalk : 0
      L isStoreFarm : 0
      L mobileCertStatus : 20
      L naAccountId : 
      L naAccountType : 0
      L originalPath : None
      L site : https://github.com/taegyumin/python_nevada
      L thumbnailPath : None
      L useNaverPayNaScript : 0
      L useSaNaScript : 0
      L useStoreFarmNaScript : 0
    channelKey : https://github.com/taegyumin/python_nevada
    channelTp : SITE
    customerId : 1839303
    delFlag : False
    editTm : 2020-02-15T10:46:36.000Z
    enabled : True
    firstChargeTm : 2020-07-05T05:33:00.000Z
    inspectTm : 2020-02-10T06:32:01.000Z
    mobileInspectStatus : PENDING
    name : nevada
    nccBusinessChannelId : bsn-a001-00-000000003298108
    pcInspectStatus : PENDING
    regTm : 2020-02-08T10:37:41.000Z
    status : PAUSED
    statusReason : BUSINESS_CHANNEL_DISAPPROVED


### 비즈니스 채널 전체 조회하기
#### 코드 예시
    result_json = bc.list()
    result_obj = CommonFunctions.json_to_object(result_json, BusinessChannelObject)
    for i in result_obj:
        CommonFunctions.print_all_attr(i)

       
#### 결과 예시

    adultStatus : NOT_ADULT_URL
    blackStatus : WHITE_URL
    businessInfo : 
      L isMobileNaverLogin : 0
      L isMobileNaverPay : 0
      L isMobileNaverTalkTalk : 0
      L isNaverLogin : 0
      L isNaverPay : 0
      L isNaverTalkTalk : 0
      L isStoreFarm : 0
      L mobileCertStatus : 20
      L naAccountId : 
      L naAccountType : 0
      L originalPath : None
      L site : https://github.com/taegyumin/python_nevada
      L thumbnailPath : None
      L useNaverPayNaScript : 0
      L useSaNaScript : 0
      L useStoreFarmNaScript : 0
    channelKey : https://github.com/taegyumin/python_nevada
    channelTp : SITE
    customerId : 1839303
    delFlag : False
    editTm : 2020-02-15T10:46:36.000Z
    enabled : True
    firstChargeTm : 2020-07-03T10:58:00.000Z
    inspectTm : 2020-02-10T06:32:01.000Z
    mobileInspectStatus : PENDING
    name : nevada
    nccBusinessChannelId : bsn-a001-00-000000003298108
    pcInspectStatus : PENDING
    regTm : 2020-02-08T10:37:41.000Z
    status : PAUSED
    statusReason : BUSINESS_CHANNEL_DISAPPROVED

### channel Type으로 비즈니스 채널 조회하기
#### 코드 예시
    result_json = bc.list_by_channel_type('SITE')
    for result in result_json:
        print(result['nccBusinessChannelId'])
        
#### 결과 예시
    bsn-a001-00-000000003298108
    
    
### ids로 여러 비즈니스 채널 조회하기
#### 코드 예시
    ids = ['bsn-a001-00-000000003298108','bsn-a001-00-000000003333742']
    result_list = bc.list_by_ids(ids)
    for result in result_list:
        print(result.nccBusinessChannelId,', ',result.name) // ?
        
#### 결과 예시
    bsn-a001-00-000000003298108 ,  nevada
    bsn-a001-00-000000003333742 ,  JunhoSong

### id로 특정 비즈니스 채널 삭제하기
#### 코드 예시
    print(len(bc.list()))
    bc.delete('bsn-a001-00-000000003333742')
    print(len(bc.list())) // ?

#### 결과 예시
    4
    failed to request
    3
    
### ids로 여러 비즈니스 채널 삭제하기
#### 코드 예시
    print(len(bc.list()))
    ids = ['bsn-a001-00-000000003333743', 'bsn-a001-00-000000003333745']
    bc.delete_by_ids(ids)
    print(len(bc.list()))  // ?
    
#### 결과 예시
    3
    failed to request
    1
    
### 비즈니스 채널 생성하기
#### 코드 예시
	추후 추가
#### 결과 예시
	추후 추가

### 비즈니스 채널 업데이트하기
#### 코드 예시
	추후 추가
#### 결과 예시
	추후 추가
	