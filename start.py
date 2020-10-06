import requests #웹페이지의 요소들을 가져오는 라이브러리, cmd에서 pip install requests를 이용해서 다운로드받아야 사용할수있다.
from bs4 import BeautifulSoup 
indeed_result = requests.get('https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=%EC%84%9C%EC%9A%B8&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch')
#상단 코드설명: requests.get을 이용하여 특정 url정보를 가져오는것#
indeed_soup = BeautifulSoup(indeed_result.text,'html.parser') # 변수명=BeautifulSoup( ,'html.parser') 여기 괄호 왼쪽란에 indeed_result.text를 넣어서 text형으로 html을 가져온다 가져온다. #

pagination = indeed_soup.find('div',{'class':'pagination'}) #첫번째 div태그의 class=pagination를 가져온다 #

pages = pagination.find_all('a') #find_all은 모든태그를 가져오는데 위에서 저장한 pagination변수의 모든 a 앵커태그를 가져온다#
spans=[] #빈 array를 만든다#
for page in pages: #반복문으로 pages에서 page 변수를 하나씩 뽑아온다.#
    spans.append(page.find('span')) #위에서 만든 빈 array인 spans에 append를 이용하여 page.find('span')를 집어넣는다. 그러면 span이 들어간 태그들이 추출된다.#
spans = spans[:-1] #spans의 범위는 0부터 -1까지인데 -1은 맽끝자리이므로 요소들은 0부터 -1앞까지 그러니까 0부터 -2에 해당되는 값들만 추출한다#