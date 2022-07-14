def plusMinus(arr):
    positive = [a for a in arr if a > 0]
    zeros = [a for a in arr if a == 0]
    negative = [a for a in arr if a < 0]

    print(format(len(positive)/len(arr), '.6f'))
    print(format(len(negative)/len(arr), '.6f'))
    print(format(len(zeros)/len(arr), '.6f'))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
