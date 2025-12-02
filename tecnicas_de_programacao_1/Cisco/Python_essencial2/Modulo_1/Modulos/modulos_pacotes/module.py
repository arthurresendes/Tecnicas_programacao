print(__name__)

if __name__ == "__main__":
    print("Estou no main")
    import sys
    for p in sys.path:
        print(p)
else:
    print("Não estou no main")
    

