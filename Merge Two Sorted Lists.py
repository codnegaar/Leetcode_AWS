class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def merge(l1: Node, l2: Node) -> Node:
    # WRITE YOUR BRILLIANT CODE HERE
    return None

def build_list(nodes, f):
    val = next(nodes, None)
    if val is None: return None
    nxt = build_list(nodes, f)
    return Node(f(val), nxt)

def format_list(node):
    if node is None: return
    yield str(node.val)
    yield from format_list(node.next)

if __name__ == '__main__':
    l1 = build_list(iter(input().split()), int)
    l2 = build_list(iter(input().split()), int)
    res = merge(l1, l2)
    print(' '.join(format_list(res)))
