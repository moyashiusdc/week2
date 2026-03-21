# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173


def go(x, y):
  if x >= N or y >= N:
    return False

if board[x][y] == -1:
  return True

jump = board[x][y]

if go(x + jump, y):
  return True

return False

if go(0,0)
print("haruharu")
      else:
print("hing")
