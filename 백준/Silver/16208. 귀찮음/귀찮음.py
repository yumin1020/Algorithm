import heapq

def minimum_cut_cost(n, lengths):
    # 힙 초기화
    heapq.heapify(lengths)
    total_cost = 0

    while len(lengths) > 1:
        # 가장 작은 두 원소를 꺼내기
        first = heapq.heappop(lengths)
        second = heapq.heappop(lengths)

        # 두 막대를 자르는 비용 계산
        cost = first * second
        total_cost += cost

        # 새로운 막대 길이 추가
        heapq.heappush(lengths, first + second)

    return total_cost

# 입력 예시
n = int(input())
lengths = list(map(int, input().split()))
print(minimum_cut_cost(n, lengths))
