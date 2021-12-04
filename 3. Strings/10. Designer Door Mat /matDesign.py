# Enter your code here. Read input from STDIN. Print output to STDOUT

def main():
   
    N,M = input().split()
    N = int(N)
    M = int(M)
    
    for i in range(N):
        if i == N//2:
            print("WELCOME".center(M,"-"))
        else:
            if i < N/2:
                j = 2*i + 1
                print(((".|.")*(j)).center(M,"-"))
            else:
                print(((".|.")*(j)).center(M,"-"))
                j = j - 2

if __name__ == "__main__":
    main()