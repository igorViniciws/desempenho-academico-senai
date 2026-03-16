from processamento import analisar_alunos, gerar_relatorio


alunos = [
    ("Igor", [8, 7.5, 9]),
    ("Maria", [5, 6]),
    ("João", [10, 9, 9]),
    ("Ana", []),
    ("Carlos", [7, 7, 8])
]


recuperacao, top_student = analisar_alunos(alunos)

gerar_relatorio(recuperacao, top_student)

print("Relatório gerado com sucesso.")