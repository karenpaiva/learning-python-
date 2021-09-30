if __name__ == '__main__':
    n = int(input())
    l=[]
    for i in range (n):
        l.append(str(i+1))
        i+=1
        ls=''.join(l)
    print(ls)
       