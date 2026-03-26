def apresentar(nome, idade):
    return f"Olá, meu nome é {nome} e tenho {idade} anos."
def maior_de_idade(idade):
    return idade >= 18
alunos = [      
    {"nome": "Eluney", "idade": 16},
    {"nome": "Rodrigo", "idade": 16},
    {"nome": "Nathan", "idade": 18}
]
for aluno in alunos:
    print(apresentar(aluno["nome"], aluno["idade"]))
    if maior_de_idade(aluno["idade"]):
        print(f"{aluno['nome']} é maior de idade.")