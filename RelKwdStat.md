# `package` API
## RelKwdStat.py

`RelKwdStat.py`는 `광고시스템 > 도구 > 키워드 도구`의 기능들을 담고 있습니다. <br>


### RelKwdStat 객체 생성하기
	from nevada.API.RelKwdStat import *
	
	base_url = 'https://api.naver.com' #그대로 두세요.
	    
	api_key = "Naver-search_AD_ACCESS_LICCENSE" #변경하세요.
	secret_key = "Naver-search_AD_SECRET_KEY" #변경하세요.
	customer_id = "Naver-search_AD_CUSTOMER_ID" #변경하세요.
	
	rel_kwd_stat = RelKwdStat(base_url=base_url, api_key=api_key, secret_key=secret_key, customer_id=customer_id)

### 연관키워드, 월간검색수(PC/모바일), 월평균클릭수(PC/모바일) 등 구하기
#### 코드 예시
    result = rel_kwd_stat.get_json(siteId=None, biztpId=None, hintKeywords='스테인레스빨대', event=None, month=None, showDetail='1')
    print(result)

    result_list = rel_kwd_stat.get_list(siteId=None, biztpId=None, hintKeywords='스테인레스빨대', event=None, month=None, showDetail='1')

    for result in result_list:
        relKeyword = result.relKeyword  # 연관 키워드
        monthlyPcQcCnt = result.monthlyPcQcCnt  # 월간(30일) PC 검색수
        monthlyMobileQcCnt = result.monthlyMobileQcCnt  # 월간(30일) 모바일 검색수
        monthlyAvePcClkCnt = result.monthlyAvePcClkCnt  # 월평균(4주) PC 클릭수
        monthlyAveMobileClkCnt = result.monthlyAveMobileClkCnt  # 월평균(4주) 모바일 클릭수
        monthlyAvePcCtr = result.monthlyAvePcCtr  # 월평균(4주) PC 클릭률
        monthlyAveMobileCtr = result.monthlyAveMobileCtr  # 월평균(4주) 모바일 클릭률
        plAvgDepth = result.plAvgDepth  # 월평균(4주) 노출광고수
        compIdx = result.compIdx  # 경쟁정도: 높음, 중간, 낮음
        print(relKeyword, monthlyPcQcCnt, monthlyMobileQcCnt, monthlyAvePcClkCnt,
              monthlyAveMobileClkCnt, monthlyAvePcCtr, monthlyAveMobileCtr, plAvgDepth, compIdx)

#### 결과 예시
    [{'relKeyword': '스테인레스빨대', 'monthlyPcQcCnt': 550, 'monthlyMobileQcCnt': 2350, 'monthlyAvePcClkCnt': 1.3, 'monthlyAveMobileClkCnt': 0.0, 'monthlyAvePcCtr': 0.25, 'monthlyAveMobileCtr': 0.0, 'plAvgDepth': 15, 'compIdx': '높음'}, {'relKeyword': '스텐빨대', 'monthlyPcQcCnt': 480, 'monthlyMobileQcCnt': 2150, 'monthlyAvePcClkCnt': 2.0, 'monthlyAveMobileClkCnt': 6.0, 'monthlyAvePcCtr': 0.43, 'monthlyAveMobileCtr': 0.29, 'plAvgDepth': 15, 'compIdx': '높음'}, {'relKeyword': '미니화로', 'monthlyPcQcCnt': 8200, 'monthlyMobileQcCnt': 25200, 'monthlyAvePcClkCnt': 55.2, 'monthlyAveMobileClkCnt': 35.3, 'monthlyAvePcCtr': 0.75, 'monthlyAveMobileCtr': 0.15, 'plAvgDepth': 15, 'compIdx': '높음'}...생략]
    
    스테인레스빨대 550 2350 1.3 0.0 0.25 0.0 15 높음
    스텐빨대 480 2150 2.0 6.0 0.43 0.29 15 높음
    미니화로 8200 25200 55.2 35.3 0.75 0.15 15 높음
    ...
    생략
