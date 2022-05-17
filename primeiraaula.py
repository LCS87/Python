contador = 0              
while contador < 10:
    contador  = contador + 1
    if contador == 1:
        print(contador, "item limpo")
    else:
        print(contador, "intens limpos")
        
print("fim da repetiçõa do bloco while")


contador = 0
while True:
    if contador < 10:
        contador = contador + 1
        if contador == 1:
            print("item limpo")
        else:
            print("itens limpos")
          
    else:  
        break
print("fim da repetiçõa do bloco while")     




texto = input("digite a sua senha : ")   
        
while texto != 'lestscode':
    texto = input('senha invalida tente novamente')
    
    print('acesso permitido ')
    
            
