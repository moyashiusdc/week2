# 백트래킹 - Word Search
# 문제 링크: https://leetcode.com/problems/word-search/description/?envType=study-plan-v2&envId=top-interview-150

뒤에 0 이 생기려면 n*10이여야된다 n*2*5이되므로 2와 5의갯수를 세야한다 
근데 2는 넘쳐나니 5만 세면된다
n이 10일경우 12345678910 
여기서 5는 56789 1 그리고 10에 2번 들어가고
11 12 13 14에 2번
15에 5는 3번 들어간다
즉 5의 배수마다 0이 1개씩 늘어난다
n이 10000까지 센다고 했으므로 2000번 연속으로 늘어날것이다

count = []
for i in range(2001)
count += 1
print(coint)
