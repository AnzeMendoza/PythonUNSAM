
def geringoso(palabra = "Geringoso"):
    pal = ""
    silabas = "AaEeIiOoUu"
    
    for i in palabra:
        if silabas.find(i) > 0:
            pal+=f'{i}p{i.lower()}'
        else:
            pal+=i
    print(pal)

def main():
    geringoso()
    
if __name__ == '__main__':  
    main()
