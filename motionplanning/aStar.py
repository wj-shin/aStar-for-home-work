class Node(): # 노드에는 현재의 위치, g,h,f 등을 저장하는 클래스입니다.
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0
    def __eq__(self, other):
        return self.position == other.position

def astar1(map, start, end): # astar 알고리즘을 구현한 부분입니다.
    start_node = Node(None, start) # 시작노드를 설정
    start_node.g = start_node.h = start_node.f = 0 # 시작노드의 값을 초기화
    end_node = Node(None, end) # 목적지 노드를 끝노드로 설정
    end_node.g = end_node.h = end_node.f = 0 # 목적지 노드의 값들을 초기화
    open_list = [] # 경로를 초기화
    closed_list = []
    open_list.append(start_node) # 경로의 시작점은 시작노드
    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        open_list.pop(current_index)
        closed_list.append(current_node)
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # 8방향의아이 노드 생성
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1]) 
            if node_position[0] > (len(map) - 1) or node_position[0] < 0 or node_position[1] > (len(map[len(map)-1]) -1) or node_position[1] < 0:
                continue # 아이 노드가 맵안에 있는 노드인지 검색해주는 코드
            if map[node_position[0]][node_position[1]] == 1:
                continue
            new_node = Node(current_node, node_position)
            children.append(new_node) # 맵안에 있는 코드면 아이 코드 배열에 추가
        for child in children:
            for closed_child in closed_list:
                if child == closed_child:
                    continue
            child.g = current_node.g + 1 # g값 검색
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2) #H 값 계산
            child.f = child.g + child.h #F값 계산
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue 
            open_list.append(child)
def astar2(map, start, end):# 8방향으로 가게 되면 시간에 따라 변하는 영역에서 아래로 가서 피해가 버리는 현상이 생겨서 그걸 방지하려고 만든 2입니다.
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0
    open_list = []
    closed_list = []
    open_list.append(start_node)
    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        open_list.pop(current_index)
        closed_list.append(current_node)
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]
        children = []
        for new_position in [(0, 1), (-1, 0), (1, 0),  (-1, 1), (1, 1)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            if node_position[0] > (len(map) - 1) or node_position[0] < 0 or node_position[1] > (len(map[len(map)-1]) -1) or node_position[1] < 0:
                continue
            if map[node_position[0]][node_position[1]] == 1:
                continue
            new_node = Node(current_node, node_position)
            children.append(new_node)
        for child in children:
            for closed_child in closed_list:
                if child == closed_child:
                    continue
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue
            open_list.append(child)
