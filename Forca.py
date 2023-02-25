import random

# lista de palavras
palavras = ['python', 'programacao', 'computador', 'jogo', 'desenvolvimento', "abacate", "abacaxi", "uva", "banana", "laranja", "limao", "morango", "cereja", "manga", "kiwi", "melancia", "melao", 'amor', 'ódio', 'felicidade', 'tristeza', 'alegria', 'raiva', 'esperança', 'desespero', 'coragem', 'medo',
                     'paz', 'guerra', 'sabedoria', 'ignorância', 'conhecimento', 'ignorar', 'aceitar', 'rejeitar', 'perdoar', 'vingar',
                     'sonhar', 'realizar', 'fracassar', 'sucesso', 'aprender', 'ensinar', 'descobrir', 'esquecer', 'lembrar', 'desconhecer',
                     'acordar', 'dormir', 'comer', 'beber', 'respirar', 'andar', 'correr', 'saltar', 'parar', 'começar',
                     'terminar', 'continuar', 'pausar', 'esperar', 'ir', 'voltar', 'chegar', 'partir', 'encontrar', 'perder',
                     'ganhar', 'roubar', 'dividir', 'multiplicar', 'subtrair', 'somar', 'comprar', 'vender', 'pagar', 'receber',
                     'viajar', 'passear', 'trabalhar', 'descansar', 'estudar', 'brincar', 'namorar', 'casar', 'separar', 'divorciar',
                     'crescer', 'envelhecer', 'jovem', 'velho', 'rico', 'pobre', 'bonito', 'feio', 'alto', 'baixo',
                     'magro', 'gordo', 'forte', 'fraco', 'feliz', 'triste', 'ocupado', 'livre', 'certo', 'errado',
                     'verdade', 'mentira', 'bem', 'mal', 'amigo', 'inimigo', 'homem', 'mulher', 'pai', 'mãe',
                     'irmão', 'irmã', 'filho', 'filha', 'neto', 'neta', 'tio', 'tia', 'primo', 'prima',
                     'sobrinho', 'sobrinha', 'avô', 'avó', 'bisavô', 'bisavó', 'genro', 'nora', 'sogro', 'sogra',
                     'enteado', 'enteados', 'sobrinhos', 'sobrinhas', 'irmãos', 'irmãs', 'primos', 'primas', 'família', 'parente',
                     'amigo', 'amigos', 'vizinho', 'vizinhos', 'colega', 'colegas', 'professor', 'professora', 'aluno', 'aluna',
                     'médico', 'médica', 'enfermeiro', 'enfermeira', 'advogado', 'advogada', 'juiz', 'juíza', 'policial', 'policial',
                     'bombeiro', 'bombeira', 'motorista', 'motoristas', 'empresário', 'empresária', 'trabalhador', 'trabalhadora','empregado', 'empregada', 'desempregado', 'desempregada', 'aposentado', 'aposentada', 'estudante', 'estudantes', 'profissional', 'profissionais',
'artista', 'artistas', 'escritor', 'escritora', 'jornalista', 'jornalistas', 'ator', 'atriz', 'cantor', 'cantora',
'músico', 'música', 'compositor', 'compositora', 'pintor', 'pintora', 'escultor', 'escultora', 'arquiteto', 'arquiteta',
'engenheiro', 'engenheira', 'cientista', 'cientistas', 'filósofo', 'filósofa', 'psicólogo', 'psicóloga', 'psiquiatra', 'psiquiatras',
'terapeuta', 'terapeutas', 'coach', 'coaches', 'consultor', 'consultora', 'guru', 'gurus', 'líder', 'líderes',
'chefe', 'chefes', 'presidente', 'presidentes', 'governador', 'governadores', 'prefeito', 'prefeitos', 'vereador', 'vereadores',
'deputado', 'deputados', 'senador', 'senadores', 'ministro', 'ministros', 'juiz', 'juízes', 'advogado', 'advogados',
'promotor', 'promotores', 'procurador', 'procuradores', 'empresário', 'empresários', 'empreendedor', 'empreendedores', 'investidor', 'investidores',
'trabalho', 'emprego', 'renda', 'salário', 'carreira', 'profissão', 'promoção', 'demissão', 'contrato', 'negociação',
'marketing', 'vendas', 'finanças', 'contabilidade', 'economia', 'investimento', 'planejamento', 'estratégia', 'gestão', 'liderança',
'inovação', 'tecnologia', 'software', 'hardware', 'internet', 'redes sociais', 'mídia', 'publicidade', 'jornalismo', 'entretenimento',
'arte', 'cultura', 'literatura', 'teatro', 'cinema', 'música', 'moda', 'beleza', 'saúde', 'bem-estar',
'nutrição', 'fitness', 'esporte', 'viagem', 'turismo', 'lazer', 'diversão', 'gastronomia', 'culinária', 'restaurantes',
'alimentos', 'bebidas', 'vinhos', 'cervejas', 'whiskies', 'destilados', 'bebidas não-alcoólicas', 'água', 'refrigerante', 'sucos',
'chá', 'café', 'sobremesas', 'doces', 'bolos', 'tortas', 'biscoitos', 'chocolates', 'sorvetes', 'frutas',
'legumes', 'verduras', 'carnes', 'aves', 'peixes', 'frutos do mar', 'massas', 'pães', 'arroz', 'feijão', 'abjeto', 'abnóxio', 'abrupto', 'acéfalo', 'acérrimo', 'aclive', 'acólito', 'acrimonioso', 'acúleo', 'adâmico', 'admoestação', 'adorno', 'afável', 'afã', 'afável', 'afável', 'afiado', 'aflição', 'afã', 'afortunado', 'afta', 'agárico', 'agalactia', 'agasalho', 'ágil', 'agourento', 'agrário', 'agreste', 'agrônomo', 'aguerrido', 'aicmofobia', 'aimoré', 'ainda', 'albino', 'alcáçuz', 'aleatório', 'alegoria', 'alfaiate', 'alhures', 'aliado', 'alicerce', 'alienado', 'alinhavo', 'alisamento', 'alma', 'alquimia', 'alquimista', 'altivez', 'alucinação', 'alusão', 'alvoroço', 'amanhã', 'amargo', 'ambição', 'ambulante', 'amenizar', 'ametista', 'amigo', 'amnésia', 'amnistia', 'amoroso', 'ampulheta', 'amuleto', 'análogo', 'anarquia', 'anátema', 'ancestral', 'ancião', 'anexo', 'anfíbio', 'angustiante', 'animação', 'aniquilamento', 'anódino', 'anomalia', 'anônimo', 'anseio', 'antagonismo', 'antebraço', 'antecessor', 'anteontem', 'antiaéreo', 'antibiótico', 'anticristo', 'antítese', 'anuência', 'anátema', 'aparato', 'apático', 'apavorado', 'apaziguar']


# escolhe uma palavra aleatória da lista
palavra = random.choice(palavras)

# cria uma string com a mesma quantidade de caracteres da palavra escolhida, com traços no lugar das letras
palavra_escondida = '-' * len(palavra)

# lista para armazenar as letras já escolhidas pelo usuário
letras_escolhidas = []

# número máximo de tentativas
max_tentativas = 15

# contador de tentativas
tentativas = 0

# loop principal do jogo
while True:
    # exibe a palavra escondida e as letras já escolhidas pelo usuário
    print(palavra_escondida)
    print('Letras escolhidas:', letras_escolhidas)
    
    # solicita ao usuário que digite uma letra
    letra = input('Digite uma letra: ').lower()
    
    # verifica se a letra já foi escolhida anteriormente
    if letra in letras_escolhidas:
        print('Você já escolheu esta letra. Tente novamente.')
        continue
    
    # adiciona a letra à lista de letras escolhidas
    letras_escolhidas.append(letra)
    
    # verifica se a letra está presente na palavra
    if letra in palavra:
        # substitui os traços pela letra nas posições correspondentes
        for i in range(len(palavra)):
            if palavra[i] == letra:
                palavra_escondida = palavra_escondida[:i] + letra + palavra_escondida[i+1:]
        
        # verifica se o usuário adivinhou a palavra
        if palavra_escondida == palavra:
            print('Parabéns! Você adivinhou a palavra:', palavra)
            break
    else:
        # incrementa o contador de tentativas e verifica se o usuário excedeu o número máximo de tentativas
        tentativas += 1
        if tentativas == max_tentativas:
            print('Você perdeu! A palavra era:', palavra)
            break
        else:
            print('Letra incorreta. Você tem mais', max_tentativas - tentativas, 'tentativas.')
    
    # exibe uma linha em branco para separar as jogadas
    print()

