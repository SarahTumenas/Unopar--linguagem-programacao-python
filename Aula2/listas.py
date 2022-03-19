# List comprehension (Compreensões de lista)
#É uma estrutura de dados do tipo sequencial que possui como principal característica ser mutável

linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]
print("Antes da listcomp = ", linguagens)

# como se trata da criação de uma lista, usam-se colchetes! Dentro do colchetes há
# uma variável chamada "item" que representará cada valor da lista original. Veja que usamos item.lower() for
# item in linguagens, e o resultado foi guardado dentro da mesma variável original, ou seja, sobrescrevemos o
# valor de "linguagens".

linguagens = [item.lower() for item in linguagens]

print("\nDepois da listcomp = ", linguagens)
