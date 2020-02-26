# API/Ad.py
`Ad.py`는 `광고시스템 > 광고관리 > 소재`의 기능을 담고 있습니다. <br>

### Ad 객체 생성하기
	from nevada.API.Ad import *
	
	base_url = "https://api.naver.com" #그대로 두세요.
	api_key = "Naver-search_AD_ACCESS_LICCENSE" #변경하세요.
	secret_key = "Naver-search_AD_SECRET_KEY" #변경하세요.
	customer_id = "Naver-search_AD_CUSTOMER_ID" #변경하세요.
	
	ad = Ad(base_url=base_url, api_key=api_key, secret_key=secret_key, customer_id=customer_id)

### nccAdId로 소재 정보 조회하기
#### 코드 예시
    CommonFunctions.print_all_attr(ad.get('nad-a001-03-000000086038948', format=True))

#### 결과 예시
	ad : 
	 L  pc_display : https://blog.naver.com/wawcast
	 L  pc_final : https://blog.naver.com/wawcast/221148564743
	 L  mobile_display : https://blog.naver.com/wawcast
	 L  mobile_final : https://blog.naver.com/wawcast/221148564743
	 L  headline : 적정기술 커뮤니티 WAW
	 L  description : 포스텍 영재기업인교육원(POSTECH CEO) 적정기술, 사회적기업 커뮤니티 WAW(We Are the World)입니다. 적정기술에 대한 소식을 확인할 수 있습니다.
	adattr : None
	customerId : 1810030
	editTm : 2020-02-16T11:47:06.000Z
	inspectRequestMsg : None
	inspectStatus : UNDER_REVIEW
	nccAdId : nad-a001-03-000000086038948
	nccAdgroupId : grp-a001-03-000000014209115
	regTm : 2020-02-16T11:47:00.000Z
	status : PAUSED
	statusReason : AD_UNDER_REVIEW
	type : CONTENTS_AD_INFORMATION
	userLock : False


### nccAdGroupId으로 해당 Adgroup에 속한 소재 정보 조회하기
#### 코드 예시
    result_list = ad.list_by_adgroup_id(nccAdGroupId='grp-a001-01-000000014208744',format=True)
    for result in result_list:
        CommonFunctions.print_all_attr(result)

#### 결과 예시
	ad : 
	 L  pc_display : https://github.com/taegyumin/python_nevada
	 L  pc_final : https://github.com/taegyumin/python_nevada
	 L  mobile_display : https://github.com/taegyumin/python_nevada
	 L  mobile_final : https://github.com/taegyumin/python_nevada
	 L  headline : python nevada
	 L  description : 네이버 검색광고 API를 쉽게 이용할 수 있도록 해주는 파이썬 라이브러리
	adattr : None
	customerId : 1810030
	editTm : 2020-02-16T10:07:10.000Z
	inspectRequestMsg : None
	inspectStatus : UNDER_REVIEW
	nccAdId : nad-a001-01-000000086037429
	nccAdgroupId : grp-a001-01-000000014208744
	regTm : 2020-02-16T10:07:10.000Z
	status : PAUSED
	statusReason : AD_UNDER_REVIEW
	type : TEXT_45
	userLock : False
	
### nccAdId의 list로 여러 소재 정보 조회하기
#### 코드 예시
    result_list = ad.list(['nad-a001-01-000000086037429','nad-a001-03-000000086038948'], format=True)
    for result in result_list:
        CommonFunctions.print_all_attr(result)
       
#### 결과 예시
	ad : 
	 L  pc_display : https://github.com/taegyumin/python_nevada
	 L  pc_final : https://github.com/taegyumin/python_nevada
	 L  mobile_display : https://github.com/taegyumin/python_nevada
	 L  mobile_final : https://github.com/taegyumin/python_nevada
	 L  headline : python nevada
	 L  description : 네이버 검색광고 API를 쉽게 이용할 수 있도록 해주는 파이썬 라이브러리
	adattr : None
	customerId : 1810030
	editTm : 2020-02-16T10:07:10.000Z
	inspectRequestMsg : None
	inspectStatus : UNDER_REVIEW
	nccAdId : nad-a001-01-000000086037429
	nccAdgroupId : grp-a001-01-000000014208744
	regTm : 2020-02-16T10:07:10.000Z
	status : PAUSED
	statusReason : AD_UNDER_REVIEW
	type : TEXT_45
	userLock : False
	
	ad : 
	 L  pc_display : https://blog.naver.com/wawcast
	 L  pc_final : https://blog.naver.com/wawcast/221148564743
	 L  mobile_display : https://blog.naver.com/wawcast
	 L  mobile_final : https://blog.naver.com/wawcast/221148564743
	 L  headline : 적정기술 커뮤니티 WAW
	 L  description : 포스텍 영재기업인교육원(POSTECH CEO) 적정기술, 사회적기업 커뮤니티 WAW(We Are the World)입니다. 적정기술에 대한 소식을 확인할 수 있습니다.
	adattr : None
	customerId : 1810030
	editTm : 2020-02-16T11:47:06.000Z
	inspectRequestMsg : None
	inspectStatus : UNDER_REVIEW
	nccAdId : nad-a001-03-000000086038948
	nccAdgroupId : grp-a001-03-000000014209115
	regTm : 2020-02-16T11:47:00.000Z
	status : PAUSED
	statusReason : AD_UNDER_REVIEW
	type : CONTENTS_AD_INFORMATION
	userLock : False
	
### 소재 업데이트하기
def update(...)

### 소재 삭제하기
def delete(...)

###소재 복사하기
def copy(...)