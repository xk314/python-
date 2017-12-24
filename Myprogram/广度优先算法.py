'''
广度优先搜索（一种图算法）能够找出两样东西之间的最短距离
解决最短路径问题的算法被称为广度优先搜索
广度优先搜索是一种用于图的查找算法，可用于解决两种问题：
从节点a出发是否可以到达节点b；从节点a出发到节点b，哪条路径最短
在广度优先搜索的过程中，搜索范围从起点开始逐渐向外延伸，即先检查一度关系，再检查二度关系。
图可以使用散列表表示，python中字典类型即为散列表

最短路径只是段数最少，但不是最快的路径。如果要找出最快的路径需要使用迪克斯特拉算法。


'''

from collections import deque  #导入队列类
graph = {}  #以字典这种散列表来表示图
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

def person_is_seller(name):
    return name[-1] == 'm'
'''
def search(name):#该函数可以保证按照广度优先从距离最近的对象开始判断
    search_queue = deque() #使用队列来保存查找顺序
    search_queue += graph[name]#依照距离的远近向队列中添加要查找的对象
    searched = []  #保存已经查找过的对象，避免重复
    while search_queue: #依照远近顺序判断队列中的对象，直到队列为空
        person = search_queue.popleft()#从队列中弹出待检查的对象
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is a seller')
                return True
            else:
                search_queue += graph[person]#向搜索队列中添加待检查的对象
                searched.append(person)#将已经检查过的对象记录下来
    return False

# search('you')

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is a seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
    
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is a seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
    
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    print(search_queue)
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is a seller')
                return True
            else:
                searched.append(person)
                search_queue += graph[person]
    return False
   
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is a seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
    
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
  
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
   
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is a seller')
                return
            else:
                searched.append(person)
                search_queue += graph[person]
    return False
 

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is a seller')
                return True
            else:
                searched.append(person)
                search_queue += graph[person]
    return False

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is a seller')
                return True
            else:
                searched.append(person)
                search_queue += graph[person]
    return False


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is seller')
                return True
            else:
                searched.append(person)
                search_queue += graph[person]
    return False
   
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is seller')
                return True
            else:
                searched.append(person)
                search_queue += graph[person]
    return False

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is seller')
                return True
            else:
                searched.append(person)
                search_queue += graph[person]
    return False
'''
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False



search('you')
