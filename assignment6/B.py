class SegmentTree:
    def __init__(self, arr, isRight:bool):
        self.n = len(arr)
        self.isRight = isRight
        self.tree = [float('inf')] * (4 * self.n)  # Make tree size 4n to ensure enough space
        self.build(arr, 1, 0, self.n - 1)
        

    def build(self, arr, node, start, end):
        # Base case: leaf node
        if start == end:
            if self.isRight:
                self.tree[node] = arr[start] + start
            else:
                self.tree[node] = arr[start] - start
            return

        # Recursive case
        mid = (start + end) // 2
        # Build left and right subtrees
        self.build(arr, 2*node, start, mid)
        self.build(arr, 2*node+1, mid+1, end)

        # Combine results
        self.tree[node] = min(self.tree[2*node], self.tree[2*node+1])

    def update(self, node, start, end, index, value):
        # Base case: leaf node to be updated
        if start == end:
            if self.isRight:
                self.tree[node] = value + start
            else:
                self.tree[node] = value - start
            return

        mid = (start + end) // 2
        
        # Decide whether to go left or right
        if index <= mid:
            self.update(2*node, start, mid, index, value)
        else:
            self.update(2*node+1, mid+1, end, index, value)

        # Recalculate parent node sum
        self.tree[node] = min(self.tree[2*node],self.tree[2*node+1])
     
      
    # finds the right or left min based on k
    def query(self, node, start, end, left, right):
        # No overlap
        if right < start or left > end:
            return float('inf')

        # Complete overlap
        if left <= start and end <= right:
            return self.tree[node]

        # Partial overlap
        mid = (start + end) // 2
        leftMin = self.query(2*node, start, mid, left, right)
        rightMin = self.query(2*node+1, mid+1, end, left, right)

        return min(leftMin, rightMin)


        

# Main input processing
n, q = map(int, input().split())
arr = list(map(int, input().split()))

# Create segment tree
rMin = SegmentTree(arr, True)
lMin = SegmentTree(arr, False)

res = []
# Process queries
for _ in range(q):
    q = list(map(int, input().split()))

    if q[0] == 1:
        _, k, x = q
        k -= 1
        rMin.update(1, 0, n-1, k, x)
        lMin.update(1, 0, n-1, k, x)

    else:
        _, k = q
        k -= 1
        leftMin = lMin.query(1, 0, n-1, 0, k)
        rightMin = rMin.query(1, 0, n-1, k, n-1)

        print(min(k + leftMin, -k + rightMin))
    