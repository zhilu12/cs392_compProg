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
        self.tree[node] = self.tree[2*node] + self.tree[2*node+1]

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
        self.tree[node] = self.tree[2*node] + self.tree[2*node+1]

    def query(self, node, start, end, left, right):
        # No overlap
        if right < start or left > end:
            return 0

        # Complete overlap
        if left <= start and end <= right:
            return self.tree[node]

        # Partial overlap
        mid = (start + end) // 2
        left_sum = self.query(2*node, start, mid, left, right)
        right_sum = self.query(2*node+1, mid+1, end, left, right)

        return left_sum + right_sum

# Main input processing
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Create segment tree
st = SegmentTree(arr)

# Process queries
for _ in range(m):
    query = list(map(int, input().split()))

    if query[0] == 1:
        # Update operation
        _, i, v = query
        st.update(1, 0, n-1, i, v)
    else:
        # Sum query: adjust right bound by -1 to query closed interval
        _, l, r = query
        print(st.query(1, 0, n-1, l, r - 1))