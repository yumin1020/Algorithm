def boxes_need():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    M = int(data[1])

    # 책의 개수가 0인 경우
    if N == 0:
        print(0)
        return
    
    
    weights = list(map(int, data[2:]))

    boxes = 0
    box_weight = 0

    for weight in weights:
        if box_weight + weight > M:
            boxes += 1
            box_weight = weight
        else:
            box_weight += weight

    if box_weight > 0:
        boxes += 1

    print(boxes)

boxes_need()