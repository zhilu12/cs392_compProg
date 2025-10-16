class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # Make tree size 4n to ensure enough space
        self.build(arr, 1, 0, self.n - 1)

    def build(self, arr, node, start, end):
        # Base case: leaf node
        if start == end:
            self.tree[node] = arr[start]
            return

        # Recursive case
        mid = (start + end) // 2
        # Build left and right subtrees
        self.build(arr, 2*node, start, mid)
        self.build(arr, 2*node+1, mid+1, end)

        # Combine results
        self.tree[node] = max(self.tree[2*node], self.tree[2*node+1])

    def update(self, node, start, end, index, value):
        # Base case: leaf node to be updated
        if start == end:
            self.tree[node] = value
            
            return

        mid = (start + end) // 2
        
        # Decide whether to go left or right
        if index <= mid:
            self.update(2*node, start, mid, index, value)
        else:
            self.update(2*node+1, mid+1, end, index, value)

        # Recalculate parent node sum
        self.tree[node] = max(self.tree[2*node],self.tree[2*node+1])
     
      
    # returns first hotel that fits, updates value
    # by subtracting at that node
    def query(self, node, start, end, x):
        if self.tree[node] < x:
            return -1
        
        if start == end:
            self.tree[node] -= x
            return start
        
        mid = (start + end)//2
        if self.tree[2*node] >= x:
            res = self.query(2*node, start, mid, x)
        else:
            res = self.query(2*node + 1, mid + 1, end, x)

        self.tree[node] = max(self.tree[2*node],self.tree[2*node+1])
        return res


        

# Main input processing
n, m = map(int, input().split())
arr = list(map(int, input().split()))
group = list(map(int, input().split()))

# Create segment tree
st = SegmentTree(arr)

res = []
# Process queries
for i in range(m):
    val = st.query(1, 0, n-1, group[i])

    res.append(0 if val == -1 else val + 1)
    
    
print(" ".join(map(str, res)))
    