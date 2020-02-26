# API/IpExclusion.py
`IpExclusion.py`는 `광고시스템 > 도구 > 광고노출제한 관리`의 기능들을 담고 있습니다.

### IpExclusion 객체 생성하기
	from nevada.API.IpExclusion import *
	
    base_url = 'https://api.naver.com' #그대로 두세요.
    
    api_key = "Naver-search_AD_ACCESS_LICCENSE" #변경하세요.
    secret_key = "Naver-search_AD_SECRET_KEY" #변경하세요.
    customer_id = "Naver-search_AD_CUSTOMER_ID" #변경하세요.
    
    ipExclusion = IpExclusion(base_url=base_url, api_key=api_key, secret_key=secret_key, customer_id=customer_id)
    
    
### 광고노출제한 IP 조회하기
#### 코드 예시
	result_list = ipExclusion.get(format=True)
	for i in result_list:
        CommonFunctions.print_all_attr(i) # from nevada.Common.Connector import * 를 해줘야 함.
	    
#### 결과 예시 

    customerId : 1839303
    filterIp : 111.111.111.112
    ipFilterId : 6777029
    memo : 테스트2
    regTm : 1581829891000
    
    customerId : 1839303
    filterIp : 111.111.111.111
    ipFilterId : 6776978
    memo : 테스트
    regTm : 1581828179000

        
### 광고노출제한 IP 추가하기
#### 코드 예시
    result = ipExclusion.create(filterIp='111.111.111.113', memo='추가 된 IP', format=True)
    
    print('customer_id :', result.customerId)
    print('filterIp :', result.filterIp)
    print('ipFilterId :', result.ipFilterId)
    print('memo :', result.memo)
    print('regTm :', result.regTm)

#### 결과 예시
    customer_id : 1839303
    filterIp : 111.111.111.113
    ipFilterId : 6777032
    memo : 추가 된 IP
    regTm : 1581829961200
    
### 광고노출제한 IP 수정하기
#### 코드 예시
    result = ipExclusion.update(filterIp='111.111.111.113', ipFilterId='6777032', memo='변경 된 메모', format=True)
    
    print('customer_id :', result.customerId)
    print('filterIp :', result.filterIp)
    print('ipFilterId :', result.ipFilterId)
    print('memo :', result.memo)
    print('regTm :', result.regTm)
    
#### 결과 예시
    customer_id : 1839303
    filterIp : 111.111.111.113
    ipFilterId : 6777032
    memo : 변경 된 메모
    regTm : 1581829961000
    

### 광고노출제한 IP 삭제하기
#### 코드 예시
    ipExclusion.delete(id='6777032')

	result_list = ipExclusion.get(format=True)
	for i in result_list:
        CommonFunctions.print_all_attr(i) # from nevada.Common.Connector import * 를 해줘야 함.


#### 결과 예시
memo가 '변경 된 메모'였던 ip주소가 목록에서 삭제된 것을 확인할 수 있다.

    customerId : 1839303
    filterIp : 111.111.111.112
    ipFilterId : 6777029
    memo : 테스트2
    regTm : 1581829891000
    
    customerId : 1839303
    filterIp : 111.111.111.111
    ipFilterId : 6776978
    memo : 테스트
    regTm : 1581828179000
    
    
### 광고노출제한 IP 여러 개 한꺼번에 삭제하기
#### 코드 예시
**ipFilterId**의 list를 구성한다.

    id_array = ['6777029', '6776978']
    
    ipExclusion.delete_by_ids(id_array)
    
	result_list = ipExclusion.get(format=True)
	for i in result_list:
        CommonFunctions.print_all_attr(i) # from nevada.Common.Connector import * 를 해줘야 함.

#### 결과 예시
ipFilterId가 6777029인 ip, 6776978인 ip를 각각 삭제하였으므로, <br> 광고노출제한 IP을 다시 조회하면 empty list가 반환된다.

	[]
	
	
#### 변수 설명
    customerId : 고객의 고유 ID
    filterIp : 광고노출제한 IP
    ipFilterId : filterIp의 고유 ID
    loginId : 시스템에 접속 중인 유저 ID
    memo : IP에 대한 메모 
    regTm : 등록 된 시간,
    userId : 사용자 ID