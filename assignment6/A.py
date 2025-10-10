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
    def query(self, node, x):
        # returns the first hotel that works
        # if not, return 0
        if self.tree[node] < x and node == 1:
            return 0
        # updating and seraching starting from left side
        # 1, 0, n-1, index of first hotel, new value or tree[n] - x
        while self.tree[2*node] != 0 and self.tree[2*node + 1] != 0:
            if self.tree[2*node] >= x:
              node *= 2
            else:
              node = (2 * node) + 1
        # breaks loop into node
        val = self.tree[node]
        new = val - x
        print("new: ", new)
        
        #update code is bugged, need to figure out how to get the index
        st.update(1, 0, n-1, node, new)
        return val

# Main input processing
n, m = map(int, input().split())
arr = list(map(int, input().split()))
group = list(map(int, input().split()))

# Create segment tree
st = SegmentTree(arr)

res = []
# Process queries
for i in range(m):
    res.append(st.query(1, group[i]))
    
    
print(" ".join(map(str, res)))
    