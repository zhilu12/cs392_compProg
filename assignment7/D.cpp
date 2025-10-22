#include <cstdio>

const int N = 1e5; // limit for array size
int n;             // array size
int q;
int t[2 * N];

void build()
{ // build the tree
  for (int i = n - 1; i > 0; --i)
    t[i] = t[i << 1] ^ t[i << 1 | 1];
}

void modify(int p, int value)
{ // set value at position p
  for (t[p += n] = value; p > 1; p >>= 1)
    t[p >> 1] = t[p] ^ t[p ^ 1];
}

int query(int l, int r)
{ // sum on interval [l, r)
  int res = 0;
  for (l += n, r += n; l < r; l >>= 1, r >>= 1)
  {
    if (l & 1)
      res ^= t[l++];
    if (r & 1)
      res ^= t[--r];
  }
  return res;
}

int main()
{
  scanf("%d %d", &n, &q);
  for (int i = 0; i < n; ++i)
    scanf("%d", t + n + i);
  build();
  for (int i = 0; i < q; ++i)
  {
    int l, r;
    scanf("%d %d", &l, &r);
    int ans = query(l - 1, r);
    printf("%d\n", ans);
  }
  return 0;
}