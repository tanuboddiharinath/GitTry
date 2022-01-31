# tuple,list,dict,sets

def diff(*args):
    dic = {}
    for i in args:
        if type(i) in dic:
            dic[type(i)].append(i)
        else:
            dic[type(i)] = [i]
    print(dic)
diff(1,3.44,[1,2,3,4],(1,2,3,4,4,5,5,))

