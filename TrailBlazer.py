"""
 # Updated at 240530 #

##################################################################################
✔✔✔
# !기능 구현 목록 #
버튼을 누르면 지도에서
우체국 , 근처 식당 , 학식 위치 표시
프린트 , ATM , 편의점/매점 , 자판기 , 아라크네 , 샤워실이 있는 건물과 층, 사진 표시 -> 학교 홈페이지에 있어요
한 번 누르면 해당 노드에 아이콘이 올라오고 , 한 번 더 누르면 아이콘이 꺼진다
현재 시간을 받아와서 건물 운영 시간이 지나면 건물 불이 꺼지고 운영중인 건물은 아이콘을 밝게 표시하는 기능을

지도 위에 오버레이해서 출력한다.

화장실,흡연구역 위치 표시 , 표시 시 자동으로 현 위치에서 가장 가까운 화장실 표시(A*였나)

건물을 노드로 표현하고 노드 안에 층별로 중첩 배열을 쓰던 리스트를 쓰던 딕셔너리를 쓰던 
리스트에 딕셔너리 붙힌 게 제일 낫겠네 그걸로 층별 뭐 있는지

흡연구역 , 샤워실 학생회에 물어보면 알겠죠?
프린트 , 자판기는 업체에 전화하거나 학생처에 물어보면 알 거고

- 대신 버튼 한번 누르면 overlay되어 겹치고 한 번 더 누르면 꺼지게
지도 위에 노드 보여주려면 음... 
지도에 background로 사진 사용

맨 위에 검색창 있어서 경로 검색 시 어디서 어디까지인지 자동 완성으로 구현 -> 힙 사용해서 탐색으로 가장 가까운 힙 3개 표시해서 탐색 기능 구현

산책로 검색 -> 크루스칼

언어 선택 기능 , 국기에 해당하는 이미지버튼으로 스위칭되게

##################################################################################

# !todo #
0. 불필요한 import문과 중복 import 제거
0. font init 위치가 first_screen init 시로 가 있는데  myApp build 시로 옮겨야 함

★ 1. 제일 먼저 d.txt랑 이거랑 정리해서 제품 기능 목록 작성하고
    1. 우선 스크린 이름 호출 때문에 처음부터 snake로 써야 하고 screenmanager에서 parameter로 소문자만 받는다 
       그럼 메서드는 파스칼로 쓰는게 좋겠지?
    1. 파일명,디렉토리명 전부 다 영어로 바꾸고 메인 TrailBlazer (TB).py로 고치고
    1. 건물 노드로 일단 만들고 그래프로 띄워야 하는데 screenmanager 위에 networkx를 겹칠 수 있는지 , 겹칠 수 없다면 networksx 모델을 뜯어서 써야 하는           	 데 그럴 수 있는지 알아보자

    2. 건물 노드로 만들어서 main.py에 붙히고
    2. 길찾기 기능 만들어 보고
    2. 내일부터 하루에 건물 하나씩 실측

    3. 탐색 써야 하니까 동아리 검색 버튼 추가


   
    4. UI는 생각을 좀 해 봐야겠지만 우선 길찾기 1번 버튼(first_screen)에 붙히자


   5. farewell에 메시지 추가 - AI generate
   5. 버튼이랑 레이아웃 싹 다듬고 Boxlayout가 아니라 relativelayout으로 해야 크로스 플랫폼 동작이 되겠죠?
   5. 설치 파일로 압축하는 모듈이 있을거고 
   5. 크로스 플랫폼 테스트도 해야 하고
   
   6. 다 하면 언어 변경 기능 이미지버튼으로 추가하고 strings.py , fonts.py에서 다중 언어팩 추가 하고
      screen.py에서 boxlayout을 relative layout으로 전부 바꾸고 

   6. 이스터에그 두개 추가
      총장님 동상 클릭하면 뭐 할까
      밤에는 꽈배기가 빛나요

   7. 이용자 수 좀 늘어나면 음... 서버를 써서 식단표 크롤링 해 와서 맛집평가나 학식 평가기능 도입



##################################################################################
# !rule #
1. TrailBlazer.py -> 구동부
2. screens.py -> 화면 내 로직과 위젯 관리 , 위젯부와 로직부 분리할 지 생각 중이다. 현재는 스크린 내 로직도 작성되어 있다.
screen 명 작성 규칙 : snake
3. utils.py -> 종료와 farewell 기능 불러오는 위젯이고 화면 구성 시 종료 , 취소 버튼과 screen 내에서 binding한다.
4. fonts.py -> 폰트 불러오는 모듈 , first_screen __init__가 아니라 myAPP build 시로 가야 한다.
5. strings.py -> 사용할 스트링 불러오는 모델 , fonts.py랑 묶어서 처리하도록 바꿔야 한다


7. 위젯에 한국어 등록할 때는 전부 font_name='youth' 있어야한다. 이는 비 라틴언어 모두에 해당하며 , 영어 제외하면 폰트 전부 적어줘야 한다.
8. 기능별로 모듈 분리할지 , 화면별로 분류해서 Screen.py에 배치할 지 생각 , 내부 로직부분과 분리하는 게 좋을 것 같은데


##################################################################################

# !note #
1. kivy는 한글 지원 안 해서 폰트로 받아와야 하는데 , 그게 안 되는 Ending_Messages 부분에는 custom title 바 추가하거나 (llama3) , 
    그냥 타이틀에 한글 쳐박으면 된다고 우기거나(gpt4o) 하는데 에러 메시지에 정답이 써 있었음
    결론 : AI는 생각보다 멍청하니까 너무 의존하지 말고 공식 문서를 먼저 보자
    Popup(title = '잘 가요! 이거 만드느라 얼마나 고생했는지 당신은 모를 거에요', title_font='youth' , content=Toast_Layout, auto_dismiss=False, size_hint=(0.8, None))
    -> 이거 title_font 추가해야 한다는 거 프로퍼티 에러 메시지
  TypeError: Properties ['font_name'] passed to __init__ may not be existing property names. Valid properties are 
  ['_anim_alpha', '_anim_duration', '_container', '_is_open', '_window', 'anchor_x', 'anchor_y', 'attach_to', 'auto_dismiss', 'background', 'background_color', 'border', 'center', 'center_x', 'center_y', 'children', 'cls', 'content', 'disabled', 'height', 'ids', 'motion_filter', 'opacity', 'overlay_color', 'padding', 'parent', 'pos', 'pos_hint', 'right', 'separator_color', 'separator_height', 
  'size', 'size_hint', 'size_hint_max', 'size_hint_max_x', 'size_hint_max_y', 'size_hint_min', 'size_hint_min_x', 'size_hint_min_y', 'size_hint_x', 'size_hint_y', 'title', 'title_align', 'title_color', 'title_font', 'title_size', 'top', 'width', 'x', 'y']
  여기서 찾음


##################################################################################
"""

"""
! TODO ! 240618 추가
★ kivy에서 matplotlib 컨트롤만 할 거니까 17번 반도체대학으로 바꾸고
1. map.py에 matplotlib 핸들러 함수 바인딩, 여기서 toggle 경로에 대한 길찾기 알고리즘 적용
2. input 힌트 기능에 힙서치 추가
3. Builder로 앱 퍼블리싱 시간 되면 해서 보고서에 추가
4. 시간 관련 기능 추가 여기서 toggle 경로에 대한 길찾기 알고리즘 사용
5. util.py에 메시지 AI generate 
6. 힌트 기능 구현(힙 서치)
7. gps 안 할 거니까 언어 추가라도
8. 노드 / 가중치 실측 후 추가 

"""   

# 구동부
from screens import MyApp

if __name__ == "__main__": 
    # 호출 시 자동 init     
    myapp = MyApp()
    myapp.run()
    
   
