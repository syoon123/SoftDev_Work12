import time

def wrapper( f ):
    def inner( *arg ):       
        print f.func_name + ": (" + str(arg[0]) + ",)" 
        return f( *arg )
    return inner

def timelog(f):
    def inner( *arg):
        start = time.time()
        f( *arg)
        end = time.time()
        return end - start
    return inner
    
@wrapper
def fact(num):
    if num == 0:
        return 1
    else:
        return fact(num - 1) * num

print fact(5)

@timelog
def fib(num):
    if num == 1 or num==2:
        return 1
    else:
        return fib(num-1) + fib(num-2)

print fib(32)
