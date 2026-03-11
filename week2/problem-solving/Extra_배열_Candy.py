# 배열 - Candy
# 문제 링크: https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150



직관적으로 12121212121...이 제일 적을것이다
예를들어 4개면 점수 2314 5개면 34251 6개면 453621 즉 짝홀에서는 1씩 늘리는걸로 되지만 홀짝일때는 안됌
음 아니다 그냥 홀짝일때 좌우변환하면 263541 이므로 성립하고 다시 1씩 늘리고 좌우변환후 2564731 성립하므로
그냥 좌우변환+1을 반복하기만 하면됨
1부터하면 1 좌우변환 1 -> 21 -> 좌우변환 12 -> 23 -> 231 -> 132 -> 243 -> 3542 -> 35421 -> 12453 -> 23564 -> 235641 

# 1. [좌 -> 우] 방향 체크 (정방향)
for i in range(1, n):
    if ratings[i] > ratings[i-1]:
        candies[i] = candies[i-1] + 1

# 2. [우 -> 좌] 방향 체크 (이게 바로 사용자님이 말씀하신 '좌우 변환'!)
for i in range(n - 2, -1, -1): # 끝에서부터 거꾸로(역순) 내려옵니다.
    if ratings[i] > ratings[i+1]:
        # 여기서 '오른쪽 아이보다 높으면 1개 더 주기' 로직이 작동하죠.
        candies[i] = max(candies[i], candies[i+1] + 1)

  https://gemini.google.com/share/8bf9a4cf534e
