import random

frases = [
    ("A lua brilha sobre o mar", "Natureza", "mar"),
    ("O vento canta entre as árvores", "Natureza", "res"),
    ("No silêncio ouço teu nome", "Amor", "ome"),
    ("O tempo voa sem avisar", "Vida", "sar"),
    ("As estrelas dançam no céu", "Universo", "céu"),
    ("O amor aquece o coração", "Amor", "ão"),
    ("A chuva cai e traz lembranças", "Reflexão", "ças"),
    ("O sol desponta no horizonte", "Natureza", "nte"),
    ("As folhas caem no outono", "Estação", "ono"),
    ("O destino escreve nossa história", "Vida", "ria"),
    ("No jardim florescem esperanças", "Natureza", "ças"),
    ("Sorrisos iluminam a escuridão", "Felicidade", "ão"),
    ("As ondas sussurram segredos", "Mar", "dos"),
    ("O tempo apaga cicatrizes", "Reflexão", "zes"),
    ("A noite envolve os sonhos", "Sonhos", "hos"),
    ("No olhar brilha a esperança", "Sentimento", "ça"),
    ("O perfume das rosas encanta", "Natureza", "nta"),
    ("Caminhos se cruzam ao acaso", "Destino", "aso"),
    ("O vento leva as palavras", "Natureza", "vas"),
    ("A música embala a saudade", "Sentimento", "ade"),
    ("As montanhas tocam o céu", "Natureza", "céu"),
    ("O silêncio grita verdades", "Reflexão", "des"),
    ("Os pássaros anunciam a manhã", "Natureza", "hã"),
    ("O brilho do sol aquece", "Natureza", "ece"),
    ("A noite esconde mistérios", "Mistério", "ios"),
    ("O riso contagia os corações", "Felicidade", "ões"),
    ("O tempo ensina lições", "Vida", "ões"),
    ("A alma dança na liberdade", "Sentimento", "ade"),
    ("No inverno o frio abraça", "Estação", "ça"),
    ("As pegadas somem na areia", "Mar", "eia"),
    ("O destino sopra mudanças", "Destino", "ças"),
    ("A esperança brota no peito", "Sentimento", "ito"),
    ("Os versos guardam segredos", "Poesia", "dos"),
    ("O sol nasce em cada sonho", "Sonhos", "ho"),
    ("O abraço afasta a tristeza", "Sentimento", "za"),
    ("As lágrimas lavam a dor", "Reflexão", "dor"),
    ("O luar beija o oceano", "Natureza", "ano"),
    ("O céu reflete nossos desejos", "Sonhos", "jos"),
    ("A noite embala os amantes", "Amor", "tes"),
    ("As estrelas contam histórias", "Universo", "ias"),
    ("A luz dissipa as sombras", "Reflexão", "ras"),
    ("O mar esconde seus mistérios", "Mar", "ios"),
    ("O sorriso desarma a dor", "Felicidade", "dor"),
    ("O amor floresce na alma", "Amor", "lma"),
    ("A manhã traz um novo dia", "Tempo", "dia"),
    ("O vento espalha canções", "Natureza", "ões"),
    ("A estrada leva ao desconhecido", "Destino", "ido"),
    ("As nuvens dançam no céu", "Natureza", "céu"),
    ("A chuva beija a terra", "Natureza", "rra"),
    ("O fogo arde na paixão", "Amor", "ão"),
    ("O rio segue sem destino", "Natureza", "ino"),
    ("O brilho nos olhos revela", "Sentimento", "ela"),
    ("O tempo escreve cicatrizes", "Reflexão", "zes"),
    ("O amor se perde no tempo", "Amor", "mpo"),
    ("O destino guia os passos", "Destino", "sos"),
    ("As ondas quebram na areia", "Mar", "eia"),
    ("A liberdade dança no vento", "Sentimento", "nto"),
    ("As sombras escondem segredos", "Mistério", "dos"),
    ("A saudade mora no peito", "Sentimento", "ito"),
    ("O eco repete os medos", "Reflexão", "dos"),
    ("A luz brilha na escuridão", "Reflexão", "ão"),
    ("O sol despede-se do dia", "Natureza", "dia"),
    ("O coração bate esperança", "Sentimento", "ça"),
    ("As pegadas contam histórias", "Vida", "ias"),
    ("O olhar fala sem palavras", "Sentimento", "vas"),
    ("A vida dança ao acaso", "Destino", "aso"),
    ("A alma canta seus versos", "Poesia", "sos"),
    ("As estrelas piscam alegrias", "Universo", "ias"),
    ("A tempestade traz mudanças", "Reflexão", "ças"),
    ("O horizonte some no mar", "Natureza", "mar"),
    ("O tempo desvenda mistérios", "Reflexão", "ios"),
    ("O abraço é porto seguro", "Sentimento", "uro"),
    ("As folhas sussurram segredos", "Natureza", "dos"),
    ("A eternidade cabe num instante", "Tempo", "nte"),
    ("O amanhecer anuncia esperanças", "Natureza", "ças"),
    ("A lua inspira poesia", "Poesia", "sia"),
    ("O vento espalha lembranças", "Sentimento", "ças"),
    ("A sombra segue nossos passos", "Reflexão", "sos"),
    ("O calor do sol revigora", "Natureza", "ora"),
    ("O mar embala pensamentos", "Mar", "tos"),
    ("Os sonhos constroem futuros", "Sonhos", "ros"),
    ("O silêncio esconde palavras", "Reflexão", "vas"),
    ("As nuvens desenham ilusões", "Natureza", "ões"),
    ("O tempo esculpe destinos", "Destino", "nos"),
    ("O amor ilumina caminhos", "Amor", "hos"),
    ("A saudade é uma canção", "Sentimento", "ão"),
    ("A verdade brilha na alma", "Reflexão", "lma"),
    ("Os versos nascem no peito", "Poesia", "ito"),
    ("O amanhã guarda surpresas", "Destino", "sas"),
    ("O brilho da lua encanta", "Natureza", "nta"),
    ("O abraço dissolve tristezas", "Sentimento", "zas"),
    ("A poesia colore a vida", "Poesia", "ida"),
    ("O olhar reflete a alma", "Sentimento", "lma"),
    ("O dia se despede suave", "Tempo", "ave"),
    ("A estrada segue sem fim", "Destino", "fim"),
    ("No horizonte brilha a lua", "Natureza", "lua"),
    ("O amor floresce sem aviso", "Amor", "iso"),
    ("O vento dança entre as folhas", "Natureza", "has"),
    ("Sonhos ecoam na madrugada", "Sonhos", "ada"),
    ("O destino escreve sua estrada", "Vida", "ada"),
    ("Sorrisos brilham como o sol", "Felicidade", "sol"),
    ("A dor ensina com paixão", "Reflexão", "ão"),
    ("As estrelas piscam no céu", "Universo", "éu"),
    ("O sol renasce toda manhã", "Natureza", "hã"),
    ("A saudade dança na memória", "Sentimento", "ria"),
    ("Os sonhos pintam o infinito", "Sonhos", "ito"),
    ("A brisa leve beija o rosto", "Natureza", "sto"),
    ("No silêncio brota a paz", "Reflexão", "paz"),
    ("O rio segue sem olhar atrás", "Natureza", "raz"),
    ("Os olhos falam sem palavras", "Sentimento", "vas"),
    ("A felicidade brilha no riso", "Felicidade", "iso"),
    ("A lua abraça a escuridão", "Universo", "ão"),
    ("O destino traça surpresas", "Destino", "sas"),
    ("As estrelas bordam a noite", "Universo", "ite"),
    ("O vento canta em liberdade", "Natureza", "ade"),
    ("As folhas caem em despedida", "Natureza", "ida"),
    ("O mar embala nossos sonhos", "Mar", "hos"),
    ("O amor floresce em cada olhar", "Amor", "har"),
    ("O tempo leva e traz memórias", "Vida", "ias"),
    ("O coração pulsa em sintonia", "Sentimento", "nia"),
    ("A esperança nasce no peito", "Sentimento", "ito"),
    ("O sol aquece até a alma", "Natureza", "lma"),
    ("A vida é feita de instantes", "Reflexão", "tes"),
    ("O amanhecer traz novos rumos", "Tempo", "mos"),
    ("Os versos dançam no papel", "Poesia", "pel"),
    ("A chuva canta sobre a terra", "Natureza", "rra"),
    ("O olhar revela o infinito", "Sentimento", "ito"),
    ("O dia se despede em luz", "Tempo", "luz"),
    ("O tempo apaga cicatrizes", "Reflexão", "zes"),
    ("A esperança colore o mundo", "Sentimento", "ndo"),
    ("O amor é chama que não se apaga", "Amor", "aga"),
    ("O vento sopra novas histórias", "Destino", "ias"),
    ("O rio murmura antigas canções", "Natureza", "ões"),
    ("A lua ilumina os apaixonados", "Amor", "dos"),
    ("A liberdade voa como um pássaro", "Sentimento", "ro"),
    ("O silêncio guarda segredos", "Reflexão", "dos"),
    ("As pegadas marcam o caminho", "Vida", "lho"),
    ("O coração transborda emoção", "Sentimento", "ão"),
    ("As estrelas piscam esperança", "Universo", "ça"),
    ("O dia amanhece com promessas", "Tempo", "sas"),
    ("A brisa espalha lembranças", "Natureza", "ças"),
    ("O céu reflete nossos sonhos", "Universo", "hos"),
    ("A tempestade precede a calmaria", "Natureza", "ria"),
    ("O abraço dissolve a distância", "Sentimento", "cia"),
    ("O olhar esconde universos", "Sentimento", "sos"),
    ("As ondas cantam sobre a areia", "Mar", "eia"),
    ("O tempo molda nossa essência", "Vida", "cia"),
    ("A poesia nasce do sentir", "Poesia", "tir"),
    ("O amor acalma o desespero", "Amor", "ero"),
    ("A noite inspira pensamentos", "Reflexão", "tos"),
    ("O dia se despede suave", "Tempo", "ave"),
    ("O vento leva os medos", "Natureza", "dos"),
    ("A alma dança em liberdade", "Sentimento", "ade"),
    ("A manhã beija a terra", "Natureza", "rra"),
    ("O destino brinca com os sonhos", "Destino", "hos"),
    ("A lua sussurra mistérios", "Universo", "ios"),
    ("O sol despede-se no horizonte", "Natureza", "nte"),
    ("Os olhos guardam promessas", "Sentimento", "sas"),
    ("O eco traz vozes do passado", "Reflexão", "ado"),
    ("O riso ilumina a escuridão", "Felicidade", "ão"),
    ("O tempo ensina sem pressa", "Reflexão", "ssa"),
    ("A saudade canta baixinho", "Sentimento", "nho"),
    ("O mar abraça os viajantes", "Mar", "tes"),
    ("A estrada se estende sem fim", "Destino", "fim"),
    ("A esperança caminha entre nós", "Sentimento", "ós"),
    ("A tempestade dança no céu", "Natureza", "céu"),
    ("Os versos ecoam na alma", "Poesia", "lma"),
    ("O futuro se faz no presente", "Tempo", "nte"),
    ("O amor cresce como semente", "Amor", "nte"),
    ("Os astros guiam a noite", "Universo", "ite"),
    ("O vento sopra entre as folhas", "Natureza", "has"),
    ("O mar guarda histórias antigas", "Mar", "gas"),
    ("A liberdade mora no olhar", "Sentimento", "har"),
    ("O brilho do sol revigora", "Natureza", "ora"),
    ("As nuvens desenham esperanças", "Natureza", "ças"),
    ("Os sonhos renascem na alvorada", "Sonhos", "ada"),
    ("O tempo desvenda mistérios", "Reflexão", "ios"),
    ("A luz dissipa o medo", "Reflexão", "edo"),
    ("A verdade brilha na alma", "Reflexão", "lma"),
    ("O destino escreve sua rota", "Destino", "ota"),
    ("O silêncio acolhe pensamentos", "Reflexão", "tos"),
    ("O amor reflete o infinito", "Amor", "ito"),
    ("A vida pulsa no coração", "Vida", "ão"),
    ("A chuva lava a tristeza", "Natureza", "za"),
    ("A lua ilumina o caminho", "Universo", "nho"),
    ("A fé renova o espírito", "Sentimento", "ito"),
    ("O tempo desenha cicatrizes", "Reflexão", "zes"),
    ("A estrada ensina lições", "Destino", "ões"),
    ("O riso espanta a solidão", "Felicidade", "ão"),
    ("Os ventos mudam direções", "Natureza", "ões"),
    ("O passado ecoa no presente", "Tempo", "nte"),
    ("Os olhos refletem sentimentos", "Sentimento", "tos"),
    ("O horizonte chama pelo amanhã", "Destino", "hã"),
    ("A eternidade cabe num instante", "Tempo", "nte"),
    ("O vento sopra e leva a dor", "Natureza", "dor"),
    ("A lua brilha no céu azul", "Universo", "zul"),
    ("As estrelas piscam sem cessar", "Universo", "sar"),
    ("O amor renasce a cada dia", "Amor", "dia"),
    ("A chuva canta no telhado", "Natureza", "ado"),
    ("O tempo voa como um pássaro", "Vida", "ro"),
    ("O destino dança entre nós", "Destino", "nós"),
    ("O mar sussurra canções antigas", "Mar", "gas"),
    ("Os sonhos voam na madrugada", "Sonhos", "ada"),
    ("A felicidade mora no instante", "Felicidade", "nte"),
    ("O silêncio abraça a noite", "Reflexão", "ite"),
    ("O sol se despede no horizonte", "Natureza", "nte"),
    ("O abraço aquece o coração", "Sentimento", "ão"),
    ("A esperança ilumina a alma", "Sentimento", "lma"),
    ("A saudade canta na distância", "Sentimento", "cia"),
    ("Os olhos guardam mil histórias", "Sentimento", "ias"),
    ("O riso colore os dias", "Felicidade", "ias"),
    ("A liberdade dança no vento", "Sentimento", "nto"),
    ("A noite guarda mistérios", "Mistério", "ios"),
    ("A estrada leva para longe", "Destino", "nge"),
    ("O eco repete a solidão", "Reflexão", "ão"),
    ("A lua inspira os amantes", "Amor", "tes"),
    ("O dia amanhece com promessas", "Tempo", "sas"),
    ("O tempo revela verdades", "Reflexão", "des"),
    ("O destino segue seu curso", "Destino", "rso"),
    ("A música embala os sonhos", "Sonhos", "hos"),
    ("O olhar traduz sentimentos", "Sentimento", "tos"),
    ("O brilho do sol aquece", "Natureza", "ece"),
    ("As ondas quebram na praia", "Mar", "aia"),
    ("O vento espalha lembranças", "Reflexão", "ças"),
    ("A poesia nasce no coração", "Poesia", "ão"),
    ("As pegadas somem na areia", "Mar", "eia"),
    ("O dia termina em cores", "Natureza", "res"),
    ("A tempestade traz renascimento", "Reflexão", "nto"),
    ("O amanhã traz novas chances", "Tempo", "ces"),
    ("A esperança mora no peito", "Sentimento", "ito"),
    ("A luz dissipa as sombras", "Reflexão", "ras"),
    ("O destino traça novos caminhos", "Destino", "hos"),
    ("O mar esconde segredos", "Mar", "dos"),
    ("A brisa leva pensamentos", "Natureza", "tos"),
    ("Os versos cantam a vida", "Poesia", "ida"),
    ("O tempo molda o futuro", "Reflexão", "uro"),
    ("A verdade brilha no olhar", "Reflexão", "har"),
    ("O silêncio acalma a alma", "Reflexão", "lma"),
    ("A sombra esconde ilusões", "Mistério", "ões"),
    ("O amor floresce em gestos", "Amor", "tos"),
    ("Os caminhos se cruzam sempre", "Destino", "pre"),
    ("A fé renova esperanças", "Sentimento", "ças"),
    ("O vento canta pelos campos", "Natureza", "pos"),
    ("As estrelas desenham sonhos", "Universo", "hos"),
    ("A alma se encanta com a arte", "Sentimento", "rte"),
    ("Os corações batem em sintonia", "Amor", "nia"),
    ("A noite se veste de magia", "Universo", "gia"),
    ("O mar reflete a imensidão", "Mar", "ão"),
    ("A luz guia pelos caminhos", "Reflexão", "hos"),
    ("O riso ilumina a alma", "Felicidade", "lma"),
    ("As lágrimas lavam a tristeza", "Sentimento", "za"),
    ("O futuro nasce no presente", "Reflexão", "nte"),
    ("A estrada se abre ao destino", "Destino", "ino"),
    ("O tempo desvenda o passado", "Reflexão", "ado"),
    ("Os olhos brilham ao entardecer", "Sentimento", "cer"),
    ("O abraço dissolve a distância", "Sentimento", "cia"),
    ("A lua dança com as estrelas", "Universo", "las"),
    ("A brisa leva segredos", "Natureza", "dos"),
    ("Os sonhos guiam a caminhada", "Sonhos", "ada"),
    ("A poesia colore os dias", "Poesia", "ias"),
    ("O olhar esconde verdades", "Reflexão", "des"),
    ("O destino escreve a jornada", "Destino", "ada"),
    ("O mar canta suas melodias", "Mar", "ias"),
    ("O tempo ensina a esperar", "Reflexão", "rar"),
    ("A noite acende os desejos", "Sentimento", "jos"),
    ("A sombra dança na parede", "Mistério", "ede"),
    ("O amor aquece até o inverno", "Amor", "rno"),
    ("As nuvens desenham esperanças", "Natureza", "ças"),
    ("O som da chuva embala sonhos", "Natureza", "hos"),
    ("O sol reflete o recomeço", "Natureza", "eço"),
    ("Os pássaros anunciam o novo dia", "Natureza", "dia"),
    ("As folhas sussurram segredos", "Natureza", "dos"),
    ("A eternidade cabe num instante", "Reflexão", "nte"),
    ("O céu se veste de dourado", "Natureza", "ado"),
    ("A alma sente a imensidão", "Sentimento", "ão"),
    ("Os rios correm para o mar", "Natureza", "mar"),
    ("A manhã traz novas promessas", "Tempo", "sas"),
    ("O silêncio grita em solidão", "Reflexão", "ão"),
    ("As pegadas contam histórias", "Vida", "ias"),
    ("Os olhos veem além do tempo", "Sentimento", "mpo"),
    ("O horizonte se abre ao futuro", "Destino", "uro"),
    ("A esperança se espalha no ar", "Sentimento", "lar"),
    ("O dia amanhece com um sorriso", "Felicidade", "iso"),
    ("O amor se encontra no olhar", "Amor", "har"),
    ("As ondas falam com a praia", "Mar", "aia"),
    ("O tempo é mestre do saber", "Reflexão", "ber"),
    ("O sol se esconde entre as nuvens", "Natureza", "ens"),
    ("O tempo ensina sem avisar", "Reflexão", "sar"),
    ("O vento dança com as folhas", "Natureza", "has"),
    ("Os sonhos brilham no escuro", "Sonhos", "uro"),
    ("O mar abraça a areia fina", "Mar", "ina"),
    ("A chuva canta sua melodia", "Natureza", "dia"),
    ("O destino sopra em silêncio", "Destino", "cio"),
    ("A brisa toca o rosto leve", "Natureza", "eve"),
    ("O amor cresce sem medida", "Amor", "ida"),
    ("A noite abraça os pensamentos", "Reflexão", "tos"),
    ("A esperança renasce no peito", "Sentimento", "ito"),
    ("Os olhos refletem a verdade", "Reflexão", "ade"),
    ("As estrelas riscam o céu", "Universo", "céu"),
    ("A lua ilumina o caminho", "Universo", "nho"),
    ("Os dias correm sem parar", "Tempo", "rar"),
    ("A sombra esconde lembranças", "Reflexão", "ças"),
    ("O silêncio grita por dentro", "Reflexão", "tro"),
    ("O rio segue sua jornada", "Natureza", "ada"),
    ("O olhar diz o que as palavras calam", "Sentimento", "lam"),
    ("O amor floresce no toque", "Amor", "que"),
    ("O riso espanta a tristeza", "Felicidade", "za"),
    ("O céu desenha promessas", "Natureza", "sas"),
    ("Os ventos mudam os destinos", "Destino", "nos"),
    ("A saudade pesa no peito", "Sentimento", "ito"),
    ("A poesia nasce da alma", "Poesia", "lma"),
    ("O brilho do sol aquece", "Natureza", "ece"),
    ("A vida sopra novos ares", "Reflexão", "res"),
    ("As folhas caem no outono", "Natureza", "ono"),
    ("O tempo apaga as dores", "Reflexão", "res"),
    ("O amanhã carrega esperanças", "Tempo", "ças"),
    ("A estrada segue sem fim", "Destino", "fim"),
    ("Os passos ecoam na rua", "Vida", "rua"),
    ("A tempestade traz renovo", "Natureza", "ovo"),
    ("O abraço dissolve medos", "Sentimento", "dos"),
    ("Os versos contam histórias", "Poesia", "ias"),
    ("O coração pulsa em segredo", "Sentimento", "edo"),
    ("O horizonte esconde mistérios", "Natureza", "ios"),
    ("A brisa leva os pensamentos", "Natureza", "tos"),
    ("A fé ilumina o impossível", "Reflexão", "vel"),
    ("O tempo lapida memórias", "Reflexão", "ias"),
    ("Os pássaros anunciam o dia", "Natureza", "dia"),
    ("O som da chuva acalma", "Natureza", "lma"),
    ("O silêncio envolve a noite", "Reflexão", "ite"),
    ("A lua sussurra canções", "Universo", "ões"),
    ("As ondas falam ao vento", "Mar", "nto"),
    ("Os sonhos atravessam o tempo", "Sonhos", "mpo"),
    ("O sorriso aquece a alma", "Felicidade", "lma"),
    ("O destino se refaz sempre", "Destino", "pre"),
    ("O olhar dança na multidão", "Sentimento", "ão"),
    ("A esperança pinta o horizonte", "Sentimento", "nte"),
    ("A verdade brilha na sombra", "Reflexão", "bra"),
    ("O toque traduz emoções", "Sentimento", "ões"),
    ("O passado dorme no presente", "Tempo", "nte"),
    ("O dia amanhece em cores", "Natureza", "res"),
    ("A estrada nos leva além", "Destino", "lem"),
    ("O mar carrega segredos", "Mar", "dos"),
    ("O tempo tece ilusões", "Reflexão", "ões"),
    ("A brisa sopra leve e fria", "Natureza", "ria"),
    ("Os olhos guardam promessas", "Sentimento", "sas"),
    ("O vento espalha lembranças", "Natureza", "ças"),
    ("O coração escreve histórias", "Sentimento", "ias"),
    ("O riso ilumina o escuro", "Felicidade", "uro"),
    ("O amor transcende distâncias", "Amor", "cias"),
    ("As nuvens escondem desejos", "Natureza", "jos"),
    ("Os rios correm para o mar", "Natureza", "mar"),
    ("A saudade ecoa na mente", "Sentimento", "nte"),
    ("O dia nasce e se despede", "Tempo", "ede"),
    ("O silêncio é voz do coração", "Reflexão", "ão"),
    ("As estrelas guiam caminhos", "Universo", "hos"),
    ("O amor colore os segundos", "Amor", "dos"),
    ("Os ventos desenham esperanças", "Natureza", "ças"),
    ("O destino sopra em mistério", "Destino", "rio"),
    ("Os sonhos flutuam no ar", "Sonhos", "lar"),
    ("A vida é feita de ciclos", "Reflexão", "cos"),
    ("O mar dança com as marés", "Mar", "rés"),
    ("A fé atravessa fronteiras", "Reflexão", "ras"),
    ("A lua reflete o infinito", "Universo", "ito"),
    ("Os versos nascem do silêncio", "Poesia", "cio"),
    ("O tempo escreve novas páginas", "Reflexão", "gas"),
    ("O olhar revela segredos", "Sentimento", "dos"),
    ("As pegadas somem na areia", "Natureza", "eia"),
    ("A sombra dança na parede", "Mistério", "ede"),
    ("O sorriso reflete esperança", "Felicidade", "ça"),
    ("A estrada ensina paciência", "Destino", "cia"),
    ("Os desejos flutuam na brisa", "Sentimento", "isa"),
    ("A verdade se esconde nas entrelinhas", "Reflexão", "has"),
    ("A eternidade cabe num instante", "Tempo", "nte"),
    ("O amor é chama que nunca apaga", "Amor", "aga"),
    ("O vento leva os pensamentos", "Natureza", "tos"),
    ("O mar abraça a imensidão", "Mar", "ão"),
    ("A lua reflete a solidão", "Universo", "ão"),
    ("O tempo escreve sem parar", "Reflexão", "rar"),
    ("As estrelas dançam no céu", "Universo", "céu"),
    ("Os sonhos sopram esperança", "Sonhos", "ça"),
    ("O amor aquece em silêncio", "Amor", "cio"),
    ("O riso ilumina a estrada", "Felicidade", "ada"),
    ("A saudade canta ao longe", "Sentimento", "nge"),
    ("A noite abraça os segredos", "Mistério", "dos"),
    ("O sol desponta no horizonte", "Natureza", "nte"),
    ("O destino pinta surpresas", "Destino", "sas"),
    ("As ondas beijam a areia", "Mar", "eia"),
    ("O silêncio fala bem alto", "Reflexão", "lto"),
    ("A estrada segue sem medo", "Destino", "edo"),
    ("O tempo apaga cicatrizes", "Reflexão", "zes"),
    ("A chuva traz novos ares", "Natureza", "res"),
    ("O olhar revela memórias", "Sentimento", "ias"),
    ("A alma dança com o vento", "Sentimento", "nto"),
    ("A esperança brilha distante", "Sentimento", "nte"),
    ("A sombra se esconde no dia", "Mistério", "dia"),
    ("Os rios buscam o oceano", "Natureza", "ano"),
    ("A paixão queima sem culpa", "Amor", "pa"),
    ("Os versos contam histórias", "Poesia", "ias"),
    ("O destino escreve sem pressa", "Destino", "ssa"),
    ("A brisa sopra canções", "Natureza", "ões"),
    ("O céu desenha fantasias", "Universo", "ias"),
    ("O sorriso reflete ternura", "Felicidade", "ura"),
    ("As folhas caem no outono", "Natureza", "ono"),
    ("O tempo ensina a esperar", "Reflexão", "rar"),
    ("Os corações pulsam em sintonia", "Amor", "nia"),
    ("A saudade ecoa no peito", "Sentimento", "ito"),
    ("O amor cresce em detalhes", "Amor", "hes"),
    ("O mar sussurra desejos", "Mar", "jos"),
    ("A estrada leva para longe", "Destino", "nge"),
    ("O horizonte some na neblina", "Natureza", "ina"),
    ("O destino brinca com a sorte", "Destino", "rte"),
    ("A lua ilumina os caminhos", "Universo", "hos"),
    ("As pegadas somem na areia", "Natureza", "eia"),
    ("A tempestade renova a vida", "Natureza", "ida"),
    ("O silêncio pesa na noite", "Reflexão", "ite"),
    ("As estrelas são poesias no céu", "Universo", "céu"),
    ("Os dias passam como nuvens", "Tempo", "ens"),
    ("O olhar carrega verdades", "Reflexão", "des"),
    ("O abraço dissolve a dor", "Sentimento", "dor"),
    ("Os segredos dormem na mente", "Mistério", "nte"),
    ("A noite veste-se de prata", "Universo", "ata"),
    ("O vento espalha lembranças", "Natureza", "ças"),
    ("A fé colore a escuridão", "Sentimento", "ão"),
    ("O tempo muda sem aviso", "Reflexão", "iso"),
    ("A lágrima conta a saudade", "Sentimento", "ade"),
    ("Os sonhos voam na brisa", "Sonhos", "isa"),
    ("O riso preenche o silêncio", "Felicidade", "cio"),
    ("O mar canta melodias antigas", "Mar", "gas"),
    ("O passado dorme no presente", "Reflexão", "nte"),
    ("O destino pinta recomeços", "Destino", "ços"),
    ("O sol aquece a esperança", "Natureza", "ça"),
    ("O eco repete a solidão", "Reflexão", "ão"),
    ("O amor é chama infinita", "Amor", "ita"),
    ("Os versos nascem do peito", "Poesia", "ito"),
    ("As estrelas piscam em segredo", "Universo", "edo"),
    ("O tempo carrega promessas", "Reflexão", "sas"),
    ("A sombra dança na parede", "Mistério", "ede"),
    ("A estrada ensina lições", "Destino", "ões"),
    ("A alma sente a imensidão", "Sentimento", "ão"),
    ("O tempo sussurra mudanças", "Reflexão", "ças"),
    ("O sol despede-se em fogo", "Natureza", "ogo"),
    ("O coração pulsa certezas", "Sentimento", "zas"),
    ("A verdade dorme no olhar", "Reflexão", "har"),
    ("Os desejos flutuam na brisa", "Sentimento", "isa"),
    ("A lua encanta os apaixonados", "Universo", "dos"),
    ("O tempo dissolve ilusões", "Reflexão", "ões"),
    ("O vento espalha suspiros", "Natureza", "ros"),
    ("Os olhos brilham na escuridão", "Sentimento", "ão"),
    ("A fé rompe barreiras", "Reflexão", "ras"),
    ("O amor floresce na espera", "Amor", "era"),
    ("As pegadas contam segredos", "Natureza", "dos"),
    ("Os dias clareiam memórias", "Tempo", "ias"),
    ("A tempestade anuncia mudanças", "Natureza", "ças"),
    ("O mar esconde mistérios", "Mar", "ios"),
    ("O tempo apaga incertezas", "Reflexão", "zas"),
    ("O olhar guarda promessas", "Sentimento", "sas"),
    ("Os sonhos acendem caminhos", "Sonhos", "hos"),
    ("A noite cobre a cidade", "Natureza", "ade"),
    ("A lua sorri para o mar", "Universo", "mar"),
    ("O destino se refaz sempre", "Destino", "pre"),
    ("O vento toca a pele fria", "Natureza", "ria"),
    ("O coração canta esperanças", "Sentimento", "ças"),
    ("As nuvens escondem mistérios", "Natureza", "ios"),
    ("A brisa toca leve a pele", "Natureza", "ele"),
    ("O sol renasce a cada dia", "Natureza", "dia"),
    ("A noite esconde os segredos", "Mistério", "dos"),
    ("O mar canta versos antigos", "Mar", "gos"),
    ("Os olhos refletem memórias", "Reflexão", "ias"),
    ("A chuva embala os corações", "Natureza", "ões"),
    ("O vento sussurra baixinho", "Natureza", "nho"),
    ("As estrelas brilham em festa", "Universo", "sta"),
    ("O tempo dança sem parar", "Reflexão", "rar"),
    ("A esperança acende caminhos", "Sentimento", "hos"),
    ("A saudade grita no peito", "Sentimento", "ito"),
    ("O riso ilumina a jornada", "Felicidade", "ada"),
    ("A lua observa em silêncio", "Universo", "cio"),
    ("Os dias correm apressados", "Tempo", "dos"),
    ("As sombras falam baixinho", "Mistério", "nho"),
    ("O amor floresce na calma", "Amor", "lma"),
    ("O destino traça mistérios", "Destino", "ios"),
    ("Os pássaros cantam a aurora", "Natureza", "ora"),
    ("O olhar atravessa distâncias", "Sentimento", "cias"),
    ("O mar esconde seus segredos", "Mar", "dos"),
    ("Os sonhos tocam o infinito", "Sonhos", "ito"),
    ("A alma respira esperança", "Sentimento", "ça"),
    ("O vento espalha promessas", "Natureza", "sas"),
    ("As pegadas somem na areia", "Natureza", "eia"),
    ("O sol aquece a memória", "Natureza", "ria"),
    ("A noite beija o horizonte", "Universo", "nte"),
    ("A tempestade traz mudanças", "Natureza", "ças"),
    ("O eco repete solidão", "Reflexão", "ão"),
    ("Os versos dançam no papel", "Poesia", "pel"),
    ("A estrada chama aventureiros", "Destino", "ros"),
    ("A neblina cobre a cidade", "Natureza", "ade"),
    ("A paixão arde como fogo", "Amor", "ogo"),
    ("O passado repousa sereno", "Reflexão", "eno"),
    ("O abraço dissolve os medos", "Sentimento", "dos"),
    ("Os dias pintam novas cores", "Tempo", "res"),
    ("A fé constrói fortalezas", "Reflexão", "zas"),
    ("O tempo sussurra verdades", "Reflexão", "des"),
    ("A chuva lava as lembranças", "Natureza", "ças"),
    ("A lua espelha os desejos", "Universo", "jos"),
    ("O coração canta baixinho", "Sentimento", "nho"),
    ("O silêncio envolve a alma", "Reflexão", "lma"),
    ("O destino sopra mistérios", "Destino", "ios"),
    ("As ondas moldam a praia", "Mar", "aia"),
    ("A brisa traz leveza", "Natureza", "eza"),
    ("Os astros tecem histórias", "Universo", "ias"),
    ("O dia clareia esperanças", "Natureza", "ças"),
    ("As palavras desenham poesia", "Poesia", "sia"),
    ("O riso ilumina o escuro", "Felicidade", "uro"),
    ("A sombra esconde o passado", "Mistério", "ado"),
    ("O céu acolhe os sonhos", "Universo", "hos"),
    ("Os olhos guardam lembranças", "Sentimento", "ças"),
    ("O vento embala os sentidos", "Natureza", "dos"),
    ("O amor tece destinos", "Amor", "nos"),
    ("O caminho ensina paciência", "Destino", "cia"),
    ("A estrada revela promessas", "Destino", "sas"),
    ("Os lábios sussurram segredos", "Sentimento", "dos"),
    ("O luar desenha fantasias", "Universo", "ias"),
    ("O dia se despede calado", "Natureza", "ado"),
    ("O tempo apaga cicatrizes", "Reflexão", "zes"),
    ("Os sinos anunciam mudanças", "Tempo", "ças"),
    ("A verdade dança na alma", "Reflexão", "lma"),
    ("A paixão se espalha no vento", "Amor", "ento"),
    ("A paz floresce no coração", "Sentimento", "ão"),
    ("Os sorrisos curam feridas", "Felicidade", "das"),
    ("A neblina esconde os passos", "Natureza", "sos"),
    ("O trovão rompe o silêncio", "Natureza", "cio"),
    ("O tempo resgata memórias", "Reflexão", "ias"),
    ("O mar guarda antigos segredos", "Mar", "dos"),
    ("O destino sopra certezas", "Destino", "zas"),
    ("O pôr do sol colore esperanças", "Natureza", "ças"),
    ("As noites abraçam o mistério", "Universo", "rio"),
    ("O silêncio sussurra verdades", "Reflexão", "des"),
    ("A estrada se perde na bruma", "Destino", "uma"),
    ("O olhar traduz emoções", "Sentimento", "ões"),
    ("O tempo reconstrói histórias", "Reflexão", "ias"),
    ("O vento traz recordações", "Natureza", "ões"),
    ("O amor se espalha no espaço", "Amor", "ço"),
    ("O sol brilha entre os galhos", "Natureza", "lhos"),
    ("A lua dança com as estrelas", "Universo", "las"),
    ("O destino escreve com vento", "Destino", "ento"),
    ("O silêncio revela a essência", "Reflexão", "cia"),
    ("O tempo ensina com paciência", "Reflexão", "cia"),
    ("Os passos ecoam na estrada", "Destino", "ada"),
    ("O céu abraça a imensidão", "Universo", "ão"),
    ("O amor aquece em qualquer estação", "Amor", "ção"),
    ("A esperança brota como flor", "Sentimento", "lor"),
    ("As marés contam sua história", "Mar", "ria"),
    ("O destino traça caminhos", "Destino", "hos"),
    ("As folhas dançam ao vento", "Natureza", "ento"),
    ("O coração pulsa forte", "Sentimento", "rte"),
    ("Os astros guiam a jornada", "Universo", "ada"),
    ("O tempo renova as dores", "Reflexão", "res"),
    ("A brisa refresca a pele", "Natureza", "ele"),
    ("O horizonte se desfaz em cores", "Natureza", "res"),
    ("Os sorrisos aquecem a alma", "Felicidade", "lma"),
    ("A chuva traz lembranças antigas", "Natureza", "gas"),
    ("Brisa toca leve a pele", "Natureza", "ele"),
    ("Sol renasce a cada dia", "Natureza", "dia"),
    ("Noite esconde os segredos", "Mistério", "dos"),
    ("Mar canta versos antigos", "Mar", "gos"),
    ("Olhos refletem memórias", "Reflexão", "ias"),
    ("Chuva embala os corações", "Natureza", "ões"),
    ("Vento sussurra baixinho", "Natureza", "nho"),
    ("Estrelas brilham em festa", "Universo", "sta"),
    ("Tempo dança sem parar", "Reflexão", "rar"),
    ("Esperança acende caminhos", "Sentimento", "hos"),
    ("Saudade grita no peito", "Sentimento", "ito"),
    ("Riso ilumina a jornada", "Felicidade", "ada"),
    ("Lua observa em silêncio", "Universo", "cio"),
    ("Dias correm apressados", "Tempo", "dos"),
    ("Sombras falam baixinho", "Mistério", "nho"),
    ("Amor floresce na calma", "Amor", "lma"),
    ("Destino traça mistérios", "Destino", "ios"),
    ("Pássaros cantam a aurora", "Natureza", "ora"),
    ("Olhar atravessa distâncias", "Sentimento", "cias"),
    ("Mar esconde seus segredos", "Mar", "dos"),
    ("Sonhos tocam o infinito", "Sonhos", "ito"),
    ("Alma respira esperança", "Sentimento", "ça"),
    ("Vento espalha promessas", "Natureza", "sas"),
    ("Pegadas somem na areia", "Natureza", "eia"),
    ("Sol aquece a memória", "Natureza", "ria"),
    ("Noite beija o horizonte", "Universo", "nte"),
    ("Tempestade traz mudanças", "Natureza", "ças"),
    ("Eco repete solidão", "Reflexão", "ão"),
    ("Versos dançam no papel", "Poesia", "pel"),
    ("Estrada chama aventureiros", "Destino", "ros"),
    ("Neblina cobre a cidade", "Natureza", "ade"),
    ("Paixão arde como fogo", "Amor", "ogo"),
    ("Passado repousa sereno", "Reflexão", "eno"),
    ("Abraço dissolve os medos", "Sentimento", "dos"),
    ("Dias pintam novas cores", "Tempo", "res"),
    ("Fé constrói fortalezas", "Reflexão", "zas"),
    ("Tempo sussurra verdades", "Reflexão", "des"),
    ("Chuva lava as lembranças", "Natureza", "ças"),
    ("Lua espelha os desejos", "Universo", "jos"),
    ("Coração canta baixinho", "Sentimento", "nho"),
    ("Silêncio envolve a alma", "Reflexão", "lma"),
    ("Destino sopra mistérios", "Destino", "ios"),
    ("Ondas moldam a praia", "Mar", "aia"),
    ("Brisa traz leveza", "Natureza", "eza"),
    ("Astros tecem histórias", "Universo", "ias"),
    ("Dia clareia esperanças", "Natureza", "ças"),
    ("Palavras desenham poesia", "Poesia", "sia"),
    ("Riso ilumina o escuro", "Felicidade", "uro"),
    ("Sombra esconde o passado", "Mistério", "ado"),
    ("Céu acolhe os sonhos", "Universo", "hos"),
    ("Olhos guardam lembranças", "Sentimento", "ças"),
    ("Vento embala os sentidos", "Natureza", "dos"),
    ("Amor tece destinos", "Amor", "nos"),
    ("Caminho ensina paciência", "Destino", "cia"),
    ("Estrada revela promessas", "Destino", "sas"),
    ("Lábios sussurram segredos", "Sentimento", "dos"),
    ("Luar desenha fantasias", "Universo", "ias"),
    ("Dia se despede calado", "Natureza", "ado"),
    ("Tempo apaga cicatrizes", "Reflexão", "zes"),
    ("Sinos anunciam mudanças", "Tempo", "ças"),
    ("Verdade dança na alma", "Reflexão", "lma"),
    ("Paixão se espalha no vento", "Amor", "ento"),
    ("Paz floresce no coração", "Sentimento", "ão"),
    ("Sorrisos curam feridas", "Felicidade", "das"),
    ("Neblina esconde os passos", "Natureza", "sos"),
    ("Trovão rompe o silêncio", "Natureza", "cio"),
    ("Tempo resgata memórias", "Reflexão", "ias"),
    ("Mar guarda antigos segredos", "Mar", "dos"),
    ("Destino sopra certezas", "Destino", "zas"),
    ("Pôr do sol colore esperanças", "Natureza", "ças"),
    ("Noites abraçam o mistério", "Universo", "rio"),
    ("Silêncio sussurra verdades", "Reflexão", "des"),
    ("Estrada se perde na bruma", "Destino", "uma"),
    ("Olhar traduz emoções", "Sentimento", "ões"),
    ("Tempo reconstrói histórias", "Reflexão", "ias"),
    ("Vento traz recordações", "Natureza", "ões"),
    ("Amor se espalha no espaço", "Amor", "ço"),
    ("Sol brilha entre os galhos", "Natureza", "lhos"),
    ("Lua dança com as estrelas", "Universo", "las"),
    ("Destino escreve com vento", "Destino", "ento"),
    ("Silêncio revela a essência", "Reflexão", "cia"),
    ("Tempo ensina com paciência", "Reflexão", "cia"),
    ("Passos ecoam na estrada", "Destino", "ada"),
    ("Céu abraça a imensidão", "Universo", "ão"),
    ("Esperança brota como flor", "Sentimento", "lor"),
    ("Marés contam sua história", "Mar", "ria"),
    ("Destino traça caminhos", "Destino", "hos"),
    ("Folhas dançam ao vento", "Natureza", "ento"),
    ("Coração pulsa forte", "Sentimento", "rte"),
    ("Astros guiam a jornada", "Universo", "ada"),
    ("Tempo renova as dores", "Reflexão", "res"),
    ("Brisa refresca a pele", "Natureza", "ele"),
    ("Horizonte se desfaz em cores", "Natureza", "res"),
    ("Sorrisos aquecem a alma", "Felicidade", "lma"),
    ("Chuva traz lembranças antigas", "Natureza", "gas"),
    ("Brisa leva os segredos", "Natureza", "dos"),
    ("Sol aquece cada instante", "Natureza", "nte"),
    ("Sombras dançam na parede", "Mistério", "ede"),
    ("Mar se agita em canção", "Mar", "ão"),
    ("Folhas sussurram memórias", "Reflexão", "ias"),
    ("Noite cobre os caminhos", "Natureza", "hos"),
    ("Vento espalha os desejos", "Natureza", "jos"),
    ("Estrelas guiam as promessas", "Universo", "sas"),
    ("Tempo apaga as pegadas", "Reflexão", "das"),
    ("Esperança floresce em silêncio", "Sentimento", "cio"),
    ("Saudade pesa no peito", "Sentimento", "ito"),
    ("Riso ilumina os passos", "Felicidade", "sos"),
    ("Lua se esconde nas nuvens", "Universo", "ens"),
    ("Dias passam sem aviso", "Tempo", "iso"),
    ("Sombras cobrem os mistérios", "Mistério", "ios"),
    ("Amor resiste às tempestades", "Amor", "des"),
    ("Destino escreve sua história", "Destino", "ria"),
    ("Pássaros cantam ao amanhecer", "Natureza", "cer"),
    ("Olhar reflete o infinito", "Sentimento", "ito"),
    ("Ondas abraçam a areia", "Mar", "eia"),
    ("Sonhos dançam entre as estrelas", "Sonhos", "las"),
    ("Alma se acalma no vento", "Sentimento", "ento"),
    ("Brisa toca os pensamentos", "Natureza", "tos"),
    ("Pegadas somem na estrada", "Natureza", "ada"),
    ("Sol desenha sombras na terra", "Natureza", "rra"),
    ("Noite se veste de prata", "Universo", "ata"),
    ("Tempestade anuncia mudanças", "Natureza", "ças"),
    ("Versos surgem na madrugada", "Poesia", "ada"),
    ("Caminhos guardam segredos", "Destino", "dos"),
    ("Neblina cobre as montanhas", "Natureza", "has"),
    ("Paixão arde como chama", "Amor", "ama"),
    ("Passado dorme na lembrança", "Reflexão", "ça"),
    ("Abraço dissolve o medo", "Sentimento", "edo"),
    ("Dias trazem novas cores", "Tempo", "res"),
    ("Fé constrói pontes invisíveis", "Reflexão", "eis"),
    ("Vento desenha melodias", "Natureza", "ias"),
    ("Chuva lava as cicatrizes", "Natureza", "zes"),
    ("Lua vigia os desejos", "Universo", "jos"),
    ("Coração canta em segredo", "Sentimento", "edo"),
    ("Silêncio sussurra verdades", "Reflexão", "des"),
    ("Destino traça seu próprio mapa", "Destino", "apa"),
    ("Ondas moldam cada história", "Mar", "ria"),
    ("Brisa traz recordações", "Natureza", "ões"),
    ("Astros contam seus mistérios", "Universo", "ios"),
    ("Dia renasce com esperança", "Natureza", "ça"),
    ("Palavras criam poesia", "Poesia", "sia"),
    ("Riso ilumina qualquer dor", "Felicidade", "dor"),
    ("Sombra guarda segredos antigos", "Mistério", "gos"),
    ("Céu acolhe cada sonho", "Universo", "nho"),
    ("Olhos escondem lembranças", "Sentimento", "ças"),
    ("Vento carrega promessas", "Natureza", "sas"),
    ("Amor floresce na espera", "Amor", "era"),
    ("Caminho ensina paciência", "Destino", "cia"),
    ("Estrada revela sua magia", "Destino", "gia"),
    ("Lábios murmuram poesia", "Sentimento", "sia"),
    ("Luar desenha novas fantasias", "Universo", "ias"),
    ("Dia repousa no horizonte", "Natureza", "nte"),
    ("Tempo suaviza feridas", "Reflexão", "das"),
    ("Sinos anunciam um recomeço", "Tempo", "eço"),
    ("Verdade brilha na alma", "Reflexão", "lma"),
    ("Paixão cresce como flor", "Amor", "lor"),
    ("Paz se espalha no tempo", "Sentimento", "mpo"),
    ("Sorrisos curam cicatrizes", "Felicidade", "zes"),
    ("Neblina esconde os caminhos", "Natureza", "hos"),
    ("Trovão rompe o silêncio", "Natureza", "cio"),
    ("Tempo revela cada lição", "Reflexão", "ão"),
    ("Mar ecoa histórias antigas", "Mar", "gas"),
    ("Destino sopra certezas", "Destino", "zas"),
    ("Pôr do sol colore o horizonte", "Natureza", "nte"),
    ("Noites guardam seus segredos", "Universo", "dos"),
    ("Silêncio revela a essência", "Reflexão", "cia"),
    ("Estrada se perde na neblina", "Destino", "ina"),
    ("Olhar desenha emoções", "Sentimento", "ões"),
    ("Tempo transforma saudades", "Reflexão", "des"),
    ("Brisa embala cada lembrança", "Natureza", "ça"),
    ("Amor se espalha pelo mundo", "Amor", "ndo"),
    ("Sol aquece os corações", "Natureza", "ões"),
    ("Lua dança sobre as águas", "Universo", "uas"),
    ("Destino escreve versos no vento", "Destino", "ento"),
    ("Silêncio ecoa no infinito", "Reflexão", "ito"),
    ("Tempo molda as memórias", "Reflexão", "ias"),
    ("Passos marcam a areia", "Destino", "eia"),
    ("Céu guarda mistérios ocultos", "Universo", "tos"),
    ("Esperança nasce entre flores", "Sentimento", "res"),
    ("Marés transformam as paisagens", "Mar", "ens"),
    ("Destino abre novas portas", "Destino", "tas"),
    ("Folhas dançam ao sabor do vento", "Natureza", "ento"),
    ("Coração pulsa em silêncio", "Sentimento", "cio"),
    ("Astros sussurram histórias antigas", "Universo", "gas"),
    ("Tempo renova as lembranças", "Reflexão", "ças"),
    ("Brisa refresca a tarde", "Natureza", "rde"),
    ("Horizonte se dissolve em cores", "Natureza", "res"),
    ("Sorrisos aquecem a alma", "Felicidade", "lma"),
    ("Chuva traz promessas distantes", "Natureza", "tes"),
    ("Coração bate em desatino", "Amor", "ino"),
    ("Teus olhos brilham como estrelas", "Amor", "las"),
    ("Em teus braços mora a calma", "Amor", "lma"),
    ("Nosso amor corre como rio", "Amor", "rio"),
    ("Teu perfume embriaga a alma", "Amor", "lma"),
    ("Sussurros doces na madrugada", "Amor", "ada"),
    ("Teus lábios trazem poesia", "Amor", "sia"),
    ("Meu peito arde em desejo", "Amor", "ejo"),
    ("Tua ausência é tempestade", "Amor", "ade"),
    ("Nosso beijo tem sabor de céu", "Amor", "éu"),
    ("Cada toque teu é chama", "Amor", "ama"),
    ("És a luz na minha estrada", "Amor", "ada"),
    ("Sentir teu cheiro me acalma", "Amor", "lma"),
    ("Teu amor é mar sereno", "Amor", "eno"),
    ("Palavras tuas são abrigo", "Amor", "igo"),
    ("No teu peito eu me perco", "Amor", "rco"),
    ("A saudade grita forte", "Amor", "rte"),
    ("Sem teus beijos, sou inverno", "Amor", "rno"),
    ("Teu sorriso é meu abrigo", "Amor", "igo"),
    ("Amar-te é voar sem medo", "Amor", "edo"),
    ("Tua voz embala sonhos", "Amor", "hos"),
    ("Meu olhar busca o teu", "Amor", "teu"),
    ("Em teus braços sou completo", "Amor", "eto"),
    ("No silêncio, teu nome ecoa", "Amor", "coa"),
    ("És a chama que me aquece", "Amor", "ece"),
    ("No teu abraço o tempo para", "Amor", "ara"),
    ("Caminho em teus sonhos leves", "Amor", "ves"),
    ("Sinto tua pele na brisa", "Amor", "isa"),
    ("A distância dói na alma", "Amor", "lma"),
    ("Entre versos, teu nome escrevo", "Amor", "evo"),
    ("Tuas promessas são estrelas", "Amor", "las"),
    ("Te amar é perder o chão", "Amor", "ão"),
    ("Ecos doces do teu riso", "Amor", "iso"),
    ("Teu olhar me desarma", "Amor", "rma"),
    ("Teu calor é minha casa", "Amor", "asa"),
    ("Nosso amor é mar revolto", "Amor", "olto"),
    ("Na tua ausência, sou sombra", "Amor", "bra"),
    ("Teu beijo é brisa suave", "Amor", "ave"),
    ("Teu toque apaga a dor", "Amor", "dor"),
    ("Teu nome vive em meu peito", "Amor", "eito"),
    ("Te espero em cada aurora", "Amor", "ora"),
    ("Tua lembrança me embriaga", "Amor", "aga"),
    ("No teu riso, encontro paz", "Amor", "az"),
    ("Nosso amor resiste ao tempo", "Amor", "mpo"),
    ("Cada verso tem teu nome", "Amor", "ome"),
    ("Nosso encontro foi destino", "Amor", "ino"),
    ("Minha alma dança em ti", "Amor", "ti"),
    ("Entre nós, só existe o infinito", "Amor", "ito"),
    ("O universo canta nosso amor", "Amor", "mor"),
    ("Amar-te é ser livre no vento", "Amor", "ento"),
    ("Sem ti, o mundo perde cor", "Amor", "cor"),
    ("Teus olhos são minha bússola", "Amor", "ola"),
    ("No teu abraço, sou imortal", "Amor", "tal"),
    ("O amor em nós sempre brilha", "Amor", "lha"),
    ("Teus gestos são poesia viva", "Amor", "iva"),
    ("No teu beijo, mora o verão", "Amor", "ão"),
    ("Tua voz é melodia doce", "Amor", "ce"),
    ("Cada toque teu é promessa", "Amor", "ssa"),
    ("Nosso amor não conhece fim", "Amor", "fim"),
    ("Nosso enlace é chama eterna", "Amor", "rna"),
    ("A vida sorri quando estás", "Amor", "tás"),
    ("No teu amor, encontro lar", "Amor", "lar"),
    ("Sem teu amor, sou inverno", "Amor", "rno"),
    ("Te amar é sempre renascer", "Amor", "cer"),
    ("És o sol que me ilumina", "Amor", "ina"),
    ("Nos teus braços, o mundo some", "Amor", "ome"),
    ("Nosso amor brilha como a lua", "Amor", "lua"),
    ("Cada instante teu é festa", "Amor", "sta"),
    ("Tua essência mora em mim", "Amor", "mim"),
    ("Teu toque é pura magia", "Amor", "gia"),
    ("Nosso amor nunca se apaga", "Amor", "aga"),
    ("Tua presença é meu refúgio", "Amor", "gio"),
    ("Em teu riso, sou criança", "Amor", "ça"),
    ("Nosso amor não tem fronteiras", "Amor", "ras"),
    ("Cada suspiro fala de ti", "Amor", "ti"),
    ("No teu olhar, o céu inteiro", "Amor", "eiro"),
    ("Sem teus braços, sou vazio", "Amor", "zio"),
    ("Te amar é dançar no vento", "Amor", "ento"),
    ("Tua pele é brisa quente", "Amor", "nte"),
    ("Teu nome pulsa em meu peito", "Amor", "eito"),
    ("Tua ausência é noite fria", "Amor", "ria"),
    ("Nosso amor escreve histórias", "Amor", "ias"),
    ("Cada suspiro teu é mel", "Amor", "mel"),
    ("Na tua voz, sou poesia", "Amor", "sia"),
    ("Teu beijo tem gosto de céu", "Amor", "éu"),
    ("Sem ti, o tempo se arrasta", "Amor", "sta"),
    ("Meu amor vive em teus versos", "Amor", "rsos"),
    ("No teu peito, sou abrigo", "Amor", "igo"),
    ("Teu abraço é mar sereno", "Amor", "eno"),
    ("Na tua luz, sou estrela", "Amor", "ela"),
    ("Nosso amor voa sem medo", "Amor", "edo"),
]

versos= []


assuntos = []



rimas= []

estilos= ["soneto","hakai", "aleatorio"]

listaHakai = []

def exibirEstatisticas():
    """Exibe estatísticas sobre o conteúdo."""
    print(f"Total de frases: {len(assuntos)}")
    print(f"Total de assuntos: {len(set([a[1] for a in assuntos]))}")
    print(f"Total de rimas: {len(set([r[1] for r in rimas]))}")

for frase in frases:
    assuntos.append(frase[1])
    rimas.append(frase[2])
    versos.append(frase[0])


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
    else:
        print(f"Uma ou ambas as rimas '{rima_a}' e '{rima_b}' não foram encontradas.")


def gerarPoemaAcrostico(palavra, assunto):
    """Gera um poema acróstico com base em uma palavra."""
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
    """Gera um poema circular onde o último verso conecta-se ao primeiro."""
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

for frase in frases:
    assuntos.append(frase[1])
    rimas.append(frase[2])
    versos.append(frase[0])

def separarEstrofes():
    print("\n---\n")

def verAssunto(assunto):
    
    r = False
    
    for i in range(len(assuntos)):
        if assuntos[i] == assunto:
            r = True
    
    return r

def verRima(rima):
    
    r = False
    
    for i in range(len(assuntos)):
        if rimas[i] == rima:
            r = True
    
    return r

def gerarpoemaPorAssunto(assunto, linhas):

    if verAssunto(assunto):
        random.shuffle(frases)
        listapoema = []
        for frase in frases:
            if frase[1] == assunto:
                listapoema.append(frase[0])

        random.shuffle(listapoema)

        for i in range(linhas):
            print(listapoema[i])

def gerarpoemaPorRimas(rima, linhas):

    random.shuffle(frases)

    listapoema = []

    for frase in frases:
        if frase[2] == rima:
            listapoema.append(frase[0])

    random.shuffle(listapoema)

    for i in range(linhas):
        print(listapoema[i])


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
    if verAssunto(assunto):
        gerarpoemaPorAssunto(assunto, 4)
        separarEstrofes()
        gerarpoemaPorAssunto(assunto, 4)
        separarEstrofes()
        gerarpoemaPorAssunto(assunto, 3)
        separarEstrofes()
        gerarpoemaPorAssunto(assunto, 3)

def gerarVersosCruzados(a,b):
    
    if verRima(a) and verRima(b):
        gerarpoemaPorRimas(a,1)
        gerarpoemaPorRimas(b,1)
        gerarpoemaPorRimas(a,1)
        gerarpoemaPorRimas(b,1)

def gerarVersosCruzadosAleatorios():
    
    random.shuffle(rimas)
    
    a = random.choice(rimas)
    b = random.choice(rimas)
    
    
    gerarpoemaPorRimas(a,1)
    gerarpoemaPorRimas(b,1)
    gerarpoemaPorRimas(a,1)
    gerarpoemaPorRimas(b,1)


def contar_frequencia_de_assuntos(assunto):
    """Conta a frequência de cada assunto."""
    a = 0
    for frase in frases:
        if frase[1] == assunto:
            a += 1
            print(frase[0])
    
    print(a)
            



gerarpoemaAleatorio(6)



