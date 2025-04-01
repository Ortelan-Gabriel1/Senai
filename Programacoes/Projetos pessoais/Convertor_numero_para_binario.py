while True:
    n = int(input("Digite o número que você deseja transformar: "))
    n1 = 0
    n2 = 0
    n3=0
    n4=0
    n5=0
    n6=0
    n7=0
    n8=0
    if n>=128:
        n1=1
        n-=128
    if n>=64:
        n2=1
        n-=64
    if n>=32:
        n3=1
        n-=32
    if n>=16:
        n4=1
        n-=16
    if n>=8:
        n5=1
        n-=8
    if n>=4:
        n6=1
        n-=4
    if n>=2:
        n7=1
        n-=2
    if n>=1:
        n8=1
        n-=1

    print   (n1,n2,n3,n4,n5,n6,n7,n8)