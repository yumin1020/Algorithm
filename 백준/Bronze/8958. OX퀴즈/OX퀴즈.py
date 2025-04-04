n = int(input())  # 테스트 케이스 개수 입력

for _ in range(n):
    quiz = input()  # OX 퀴즈 결과 문자열 입력
    score = 0  # 총 점수
    streak = 0  # 연속된 O의 개수

    for ch in quiz:
        if ch == 'O':
            streak += 1  # 연속된 O 개수 증가
            score += streak  # 점수에 추가
        else:
            streak = 0  # X가 나오면 연속된 O 개수 초기화

    print(score)  # 결과 출력
