# API/RelKwdStat.py
`RelKwdStat.py`는 `광고시스템 > 도구 > 키워드 도구`의 기능들을 담고 있습니다. <br>


### RelKwdStat 객체 생성하기
	from nevada.API.RelKwdStat import *
	
	base_url = "https://api.naver.com" #그대로 두세요.
	api_key = "Naver-search_AD_ACCESS_LICCENSE" #변경하세요.
	secret_key = "Naver-search_AD_SECRET_KEY" #변경하세요.
	customer_id = "Naver-search_AD_CUSTOMER_ID" #변경하세요.
	
	relKwdStat = RelKwdStat(base_url=base_url, api_key=api_key, secret_key=secret_key, customer_id=customer_id)
x
### 연관키워드, 월간검색수(PC/모바일), 월평균클릭수(PC/모바일) 등 구하기
#### 코드 예시
    result_json = rel_kwd_stat.list(siteId=None, biztpId=None, hintKeywords='스테인레스빨대', event=None, month=None, showDetail='1')
    result_obj = CommonFunctions.json_to_object(result_json, RelKwdStatObject)
    
    for i in result_obj:
        CommonFunctions.print_all_attr(i)

#### 결과 예시
    relKeyword : 스테인레스빨대
    monthlyPcQcCnt : 660
    monthlyMobileQcCnt : 3040
    monthlyAvePcClkCnt : 2.9
    monthlyAveMobileClkCnt : 1.3
    monthlyAvePcCtr : 0.48
    monthlyAveMobileCtr : 0.05
    plAvgDepth : 15
    compIdx : 높음
    
    relKeyword : 스텐빨대
    monthlyPcQcCnt : 410
    monthlyMobileQcCnt : 2190
    monthlyAvePcClkCnt : 1.5
    monthlyAveMobileClkCnt : 6.2
    monthlyAvePcCtr : 0.4
    monthlyAveMobileCtr : 0.31
    plAvgDepth : 15
    compIdx : 높음
    
    ...
    생략
    
#### 변수 설명
    relKeyword : 연관 키워드, monthlyPcQcCnt : 월간(30일) PC검색 수, monthlyMobileQcCnt : 월간(30일) 모바일 검색 수
    monthlyAvePcClkCnt : 월평균(4주) PC 클릭 수, monthAveMobileClkCnt : 월평균(4주) 모바일 클릭 수
    monthlyAvePcCtr : 월평균(4주) PC 클릭률, monthlyAveMobileCtr : 월평균(4주) 모바일 클릭률
    plAvgDepth : 월평균(4주) 노출광고수, compIdx : 경쟁정도(높음, 중간, 낮음)
