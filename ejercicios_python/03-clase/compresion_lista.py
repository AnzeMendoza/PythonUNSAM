#%%
a = [i for i in range(1,6)]
print(a)
b = [2*x for x in a]
print(b)
#%%
nombres = ['Franquito','Sucho']
print(nombres)

a = [nombre.lower() for nombre in nombres]
print(a)
#%%
a = [1, -5, 4, 2, -2, 10]
b = [2*x for x in a if x>=10]
print(b)
#%%