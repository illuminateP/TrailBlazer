import networkx as nx
import matplotlib.pyplot as plt
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Line, Ellipse
from kivy.clock import Clock

# 다익스트라 알고리즘을 사용하여 그래프에서 최단 경로를 찾기
G = nx.DiGraph()
edges = [
    (1, 2, 1.0), (1, 3, 4.0),
    (2, 3, 2.0), (2, 4, 5.0),
    (3, 4, 1.0)
]
G.add_weighted_edges_from(edges)

# 출발점과 도착점을 설정하고 다익스트라 알고리즘 실행
start_node = 1
end_node = 4
path = nx.dijkstra_path(G, start_node, end_node)
path_edges = list(zip(path, path[1:]))

class GraphWidget(Widget):
    def __init__(self, **kwargs):
        super(GraphWidget, self).__init__(**kwargs)
        self.graph = G
        self.layout = FloatLayout()
        self.path = path
        self.path_edges = path_edges
        Clock.schedule_once(self.draw_graph, 1)

    def draw_graph(self, dt):
        pos = nx.spring_layout(self.graph)
        self.pos = pos
        
        with self.canvas:
            # 모든 노드를 그리기
            for node, (x, y) in pos.items():
                x = (x + 1) * self.width / 2
                y = (y + 1) * self.height / 2
                Ellipse(pos=(x - 10, y - 10), size=(20, 20))
                self.add_widget(Label(text=str(node), pos=(x - 10, y - 10), size_hint=(None, None), size=(20, 20)))

            # 모든 간선을 그리기
            Color(0, 0, 1, 1)  # 파란색
            for edge in self.graph.edges:
                x1, y1 = pos[edge[0]]
                x2, y2 = pos[edge[1]]
                x1 = (x1 + 1) * self.width / 2
                y1 = (y1 + 1) * self.height / 2
                x2 = (x2 + 1) * self.width / 2
                y2 = (y2 + 1) * self.height / 2
                Line(points=[x1, y1, x2, y2], width=2)

            # 최단 경로를 강조하여 그리기
            Color(1, 0, 0, 1)  # 빨간색
            for edge in self.path_edges:
                x1, y1 = pos[edge[0]]
                x2, y2 = pos[edge[1]]
                x1 = (x1 + 1) * self.width / 2
                y1 = (y1 + 1) * self.height / 2
                x2 = (x2 + 1) * self.width / 2
                y2 = (y2 + 1) * self.height / 2
                Line(points=[x1, y1, x2, y2], width=2)

class GraphApp(App):
    def build(self):
        return GraphWidget()

if __name__ == '__main__':
    GraphApp().run()
