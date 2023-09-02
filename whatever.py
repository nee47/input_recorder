
def hola1():
    print("hola1")

def hola2():
    print("hola2")

def hola3():
    print("hola3")

def hola4():
    print("hola4")

def hola5():
    print("hola5")
n = input("ingresa")
func_list = [hola1, hola2, hola3, hola4, hola5][int(n)-1]
func_list()

