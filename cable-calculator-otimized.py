from itertools import combinations
import pprint


class InstallationOtimized:
    def __init__(self):
        self.cameras = {180: 2, 150: 1, 120: 3, 90: 2}
        self.rolls_size = 300
        self.rolls_used = 0
        self.scraps = []
        self.organization = {}

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

    def get_list(self):
        return {
            self.cameras,
            self.rolls_size,
            self.rolls_used,
            self.scraps,
            self.organization,
        }

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

    def install_organizer(self):
        cam_list = self.cam_list()
        organizer = {}
        roll = 1

        while cam_list:
            defined = self.define_cam(cam_list, self.rolls_size)
            organizer[roll] = defined
            for cam in defined.keys():
                del cam_list[cam]
            roll += 1

        return organizer


user = InstallationOtimized()
pprint.pprint(user.install_organizer())
