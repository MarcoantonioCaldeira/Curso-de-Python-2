from typing import Any, Dict

cont_idade = 0 -> Dict[str, Any]
soma_idade = 0  # type: Dict[str, Any]
media_idade = 0  # type: Dict[str, Any]

while True:

    idade = input("Digite a sua idade: "))
    cont_idade += 1

    soma_idade=cont_idade + soma_idade
    media_idade=soma_idade / cont_idade

    if cont_idade > 1:

        desicao=input("Deseja continuar: S/N")

        if desicao == 'N':

            break
