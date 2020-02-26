# API/LabelRef.py
`LabelRef.py`는 `광고관리 > 즐겨찾기`에서 광고그룹, 소재, 키워드, 확장 소재 등을 즐겨찾기에 추가하거나 목록에서 삭제하는 기능을 담고 있습니다. <br>


### LabelRef 객체 생성하기
	from nevada.API.LabelRef import *

	base_url = "https://api.naver.com" #그대로 두세요.
	api_key = "Naver-search_AD_ACCESS_LICCENSE" #변경하세요.
	secret_key = "Naver-search_AD_SECRET_KEY" #변경하세요.
	customer_id = "Naver-search_AD_CUSTOMER_ID" #변경하세요.

	lr = LabelRef(base_url=base_url, api_key=api_key, secret_key=secret_key, customer_id=customer_id)


### 광고그룹, 소재, 키워드, 확장 소재 등을 즐겨찾기에 추가하기
#### 코드 예시
**enable을 True로 설정하면 '추가하기'가 되고, False로 설정하면 삭제하기'가 된다.** <br>
editTm과 regTm은 input값으로 주지 않아도 무방하다. <br>

    result = lr.update(editTm='2020-02-10T03:14:52.000Z', customerId=1810030, enable=True, nccLabelId='lbl-a001-00-000000000106050',refId='nad-a001-01-000000086037429', refTp='AD', regTm='2020-02-10T02:48:38.000Z', format=True)
    for i in result:
        CommonFunctions.print_all_attr(i)

#### 결과 예시
	nccLabelId : lbl-a001-00-000000000106050
	customerId : 1810030
	refId : nad-a001-01-000000086037429
	refTp : AD
	enable : True
	
### 광고그룹, 소재, 키워드, 확장 소재 등을 즐겨찾기 목록에서 삭제하기
#### 코드 예시
    result = lr.update(editTm='2020-02-10T03:14:52.000Z', customerId=1810030, enable=False, nccLabelId='lbl-a001-00-000000000106050',refId='nad-a001-01-000000086037429', refTp='AD', regTm='2020-02-10T02:48:38.000Z', format=True)
    for i in result:
        CommonFunctions.print_all_attr(i)


#### 결과 예시
	nccLabelId : lbl-a001-00-000000000106050
	customerId : 1810030
	refId : nad-a001-01-000000086037429
	refTp : AD
	enable : False