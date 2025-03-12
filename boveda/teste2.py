#!/usr/bin/python3

from semanticscholar import SemanticScholar

# Inicializa o cliente
sch = SemanticScholar()

# Define o título do artigo a ser pesquisado
titulo_artigo = "A survey of video human behaviour recognition Methodologies in the Perspective of Spatial-Temporal"

# Busca o artigo pelo título
resultados = sch.search_paper(titulo_artigo)

# Verifica se encontrou algum artigo
if resultados:
    primeiro_artigo = resultados[0]
    paper_id = primeiro_artigo['paperId']  # Obtém o ID do artigo

    '''
    # Busca os detalhes do artigo, incluindo os artigos que o citaram
    artigo_completo = sch.get_paper(paper_id, fields=[ "citations"])
        
    print("\nArtigos que citaram este artigo:")
    for citacao in artigo_completo.citations:
        print(f"- {citacao}")
        
    '''
    artigo_completo = sch.get_paper(paper_id, fields=[ "references"])
    # Exibir as referências (artigos citados por este artigo)
    print("\nReferências deste artigo:")
    for referencia in artigo_completo.references:
        print(f"- {referencia})")
    
else:
    print("Nenhum artigo encontrado com o título fornecido.")

