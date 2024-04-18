def serie(num):
    a,b=0,1
    lista=[]
    for i in range(num):
        if b>num:return lista
        else:
            lista.append(b)
            b,a=b+a,b
print(serie(42))
