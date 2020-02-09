# API/IpExclusion.py

`IpExclusion.py`는 `광고시스템 > 도구 > 광고노출제한 관리`의 기능들을 담고 있습니다.

### IpExclusion 객체 생성하기
	from nevada.API.IpExclusion import *
	
    base_url = 'https://api.naver.com' #그대로 두세요.
    
    api_key = "Naver-search_AD_ACCESS_LICCENSE" #변경하세요.
    secret_key = "Naver-search_AD_SECRET_KEY" #변경하세요.
    customer_id = "Naver-search_AD_CUSTOMER_ID" #변경하세요.
    
    ip = IpExclusion(base_url=base_url, api_key=api_key, secret_key=secret_key, customer_id=customer_id)
    
    
### 광고노출제한 IP 조회하기
#### 코드 예시
	result = ip.get_ip_exclusion_json()
	print(result)
	    
	result_list = ip.get_ip_exclusion_list()
	for result in result_list:
	    print('customer_id:', result.customerId, end=' & ')
	    print('filterIp:', result.filterIp, end=' & ')
	    print('ipFilterId:', result.ipFilterId, end=' & ')
	    print('memo:', result.memo, end=' & ')
	    print('regTm:', result.regTm)


#### 결과 예시
	[{'ipFilterId': 6672662, 'customerId': 1810030, 'filterIp': '125.128.118.179', 'regTm': 1579704772000, 'memo': '누구의 IP 주소일까'}, {'ipFilterId': 6672661, 'customerId': 1810030, 'filterIp': '125.128.118.178', 'regTm': 1579704752000, 'memo': '나의 IP 주소'}]
	
	customer_id: 1810030 & filterIp: 125.128.118.179 & ipFilterId: 6672662 & memo: 누구의 IP 주소일까 & regTm: 1579704772000
	customer_id: 1810030 & filterIp: 125.128.118.178 & ipFilterId: 6672661 & memo: 나의 IP 주소 & regTm: 1579704752000
	
### 광고노출제한 IP 추가하기
#### 코드 예시
    result = ip.create_ip_exclusion(filterIp='125.128.118.180', memo='누구의 IP 주소일까 22')
    
    print('customer_id:', result.customerId, end=' & ')
    print('filterIp:', result.filterIp, end=' & ')
    print('ipFilterId:', result.ipFilterId, end=' & ')
    print('memo:', result.memo, end=' & ')
    print('regTm:', result.regTm)
    
#### 결과 예시
    customer_id: 1810030 & filterIp: 125.128.118.180 & ipFilterId: 6672680 & memo: 누구의 IP 주소일까 22 & regTm: 1579706122737
    
### 광고노출제한 IP 수정하기
#### 코드 예시
    result = ip.update_ip_exclusion(filterIp='125.128.118.180', ipFilterId='6672681', memo='memo를 변경했다')
    
    print('customer_id:', result.customerId, end=' & ')
    print('filterIp:', result.filterIp, end=' & ')
    print('ipFilterId:', result.ipFilterId, end=' & ')
    print('memo:', result.memo, end=' & ')
    print('regTm:', result.regTm)
    
#### 결과 예시
    customer_id: 1810030 & filterIp: 125.128.118.180 & ipFilterId: 6672681 & memo: memo를 변경했다 & regTm: 1579706196000
    

### 광고노출제한 IP 삭제하기
#### 코드 예시
    ip.delete_ip_exclusion(id='6672681')

    result_list = ip.get_ip_exclusion_list()
    for result in result_list:
        print('customer_id:', result.customerId, end=' & ')
        print('filterIp:', result.filterIp, end=' & ')
        print('ipFilterId:', result.ipFilterId, end=' & ')
        print('memo:', result.memo, end=' & ')
        print('regTm:', result.regTm)

#### 결과 예시
memo가 'memo를 변경했다'였던 ip주소가 목록에서 삭제된 것을 확인할 수 있다.

    customer_id: 1810030 & filterIp: 125.128.118.179 & ipFilterId: 6672662 & memo: 누구의 IP 주소일까 & regTm: 1579704772000
    customer_id: 1810030 & filterIp: 125.128.118.178 & ipFilterId: 6672661 & memo: 나의 IP 주소 & regTm: 1579704752000
    
    
### 광고노출제한 IP 여러 개 한꺼번에 삭제하기
#### 코드 예시
**ipFilterId**의 list를 구성한다.
		
	id_array = ['6672662','6672661']
	ip.delete_ip_exclusion_many(id_array)
		
	result = ip.get_ip_exclusion_json()
	print(result)

#### 결과 예시
ipFilterId가 6672662인 ip, 6672661인 ip를 각각 삭제하였으므로, <br> 광고노출제한 IP을 다시 조회하면 empty list가 반환된다.

	[]