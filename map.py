import networkx as nx
import matplotlib.pyplot as plt

class Graph_Manager:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node_id, **attrs):
        self.graph.add_node(node_id, **attrs)

    def add_edge(self, node1, node2, weight):
        self.graph.add_edge(node1, node2, weight=weight)

    def get_graph(self):
        return self.graph

    def dijkstra_path(self, start_node, end_node):
        return nx.dijkstra_path(self.graph, start_node, end_node, weight='weight')

    def draw_graph(self):
        pos = nx.get_node_attributes(self.graph, 'pos')
        labels = nx.get_node_attributes(self.graph, 'name')

        fig, ax = plt.subplots()

        nx.draw(self.graph, pos, with_labels=True, labels=labels, node_size=500, node_color='lightblue', font_size=10, ax=ax)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels={(u, v): d['weight'] for u, v, d in self.graph.edges(data=True)}, ax=ax)

        def on_click(event):
            x, y = event.xdata, event.ydata
            if x is None or y is None:
                return
            for node, (nx_pos, ny_pos) in pos.items():
                if (nx_pos - x) ** 2 + (ny_pos - y) ** 2 < 2000:  # 클릭 범위 설정
                    facilities = self.graph.nodes[node]['facilities']
                    self.show_facilities(ax, nx_pos, ny_pos, node, facilities)
                    break

        fig.canvas.mpl_connect('button_press_event', on_click)
        plt.show()

    def show_facilities(self, ax, x, y, node_name, facilities):
        text = f"Building: {node_name}\nFacilities: {', '.join(facilities)}"
        ax.text(x, y, text, fontsize=12, bbox=dict(facecolor='yellow', alpha=0.5))
        plt.draw()

# 그래프 인스턴스 생성 및 노드, 엣지 추가
def create_graph():
    graph_manager = Graph_Manager()
    # 노드 추가
    graph_manager.add_node('Building A', name='Building A', pos=(100, 200), facilities=['Cafe', 'Library'])
    graph_manager.add_node('Building B', name='Building B', pos=(300, 400), facilities=['Gym', 'Cafeteria'])
    graph_manager.add_node('Building C', name='Building C', pos=(500, 600), facilities=['Bookstore'])
    # 추가적인 노드 정의

    # 엣지 추가 (노드 간의 경로와 가중치)
    graph_manager.add_edge('Building A', 'Building B', weight=10)
    graph_manager.add_edge('Building B', 'Building C', weight=15)
    graph_manager.add_edge('Building A', 'Building C', weight=30)
    # 추가적인 엣지 정의

    return graph_manager

# 모듈 테스트
if __name__ == "__main__":
    graph_manager = create_graph()
    graph_manager.draw_graph()
