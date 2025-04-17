import random

from frases import frases



rimas = []

assuntos = []

versos= []


def verAssunto(a):
    b = False
    
    if a in assuntos:
        b = True
    return b

def verRima(a):
    b = False
    
    if a in rimas:
        b = True
    return b


for frase in frases:
    if verAssunto(frase[1])  == False:
        assuntos.append(frase[1])
    if verRima(frase[2])  == False:
        rimas.append(frase[2])
    
    versos.append(frase[0] if frase[0] not in versos else None)
        
        
    rimas.sort()
    assuntos.sort()

print(len(versos))

estilos= ["soneto","hakai", "aleatorio"]

listaHakai = []



def exibirEstatisticas():
    """Exibe estatísticas sobre o conteúdo."""
    print(f"Total de frases: {len(frases)}")
    print(f"Total de assuntos: {len(set(assuntos))}")
    print(f"Total de rimas: {len(rimas)}")


# funções Externas
def carregarFrasesDeArquivo(caminho_arquivo):
    """Carrega frases, assuntos e rimas de um arquivo externo."""
    global assuntos, rimas
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            frase, assunto, rima = linha.strip().split(';')
            assuntos.append((frase, assunto))
            rimas.append((frase, rima))

def salvarPoemaEmArquivo(poema, caminho_arquivo):
    """Salva o poema gerado em um arquivo de texto."""
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write('\n'.join(poema))
        print(f"Poema salvo em {caminho_arquivo}")

def gerarHaikai():
    """Gera um haikai com 3 versos (5, 7, 5 sílabas)."""
    if len(rimas) >= 3:
        random.shuffle(rimas)
        print(rimas[0])  # 5 sílabas
        print(rimas[1])  # 7 sílabas
        print(rimas[2])  # 5 sílabas
    else:
        print("Não há rimas suficientes para gerar um haikai.")

def listarAssuntosDisponiveis():
    """Lista todos os assuntos disponíveis."""
    print("Assuntos disponíveis:")
    for assunto in set([a[1] for a in assuntos]):
        print(f"- {assunto}")

def listarRimasDisponiveis():
    """Lista todas as rimas disponíveis."""
    print("Rimas disponíveis:")
    for rima in set([r[1] for r in rimas]):
        print(f"- {rima}")

def gerarPoemaComEstilo(estilo, assunto=None):
    """Gera um poema com base no estilo escolhido."""
    if estilo == "soneto":
        gerarSoneto(assunto)
    elif estilo == "haikai":
        gerarHaikai()
    elif estilo == "aleatorio":
        gerarpoemaAleatorio(10)
    else:
        print(f"Estilo '{estilo}' não reconhecido.")

def contarFrasesPorAssunto():
    """Conta e exibe o número de frases disponíveis para cada assunto."""
    contagem = {}
    for _, assunto in assuntos:
        contagem[assunto] = contagem.get(assunto, 0) + 1
    for assunto, quantidade in contagem.items():
        print(f"{assunto}: {quantidade} frases")


def removerFrase(frase):
    """Remove uma frase específica das listas de assuntos e rimas."""
    global assuntos, rimas
    assuntos = [a for a in assuntos if a[0] != frase]
    rimas = [r for r in rimas if r[0] != frase]
    print(f"Frase '{frase}' removida.")

def gerarPoemaComTamanhoFixo(tamanho):
    """Gera um poema com um número fixo de caracteres."""
    poema = []
    total_caracteres = 0
    random.shuffle(versos)
    for frase in versos:
        if total_caracteres + len(frase) <= tamanho:
            poema.append(frase)
            total_caracteres += len(frase)
        else:
            break
    print('\n'.join(poema))

def buscarFrasePorPalavraChave(palavra):
    """Busca frases que contenham uma palavra-chave."""
    resultados = [frase for frase, _ in assuntos if palavra in frase]
    if resultados:
        print("Frases encontradas:")
        for frase in resultados:
            print(f"- {frase}")
    else:
        print(f"Nenhuma frase encontrada com a palavra-chave '{palavra}'.")



def gerarPoemaComTamanhoFixoPorAssunto(tamanho,assunto):
    """Gera um poema com um número fixo de caracteres."""
    poema = []
    total_caracteres = 0

    random.shuffle(frases)
    listapoema = []
    
    for frase in frases:
        if frase[1] == assunto:
            if total_caracteres + len(frase) <= tamanho:
                listapoema.append(frase[0])
                total_caracteres += len(frase)
        else:
            break
        
    print('\n'.join(poema))

def editarFrase(frase_antiga, nova_frase, novo_assunto, nova_rima):
    """Edita uma frase existente, alterando seu texto, assunto ou rima."""
    global assuntos, rimas
    for i, (frase, assunto) in enumerate(assuntos):
        if frase == frase_antiga:
            assuntos[i] = (nova_frase, novo_assunto or assunto)
    for i, (frase, rima) in enumerate(rimas):
        if frase == frase_antiga:
            rimas[i] = (nova_frase, nova_rima or rima)
    print(f"Frase '{frase_antiga}' editada com sucesso.")

def gerarPoemaComRimasAlternadas(rima_a, rima_b, linhas_por_estrofe):
    """Gera um poema com rimas alternadas (ABAB)."""
    if verRima(rima_a) and verRima(rima_b):
        for _ in range(linhas_por_estrofe // 2):
            gerarpoemaPorRimas(rima_a, 1)
            gerarpoemaPorRimas(rima_b, 1)
        separarEstrofes()
    


def gerarPoemaAcrostico(palavra, assunto):

    palavra = palavra.upper()
    frases_filtradas = [frase for frase  in assuntos if not assunto or assunto in frase]
    if len(frases_filtradas) < len(palavra):
        print("Não há frases suficientes para gerar o acróstico.")
        return
    for letra in palavra:
        for frase in frases_filtradas:
            if frase.startswith(letra):
                print(frase)
                frases_filtradas.remove(frase)
                break
        else:
            print(f"(Nenhuma frase encontrada para a letra '{letra}')")

def gerarPoemaCircular(assunto, linhas):
    if verAssunto(assunto):
        frases_filtradas = [frase for frase in assuntos if assunto in frase]
        random.shuffle(frases_filtradas)
        poema = frases_filtradas[:linhas]
        if len(poema) > 1:
            poema[-1] += f" ({poema[0]})"  # Conecta o último verso ao primeiro
        print('\n'.join(poema))
    else:
        print(f"Assunto '{assunto}' não encontrado.")

def gerarPoemaAleatorioComRestricoes(linhas, incluir=None, evitar=None):
    """Gera um poema aleatório com palavras obrigatórias ou proibidas."""
    incluir = incluir or []
    evitar = evitar or []
    poema = []
    for frase, _ in assuntos:
        if any(palavra in frase for palavra in incluir) and not any(palavra in frase for palavra in evitar):
            poema.append(frase)
            if len(poema) == linhas:
                break
    if poema:
        print('\n'.join(poema))
    else:
        print("Nenhuma frase atende às restrições.")

def gerarPoemaComEstrofesFixas(assunto, estrofes, linhas_por_estrofe):
    """Gera um poema com um número fixo de estrofes e linhas por estrofe."""
    if verAssunto(assunto):
        for _ in range(estrofes):
            gerarpoemaPorAssunto(assunto, linhas_por_estrofe)
            separarEstrofes()
    else:
        print(f"Assunto '{assunto}' não encontrado.")

def filtrarFrasesPorTamanho(min_caracteres, max_caracteres):
    """Filtra frases com base no número de caracteres."""
    frases_filtradas = [
        frase for frase in assuntos
        if (min_caracteres is None or len(frase) >= min_caracteres) and
            (max_caracteres is None or len(frase) <= max_caracteres)
    ]
    print("Frases filtradas:")
    print('\n'.join(frases_filtradas) if frases_filtradas else "Nenhuma frase encontrada.")

def salvarEstatisticasEmArquivo(caminho_arquivo):
    """Salva as estatísticas em um arquivo de texto."""
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(f"Total de frases: {len(assuntos)}\n")
        arquivo.write(f"Total de assuntos: {len(set([a[1] for a in assuntos]))}\n")
        arquivo.write(f"Total de rimas: {len(set([r[1] for r in rimas]))}\n")
    print(f"Estatísticas salvas em {caminho_arquivo}")

def buscarFrasesPorMultiplasPalavrasChave(palavras, todas=True):
    """Busca frases que contenham todas ou qualquer uma das palavras-chave."""
    resultados = []
    for frase, _ in assuntos:
        if todas and all(palavra in frase for palavra in palavras):
            resultados.append(frase)
        elif not todas and any(palavra in frase for palavra in palavras):
            resultados.append(frase)
    if resultados:
        print("Frases encontradas:")
        print('\n'.join(resultados))
    else:
        print("Nenhuma frase encontrada com as palavras-chave fornecidas.")

def gerarPoemaComRimasEspecificas(rimas_especificas, linhas):
    """Gera um poema com rimas específicas fornecidas."""
    poema = []
    for rima in rimas_especificas:
        for frase, r in rimas:
            if r == rima:
                poema.append(frase)
                if len(poema) == linhas:
                    break
        if len(poema) == linhas:
            break
    if poema:
        print('\n'.join(poema))
    else:
        print("Não foi possível gerar um poema com as rimas fornecidas.")

def exportarFrasesFiltradas(caminho_arquivo, assunto=None, rima=None, min_caracteres=None, max_caracteres=None):
    """Exporta frases filtradas para um arquivo de texto."""
    frases_filtradas = [
        frase for frase, a in assuntos
        if (assunto is None or a == assunto) and
            (rima is None or any(r == rima for f, r in rimas if f == frase)) and
            (min_caracteres is None or len(frase) >= min_caracteres) and
            (max_caracteres is None or len(frase) <= max_caracteres)
    ]
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write('\n'.join(frases_filtradas))
    print(f"Frases exportadas para {caminho_arquivo}")

def importarFrasesDeMultiplosArquivos(lista_caminhos):
    """Importa frases de múltiplos arquivos."""
    global assuntos, rimas
    for caminho in lista_caminhos:
        carregarFrasesDeArquivo(caminho)
    print("Frases importadas com sucesso.")

def gerarPoemaComEstruturaPersonalizada(estrutura, assunto=None):
    """Gera um poema com uma estrutura personalizada (ex.: ABBA, AABB)."""
    poema = []
    for rima in estrutura:
        for frase, r in rimas:
            if r == rima and (assunto is None or any(a == assunto for f, a in assuntos if f == frase)):
                poema.append(frase)
                break
    if len(poema) == len(estrutura):
        print('\n'.join(poema))
    else:
        print("Não foi possível gerar o poema com a estrutura fornecida.")

def removerFrasesDuplicadas():
    """Remove frases duplicadas das listas globais."""
    global assuntos, rimas, versos
    frases_unicas = set()
    assuntos = [(f, a) for f, a in assuntos if not (f in frases_unicas or frases_unicas.add(f))]
    rimas = [(f, r) for f, r in rimas if f in frases_unicas]
    versos = [v for v in versos if v in frases_unicas]
    print("Frases duplicadas removidas.")

def gerarPoemaComPalavrasObrigatorias(linhas, palavras):
    """Gera um poema que inclua obrigatoriamente palavras fornecidas."""
    poema = []
    for frase, _ in assuntos:
        if all(palavra in frase for palavra in palavras):
            poema.append(frase)
            if len(poema) == linhas:
                break
    if poema:
        print('\n'.join(poema))
    else:
        print("Nenhuma frase atende às palavras obrigatórias fornecidas.")

def listarFrasesPorAssuntoOrdenadas(assunto):
    """Lista frases de um assunto específico em ordem alfabética."""
    frases = [f for f, a in assuntos if a == assunto]
    if frases:
        print(f"Frases do assunto '{assunto}':")
        print('\n'.join(sorted(frases)))
    else:
        print(f"Nenhuma frase encontrada para o assunto '{assunto}'.")

def gerarPoemaComLimiteDePalavras(limite_palavras):
    """Gera um poema com um número máximo de palavras."""
    poema = []
    total_palavras = 0
    for frase in versos:
        palavras = len(frase.split())
        if total_palavras + palavras <= limite_palavras:
            poema.append(frase)
            total_palavras += palavras
        else:
            break
    print('\n'.join(poema))



def separarEstrofes():
    print("\n---\n")
    
    return("\n---\n")



def gerarpoemaPorAssunto(assunto, linhas):
    
    listapoema = []
    listaRetorno = []

    if verAssunto(assunto):
        random.shuffle(frases)
        
        for frase in frases:
            if frase[1] == assunto:
                listapoema.append(frase[0])

        random.shuffle(listapoema)

        for i in range(linhas):
            print(listapoema[i])
            listaRetorno.append(listapoema[i])
        
    return listaRetorno


    

    random.shuffle(frases)

    listapoema = []
    
    listaRetorno = []

    for frase in frases:
        if frase[2] == rima:
            listapoema.append(frase[0])

    random.shuffle(listapoema)

    for i in range(linhas):
        print(listapoema[i])
        listaRetorno.append(listapoema[i])
    
    return listaRetorno


def gerarpoemaAleatorio(linhas):
    
    poema = []

    for i in range(linhas):
        random.shuffle(frases)
        print(frases[0][0])
        poema.append(frases[0][0])
    
    return poema




def gerarSonetoSolto(assunto):
    if verAssunto(assunto):
        gerarpoemaPorAssunto(assunto, 4)
        separarEstrofes()
        gerarpoemaPorAssunto(assunto, 4)
        separarEstrofes()
        gerarpoemaPorAssunto(assunto, 3)
        separarEstrofes()
        gerarpoemaPorAssunto(assunto, 3)

def gerarSoneto(assunto):
    lisaRetorno = []
    if verAssunto(assunto):
        gerarpoemaPorAssunto(assunto, 4)
        separarEstrofes()
        gerarpoemaPorAssunto(assunto, 4)
        separarEstrofes()
        gerarpoemaPorAssunto(assunto, 3)
        separarEstrofes()
        gerarpoemaPorAssunto(assunto, 3)
        for i in gerarpoemaPorAssunto(assunto, 4):
            lisaRetorno.append(i)
        lisaRetorno.append(separarEstrofes())
        for i in gerarpoemaPorAssunto(assunto, 4):
            lisaRetorno.append(i)
        lisaRetorno.append(separarEstrofes())
        for i in gerarpoemaPorAssunto(assunto, 3):
            lisaRetorno.append(i)
        lisaRetorno.append(separarEstrofes())
        for i in gerarpoemaPorAssunto(assunto, 3):
            lisaRetorno.append(i)
    
    return lisaRetorno

def gerarVersosCruzados(a,b):
    lisaRetorno = []
    if verRima(a) and verRima(b):
        gerarpoemaPorRimas(a,1)
        gerarpoemaPorRimas(b,1)
        gerarpoemaPorRimas(a,1)
        gerarpoemaPorRimas(b,1)
        
        for i in gerarpoemaPorRimas(a,1):
            lisaRetorno.append(i)
        for i in gerarpoemaPorRimas(b,1):
            lisaRetorno.append(i)
        for i in gerarpoemaPorRimas(a,1):
            lisaRetorno.append(i)
        for i in gerarpoemaPorRimas(b,1):
            lisaRetorno.append(i)
    return lisaRetorno

def gerarVersosCruzadosAleatorios():
    
    random.shuffle(rimas)
    
    a = random.choice(rimas)
    b = random.choice(rimas)
    
    listaRetorno = []
    
    
    
    
    listaRetorno.append(gerarpoemaPorRimas(a,1))
    listaRetorno.append(gerarpoemaPorRimas(b,1))
    listaRetorno.append(gerarpoemaPorRimas(a,1))
    listaRetorno.append(gerarpoemaPorRimas(b,1))
    
    return listaRetorno


def contar_frequencia_de_assuntos(assunto):
    """Conta a frequência de cada assunto."""
    a = 0
    for frase in frases:
        if frase[1] == assunto:
            a += 1
            print(frase[0])
    
    print(a)
            
            


