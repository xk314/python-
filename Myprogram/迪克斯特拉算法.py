'''
图(散列表)graph 中保存着每个节点的邻居和前往邻居的开销
节点的开销是指从起点出来前往该节点需要多长时间
对于不知道开销的节点将其设置为无限大 infinity = float('inf')
'''
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

#创建开销表
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity
#存储父节点的散列表
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = 'None'
#记录处理过的节点的列表
processed = []