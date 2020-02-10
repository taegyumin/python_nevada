# API/Label.py

`Label.py`는 `광고관리 > 즐겨찾기`의 기능들을 담고 있습니다. <br>


### Label 객체 생성하기
	from nevada.API.Label import *

	base_url = 'https://api.naver.com' #그대로 두세요.

	api_key = "Naver-search_AD_ACCESS_LICCENSE" #변경하세요.
	secret_key = "Naver-search_AD_SECRET_KEY" #변경하세요.
	customer_id = "Naver-search_AD_CUSTOMER_ID" #변경하세요.

	label = Label(base_url=base_url, api_key=api_key, secret_key=secret_key, customer_id=customer_id)


### 즐겨찾기 관련 데이터 구하기
#### 코드 예시
	result_list = label.get_label_list()

	for result in result_list:
	    color = result.color  # 즐겨찾기의 색
	    customer_id = result.customerId  # 고객 ID
	    name = result.name  # 즐겨찾기의 이름
	    nccLabelId = result.nccLabelId  # 즐겨찾기의 ID
	    regTm = result.regTm  # 즐겨찾기가 생성 된 시간
	    editTm = result.editTm  # 즐겨찾기가 수정 된 시간
	    print(color, customer_id, name, nccLabelId, regTm, editTm)


#### 결과 예시
	#E65050 1839303 PINK lbl-a001-00-000000000106051 2020-02-10T02:51:15.000Z 2020-02-10T03:11:08.000Z
    #E6A050 1839303 ORANGE lbl-a001-00-000000000106052 2020-02-10T02:51:23.000Z None
    #CCCC04 1839303 label-3 LABEL-3 None None
    #5DD47D 1839303 label-4 LABEL-4 None None
    #1ABA3D 1839303 label-5 LABEL-5 None None
    #4887E0 1839303 label-6 LABEL-6 None None
    #6C58C7 1839303 label-7 LABEL-7 None None
    #CF81D6 1839303 label-8 LABEL-8 None None
    #8C8C9D 1839303 label-9 LABEL-9 None None
    #FF5959 1839303 label-10 LABEL-10 None None
    
   
### 즐겨찾기 데이터 업데이트
#### 코드 예시
    updateLabelObject = UpdateLabelObject(color="#E65050", name="RED", nccLabelId="lbl-a001-00-000000000106051")
    result = label.update_label(updateLabelObject)
    print(result.color, result.customerId, result.name, result.nccLabelId, result.regTm, result.editTm)
    
#### 결과 예시
    #E65050 1839303 PINK lbl-a001-00-000000000106051 2020-02-10T02:51:15.000Z 2020-02-10T03:11:08.000Z
     -> #E65050 1839303 RED lbl-a001-00-000000000106051 2020-02-10T02:51:15.000Z 2020-02-10T03:39:18.000Z
    
