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
    result = label.get_label_json()
    print(result, "\n")
    
    result_list = label.get_label_list()
    for i in result_list:
        CommonFunctions.print_all_attr(i) # from nevada.Common.Connector import * 를 해줘야 함.

#### 결과 예시
    [{'nccLabelId': 'lbl-a001-00-000000000106051', 'customerId': 1839303, 'name': 'RED', 'color': '#E65050', 'editTm': '2020-02-10T03:56:14.000Z', 'regTm': '2020-02-10T02:51:15.000Z'}, {'nccLabelId': 'lbl-a001-00-000000000106052', 'customerId': 1839303, 'name': 'ORANGE', 'color': '#E6A050', 'regTm': '2020-02-10T02:51:23.000Z'}, {'nccLabelId': 'LABEL-3', 'customerId': 1839303, 'name': 'label-3', 'color': '#CCCC04'}, {'nccLabelId': 'LABEL-4', 'customerId': 1839303, 'name': 'label-4', 'color': '#5DD47D'}, {'nccLabelId': 'LABEL-5', 'customerId': 1839303, 'name': 'label-5', 'color': '#1ABA3D'}, {'nccLabelId': 'LABEL-6', 'customerId': 1839303, 'name': 'label-6', 'color': '#4887E0'}, {'nccLabelId': 'LABEL-7', 'customerId': 1839303, 'name': 'label-7', 'color': '#6C58C7'}, {'nccLabelId': 'LABEL-8', 'customerId': 1839303, 'name': 'label-8', 'color': '#CF81D6'}, {'nccLabelId': 'LABEL-9', 'customerId': 1839303, 'name': 'label-9', 'color': '#8C8C9D'}, {'nccLabelId': 'LABEL-10', 'customerId': 1839303, 'name': 'label-10', 'color': '#FF5959'}]
    
    color : #E65050
    customerId : 1839303
    editTm : 2020-02-11T00:42:21.000Z
    name : BLUE
    nccLabelId : lbl-a001-00-000000000106051
    regTm : 2020-02-10T02:51:15.000Z
    
    color : #E6A050
    customerId : 1839303
    editTm : None
    name : ORANGE
    nccLabelId : lbl-a001-00-000000000106052
    regTm : 2020-02-10T02:51:23.000Z
    
    color : #CCCC04
    customerId : 1839303
    editTm : None
    name : label-3
    nccLabelId : LABEL-3
    regTm : None
    
    ...
    생략
    
   
### 즐겨찾기 데이터 업데이트
즐겨찾기 데이터를 수정할 때는 주의할 점이 있다. <br> 네이버 광고 시스템에서 즐겨찾기 기능을 처음 사용하는 경우, 즐겨찾기 데이터 업데이트를 하기 전에 먼저 해줘야 할 작업이 있다. <br> 네이버 광고 시스템 사이트에 들어가서 데이터를 업데이트할 즐겨찾기의 이름을 직접 변경해준다. <br> 예를 들어, '즐겨찾기-1'을 'RED'로 변경해주는 것이다. <br> 이래야 **nccLabelId**이 부여가 되며, 즐겨찾기 데이터 업데이트가 가능해진다. <br> 위의 **즐겨찾기 관련 데이터 구하기**의 **결과 예시**를 보면, RED와 ORANGE라는 이름의 즐겨찾기는 **nccLabelId**가 부여돼 있지만, 나머지는 **LABEL-n**꼴임을 확인할 수 있다.

#### 코드 예시
    result = label.update_label(color="#E65050", name="BLUE", nccLabelId="lbl-a001-00-000000000106051")
    print(result.color, result.customerId, result.name, result.nccLabelId, result.regTm, result.editTm)
    
#### 결과 예시
원래 **RED**였던 즐겨찾기가 **BLUE**로 이름이 변경된 것을 확인할 수 있다.

	#E65050 1839303 BLUE lbl-a001-00-000000000106051 2020-02-10T02:51:15.000Z 2020-02-10T03:58:26.000Z
	
#### 변수 설명
    color : 즐겨찾기의 색, customer_id : 고객 ID, name : 즐겨찾기의 이름
    nccLabelId : 즐겨찾기의 ID, regTm : 즐겨찾기가 생성 된 시간, editTm : 즐겨찾기가 수정 된 시간