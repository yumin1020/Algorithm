A, B = map(int, input().split())

def compare(A, B):
    if(A > B):
        print('>')
    elif(A < B):
        print('<')
    elif(A == B):
        print('==')

compare(A, B)