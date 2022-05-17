import math
import  threading

def thread (i, j, A):
    A[j] = A[j] + A [j-pow(2,i-1)]
    print(A)

def sumaCREW():
    A = [0,5,2,10,1,8,12,7,3]
    n = len(A)
    lg = int(math.log(n,2))
    for i in range( 1, lg-1):
        for j in range((pow(2,i-1)+1),n):
            t = threading.Thread(target=thread(i,j,A))
            t.start()
            t.join()
            print(A)
    print(A)


def main():
    sumaCREW()

if __name__ == '__main__':
    main()