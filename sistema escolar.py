# ==========================================
# SISTEMA ESCOLAR
# ==========================================

# Lista que armazenará todos os alunos
alunos = []


# ==========================================
# FUNÇÕES
# ==========================================

def calcular_media(notas):
    """Calcula a média das notas do aluno."""
    return sum(notas) / len(notas)


def verificar_situacao(media):
    """Define a situação do aluno de acordo com a média."""

    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def cadastrar_aluno():
    """Cadastra um novo aluno."""

    print("\n===== CADASTRO DE ALUNO =====")

    nome = input("Digite o nome do aluno: ").strip()

    if nome == "":
        print("O nome não pode ficar vazio.")
        return

    notas = []

    for i in range(1, 5):

        while True:

            try:
                nota = float(input(f"Digite a nota {i} do aluno: "))

                if nota < 0 or nota > 10:
                    print("A nota deve estar entre 0 e 10.")
                else:
                    notas.append(nota)
                    break

            except ValueError:
                print("Digite apenas números.")

    media = calcular_media(notas)
    situacao = verificar_situacao(media)

    aluno = {
        "nome": nome,
        "notas": notas,
        "media": media,
        "situacao": situacao
    }

    alunos.append(aluno)

    print("\nAluno cadastrado com sucesso!")
    print(f"Nome: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")


def listar_alunos():
    """Exibe todos os alunos cadastrados."""

    print("\n===== LISTA DE ALUNOS =====")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    for i, aluno in enumerate(alunos, start=1):

        print(
            f"{i}. {aluno['nome']} "
            f"| Média: {aluno['media']:.2f} "
            f"| Situação: {aluno['situacao']}"
        )


def buscar_aluno():
    """Busca um aluno pelo nome."""

    print("\n===== BUSCAR ALUNO =====")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    nome_busca = input("Digite o nome do aluno: ").strip().lower()

    encontrado = False

    for aluno in alunos:

        if aluno["nome"].lower() == nome_busca:

            print("\n===== ALUNO ENCONTRADO =====")
            print(f"Nome: {aluno['nome']}")
            print(f"Notas: {aluno['notas']}")
            print(f"Média: {aluno['media']:.2f}")
            print(f"Situação: {aluno['situacao']}")

            encontrado = True
            break

    if not encontrado:
        print("Aluno não encontrado.")


def relatorio_geral():
    """Exibe um relatório completo dos alunos."""

    print("\n===== RELATÓRIO GERAL =====")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    total_alunos = len(alunos)
    aprovados = 0
    recuperacao = 0
    reprovados = 0

    for aluno in alunos:

        if aluno["situacao"] == "Aprovado":
            aprovados += 1

        elif aluno["situacao"] == "Recuperação":
            recuperacao += 1

        else:
            reprovados += 1

    print(f"Total de alunos: {total_alunos}")
    print(f"Aprovados: {aprovados}")
    print(f"Recuperação: {recuperacao}")
    print(f"Reprovados: {reprovados}")


def menu():
    """Exibe o menu principal."""

    while True:

        print("\n================================")
        print("        SISTEMA ESCOLAR")
        print("================================")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Buscar aluno")
        print("4 - Relatório geral")
        print("5 - Sair")
        print("================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()

        elif opcao == "2":
            listar_alunos()

        elif opcao == "3":
            buscar_aluno()

        elif opcao == "4":
            relatorio_geral()

        elif opcao == "5":
            print("\nEncerrando o sistema...")
            break

        else:
            print("\nOpção inválida. Escolha uma opção de 1 a 5.")


# ==========================================
# EXECUÇÃO DO SISTEMA
# ==========================================

print("================================")
print("     BEM-VINDO AO SISTEMA")
print("================================")

menu()
