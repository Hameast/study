# 노드 클래스 구현
class Node:
    def __init__(self, val=None, link=None):
        self.val = val
        self.link = link


# 링크드 리스트 클래스 구현
class LinkedList:
    # 생성자
    # head와 curr를 입력으로 받지만 기본값은 설정해 뒀읍니다.
    def __init__(self, head=None, curr=0):
        self.head = head
        self.curr = curr
        self.size = 0

    # 인덱스와 값을 입력받습니다.
    # 입력받은 값을 가지는 노드를 생성합니다.
    # 인덱스 값이 가리키는 곳까지 curr를 이동시킵니다
    # 새로 생성한 노드의 링크값을 curr의 링크로 저장하고
    # curr의 링크를 새로생성한 노드로 저장합니다.
    def insert(self, index, val=0):
        self.curr = self.head
        node = Node(val)

        cnt = 0
        while cnt != index and self.curr.link:
            self.curr = self.curr.link
            cnt += 1

        node.link = self.curr.link
        self.curr.link = node
        self.size += 1

    # 인덱스를 입력받습니다.
    # 인덱스 값이 가리키는 곳까지 curr를 이동시킵니다
    # curr의 링크가 다다음 노드를 가르키게 함으로써
    # 다음 노드를 삭제할 수 있습니다.
    def delete(self, index):
        self.curr = self.head

        cnt = 0
        while cnt != index and self.curr.link:
            self.curr = self.curr.link
            cnt += 1

        self.curr.link = self.curr.link.link
        self.size -= 1

    # linked list가 가진 값들을 모두 출력합니다.
    def print(self):
        self.curr = self.head
        while self.curr:
            print(self.curr.val)
            self.curr = self.curr.link