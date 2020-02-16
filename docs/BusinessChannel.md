# API/BusinessChannel.py

`BusinessChannel.py`는 `광고시스템 > 도구 > 비즈채널 관리`의 기능들을 담고 있습니다. <br>

### BusinessChannel 객체 생성하기
	from nevada.API.BusinessChannel import *
	
	base_url = 'https://api.naver.com' #그대로 두세요.
	api_key = "Naver-search_AD_ACCESS_LICCENSE" #변경하세요.
	secret_key = "Naver-search_AD_SECRET_KEY" #변경하세요.
	customer_id = "Naver-search_AD_CUSTOMER_ID" #변경하세요.
	
	bc = BusinessChannel(base_url=base_url, api_key=api_key, secret_key=secret_key, customer_id=customer_id)

### 비즈니스 채널 전체 조회하기
#### 코드 예시
    result = bc.get_business_channel_all_json()
    print(result, end='\n\n')

    result_list = bc.get_business_channel_all_list()
    for result in result_list:
        CommonFunctions.print_all_attr(result) 
       
#### 결과 예시
	[{'nccBusinessChannelId': 'bsn-a001-00-000000003298108', 'customerId': 1839303, 'channelTp': 'SITE', 'name': 'nevada', 'channelKey': 'https://github.com/taegyumin/python_nevada', 'businessInfo': {'site': 'https://github.com/taegyumin/python_nevada', 'isNaverPay': 0, 'isMobileNaverPay': 0, 'isStoreFarm': 0, 'isNaverLogin': 0, 'isMobileNaverLogin': 0, 'isNaverTalkTalk': 0, 'isMobileNaverTalkTalk': 0, 'useSaNaScript': 0, 'useNaverPayNaScript': 0, 'useStoreFarmNaScript': 0, 'naAccountId': '', 'naAccountType': 0, 'mobileCertStatus': 20, 'isMedical': 0, 'inspectId': '', 'inspectPw': ''}, 'delFlag': False, 'regTm': '2020-02-08T10:37:41.000Z', 'editTm': '2020-02-15T10:46:36.000Z', 'firstChargeTm': '2020-02-15T11:19:32.000Z', 'inspectTm': '2020-02-10T06:32:01.000Z', 'pcInspectStatus': 'PENDING', 'mobileInspectStatus': 'PENDING', 'status': 'PAUSED', 'statusReason': 'BUSINESS_CHANNEL_DISAPPROVED', 'adultStatus': 'NOT_ADULT_URL', 'enabled': True, 'blackStatus': 'WHITE_URL'}, {'nccBusinessChannelId': 'bsn-a001-00-000000003333742', 'customerId': 1839303, 'channelTp': 'CONTENTS', 'name': 'JunhoSong', 'channelKey': 'https://github.com/6-6ho', 'businessInfo': {'site': 'http://github.com/6-6ho', 'contentsUrl': 'https://github.com/6-6ho', 'contentsChannelType': 'BLOG'}, 'delFlag': False, 'regTm': '2020-02-15T10:42:48.000Z', 'editTm': '2020-02-15T10:45:53.000Z', 'firstChargeTm': '2020-02-15T11:19:32.000Z', 'inspectRequestTm': '2020-02-15T10:42:48.000Z', 'pcInspectStatus': 'UNDER_REVIEW', 'mobileInspectStatus': 'UNDER_REVIEW', 'status': 'PAUSED', 'statusReason': 'BUSINESS_CHANNEL_UNDER_REVIEW', 'adultStatus': 'NOT_ADULT_URL', 'enabled': True, 'blackStatus': 'WHITE_URL'}, {'nccBusinessChannelId': 'bsn-a001-00-000000003333743', 'customerId': 1839303, 'channelTp': 'PHONE', 'name': "Junho's_favorite_food", 'channelKey': '07070170385', 'businessInfo': {'phone': '07070170385', 'primary': None, 'secondary': None, 'countryCallingCode': '+82', 'phoneTp': 'NORMAL', 'mobileCertStatus': None}, 'delFlag': False, 'regTm': '2020-02-15T10:44:22.000Z', 'editTm': '2020-02-15T10:45:24.000Z', 'firstChargeTm': '2020-02-15T11:19:32.000Z', 'inspectTm': '2020-02-15T10:45:24.000Z', 'pcInspectStatus': 'APPROVED', 'mobileInspectStatus': 'APPROVED', 'status': 'ELIGIBLE', 'statusReason': 'ELIGIBLE', 'adultStatus': 'NOT_ADULT_URL', 'enabled': True, 'blackStatus': 'WHITE_URL'}, {'nccBusinessChannelId': 'bsn-a001-00-000000003333745', 'customerId': 1839303, 'channelTp': 'ADDRESS', 'name': '프로젝트얼스', 'channelKey': '서울특별시 성북구 성북로15길 21 (성북동)1층', 'businessInfo': {'roadNameAddress': '서울특별시 성북구 성북로15길 21 (성북동)', 'roadNameExtendAddress': '1층', 'lotNumberAddress': '서울특별시 성북구 성북동 126-31', 'lotNumberExtendAddress': '1층', 'mapZoomLevelV5': 16, 'latitude': 37.592787, 'longitude': 126.9998168, 'zipCode': '136-824', 'mapZoomLevel': 12, 'mobileCertStatus': None}, 'delFlag': False, 'regTm': '2020-02-15T10:45:17.000Z', 'editTm': '2020-02-15T10:45:24.000Z', 'firstChargeTm': '2020-02-15T11:19:32.000Z', 'inspectTm': '2020-02-15T10:45:24.000Z', 'pcInspectStatus': 'APPROVED', 'mobileInspectStatus': 'APPROVED', 'status': 'ELIGIBLE', 'statusReason': 'ELIGIBLE', 'adultStatus': 'NOT_ADULT_URL', 'enabled': True, 'blackStatus': 'WHITE_URL'}]

	adultStatus : NOT_ADULT_URL
	blackStatus : WHITE_URL
	businessInfo : 
	 L  isMobileNaverLogin : 0
	 L  isMobileNaverPay : 0
	 L  isMobileNaverTalkTalk : 0
	 L  isNaverLogin : 0
	 L  isNaverPay : 0
	 L  isNaverTalkTalk : 0
	 L  isStoreFarm : 0
	 L  mobileCertStatus : 20
	 L  naAccountId : 
	 L  naAccountType : 0
	 L  originalPath : None
	 L  site : https://github.com/taegyumin/python_nevada
	 L  thumbnailPath : None
	 L  useNaverPayNaScript : 0
	 L  useSaNaScript : 0
	 L  useStoreFarmNaScript : 0
	channelKey : https://github.com/taegyumin/python_nevada
	channelTp : SITE
	customerId : 1839303
	delFlag : False
	editTm : 2020-02-15T10:46:36.000Z
	enabled : True
	firstChargeTm : 2020-02-16T04:47:11.000Z
	inspectTm : 2020-02-10T06:32:01.000Z
	mobileInspectStatus : PENDING
	name : nevada
	nccBusinessChannelId : bsn-a001-00-000000003298108
	pcInspectStatus : PENDING
	regTm : 2020-02-08T10:37:41.000Z
	status : PAUSED
	statusReason : BUSINESS_CHANNEL_DISAPPROVED
	
	adultStatus:  NOT_ADULT_URL
	blackStatus:  WHITE_URL
	businessInfo:  
	 L  isMobileNaverLogin:  None
	 L  isMobileNaverPay::  None
	 L  isMobileNaverTalkTalk:  None
	 L  isNaverLogin:  None
	 L  isNaverPay:  None
	 L  isNaverTalkTalk:  None
	 L  isStoreFarm:  None
	 L  mobileCertStatus:  None
	 L  naAccountId:  None
	 L  naAccountType:  None
	 L  originalPath:  None
	 L  site:  http://github.com/6-6ho
	 L  thumbnailPath:  None
	 L  useNaverPayNaScript:  None
	 L  useSaNaScript:  None
	 L  useStoreFarmNaScript:  None
	channelKey:  https://github.com/6-6ho
	channelTp:  CONTENTS
	customerId:  1839303
	delFlag:  False
	editTm:  2020-02-15T10:45:53.000Z
	enabled:  True
	firstChargeTm:  2020-02-15T11:21:03.000Z
	inspectTm:  None
	mobileInspectStatus:  UNDER_REVIEW
	name:  JunhoSong
	nccBusinessChannelId:  bsn-a001-00-000000003333742
	pcInspectStatus:  UNDER_REVIEW
	regTm:  2020-02-15T10:42:48.000Z
	status:  PAUSED
	statusReason:  BUSINESS_CHANNEL_UNDER_REVIEW
	
	adultStatus:  NOT_ADULT_URL
	blackStatus:  WHITE_URL
	businessInfo:  
	 L  isMobileNaverLogin:  None
	 L  isMobileNaverPay::  None
	 L  isMobileNaverTalkTalk:  None
	 L  isNaverLogin:  None
	 L  isNaverPay:  None
	 L  isNaverTalkTalk:  None
	 L  isStoreFarm:  None
	 L  mobileCertStatus:  None
	 L  naAccountId:  None
	 L  naAccountType:  None
	 L  originalPath:  None
	 L  site:  None
	 L  thumbnailPath:  None
	 L  useNaverPayNaScript:  None
	 L  useSaNaScript:  None
	 L  useStoreFarmNaScript:  None
	channelKey:  07070170385
	channelTp:  PHONE
	customerId:  1839303
	delFlag:  False
	editTm:  2020-02-15T10:45:24.000Z
	enabled:  True
	firstChargeTm:  2020-02-15T11:21:03.000Z
	inspectTm:  2020-02-15T10:45:24.000Z
	mobileInspectStatus:  APPROVED
	name:  Junho's_favorite_food
	nccBusinessChannelId:  bsn-a001-00-000000003333743
	pcInspectStatus:  APPROVED
	regTm:  2020-02-15T10:44:22.000Z
	status:  ELIGIBLE
	statusReason:  ELIGIBLE
	
	adultStatus:  NOT_ADULT_URL
	blackStatus:  WHITE_URL
	businessInfo:  
	 L  isMobileNaverLogin:  None
	 L  isMobileNaverPay::  None
	 L  isMobileNaverTalkTalk:  None
	 L  isNaverLogin:  None
	 L  isNaverPay:  None
	 L  isNaverTalkTalk:  None
	 L  isStoreFarm:  None
	 L  mobileCertStatus:  None
	 L  naAccountId:  None
	 L  naAccountType:  None
	 L  originalPath:  None
	 L  site:  None
	 L  thumbnailPath:  None
	 L  useNaverPayNaScript:  None
	 L  useSaNaScript:  None
	 L  useStoreFarmNaScript:  None
	channelKey:  서울특별시 성북구 성북로15길 21 (성북동)1층
	channelTp:  ADDRESS
	customerId:  1839303
	delFlag:  False
	editTm:  2020-02-15T10:45:24.000Z
	enabled:  True
	firstChargeTm:  2020-02-15T11:21:03.000Z
	inspectTm:  2020-02-15T10:45:24.000Z
	mobileInspectStatus:  APPROVED
	name:  프로젝트얼스
	nccBusinessChannelId:  bsn-a001-00-000000003333745
	pcInspectStatus:  APPROVED
	regTm:  2020-02-15T10:45:17.000Z
	status:  ELIGIBLE
	statusReason:  ELIGIBLE

### channel Type으로 비즈니스 채널 조회하기
#### 코드 예시
    result_list = bc.get_business_channel_by_type_json('SITE')
    for result in result_list:
        print(result['nccBusinessChannelId'])

    print()

    result_list = bc.get_business_channel_by_type_list('SITE')
    for result in result_list:
        print(result.nccBusinessChannelId)
        
#### 결과 예시
    bsn-a001-00-000000003298108

    bsn-a001-00-000000003298108
    
    
### ids로 여러 비즈니스 채널 조회하기
#### 코드 예시
    ids = ['bsn-a001-00-000000003298108','bsn-a001-00-000000003333742']
    # result_list = bc.get_business_channel_by_ids_json(ids) 도 있음.
    result_list = bc.get_business_channel_by_ids_list(ids)
    for result in result_list:
        print(result.nccBusinessChannelId,', ',result.name)
        
#### 결과 예시
    bsn-a001-00-000000003298108 ,  nevada
    bsn-a001-00-000000003333742 ,  JunhoSong

### id로 특정 비즈니스 채널 검색하기
#### 코드 예시
	result = bc.get_business_channel_json('bsn-a001-00-000000003298108')
    print(result)
    print()
    
    result = bc.get_business_channel_list('bsn-a001-00-000000003298108')
    print(result.nccBusinessChannelId, result.name)

#### 결과 예시
	{'nccBusinessChannelId': 'bsn-a001-00-000000003298108', 'customerId': 1839303, 'channelTp': 'SITE', 'name': 'nevada', 'channelKey': 'https://github.com/taegyumin/python_nevada', 'businessInfo': {'site': 'https://github.com/taegyumin/python_nevada', 'isNaverPay': 0, 'isMobileNaverPay': 0, 'isStoreFarm': 0, 'isNaverLogin': 0, 'isMobileNaverLogin': 0, 'isNaverTalkTalk': 0, 'isMobileNaverTalkTalk': 0, 'useSaNaScript': 0, 'useNaverPayNaScript': 0, 'useStoreFarmNaScript': 0, 'naAccountId': '', 'naAccountType': 0, 'mobileCertStatus': 20, 'isMedical': 0, 'inspectId': '', 'inspectPw': ''}, 'delFlag': False, 'regTm': '2020-02-08T10:37:41.000Z', 'editTm': '2020-02-15T10:46:36.000Z', 'firstChargeTm': '2020-02-16T05:16:21.000Z', 'inspectTm': '2020-02-10T06:32:01.000Z', 'pcInspectStatus': 'PENDING', 'mobileInspectStatus': 'PENDING', 'status': 'PAUSED', 'statusReason': 'BUSINESS_CHANNEL_DISAPPROVED', 'adultStatus': 'NOT_ADULT_URL', 'enabled': True, 'blackStatus': 'WHITE_URL'}
	
    bsn-a001-00-000000003298108 nevada
    
### id로 특정 비즈니스 채널 삭제하기
#### 코드 예시
    print(len(bc.get_business_channel_all_json()))
    bc.delete_business_channel('bsn-a001-00-000000003333742')
    print(len(bc.get_business_channel_all_json()))

#### 결과 예시
    4
    failed to request
    3
    
### ids로 여러 비즈니스 채널 삭제하기
#### 코드 예시
    print(len(bc.get_business_channel_json()))
    ids = ['bsn-a001-00-000000003333743', 'bsn-a001-00-000000003333745']
    bc.delete_business_channel_by_ids(ids)
    print(len(bc.get_business_channel_json()))
    
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