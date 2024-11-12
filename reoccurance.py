def reoccurance(n) :
    my_list=["Ruturaj","is","my","first","name","whereas","patil","is","my","last","name","or","surname"]
    if n==len(my_list) :
        return
    else :
        print(my_list[n],end=" ")
        return reoccurance(n+1)
    
reoccurance(0)
