import matplotlib.pyplot as plt
import networkx as nx

# 创建有向图
G = nx.DiGraph()

# 添加节点和边
nodes = [
    "动物", "哺乳动物", "鸟类", "鱼类",
    "计算机", "硬件", "软件",
    "温室气体增加", "全球变暖",
    "心脏", "泵血",
    "刀", "切割",
    "猫", "狗",
    "热", "冷",
    "教师", "学生",
    "供给", "需求",
    "种子发芽", "生长",
    "城市", "国家"
]

edges = [
    ("动物", "哺乳动物"),
    ("动物", "鸟类"),
    ("动物", "鱼类"),
    ("计算机", "硬件"),
    ("计算机", "软件"),
    ("温室气体增加", "全球变暖"),
    ("心脏", "泵血"),
    ("刀", "切割"),
    ("猫", "狗"),
    ("热", "冷"),
    ("教师", "学生"),
    ("供给", "需求"),
    ("种子发芽", "生长"),
    ("城市", "国家")
]

G.add_nodes_from(nodes)
G.add_edges_from(edges)

# 绘制图形
plt.figure(figsize=(14, 10))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", arrows=True, arrowstyle='-|>', arrowsize=20)
plt.title("概念与概念之间的关系示例", fontsize=15)
plt.show()