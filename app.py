# Lista de frutas
frutas = ["Laranja", "Cajá", "Caju", "Goiaba", "Maçã", "Morango", "Uva"]

# Exibir a lista original
for i in range(len(frutas)):
    print(f"índice {i}: {frutas[i]}")

# usuário deve informar o índice que deseja deletar
try:
    indice = int(input("Informe o indice da fruta que deseja deletar: "))
    confirmacao = input(f"Deseja deletar a fruta {frutas[indice]}? Digite 'sim' para confirmar.")

    if confirmacao == "sim":
        del(frutas[indice])
        print("Fruta deletada com sucesso.")
    else:
        ...
except Exception as e:
    print(f"Não foi possível deletar a fruta. {e}")
finally:
    # exibe a lista atualizada
    for i in range(len(frutas)):
        print(f"Índice {i}: {frutas[i]}.")