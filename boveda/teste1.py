from semanticscholar import SemanticScholar

# Inicializa o cliente
sch = SemanticScholar()

# Define o título do artigo que deseja buscar
titulo_artigo = "A survey of video human behaviour recognition Methodologies in the Perspective of Spatial-Temporal"

# Realiza a busca por artigos com o título fornecido
resultados = sch.search_paper(titulo_artigo)

# Verifica se há resultados e exibe informações do primeiro artigo encontrado
if resultados:
    primeiro_artigo = resultados[0]

    print(f"ID: {primeiro_artigo['paperId']}")
    print(f"Título: {primeiro_artigo['title']}")
    print(f"Ano de publicação: {primeiro_artigo['year']}")
    print(f"Autores: {', '.join(autor['name'] for autor in primeiro_artigo['authors'])}")
    print(f"Resumo: {primeiro_artigo['abstract']}")
    print(f"URL: {primeiro_artigo['url']}")
else:
    print("Nenhum artigo encontrado com o título fornecido.")

