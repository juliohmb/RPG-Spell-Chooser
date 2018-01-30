# JUL10#M8
class LMagias(object):
    def __init__(self, classe):
        self.classe = classe
        self.magias_dic = {}
        self.magias_esc_dic = {}

    def truques(self):
        truques_keys = open('keys/truques_keys.txt', 'r')
        truques = open('magias/truques.txt', 'r')
        lista_magias = truques.readlines()
        lista_magias_org = []
        for n in range(27):
            while lista_magias[0] == '\n':
                lista_magias.pop(0)
            lista_magias_org.append(lista_magias[:lista_magias.index('\n')])
            del lista_magias[:lista_magias.index('\n')]
        del lista_magias
        for n in range(27):
            self.magias_dic[truques_keys.readline().replace('\n', '').upper()] = ''.join(lista_magias_org[n])

    def magia_n1(self):
        magias_1 = open('magias/magias_n1.txt', 'r')
        lista_magias = ['Alarme','Área Escorregadia','Armadura Arcana','Armadura de Agathys','Ataque Restringente','Auxílio Divino','Bênção','Bom Fruto','Braços de Hadar','Chuva de Espinhos','Comando','Compreender Idiomas','Constrição','Convocar Familiar','Criar ou Destruir Água','Curar Ferimentos','Detectar Bem e Mal','Detectar Magia','Detectar Veneno e Doença','Disco Flutuante de Tenser','Enfeitiçar Animal','Enfeitiçar Pessoa','Escrita Ilusória','Escudo Arcano','Escudo da Fé','Faísca da Bruxa','Falar com Animais','Fogo das Fadas','Forçar Duelo','Heroísmo','Identificar','Imagem Silenciosa','Infligir Ferimentos','Leque Cromático','Maldição','Mãos Flamejantes','Marca do Caçador','Mísseis Mágicos','Névoa','Onda Trovejante','Orbe Cromático','Palavra de Cura','Passos Longos','Praga','Proteção Contra Bem e Mal','Punição Ardente','Punição Furiosa','Punição Trovejante','Purificar Comida e Bebida','Queda Suave','Raio Doentio','Raio Guiado','Recuo Acelerado','Repreensão Infernal','Riso Histérico de Tasha','Salto','Santuário','Servo Invisível','Sono','Sussurros Perturbadores','Transformação Momentânea','Vitalidade Ilusória']
        lista_des = magias_1.readlines()
        lista_magias_org = []
        for i in range(len(lista_magias)):
            while lista_des[0] == '\n':
                lista_des.pop(0)
            lista_magias_org.append(lista_des[:lista_des.index('\n')])
            del lista_des[:lista_des.index('\n')]
        for n in lista_magias:
            self.magias_dic[n.upper()] = ''.join(lista_magias_org[lista_magias.index(n)])

    def magia_n2(self):
        magias_2 = open('magias/magias_n2.txt', 'r')
        lista_magias = ['Abrir','Acalmar Emoções','Ajuda','Alterar-se','Arma Espiritual','Arma Mágica','Aumentar/Diminuir','Augúrio','Aura Mágica de Nystul','Bloqueio de Flechas','Boca Mágica','Borrão','Cativar','Cegueira/Surdez','Chama Contínua','Convocar Montaria','Coroa da Loucura','Crescer Espinhos','Descanso Tranquilo','Despedaçar','Detectar Pensamentos','Encontrar Armadilhas','Escuridão','Esfera Flamejante','Esquentar Metais','Flecha Ácida de Melf','Força Fantasmagórica','Habilidade Melhorada','Imobilizar Pessoa','Invisibilidade','Lâmina Flamejante','Levitação','Localizar Animais ou Plantas','Localizar Objeto','Lufada de Vento','Mensageiro Animal','Nuvem de Adagas','Oração de Cura','Passo das Brumas','Passo sem Pegadas','Patas de Aranha','Pele de Árvore','Proteção Contra Venenos','Punição Sinalizadora','Raio Ardente','Raio do Enfraquecimento','Raio Lunar','Reflexos','Restauração Menor','Sentidos da Besta','Silêncio','Sugestão','Teia','Tranca Arcana','Truque da Corda','Ver o Invisível','Vínculo de Proteção','Visão no Escuro','Zona da Verdade']
        lista_des = magias_2.readlines()
        lista_magias_org = []
        for i in range(len(lista_magias)):
            while lista_des[0] == '\n':
                lista_des.pop(0)
            lista_magias_org.append(lista_des[:lista_des.index('\n')])
            del lista_des[:lista_des.index('\n')]
        for n in lista_magias:
            self.magias_dic[n.upper()] = ''.join(lista_magias_org[lista_magias.index(n)])

    def magia_n3(self):
        magias_3 = open('magias/magias_n3.txt', 'r')
        lista_magias = ['Ampliar Plantas', 'Animar os Mortos', 'Arma Elemental', 'Aura de Vitalidade', 'Bola de Fogo', 'Caminhar na Água', 'Círculo Mágico', 'Clarividência', 'Conjurar Artilharia', 'Contramágica', 'Convocar Relâmpagos', 'Criar Água e Comida', 'Dificultar Detecção', 'Dissipar Magia', 'Enviar Mensagem', 'Falar com os Mortos', 'Falar com Plantas', 'Farol de Esperança', 'Fingir-se de Morto', 'Flecha Elétrica', 'Fome de Hadar', 'Forma Gasosa', 'Guardiões Espirituais', 'Idiomas',
                        'Imagem Maior', 'Invocar Animais', 'Lentidão', 'Luz do Dia', 'Manto do Cruzado', 'Medo', 'Mesclar-se às Rochas', 'Montaria Fantasmagórica', 'Muralha de Vento', 'Nevasca', 'Névoa Fétida', 'Padrão Hipnótico', 'Palavra de Cura em Massa', 'Pequeno Refúgio de Leomund', 'Piscar', 'Proteção Contra Energia', 'Punição Cegante', 'Relâmpago', 'Remover Maldição', 'Respirar na Água', 'Reviver', 'Rogar Maldição', 'Símbolo de Proteção', 'Toque Vampírico',
                        'Velocidade', 'Voo']
        lista_des = magias_3.readlines()
        lista_magias_org = []
        for i in range(len(lista_magias)):
            while lista_des[0] == '\n':
                lista_des.pop(0)
            lista_magias_org.append(lista_des[:lista_des.index('\n')])
            del lista_des[:lista_des.index('\n')]
        for n in lista_magias:
            self.magias_dic[n.upper()] = ''.join(lista_magias_org[lista_magias.index(n)])

    def magia_n4(self):
        magias_4 = open('magias/magias_n4.txt', 'r')
        lista_magias = ['Adivinhação', 'Arca Secreta de Leomund', 'Assassino Fantasmagórico', 'Aura de Pureza', 'Aura de Vida', 'Banimento', 'Cão Fiel de Mordenkainen', 'Compulsão', 'Confusão', 'Controlar Água', 'Dominar Animais', 'Escudo de Fogo', 'Esfera Resiliente de Otiluke', 'Fabricação', 'Guardião da Fé', 'Inseto Gigante', 'Invisibilidade Maior', 'Invocar Elementais Menores', 'Invocar Seres da Floresta', 'Localizar Criatura', 'Metamorfose', 'Moldar Rochas', 'Movimentação Livre', 'Muralha de Fogo',
                        'Olho Arcano', 'Pele Rochosa', 'Porta Dimensional', 'Proteção Contra a Morte', 'Punição Arrebatadora', 'Santuário Particular de Mordenkainen', 'Secar', 'Tempestade Glacial', 'Tentáculos Negros de Evard', 'Terreno Ilusório', 'Vinhas Sufocantes']
        lista_des = magias_4.readlines()
        lista_magias_org = []
        for i in range(len(lista_magias)):
            while lista_des[0] == '\n':
                lista_des.pop(0)
            lista_magias_org.append(lista_des[:lista_des.index('\n')])
            del lista_des[:lista_des.index('\n')]
        for n in lista_magias:
            self.magias_dic[n.upper()] = ''.join(lista_magias_org[lista_magias.index(n)])

    def magia_n5(self):
        magias_5 = open('magias/magias_n5.txt', 'r')
        lista_magias = ['Aljava Veloz', 'Âncora Planar', 'Animar Objetos', 'Barreira Antivida', 'Caminhar por Árvores', 'Círculo de Poder', 'Círculo de Teletransporte', 'Coluna de Chamas', 'Comunhão', 'Comunhão com a Natureza', 'Cone Glacial', 'Conjurar Rajada', 'Contato Extraplanar', 'Criação', 'Criar Passagens', 'Curar Ferimentos em Massa', 'Despertar', 'Despistar', 'Dissipar Bem e Mal', 'Dominar Pessoa', 'Epidemia', 'Imobilizar Monstro', 'Invocar Elemental', 'Lendas e Histórias',
                        'Ligação Telepática de Rary', 'Mão de Bigby', 'Missão', 'Modificar Memória', 'Muralha de Energia', 'Muralha de Pedra', 'Névoa Mortal', 'Praga de Insetos', 'Punição Banidora', 'Punição Destrutiva', 'Reencarnação', 'Restauração Maior', 'Reviver Mortos', 'Santificar', 'Similaridade', 'Sonho', 'Telecinésia', 'Vidência']
        lista_des = magias_5.readlines()
        lista_magias_org = []
        for i in range(len(lista_magias)):
            while lista_des[0] == '\n':
                lista_des.pop(0)
            lista_magias_org.append(lista_des[:lista_des.index('\n')])
            del lista_des[:lista_des.index('\n')]
        for n in lista_magias:
            self.magias_dic[n.upper()] = ''.join(lista_magias_org[lista_magias.index(n)])

    def magia_n6(self):
        magias_6 = open('magias/magias_n6.txt', 'r')
        lista_magias = ['Aliado Extra-Planar', 'Ataque Visual', 'Banquete de Heróis', 'Barreira de Lâminas', 'Caminhar no Vento', 'Carne para Pedra', 'Círculo da Morte', 'Contingência', 'Corrente de Relâmpagos', 'Criar Morto-Vivo', 'Cura', 'Dança Irresistível de Otto', 'Desintegrar', 'Doença Plena', 'Encontrar o Caminho', 'Esfera Gélida de Otiluke', 'Globo de Invulnerabilidade', 'Ilusão Programada', 'Invocação Instantânea de Drawmij', 'Invocar Feérico', 'Mover Terra', 'Muralha de Espinhos', 'Muralha de Gelo', 'Palavra de Recordação',
                        'Portão Arcano', 'Proibição', 'Proteger Fortalezas', 'Raio de Sol', 'Recipiente Arcano', 'Sugestão em Massa', 'Teletransporte por Árvores', 'Visão da Verdade']
        lista_des = magias_6.readlines()
        lista_magias_org = []
        for i in range(len(lista_magias)):
            while lista_des[0] == '\n':
                lista_des.pop(0)
            lista_magias_org.append(lista_des[:lista_des.index('\n')])
            del lista_des[:lista_des.index('\n')]
        for n in lista_magias:
            self.magias_dic[n.upper()] = ''.join(lista_magias_org[lista_magias.index(n)])

    def magia_n7(self):
        magias_7 = open('magias/magias_n7.txt', 'r')
        lista_magias = ['Bola de Fogo Controlável', 'Cubo de Energia', 'Dedo da Morte', 'Espada de Mordenkainen', 'Forma Etérea', 'Inverter a Gravidade', 'Invocar Celestial', 'Isolar', 'Mansão Magnífica de Mordenkainen', 'Miragem Arcana', 'Palavra Divina', 'Projetar Imagem', 'Rajada Prismática', 'Regeneração', 'Ressurreição', 'Símbolo', 'Simulacro', 'Teletransporte', 'Tempestade de Fogo', 'Viagem Planar']
        lista_des = magias_7.readlines()
        lista_magias_org = []
        for i in range(len(lista_magias)):
            while lista_des[0] == '\n':
                lista_des.pop(0)
            lista_magias_org.append(lista_des[:lista_des.index('\n')])
            del lista_des[:lista_des.index('\n')]
        for n in lista_magias:
            self.magias_dic[n.upper()] = ''.join(lista_magias_org[lista_magias.index(n)])

    def magia_n8(self):
        magias_8 = open('magias/magias_n8.txt', 'r')
        lista_magias = ['Antipatia/Simpatia', 'Aura Sagrada', 'Campo Antimagia', 'Clone', 'Controlar o Clima', 'Dominar Monstro', 'Eloquência', 'Explosão Solar', 'Forma Animal', 'Labirinto', 'Limpar a Mente', 'Mente Débil', 'Nuvem Incendiária', 'Palavra de Poder Atordoar', 'Semiplano', 'Telepatia', 'Terremoto', 'Tsunami']
        lista_des = magias_8.readlines()
        lista_magias_org = []
        for i in range(len(lista_magias)):
            while lista_des[0] == '\n':
                lista_des.pop(0)
            lista_magias_org.append(lista_des[:lista_des.index('\n')])
            del lista_des[:lista_des.index('\n')]
        for n in lista_magias:
            self.magias_dic[n.upper()] = ''.join(lista_magias_org[lista_magias.index(n)])

    def magia_n9(self):
        magias_9 = open('magias/magias_n9.txt', 'r')
        lista_magias = ['Alterar Forma', 'Aprisionamento', 'Chuva de Meteoros', 'Cura em Massa', 'Desejo', 'Metamorfose Verdadeira', 'Muralha Prismática', 'Palavra de Poder Curar', 'Palavra de Poder Matar', 'Parar o Tempo', 'Pavor', 'Portal', 'Previsão', 'Projeção Astral', 'Ressurreição Verdadeira', 'Tempestade da Vingança']
        lista_des = magias_9.readlines()
        lista_magias_org = []
        for i in range(len(lista_magias)):
            while lista_des[0] == '\n':
                lista_des.pop(0)
            lista_magias_org.append(lista_des[:lista_des.index('\n')])
            del lista_des[:lista_des.index('\n')]
        for n in lista_magias:
            self.magias_dic[n.upper()] = ''.join(lista_magias_org[lista_magias.index(n)])

    def classe_magias(self):
        classe = self.classe
        if classe == 'BARDO':
            magias = open('raças/bardo.txt', 'r')
            print('-'*20)
            print(magias.read())
            magias.close()
        if classe == 'BRUXO':
            magias = open('raças/bruxo.txt', 'r')
            print('-'*20)
            print(magias.read())
            magias.close()
        if classe == 'Clérigo':
            magias = open('raças/clérigo.txt', 'r')
            print('-'*20)
            print(magias.read())
            magias.close()
        if classe == 'DRUIDA':
            magias = open('raças/druida.txt', 'r')
            print('-'*20)
            print(magias.read())
            magias.close()
        if classe == 'FEITICEIRO':
            magias = open('raças/feiticeiro.txt', 'r')
            print('-'*20)
            print(magias.read())
            magias.close()
        if classe == 'Mago':
            magias = open('raças/mago.txt', 'r')
            print('-'*20)
            print(magias.read())
            magias.close()
        if classe == 'PALADINO':
            magias = open('raças/paladino.txt', 'r')
            print('-'*20)
            print(magias.read())
            magias.close()
        if classe == 'RANGER':
            magias = open('raças/ranger.txt', 'r')
            print('-'*20)
            print(magias.read())
            magias.close()

    def magias_des(self):
        print('-' * 20)
        while True:
            mag = input('Digite o nome da magia que deseja ler a descrição(ACENTOS CONTAM), '
                        '\ndigite [0] para terminar a consulta de magias:\n').upper()
            if mag.isnumeric() and int(mag) == 0:
                print('-' * 20)
                break
            elif mag == '':
                continue
            elif mag.isnumeric() and int(mag) != 0:
                print('Valor invalido')
                continue
            try:
                print('-' * 20)
                print(self.magias_dic[mag])
            except:
                continue
            print('-' * 20)
            esc = input('Para outra consulta, digite [0], para aprender esta magia, digite [1]\n')
            if esc.isnumeric():
                esc = int(esc)
                if esc == 1:
                    self.magias_esc_dic[mag] = self.magias_dic[mag] + '\n'
                    print('-' * 20)
                else:
                    print('-' * 20)
                    continue
            self.classe_magias()
            print('-' * 20)

    def arquivo_magias(self):
        magias_escolhidas = open('magias_escolhidas/magias_escolhidas.txt', 'w')
        for n in self.magias_esc_dic.keys():
            magias_escolhidas.write(self.magias_esc_dic[n])
        magias_escolhidas.close()


def pergunta():
    lista_classes = ['BARDO', 'BRUXO', 'Clérigo', 'DRUIDA', 'FEITICEIRO', 'Mago', 'PALADINO', 'RANGER']
    print('Você escolheu uma classe que possui truques e/ou magias!\nPor isso deve escolher as que mais te agradar')
    print('Antes de tudo precisa me dizer sua classe')
    while True:
        classe = input('\nDigite sua classe:\n').upper()
        if classe in lista_classes:
            break
        else:
            continue
    return classe


def main():
    per = pergunta()
    l_magias = LMagias(per)
    l_magias.classe_magias()
    l_magias.truques()
    l_magias.magia_n1()
    l_magias.magia_n2()
    l_magias.magia_n3()
    l_magias.magia_n4()
    l_magias.magia_n5()
    l_magias.magia_n6()
    l_magias.magia_n7()
    l_magias.magia_n8()
    l_magias.magia_n9()
    l_magias.magias_des()
    l_magias.arquivo_magias()


main()
