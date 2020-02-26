# API/ManagedKeyword.py
`ManagedKeyword.py`는 광고 키워드의 상세 정보를 보여줍니다. <br>

### ManagedKeyword 객체 생성하기
	from nevada.API.ManagedKeyword import *
	
	base_url = "https://api.naver.com" #그대로 두세요.
	api_key = "Naver-search_AD_ACCESS_LICCENSE" #변경하세요.
	secret_key = "Naver-search_AD_SECRET_KEY" #변경하세요.
	customer_id = "Naver-search_AD_CUSTOMER_ID" #변경하세요.
	
	mk = ManagedKeyword(base_url=base_url, api_key=api_key, secret_key=secret_key, customer_id=customer_id)

### 키워드 정보 조회하기
#### 코드 예시
    keywords = ['스테인레스빨대', '종이빨대']
    result_list = mk.list_by_keywords(keywords, format=True)
    for result in result_list:
        CommonFunctions.print_all_attr(result)

#### 결과 예시
	keyword : 스테인레스빨대
	managedKeyword : 
	 L  PCPLMaxDepth : 15
	 L  editTm : 2017-09-19T20:59:03.000Z
	 L  isAdult : False
	 L  isBrand : None
	 L  isLowSearchVolume : False
	 L  isRestricted : False
	 L  isSeason : False
	 L  isSellProhibit : False
	 L  keyword : 스테인레스빨대
	 L  regTm : 2016-03-07T18:34:30.000Z
	
	keyword : 종이빨대
	managedKeyword : 
	 L  PCPLMaxDepth : 15
	 L  editTm : 2016-11-02T05:51:17.000Z
	 L  isAdult : False
	 L  isBrand : None
	 L  isLowSearchVolume : False
	 L  isRestricted : False
	 L  isSeason : False
	 L  isSellProhibit : False
	 L  keyword : 종이빨대
	 L  regTm : 2016-03-07T18:34:30.000Z