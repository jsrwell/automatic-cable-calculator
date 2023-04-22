from itertools import combinations
import pprint


class InstallationOtimized:
    def __init__(self):
        self.cameras = {150: 2, 130: 1, 110: 3, 90: 2, 60: 3}
        self.rolls_size = 300
        self.rolls_used = 0
        self.scraps = []
        self.organization = {}

    # ADICIONAR CAMERAS AO OBJETO
    def add_cameras(self):
        # checagem para metragem das cameras a serem adicionadas
        print("Qual a metragem das cameras que você irá adicionar?")
        camera_input_length = int(input().strip())
        # checagem para quantidade com base na metragem
        print(f"Quantas cameras de {camera_input_length} você irá adicionar?")
        camera_input_qnt = int(input().strip())
        # verificar se a metragem já existe
        if camera_input_length in self.cameras:
            # soma se já existir
            self.cameras[camera_input_length] += camera_input_qnt
        else:
            # cria e atribui o valor
            self.cameras[camera_input_length] = camera_input_qnt
        # retorno com a lista atualizada
        print(self.cameras)

    # DELETAR CAMERAS DO OBJETO
    def del_cameras(self):
        # checagem para metragem das cameras a serem adicionadas
        print("Qual a metragem das cameras que você procura?")
        camera_input_length = int(input().strip())
        # verificar se a metragem já existe
        if camera_input_length in self.cameras:
            # se existir, prossegue para as quantidades
            print(f'Existem {self.cameras[camera_input_length]} adicionadas, quantas deseja remover?')  # noqa E501
            camera_input_qnt = int(input().strip())
            # checa se será apenas uma subtração ou se irá remover todas
            if self.cameras[camera_input_length] > camera_input_qnt:
                # subtrai se o numero for menor do que existe
                self.cameras[camera_input_length] -= camera_input_qnt
            else:
                # apaga a chave se for maior
                del self.cameras[camera_input_length]
        else:
            # informa que não foram localizadas cameras com essa metragem
            print(
                f'Não existem cameras com {camera_input_length} adicionadas.'
            )
        # retorno com a lista atualizada
        print(self.cameras)

    # DEFINE O TAMANHO PADRÃO DOS ROLOS DO OBJETO
    def set_roll(self):
        # questiona novo tamanho informando o tamanho atual
        print(f'Qual o novo tamanho do rolo? (atual: {self.rolls_size})')
        roll = int(input().strip())
        # checa se o valor informado é o mesmo
        if roll == self.rolls_size:
            # informa que o tamanho foi o mesmo
            print('O tamanho inserido foi o mesmo, portanto o valor mantido.')
        else:
            # altera o valor
            self.rolls_size = roll
        # retorno o tamanho do rolo
        print(self.rolls_size)

    # RETORNA A LISTA COM TODOS OS DADOS DO OBJETO
    def get_list(self):
        return {
            self.cameras,
            self.rolls_size,
            self.rolls_used,
            self.scraps,
            self.organization,
        }

    # FUNÇÃO CHAMADA POR install_organizer(self) -> ORGANIZA AS CAMERAS POR NOME
    def cam_list(self):
        # cria a lista e numeração das cameras
        cam_list = {}
        cam_num = 1
        # itera sobre os itens no dicionario das cameras
        for length, num in self.cameras.items():
            # com base na quantidade de cameras para a distancia monta a lista
            for _ in range(num):
                cam_list[f'Camera {cam_num}'] = length
                cam_num += 1
        # retorna a lista numerada das cameras
        return cam_list

    # FUNÇÃO CHAMADA POR install_organizer(self) -> DEFINE O MELHOR GRUPO DE CAMERAS POR ROLO
    def define_cam(self, cam_list, rolls_size):
        best_combination = {}
        best_value = 0

        for i in range(1, len(cam_list)+1):
            for combination in combinations(cam_list.items(), i):
                value = sum([v for k, v in combination])
                if value <= rolls_size and value >= best_value:
                    best_combination = dict(combination)
                    best_value = value
                    if value == rolls_size:
                        return best_combination
        return best_combination

    # DEFINE A ORGANIZAÇÃO GERAL DE INSTALAÇÃO
    def install_organizer(self):
        # organiza a lista de cameras nomeando elas
        cam_list = self.cam_list()
        organizer = {}
        roll = 0
        # realiza a função enquanto houver itens dentro da lista de cameras
        while cam_list:
            # numera o rolo
            roll += 1
            # acha a melhor combinação de cameras para menor sobra o possível
            defined = self.define_cam(cam_list, self.rolls_size)
            # atribui a melhor combinação a lista organizada
            organizer[f'Rolo nº {roll}'] = defined
            # deleta todos os itens da lista de cameras disponíveis
            for cam in defined.keys():
                del cam_list[cam]
            # adiciona as sobras
            organizer[f'Rolo nº {roll}']['Sobra'] = self.rolls_size - \
                sum(defined.values())
        # define a organização do objeto
        self.organization = organizer
        # retorna a lista organizada dos rolos com cada camera e sobras
        return organizer


user = InstallationOtimized()
pprint.pprint(user.install_organizer())
