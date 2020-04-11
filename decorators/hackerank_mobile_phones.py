def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            if len(l[i]) > 10:
                l[i] = l[i][len(l[i]) - 10:]
        l_new = [ "+91 " + str(l[i][0:5]) + " " + str(l[i][5:]) for i in range(len(l))]    
        return f(l_new)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

ls = ['07895462130', '919875641230', '9195969878']

sort_phone(ls)
