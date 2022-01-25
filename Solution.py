from timeit import Timer
var1 = Timer("for i in range(100):1+1")
print(var1.timeit())
