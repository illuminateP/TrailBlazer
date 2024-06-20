import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import font_manager
import heapq

from kivy.resources import resource_find

font_path = resource_find('fonts/Youth.ttf')  # Youth.ttf 폰트 경로 , kivy와 matplotlib는 별도의 폰트를 사용하기에 따로 등록해 주어야 한다.

if not font_path:
    raise FileNotFoundError(f"Font file not found: {font_path}")

font_prop = font_manager.FontProperties(fname=font_path)
plt.rc('font', family=font_prop.get_name())
plt.rcParams['axes.unicode_minus'] = False


def heap_dijkstra(graph, start):
    # 우선순위 큐 초기화: (거리, 정점)
    priority_queue = [(0, start)]
    # 시작 정점에서 각 정점까지의 최단 거리를 저장하는 딕셔너리
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    shortest_path_tree = {node: None for node in graph}

    while priority_queue:
        # 현재까지의 최단 거리와 현재 정점을 우선순위 큐에서 추출
        current_distance, current_node = heapq.heappop(priority_queue)

        # 이미 찾은 최단 거리보다 현재 거리가 더 길다면 무시
        if current_distance > distances[current_node]:
            continue

        # 현재 정점과 인접한 모든 정점을 확인
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # 현재 경로가 더 짧은 경우에만 최단 거리를 갱신
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path_tree[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, shortest_path_tree


class Graph_Manager:
    def __init__(self):
        self.graph = nx.Graph()
        self.texts = {}  # 텍스트 객체를 저장할 딕셔너리

    def add_node(self, node_id, label, **attrs):
        self.graph.add_node(node_id, label=label, **attrs)

    def add_edge(self, node1, node2, weight):
        self.graph.add_edge(node1, node2, weight=weight)

    def get_graph(self):
        return self.graph

    # 전체 그래프 출력하는 메서드(first_functional_button_clicked)
    def draw_graph(self, highlight_nodes=None, highlight_path=None):
        if highlight_nodes is None:
            highlight_nodes = []
        if highlight_path is None:
            highlight_path = []

        fixed_positions = {
            30: (-50, 0),  # 복정동 주거단지
            29: (50, 0),   # 가천대역 1번 출구
            23: (0, 0),    # 무한광장
            1: (25, 20),    # 가천관
            17: (0, -20)   # 반도체대학
        }

        fixed_nodes = fixed_positions.keys()
        pos = nx.spring_layout(self.graph, pos=fixed_positions, fixed=fixed_nodes, seed=42, k=10)

        labels = nx.get_node_attributes(self.graph, 'label')

        fig, ax = plt.subplots()
        nodes = self.graph.nodes()

        node_colors = ['yellow' if node in highlight_nodes else 'lightblue' for node in nodes]
        edges = self.graph.edges()
        edge_colors = ['red' if (u, v) in highlight_path or (v, u) in highlight_path else 'lightgrey' for u, v in edges]
        nx.draw(self.graph, pos, with_labels=True, labels=labels, node_size=500, node_color=node_colors, font_size=10, ax=ax, font_family='Youth')
        nx.draw_networkx_edges(self.graph, pos, edgelist=edges, edge_color=edge_colors, ax=ax)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels={(u, v): d['weight'] for u, v, d in self.graph.edges(data=True)}, ax=ax)

        def on_click(event):
            x, y = event.xdata, event.ydata
            if x is None or y is None:
                return
            closest_node = None
            min_distance = float('inf')
            for node, (nx_pos, ny_pos) in pos.items():
                distance = (nx_pos - x) ** 2 + (ny_pos - y) ** 2
                if distance < min_distance:
                    min_distance = distance
                    closest_node = node

            if closest_node is not None:
                if closest_node in self.texts:
                    # 이미 텍스트가 있는 경우 제거
                    self.texts[closest_node].remove()
                    del self.texts[closest_node]
                else:
                    # 텍스트가 없는 경우 추가
                    facilities = self.graph.nodes[closest_node]['facilities']
                    text = self.show_facilities(ax, pos[closest_node][0], pos[closest_node][1], self.graph.nodes[closest_node]['name'], facilities)
                    self.texts[closest_node] = text
                plt.draw()

        fig.canvas.mpl_connect('button_press_event', on_click)
        plt.show()

    # 노드만 출력하는 그래프, 편의시설 출력(second ~ fourth functional button clicked) 용
    def draw_node_graph(self, highlight_nodes):
        fixed_positions = {
            30: (-50, 0),  # 복정동 주거단지
            29: (50, 0),   # 가천대역 1번 출구
            23: (0, 0),    # 무한광장
            1: (25, 20),    # 가천관
            17: (0, -20)   # 반도체대학
        }

        fixed_nodes = fixed_positions.keys()
        pos = nx.spring_layout(self.graph, pos=fixed_positions, fixed=fixed_nodes, seed=42, k=2.5)
        labels = nx.get_node_attributes(self.graph, 'label')

        fig, ax = plt.subplots()
        nodes = self.graph.nodes()

        node_colors = ['yellow' if node in highlight_nodes else 'lightblue' for node in nodes]
        nx.draw(self.graph, pos, with_labels=True, labels=labels, node_size=500, node_color=node_colors, font_size=10, ax=ax, font_family='Youth')

        def on_click(event):
            x, y = event.xdata, event.ydata
            if x is None or y is None:
                return
            closest_node = None
            min_distance = float('inf')
            for node, (nx_pos, ny_pos) in pos.items():
                distance = (nx_pos - x) ** 2 + (ny_pos - y) ** 2
                if distance < min_distance:
                    min_distance = distance
                    closest_node = node

            if closest_node is not None:
                if closest_node in self.texts:
                    self.texts[closest_node].remove()
                    del self.texts[closest_node]
                else:
                    facilities = self.graph.nodes[closest_node]['facilities']
                    text = self.show_facilities(ax, pos[closest_node][0], pos[closest_node][1], self.graph.nodes[closest_node]['name'], facilities)
                    self.texts[closest_node] = text
                plt.draw()

        fig.canvas.mpl_connect('button_press_event', on_click)
        plt.show()  
    
    
    # 시작 노드와 끝 노드까지의 경로를 강조하는 그래프, 다익스트라 알고리즘 출력(on_search) 용 
    # 가천관, 가천대역 1번출구 복정동 주거단지를 중심으로 위치를 잡는다.
    def draw_dijkstra_graph(self, start_node, end_node, path):
        fixed_positions = {
            30: (-50, 0),  # 복정동 주거단지
            29: (50, 0),   # 가천대역 1번 출구
            23: (0, 0),    # 무한광장
            1: (25, 20),    # 가천관
            17: (0, -20)   # 반도체대학
        }

        fixed_nodes = fixed_positions.keys()
        pos = nx.spring_layout(self.graph, pos=fixed_positions, fixed=fixed_nodes, seed=42, k=2.5)
        labels = nx.get_node_attributes(self.graph, 'label')

        fig, ax = plt.subplots()
        nodes = self.graph.nodes()

        node_colors = ['yellow' if node in path else 'lightblue' for node in nodes]
        nx.draw(self.graph, pos, with_labels=True, labels=labels, node_size=500, node_color=node_colors, font_size=10, ax=ax, font_family='Youth')

        edges = [(u, v) for u, v in zip(path, path[1:])]
        edge_colors = ['red' if (u, v) in edges or (v, u) in edges else 'lightgrey' for u, v in self.graph.edges()]
        nx.draw_networkx_edges(self.graph, pos, edgelist=self.graph.edges(), edge_color=edge_colors, ax=ax)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels={(u, v): d['weight'] for u, v, d in self.graph.edges(data=True)}, ax=ax)
        plt.show()
        
    def show_facilities(self, ax, x, y, node_name, facilities):
        text = f"건물: {node_name}\n시설: {', '.join(facilities)}"
        return ax.text(x, y, text, fontsize=12, bbox=dict(facecolor='yellow', alpha=0.5), fontproperties=font_prop)

    def find_nodes_with_facility(self, facility_name):
        return [node for node, data in self.graph.nodes(data=True) if facility_name in data.get('facilities', {})]
    
# 그래프 인스턴스 생성 및 노드, 엣지 추가
def create_graph():
    graph_manager = Graph_Manager()

        # 노드 추가
    graph_manager.add_node(1, label='1. 가천관', name='가천관', pos=(0, 20), facilities={
                        '아르테크네': {'위치': '가천관 1층 입구 왼편, 가천관 지하 1층, 지하 3층','운영시간': '09:00 ~ 17:00'}
                        ,'프린터': {'위치' : '가천관 2층','운영시간' : '24시간'}})

    graph_manager.add_node(2, label='2. 비전타워', name='비전타워', pos=(10, -10), facilities={
                        '편의점': {'위치': '비전타워 지하 4층 상점가', '운영시간': '07:00 ~ 24:00'},
                        '아르테크네': {'위치': '비전타워 2층, 3층, 4층, 5층, 6층', '운영시간': '09:00 ~ 21:00'}
                        , '자판기': {'위치' : '층마다 존재'}})

    graph_manager.add_node(3, label='3. 법과대학', name='법과대학', pos=(20, -5), facilities={
                        '아르테크네': {'위치': '법과대학 1층 하나은행 옆','운영시간': '09:00 ~ 00:02, 00:02 이후 강제 소등'}})

    graph_manager.add_node(4, label='4. 공과대학1', name='공과대학1', pos=(-10, -10), facilities={
                        '아르테크네': {'위치': '공과대학1 2층','운영시간': '09:00 ~ 21:00'}})

    graph_manager.add_node(5, label='5. 공과대학2', name='공과대학2', pos=(15, 10), facilities={
                        '아르테크네': {'위치': '공과대학2 1층 입구','운영시간': '09:00 ~ 21:00'}})

    graph_manager.add_node(6, label='6. 한의과대학', name='한의과대학', pos=(-10, 20), facilities={})

    graph_manager.add_node(7, label='7. 예술·체육대학1', name='예술·체육대학1', pos=(5, 15), facilities={
                        '아르테크네': {'위치': '예술·체육대학1 2층, 3층','운영시간': '09:00 ~ 21:00'}})

    graph_manager.add_node(8, label='8. 예술·체육대학2', name='예술·체육대학2', pos=(-5, 15), facilities={
                        '아르테크네': {'위치': '예술·체육대학2 3층','운영시간': '09:00 ~ 21:00'}})

    graph_manager.add_node(9, label='9. AI관', name='AI관', pos=(-15, -10), facilities={
                        '아르테크네': {'위치': 'AI 공학관 1층, 2층, 4층, 5층, 7층','운영시간': '24시간'}
                            , '자판기': {'위치' : 'AI 공학관 3층, 5층'}})

    graph_manager.add_node(10, label='10. 바이오나노대학', name='바이오나노대학', pos=(-20, -5), facilities={})

    graph_manager.add_node(11, label='11. 중앙도서관', name='중앙도서관', pos=(20, 15), facilities={
                        '편의점': {'위치': '지하 1층','운영시간': '24:00'}})

    graph_manager.add_node(12, label='12. 전자정보도서관', name='전자정보도서관', pos=(-20, -20), facilities={
                        '프린터': {'위치': '1층 입구 오른편'}})

    graph_manager.add_node(13, label='13. 대학원·(원격)평생교육원', name='대학원·(원격)평생교육원', pos=(0, 10), facilities={})
    graph_manager.add_node(14, label='14. 교육대학원', name='교육대학원', pos=(15, 5), facilities={
                        '아르테크네': {'위치': '교육대학원 1층, 2층, 4층','운영시간': '09:00 ~ 21:00'}})
    graph_manager.add_node(15, label='15. 바이오나노연구원', name='바이오나노연구원', pos=(-10, 0), facilities={})
    graph_manager.add_node(16, label='16. 산학협력관1', name='산학협력관1', pos=(10, 20), facilities={})

    graph_manager.add_node(17, label='17. 반도체대학', name='반도체대학', pos=(0, -20), facilities={
                        '아르테크네': {'위치': '반도체대학 1층 입구','운영시간': '24시간'}
                            , '자판기': {'위치' : '반도체대학 1층'}})

    graph_manager.add_node(18, label='18. 학생회관/학군단', name='학생회관/학군단', pos=(25, -10), facilities={})
    graph_manager.add_node(19, label='19. 제1학생생활관', name='제1학생생활관', pos=(-5, -15), facilities={})
    graph_manager.add_node(20, label='20. 제2학생생활관', name='제2학생생활관', pos=(20, -15), facilities={})
    graph_manager.add_node(21, label='21. 제3학생생활관', name='제3학생생활관', pos=(25, 0), facilities={
                        '편의점': {'위치': '1층 기숙사 오른편','운영시간': '24:00, 22:00 이후 카드 인식해야 문이 열림'},
                        '아르테크네' : {'위치': '제3학생생활관 1층 편의점 옆','운영시간': '24시간이나 22:00 이후 기숙사생만 출입 가능하게 문이 열림'}})

    graph_manager.add_node(22, label='22. 글로벌센터', name='글로벌센터', pos=(-20, 10), facilities={
                        '아르테크네': {'위치': '글로벌센터 1층, 5층, 6층','운영시간': '09:00 ~ 21:00'}})

    graph_manager.add_node(23, label='A. 무한광장', name='무한광장', pos=(0, 0), facilities={})
    graph_manager.add_node(24, label='B. 스타덤광장', name='스타덤광장', pos=(10, 0), facilities={})
    graph_manager.add_node(25, label='C. 프리덤광장', name='프리덤광장', pos=(5, -5), facilities={})
    graph_manager.add_node(26, label='D. 바람개비광장', name='바람개비광장', pos=(15, 0), facilities={})
    graph_manager.add_node(27, label='E. 대정원', name='잔디광장', pos=(20, 10), facilities={})
    graph_manager.add_node(28, label='F. 대운동장', name='대운동장', pos=(-25, 5), facilities={})

    graph_manager.add_node(29, label='G. 가천대역 1번 출구', name='가천대역 1번 출구', pos=(50, 0), facilities={})
    graph_manager.add_node(30, label='H. 복정동 주거단지', name='복정동 주거단지', pos=(-50, 0), facilities={})
    
    graph_manager.add_edge(29, 2, weight=10)
    graph_manager.add_edge(29, 3, weight=10)
    
    graph_manager.add_edge(2, 3, weight=10)
    graph_manager.add_edge(3, 5, weight=10)
    graph_manager.add_edge(5, 16, weight=10)
    graph_manager.add_edge(16, 1, weight=10)
    graph_manager.add_edge(1, 23, weight=10)
    graph_manager.add_edge(23, 27, weight=10)
    graph_manager.add_edge(27, 14, weight=10)    
    graph_manager.add_edge(14, 11, weight=10)
    graph_manager.add_edge(11, 18, weight=10)   
    graph_manager.add_edge(18, 28, weight=10)    
    graph_manager.add_edge(28, 19, weight=10)  
    graph_manager.add_edge(19, 20, weight=10) 
    graph_manager.add_edge(20, 9, weight=10)
    graph_manager.add_edge(9, 21, weight=10)
    graph_manager.add_edge(9, 30, weight=10)
    
    graph_manager.add_edge(30, 22, weight=10)
    graph_manager.add_edge(22, 7, weight=10)    
    graph_manager.add_edge(7, 8, weight=10)    
    graph_manager.add_edge(7, 10, weight=10) 
    graph_manager.add_edge(7, 26, weight=10)        
    graph_manager.add_edge(10, 13, weight=10)    
    graph_manager.add_edge(13, 14, weight=10)          
    graph_manager.add_edge(22, 17, weight=10)        
    graph_manager.add_edge(17, 4, weight=10)    
    graph_manager.add_edge(4, 27, weight=10)    
    graph_manager.add_edge(17, 24, weight=10)   
    graph_manager.add_edge(24, 25, weight=10)   
    graph_manager.add_edge(24, 12, weight=10)
    graph_manager.add_edge(25, 6, weight=10)     
    graph_manager.add_edge(6, 15, weight=10)   
    graph_manager.add_edge(15, 2 , weight=10)   

    return graph_manager
    


"""
    # 23 ~ 30 은 편의시설이 없는 장소이고, 지도에 알파벳으로 표시되어 있거나 아예 없으나(29, 30)
    # djikstra Algorithm에서 heapq으로 우선순위 큐를 구현하는데, 요소들끼리 서로 비교하는 부분(우선적으로 가중치를 비교히지만, 동일한 우선순위의 경우 두 번째 원소
    # (여기서는 ID)을 비교하는 부분이 있어 ID는 정수형으로 정의해야 함에 유의
    graph_manager.add_node(23, label='A. 무한광장', name='무한광장', pos=(0.5, 0.5), facilities={})
    graph_manager.add_node(24, label='B. 스타덤광장', name='스타덤광장', pos=(0.6, 0.6), facilities={})
    graph_manager.add_node(25, label='C. 프리덤광장', name='프리덤광장', pos=(0.65, 0.55), facilities={})
    graph_manager.add_node(26, label='D. 바람개비광장', name='바람개비광장', pos=(0.4, 0.55), facilities={})
    graph_manager.add_node(27, label='E. 대정원', name='잔디광장', pos=(0.3, 0.45), facilities={})
    graph_manager.add_node(28, label='F. 대운동장', name='대운동장', pos=(0.2, 0.5), facilities={})
    
    # 새로 추가한 노드 
    graph_manager.add_node(29, label='G. 가천대역 1번 출구', name='가천대역 1번 출구', pos=(0.9, 0.5), facilities={})
    graph_manager.add_node(30, label='H. 복정동 주거단지', name='복정동 주거단지', pos=(0.1, 0.5), facilities={})
"""

