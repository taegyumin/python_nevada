# nevada

##### 한국어 문서는 [여기](https://github.com/taegyumin/python_nevada/blob/master/README.md) 있습니다.

<img src="https://img.shields.io/pypi/v/0.0.1">

## What is nevada?
'nevada' is the Python library for improving the productivity of those who use the [Naver Search Ad API](https://github.com/naver/searchad-apidoc).

## Requirements
- [Python](https://www.python.org/) <br>
- [Git client](https://git-scm.com/downloads) <br>

## Installation
- `pip3 install nevada` <br>
- `git clone https://github.com/taegyumin/python_nevada.git` <br>

## Issue the API License and the secret key

1. Sign up for NAVER SEARCH ADVERTISER's Center ([http://searchad.naver.com](http://searchad.naver.com))
2. Go to ([http://manage.searchad.naver.com](http://manage.searchad.naver.com))
3. Go to Tools > API Manager
4. Create API license

## Verification
Create a Python file, run the code below. <br>
If the current time is output, the code ran successfully. <br>
In your code, change the values of `api_key`, `secret_key`, and `customer_id` to those issued by the NAVER Search Ads system.

	from nevada.Common.Connector import *
	
	base_url = 'https://api.naver.com'
	api_key = "Naver-search-AD_ACCESS_LICCENSE"
	secret_key = "Naver-search-AD_SECRET_KEY"
	customer_id = "Naver-search-AD_CUSTOMER_ID"

	conn = Connector(base_url, api_key, secret_key, customer_id)
	print(conn.get_datetime())
	
---

### More details of nevada are in [Docs](https://github.com/taegyumin/python_nevada/tree/master/Docs).

