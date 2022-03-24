# Criar jogo da forca usando funções
# para criar repetição
from random import choice as cho

def jogar_novamente():
    escolhas='sim','nao'
    jogar_novamente=input('Deseja jogar novamente?(Sim/Não): ').lower().strip()
    jogar_novamente=jogar_novamente.replace('ã','a')
    if jogar_novamente=='sim':
        jogo_da_forca()
    if jogar_novamente=='nao':
        exit()
    if jogar_novamente not in escolhas:
        while jogar_novamente not in escolhas:
            print('Digite Sim ou Não: ')
            jogar_novamente=input('Deseja jogar novamente?(Sim/Não): ').lower().strip()
        else:
            if jogar_novamente=='sim':
                jogo_da_forca()
            if jogar_novamente=='nao':
                exit() 

def jogo_da_forca():
    palavra_escolhida=' '
    fruta=['banana','abacate','melancia','jaca','uva','melão','maça','laranja'
    ,'abacaxi','açai','acerola','amora','ameixa','cacau','carambola','pinha',
    'cereja','coco','figo','framboesa','goiaba','groselha','jabuticaba','kiwi','mamão',
    'manga','maracujá','morango','pequi','pêra','pêssego','pitanga','pitaya','tamarindo']
    
    pais=['afeganistão','áfrica do sul','albânia','alemanha','andorra','angola',
    'arábia saudita','argélia','argentina','arménia','austrália','áustria','azerbaijão'
    ,'bahamas','banglandexe','barbados','bélgica','belize','bolívia','brasil','bulgária'
    ,'burquina faso','butão','cabo verde','camarões','camboja','canadá','catar'
    ,'cazaquistão','chile','china','chipre','colômbia','coreia do norte','coreia do sul'
    ,'costa do marfim','costa rica','croácia','cuaite','cuba','dinamarca','egito',
    'emirados árabes unidos','equador','eslováquia','eslovénia','espanha',
    'estados unidos da américa','estónia','etiópia','filipinas','finlândia','frança'
    ,'gâmbia','gana','grécia','guatemala','guiana','guiné','guiné equatorial','haiti',
    'honduras','hungria','índia','indonésia','iraque','irlanda','islândia','israel',
    'itália','jamaica','japão','jordânia','letónia','líbano','libéria','líbia',
    'lituânia','luxemburgo','malásia','maldivas','marrocos','méxico','moçambique',
    'moldávia','mônaco','mongólia','namíbia','nepal','nicarágua','nigéria','noruega',
    'nova zelândia','panamá','paquistão','papua nova guiné','paraguai','peru','polônia'
    ,'portugal','quênia','inglaterra','república tcheca','república dominicana',
    'república democratica do congo','romênia','ruanda','rússia','senegal','sérvia',
    'singapura','síria','somália','suécia','suíça','suriname','tailândia',
    'tunísia','turquia','ucrânia','uruguai','vaticano','vietnam','zâmbia']
    
    comida=['macarrão','carne','ovo','arroz','feijão','strogonoff','pizza','hamburguer',
    'acarajé','baião de dois','biscoito de polvilho','camarão','bolinho de chuva',
    'tapioca','mandioca','brigadeiro','canjica','caranguejo','carne de sol',
    'churrasco','cocada','coxinha','cuscuz','empadão','farofa','feijoada',
    'frango','quiabo','galinhada','paçoca','pamonha','pão de queijo','curau',
    'pastel','pato no tucupi','pudim','queijo','rapadura']
    
    cor=['azul','amarelo','verde','rosa','preto','vermelho','marrom','cinza',
    'laranja','roxo','branco','bege','bordô','bronze','ciano','dourado','violeta']
    
    planeta=['mercúrio','vênus','terra','marte','júpiter','saturno','urano','netuno']
    teste=['maringá']
    teste2=['açaí']
    temas='Fruta, Pais, Comida, Cor, Planeta'
    temas0='fruta','carro','pais','comida','cor','planeta','sair'
    tema=input(f'Escolha o tema da palavra {temas}: ').lower().strip()
    if tema=='comida':
        palavra_escolhida=cho(comida) 
    if tema=='planeta':
        palavra_escolhida=cho(planeta) 
    if tema=='cor':
        palavra_escolhida=cho(cor)    
    if tema=='fruta':
        palavra_escolhida=cho(fruta)
    if tema=='pais':
        palavra_escolhida=cho(pais)
    if tema=='teste':
        palavra_escolhida=cho(teste)
    if tema=='teste2':
        palavra_escolhida=cho(teste2)
    if tema=='sair':
        exit()
    if tema not in temas0:
        while tema not in temas0:
            print(f'Tema Inexistente! Digite um tema da lista {temas}')
            tema=input(f'Escolha o tema da palavra {temas}: ').lower()
        else:
            if tema=='comida':
                palavra_escolhida=cho(comida) 
            if tema=='cor':
                palavra_escolhida=cho(cor)     
            if tema=='fruta':
                palavra_escolhida=cho(fruta)
            if tema=='pais':
                palavra_escolhida=cho(pais)
            if tema=='planeta':
                palavra_escolhida=cho(planeta)
            if tema=='sair':
                exit()
    tam_palav=len(palavra_escolhida)
    #print(palavra_escolhida)
    palavra_escolhida0=palavra_escolhida.title()
    letra=0
    á='á'
    ã='ã'
    ê='ê'
    í='í'
    â='â'
    é='é'
    î='î'
    ó='ó'
    ô='ô'
    õ='õ'
    ú='ú'
    û='û'
    ç='ç'
    chances=0
    letras_digitadas=[]
    letras_temporarias=' '
    espaco=' '
    espacos=palavra_escolhida.count(' ')
    if len(palavra_escolhida) <=5:
        chances=5
    elif len(palavra_escolhida)>=6 and len(palavra_escolhida)<=10:
        chances=7
    elif len(palavra_escolhida)>10:
        chances=10

    print(f'Você tem {chances} chances!')
    print(f'A palavra escolhida tem {tam_palav} letras')
    if espaco in palavra_escolhida:
        letras_digitadas.append(' ')
    for letra in palavra_escolhida:
        if letra in letras_digitadas:
            letras_temporarias+=letra
        else:
            letras_temporarias+='*'
    print(f'A palavra é assim: {letras_temporarias}')        
    
    while letra !='sair':

        letra=str(input('Digite uma letra: ')).lower().strip()
        
        if letra=='sair':
            print('Obrigado por jogar!')
            exit()

        if letra=='c' and letra in palavra_escolhida and letra in letras_digitadas:
            print('Letra já digitada! ')
        elif letra=='c' and letra not in palavra_escolhida and letra in letras_digitadas:
            print(f'Letra já digitada,você ainda tem {chances} tentativas')
        if letra=='a' and letra in palavra_escolhida and letra in letras_digitadas:
            print('Letra já digitada! ')
        elif letra=='a' and letra not in palavra_escolhida and letra in letras_digitadas:
            print(f'Letra já digitada,você ainda tem {chances} tentativas')
        if letra=='e' and letra in palavra_escolhida and letra in letras_digitadas:
            print('Letra já digitada! ')
        elif letra=='e' and letra not in palavra_escolhida and letra in letras_digitadas:
            print(f'Letra já digitada,você ainda tem {chances} tentativas')
        if letra=='i' and letra in palavra_escolhida and letra in letras_digitadas:
            print('Letra já digitada! ')
        elif letra=='i' and letra not in palavra_escolhida and letra in letras_digitadas:
            print(f'Letra já digitada,você ainda tem {chances} tentativas')
        if letra=='o' and letra in palavra_escolhida and letra in letras_digitadas:
            print('Letra já digitada! ')
        elif letra=='o' and letra not in palavra_escolhida and letra in letras_digitadas:
            print(f'Letra já digitada,você ainda tem {chances} tentativas')
        if letra=='u' and letra in palavra_escolhida and letra in letras_digitadas:
            print('Letra já digitada! ')
        elif letra=='u' and letra not in palavra_escolhida and letra in letras_digitadas:
            print(f'Letra já digitada,você ainda tem {chances} tentativas')

        if len(letra) == 1:
            if á or â or ã or ê or é or í or î or ú or û or ó or ô or õ or ç in palavra_escolhida:
                if á in palavra_escolhida:
                    if letra == 'a':
                        letras_digitadas.append('a')
                        letras_digitadas.append('á')
                if ã in palavra_escolhida:
                    if letra == 'a':
                        letras_digitadas.append('a')
                        letras_digitadas.append('ã')
                if â in palavra_escolhida:
                    if letra == 'a':
                        letras_digitadas.append('a')
                        letras_digitadas.append('â')
                if ê in palavra_escolhida:
                    if letra == 'e':
                        letras_digitadas.append('e')
                        letras_digitadas.append('ê')
                if é in palavra_escolhida:
                    if letra == 'e':
                        letras_digitadas.append('e')
                        letras_digitadas.append('é')
                if í in palavra_escolhida:
                    if letra == 'i':
                        letras_digitadas.append('i') 
                        letras_digitadas.append('í')
                    if letra=='i' and letra in letras_digitadas:
                        print('Letra já digitada! ')   
                if î in palavra_escolhida:
                    if letra == 'i':
                        letras_digitadas.append('i')
                        letras_digitadas.append('î')
                if ó in palavra_escolhida:
                    if letra == 'o':
                        letras_digitadas.append('o')
                        letras_digitadas.append('ó')
                if ô in palavra_escolhida:
                    if letra == 'o':
                        letras_digitadas.append('o')
                        letras_digitadas.append('ô')
                if õ in palavra_escolhida:
                    if letra == 'o':
                        letras_digitadas.append('o')
                        letras_digitadas.append('õ')
                if ú in palavra_escolhida:
                    if letra == 'u':
                        letras_digitadas.append('u')
                        letras_digitadas.append('ú')
                if û in palavra_escolhida:
                    if letra == 'u':
                        letras_digitadas.append('u')
                        letras_digitadas.append('û')
                if ç in palavra_escolhida:
                    if letra == 'c':
                        letras_digitadas.append('c')
                        letras_digitadas.append('ç')

            if letra not in palavra_escolhida and letra not in letras_digitadas:
                chances = chances-1
                print(f'Você ainda tem mais {chances} tentativas')
            elif letra =='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u' or letra=='c' and letra not in palavra_escolhida and letra in letras_digitadas:
                print()
            elif letra not in palavra_escolhida and letra in letras_digitadas:
                print(f'Letra já digitada,você ainda tem {chances} tentativas')
            elif letra in palavra_escolhida and letra in letras_digitadas:
                print('Letra já digitada')
        else:
            print('Digite uma letra por vez')

        if chances==0:
            print(f'Você perdeu! A palavra certa era {palavra_escolhida0}')
            jogar_novamente()
        
        letras_digitadas.append(letra)
        letras_temporarias=''
        if espaco in palavra_escolhida:
            letras_digitadas.append(' ')
            if len(letras_temporarias) == len(palavra_escolhida)-espacos:
                print('Parabéns!Você ganhou!!')
                break

        for letra in palavra_escolhida:
            if letra in letras_digitadas:
                letras_temporarias+=letra
            else:
                letras_temporarias+='*'
    
        if letras_temporarias==palavra_escolhida:
            print(f"Parabéns,você venceu! A palavra era {palavra_escolhida0} ")
            jogar_novamente()
        else:
            print(f'A palavra secreta está assim {letras_temporarias}')
            #(f'Letras já digitadas:{letras_ja_digitadas}')
        
        
jogar=input('Deseja jogar?(Sim/Não)').lower().strip()
jogar=jogar.replace('ã','a')
while jogar!='sim' or 'nao':
    if jogar=='sim':
        jogo_da_forca()
    elif jogar=='nao':
        print('Obrigado por jogar!')
        break
    else:
        print('Digite sim ou nao: ')
        jogar=input('Deseja jogar?(Sim/Nao)').lower().strip()