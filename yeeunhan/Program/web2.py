from bs4 import BeautifulSoup
import requests
import time #네이버에 계속 요청하면 막히니까 시간 간격을 줄거임
from collections import deque
# import hashlib 


# def get_filename(url):
#     return hashlib.shal(url)
# stack과 que의 차이점? stack은 오른쪽(끝)에서 부터 빼가고, que는 왼쪽(첫번째)부터 빼감.

visited = {}
queue = deque()

def fetch(url): # 웹 페이지 내용을 가져오는 함수 
    return requests.get(url)


def get_links(soup): #html 모든 링크 리턴
    return soup.find_all('a') # a = 앵커 


def enqueue_link(url): #url 하나를 가져오는 링크 만드는 함수
    pass


def link_exists(url): #url이 주어졌을 때, 이미 있는 건지 판단하는 함수 
    return url in visited #cache dict를 만들어서 이미 받았던 url 저장
    

def crawl(url):
    print(f'Fetching {url}...') # 실행되고 있다는 표시 # 링크 클릭시엔 ... 빼고 복사
    resp = fetch(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser') # 여기서 내가 원하는 키워드를 뽑아서 그런 뉴스만 뽑게 만들기
        links = get_links(soup)
        # 내용을 파일로 저장하거나, 뭔가 다른 일을 하기 
        # 파일로 저장하는 방법 : ssh 
       

        for link in links:
            href = link.get('href')
            if href.startswith('https://news.naver.com/main/read.nhn') and href not in visited:
                queue.append(href)
                #우리가 추출한 웹 주소가 저거고, 이미 방문한 url이 아니라면 진행하라
                # 우리가 관심있는 건 news.com.naver 요것만 출력하게끔 만들어줌
                # 그 전엔 잡스러운 것들이 많았음
                visited[href] = 0 
                time.sleep(1) #1초 쉬었다 가기 
                crawl(href) #가장 중요한 부분  - 재귀호출 : 함수가 자기 자신을 부름
                # 네이버 뉴스 라는 링크를 봤을 때, 이미 불러온 건 저장하고(visited url) 새로운 건(href)호출한다는 뜻 
                # 근데 이렇게 하면 1000개쯤 불러오면 데이터가 커져서 오류가 남. 그래서 enqueue 함수를 만들어서 제동을 걸어줌.
    else:
        print(f'Failed to fetch {url}')


if __name__ == '__main__':
    queue.append('https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=293&aid=0000025345&date=20191016&type=1&rankingSeq=9&rankingSectionId=105')
    while queue:
        url = queue.pop()
        crawl(url)
        time.sleep(1)
    # crawl('https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=293&aid=0000025345&date=20191016&type=1&rankingSeq=9&rankingSectionId=105')

