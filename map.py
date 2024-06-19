import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

# 한글 폰트 설정
font_path = os.path.join(current_dir, 'fonts', 'Youth.ttf')  # Youth.ttf 폰트 경로
if not os.path.exists(font_path):
    raise FileNotFoundError(f"Font file not found: {font_path}")

font_prop = font_manager.FontProperties(fname=font_path)
plt.rc('font', family=font_prop.get_name())


plt.rc('font', family=font_prop.get_name())
plt.rcParams['axes.unicode_minus'] = False

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

    def dijkstra_path(self, start_node, end_node):
        return nx.dijkstra_path(self.graph, start_node, end_node, weight='weight')

    def draw_graph(self):
        pos = nx.get_node_attributes(self.graph, 'pos')
        labels = nx.get_node_attributes(self.graph, 'label')

        fig, ax = plt.subplots()

        nx.draw(self.graph, pos, with_labels=True, labels=labels, node_size=500, node_color='lightblue', font_size=10, ax=ax, font_family ='Youth')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels={(u, v): d['weight'] for u, v, d in self.graph.edges(data=True)}, ax=ax)

        def on_click(event):
            x, y = event.xdata, event.ydata
            if x is None or y is None:
                return
            for node, (nx_pos, ny_pos) in pos.items():
                if (nx_pos - x) ** 2 + (ny_pos - y) ** 2 < 2000:  # 클릭 범위 설정
                    if node in self.texts:
                        # 이미 텍스트가 있는 경우 제거
                        self.texts[node].remove()
                        del self.texts[node]
                    else:
                        # 텍스트가 없는 경우 추가
                        facilities = self.graph.nodes[node]['facilities']
                        text = self.show_facilities(ax, nx_pos, ny_pos, self.graph.nodes[node]['name'], facilities)
                        self.texts[node] = text
                    plt.draw()
                    break

        fig.canvas.mpl_connect('button_press_event', on_click)
        plt.show()

    def show_facilities(self, ax, x, y, node_name, facilities):
        text = f"건물: {node_name}\n시설: {', '.join(facilities)}"
        return ax.text(x, y, text, fontsize=12, bbox=dict(facecolor='yellow', alpha=0.5), fontproperties=font_prop)

# 그래프 인스턴스 생성 및 노드, 엣지 추가
def create_graph():
    graph_manager = Graph_Manager()

    # 노드 추가
    graph_manager.add_node(1, label='1. 가천관', name='가천관', pos=(610, 120), facilities=[])
    graph_manager.add_node(2, label='2. 비전타워', name='비전타워', pos=(670, 520), facilities=[])
    graph_manager.add_node(3, label='3. 법과대학', name='법과대학', pos=(710, 550), facilities=[])
    graph_manager.add_node(4, label='4. 공과대학1', name='공과대학1', pos=(740, 480), facilities=[])
    graph_manager.add_node(5, label='5. 공과대학2', name='공과대학2', pos=(770, 500), facilities=[])
    graph_manager.add_node(6, label='6. 한의과대학', name='한의과대학', pos=(800, 450), facilities=[])
    graph_manager.add_node(7, label='7. 예술·체육대학1', name='예술·체육대학1', pos=(830, 580), facilities=[])
    graph_manager.add_node(8, label='8. 예술·체육대학2', name='예술·체육대학2', pos=(860, 330), facilities=[])
    graph_manager.add_node(9, label='9. AI관', name='AI관', pos=(890, 270), facilities=[])
    graph_manager.add_node(10, label='10. 바이오나노대학', name='바이오나노대학', pos=(920, 300), facilities=[])
    graph_manager.add_node(11, label='11. 중앙도서관', name='중앙도서관', pos=(950, 600), facilities=[])
    graph_manager.add_node(12, label='12. 전자정보도서관', name='전자정보도서관', pos=(980, 200), facilities=[])
    graph_manager.add_node(13, label='13. 대학원·(원격)평생교육원', name='대학원·(원격)평생교육원', pos=(1010, 180), facilities=[])
    graph_manager.add_node(14, label='14. 교육대학원', name='교육대학원', pos=(1040, 410), facilities=[])
    graph_manager.add_node(15, label='15. 바이오나노연구원', name='바이오나노연구원', pos=(1070, 230), facilities=[])
    graph_manager.add_node(16, label='16. 산학협력관1', name='산학협력관1', pos=(1100, 330), facilities=[])
    graph_manager.add_node(17, label='17. 반도체대학', name='반도체대학', pos=(1130, 410), facilities=[])
    graph_manager.add_node(18, label='18. 학생회관/학군단', name='학생회관/학군단', pos=(1160, 170), facilities=[])
    graph_manager.add_node(19, label='19. 제1학생생활관', name='제1학생생활관', pos=(1190, 270), facilities=[])
    graph_manager.add_node(20, label='20. 제2학생생활관', name='제2학생생활관', pos=(1220, 400), facilities=[])
    graph_manager.add_node(21, label='21. 제3학생생활관', name='제3학생생활관', pos=(1220, 400), facilities=[])
    graph_manager.add_node(22, label='22. 글로벌센터', name='글로벌센터', pos=(1220, 400), facilities=[])

    graph_manager.add_node('A', label='A. 대운동장', name='대운동장', pos=(640, 140), facilities=[])
    graph_manager.add_node('B', label='B. 스타덤광장', name='스타덤광장', pos=(690, 550), facilities=[])
    graph_manager.add_node('C', label='C. 프리덤광장', name='프리덤광장', pos=(720, 520), facilities=[])
    graph_manager.add_node('D', label='D. 바람개비광장', name='바람개비광장', pos=(760, 490), facilities=[])
    graph_manager.add_node('E', label='E. 잔디광장', name='잔디광장', pos=(800, 460), facilities=[])
    graph_manager.add_node('F', label='F. 복정동 주거단지', name='복정동 주거단지', pos=(800, 460), facilities=[])
    graph_manager.add_node('G', label='G. 가천대역 1번 출구', name='가천대역 1번 출구', pos=(800, 460), facilities=[])

    # 추가적인 엣지 정의 (예시로 몇 개의 엣지 추가)
    graph_manager.add_edge(1, 2, weight=10)
    graph_manager.add_edge(2, 3, weight=15)
    graph_manager.add_edge(3, 4, weight=20)
    graph_manager.add_edge(4, 5, weight=10)
    graph_manager.add_edge(5, 6, weight=10)
    graph_manager.add_edge(6, 7, weight=10)
    graph_manager.add_edge(7, 8, weight=10)
    graph_manager.add_edge(8, 9, weight=10)
    graph_manager.add_edge(9, 10, weight=10)
    graph_manager.add_edge(10, 11, weight=10)
    graph_manager.add_edge(11, 12, weight=10)
    graph_manager.add_edge(12, 13, weight=10)
    graph_manager.add_edge(13, 14, weight=10)
    graph_manager.add_edge(14, 15, weight=10)
    graph_manager.add_edge(15, 16, weight=10)
    graph_manager.add_edge(16, 17, weight=10)
    graph_manager.add_edge(17, 18, weight=10)
    graph_manager.add_edge(18, 19, weight=10)
    graph_manager.add_edge(19, 20, weight=10)
    graph_manager.add_edge(1, 'A', weight=5)
    graph_manager.add_edge(2, 'B', weight=5)
    graph_manager.add_edge(3, 'C', weight=5)
    graph_manager.add_edge(4, 'D', weight=5)
    graph_manager.add_edge(5, 'E', weight=5)

    return graph_manager

# 모듈 테스트용, 실행은 TrailBlazer.py에서!

if __name__ == "__main__":
    graph_manager = create_graph()
    graph_manager.draw_graph()
