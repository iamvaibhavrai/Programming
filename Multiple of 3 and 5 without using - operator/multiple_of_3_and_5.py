def main():
    n = int(input())
    for i in range(1,n+1):
        if i/3 == i//3:
            print("Multiple of 3.",end='')
        if i/5 == i//5:
            print("Multiple of 5.",end='')
        if i/5 != i//5 and i/3 != i//3:
            print(i,end='')
        print('')

if __name__ == '__main__':
    main()
