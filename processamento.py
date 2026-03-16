def validar_notas(notas):

    if not isinstance(notas, list):
        return False

    if len(notas) == 0:
        return False

    return True


def calcular_media(notas):
    return sum(notas) / len(notas)


def analisar_alunos(lista_alunos):

    recuperacao = []
    melhor_aluno = None
    maior_media = 0

    for nome, notas in lista_alunos:

        if not validar_notas(notas):
            print(f"Dados inválidos para {nome}")
            continue

        media = calcular_media(notas)

        if media < 7:
            recuperacao.append((nome, media))

        if media > maior_media:
            maior_media = media
            melhor_aluno = (nome, media)

    return recuperacao, melhor_aluno


def gerar_relatorio(recuperacao, melhor_aluno):

    with open("resultado.txt", "w", encoding="utf-8") as arquivo:

        arquivo.write("RELATÓRIO DE DESEMPENHO ACADÊMICO\n\n")

        arquivo.write("Alunos em Recuperação:\n")

        for nome, media in recuperacao:
            arquivo.write(f"{nome} - Média: {media:.2f}\n")

        arquivo.write("\nTop Student:\n")

        arquivo.write(f"{melhor_aluno[0]} - Média: {melhor_aluno[1]:.2f}")