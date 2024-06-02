"""
# !rule #
1 . TrailBlazer.py -> 구동부
2. screens.py -> 화면 내 로직과 위젯 관리 , 위젯부와 로직부 분리할 지 생각 중이다. 현재는 스크린 내 로직도 작성되어 있다.
screen 명 작성 규칙 : snake 
★ screen 추가 시 1) 이름이 소문자인지 , snake 규칙을 따르는지 확인하고
2)
class first_screen(Screen):
    def __init__(self, app, **kwargs):
        super(first_screen, self).__init__(**kwargs)
        self.app = app
    으로 init시 app parameter passing 확인하며
3)
class MyApp(App):
    def build(self):
        self.screen_manager.add_widget(self.main_screen)
        self.screen_manager.add_widget(self.first_screen)
    로 screen_mananger에 스크린 등록하고 있는지 확인!  
    
3. utils.py -> 종료와 farewell 기능 불러오는 위젯이고 화면 구성 시 종료 , 취소 버튼과 screen 내에서 binding한다.
4. fonts.py -> 폰트 불러오는 모듈 , first_screen __init__가 아니라 myAPP build 시로 가야 한다.
5. strings.py -> 사용할 스트링 불러오는 모듈, fonts.py와 합쳐서 string 처리하도록 바꿔야 한다
6. map.py -> 지도 기능에 사용할 모듈이고 기능별로 모듈 분리할거면 first_screen 여기다 붙혀야 한다.


7. 위젯에 한국어 등록할 때는 전부 font_name='youth' 있어야한다. 이는 비 라틴언어 모두에 해당하며 , 영어 제외하면 폰트 전부 적어줘야 한다.
8. 기능별로 모듈 분리할지 , 화면별로 분류해서 Screen.py에 배치할 지 생각 , 내부 로직부분과 분리하는 게 좋을 것 같은데

"""

import networkx as nx

class Graph_Manager:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node_id, **attrs):
        self.graph.add_node(node_id, **attrs)

    def add_edge(self, node1, node2, **attrs):
        self.graph.add_edge(node1, node2, **attrs)

    def get_graph(self):
        return self.graph

# 그래프 인스턴스 생성 및 노드, 엣지 추가
graph_manager = Graph_Manager()
for i in range(20):  # 예제: 20개의 노드 생성
    graph_manager.add_node(i, pos=(i * 10, i * 10))

# 예제: 엣지 추가
graph_manager.add_edge(0, 1)
graph_manager.add_edge(1, 2)
graph_manager.add_edge(2, 3)
