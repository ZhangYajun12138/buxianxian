# coding:utf-8
# yield

def fib(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
        yield a

def test_yield():
    print("yield-----")
    yield


def main():
    # for vol in fib(20):
    #     print(vol)
    t = test_yield()
    t.__next__()

if __name__ == '__main__':
    main()