#!/usr/bin/env python
# coding: utf-8

# In[55]:


print('§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§')
print('§§§§§ armazenamento de dados em um arquivo §§§§§'.upper())
print('§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§\n')

pessoa = str(input('Qual o seu nome? '))
cpf = int(input('Digite seu CPF: '))
cep = int(input('Qual o seu CEP? '))

d = open('usuarios.txt', 'a') #criação de um arquivo e adição de dados
d.write('Nome: {} - CPF: {} - CEP: {}\n'.format(pessoa,cpf,cep))
d.close()

print('dados armazenados com sucesso!'.upper())


# In[ ]:





# In[ ]:





# In[ ]:




