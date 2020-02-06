for i in range(1,int(input())+1):
    if i%5==0:
        if i%7==0:
            print('FooBar')
        else:
            print('Foo')
    elif i%7==0:
        print('Bar')
    else:
        print(i)