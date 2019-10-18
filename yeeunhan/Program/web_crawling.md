```python
➜  program git:(master) ✗ python  # 파이썬 불러오기 (git bash) 
    Python 3.7.4 (default, Jul  9 2019, 18:13:23) 
    [Clang 10.0.1 (clang-1001.0.46.4)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import requests #requests 불러오기
    >>> url = 'https://finance.naver.com/news/news_read.nhn?article_id=0004252776&office_id=421&mode=mainnews&type=1&date=2019-10-16' #url 변수저장
    >>> requests.get(url)
    <Response [200]>
    >>> resp = requests.get(url) # requests url 변수 저장 
    >>> resp
    <Response [200]> # 응답코드
    >>> type(resp) #타입
    <class 'requests.models.Response'>
    >>> dir(resp)
    ['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']
    >>> resp.text #겁나 길게 쫘르륵 뜸) 
    >>> resp.text.split('\n')[789:792] # \n(엔터)를 기준으로 789번줄부터 791까지 자르기
    >>> from newspaper import Article
    >>> url = 'https://finance.naver.com/news/news_read.nhn?article_id=0004252776&office_id=421&mode=mainnews&type=1&date=2019-10-16'
    >>> article = Article(url)
    >>> article.download() #html 가져오고
    >>> article.parse() #파치 불러오기 
    >>> dir(article)
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'additional_data', 'article_html', 'authors', 'build', 'build_resource_path', 'canonical_link', 'clean_doc', 'clean_top_node', 'config', 'doc', 'download', 'download_exception_msg', 'download_state', 'extractor', 'fetch_images', 'get_parse_candidate', 'get_resource_path', 'has_top_image', 'html', 'images', 'imgs', 'is_media_news', 'is_parsed', 'is_valid_body', 'is_valid_url', 'keywords', 'link_hash', 'meta_data', 'meta_description', 'meta_favicon', 'meta_img', 'meta_keywords', 'meta_lang', 'movies', 'nlp', 'parse', 'publish_date', 'release_resources', 'set_article_html', 'set_authors', 'set_canonical_link', 'set_html', 'set_imgs', 'set_keywords', 'set_meta_data', 'set_meta_description', 'set_meta_favicon', 'set_meta_img', 'set_meta_keywords', 'set_meta_language', 'set_movies', 'set_reddit_top_img', 'set_summary', 'set_tags', 'set_text', 'set_title', 'set_top_img', 'set_top_img_no_check', 'source_url', 'summary', 'tags', 'text', 'throw_if_not_downloaded_verbose', 'throw_if_not_parsed_verbose', 'title', 'top_image', 'top_img', 'top_node', 'url']
    >>> article.title #기사 제목 호출
    '네이버 금융' #잘 못가져옴 페이지 명을 가져옴 
    >>> article.text # 텍스트는 잘 가져와짐
    '© News1 DB © News1 DB\n\n(서울=뉴스1) 전민 기자 = 16일 코스피 지수는 뉴욕 증시 상승과 반도체주 강세에 힘입어 2080선에 올라섰다. 코스닥도 0.8% 올랐다. 달러/원 환율은 기준금리 인하 영향으로 소폭 상승했다.이날 코스피 지수는 14.66p(0.71%) 오른 2082.83에 마감했다. 코스피는 12.75p(0.62%) 오른 2080.92로 출발해 외국인과 기관의 순매수에 상승세를 지켰다. 코스피 시장에서 외국인과 기관은 각각 46억원, 1452억원 순매수했다. 개인은 1780억원 순매도했다.업종별로 의약품(2.42%), 전기전자(1.20%), 비금속광물(1.07%), 건설업(0.91%) 등은 올랐다. 종이목재(-0.59%), 통신업(-0.41%) 등은 하락했다.시가총액 상위 10개 종목 중 삼성전자(1.20%), SK하이닉스(1.48%), 현대차(0.82%), NAVER(1.98%), 셀트리온(1.91%), 삼성바이오로직스(3.99%), 신한지주(0.35%) 등은 상승했다. 현대모비스(-0.61%)는 하락했다.서상영 키움증권 투자전략팀장은 "한국 증시는 미 증시 강세에 힘입어 상승 출발했으며, 데이터 센터 관련 산업에 대한 긍정적 발표가 잇달아 발표되는 등 반도체 업황에 대한 기대 심리도 긍정적 요인이었다"면서 "중국 외교부가 미국산 농산물 수입을 이미 시작했다고 발표하며 스몰딜 합의 불확실성을 완화시킨 점도 긍정적 요인"이라고 설명했다.새벽에 끝난 뉴욕 증시에서는 양호한 기업 실적 발표에 힘입어 다우산업(0.89%), 나스닥종합(1.24%), S&P 500(1%) 등 주가지수가 일제히 상승했다.코스닥 지수는 5.16p(0.80%) 오른 641.96에 거래를 마쳤다. 코스닥 시장에서 외국인은 559억원 순매수했다. 개인과 기관은 각각 476억원, 27억원 순매도했다.시가총액 상위 10개 종목 중 셀트리온헬스케어(2.20%), 에이치엘비(4.49%), CJ ENM(1.03%), 케이엠더블유(0.43%), 펄어비스(1.16%), 메디톡스(2.94%), SK머티리얼즈(1.47%) 등은 상승했다. 휴젤(-0.42%), 헬릭스미스(-14.96%), 스튜디오드래곤(-0.30%) 등은 하락했다.서울외환시장에서 달러/원 환율은 2.6원 오른 1187.8원에 거래를 마쳤다.min785@news1.kr\n\n▶ [ 크립토허브 ] ▶ [ 해피펫 ]\n\n▶ 네이버 메인에서 [뉴스1] 구독하기!\n\n[© 뉴스1코리아(news1.kr), 무단 전재 및 재배포 금지]'
    


```
### 크롤링을 할 때, 페이지 하나만 가지고 하진 않음. 목적이 있어야함 
- (어디서부터 어디까지 할꺼다)