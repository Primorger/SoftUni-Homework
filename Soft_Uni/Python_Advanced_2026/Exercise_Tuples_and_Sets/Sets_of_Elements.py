n_length, m_length = input().split()

n_length = int(n_length)
m_length = int(m_length)

n = set()
m = set()

for _ in range(n_length):
    n.add(int(input()))

for _ in range(m_length):
    m.add(int(input()))

result = n & m

print(*result, sep="\n")