class Queue:
    def __init__(self):
        self.__lista = []
        self.__count = 0

    def put(self, elem):
        self.__lista.insert(0,elem)
        self.__count += 1
        return elem

    def get(self):
        if self.__count == 0:
            return None
        
        elem = self.__lista.pop() 
        self.__count -= 1
        return elem

que = Queue()
print(que.put(1))
print(que.put("dog"))
print(que.put(False))
try:
    for i in range(4):
        print(que.get())
except:
    print("Erro da fila")
