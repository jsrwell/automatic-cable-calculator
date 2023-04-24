from itertools import combinations
import pprint
import pandas as pd


class InstallationOtimized:
    def __init__(self):
        # Format: {INT Length: INT Qnt}
        self.cameras = {}
        # Format: INT length
        self.rolls_size = 305
        # Format: INT rolls
        self.rolls_used = 0
        # Format: [INT length]
        self.scraps = []
        # Format: {STR Name_Roll: {STR Name_Cam: INT length, STR Scraps: INT length}} # noqa E501
        self.organization = {}

    # BAIXA CAMERAS E TOTAIS DA PLANILHA
    def table_cameras(self, tb_name):
        # colunas antes do cabeçalho
        pre_header = 3
        # lista completa da planilha
        table = pd.read_excel(tb_name, 'POSICIONAMENTO',
                              header=None, skiprows=pre_header).values.tolist()
        # titulo do cabeçalho sendo procurado
        search_cam = 'CÂMERA'
        search_length = 'TOTAL'
        # index da coluna
        index_cam = table[0].index(search_cam)
        index_length = table[0].index(search_length)
        # listando todos os nomes de câmeras
        camera_names = {}
        for i, cam in enumerate(table[1:-1]):
            if cam[index_cam].startwith('CF'):
                camera_names[f'CF{int(cam[index_cam].replace("CF", "")).zfill(3)}'] = int(
                    cam[index_length])
            elif cam[index_cam].startwith('CD'):
                camera_names[f'CD{int(cam[index_cam].replace("CD", "")).zfill(3)}'] = int(
                    cam[index_length])
            else:
                camera_names[f'ID{str(i+1).zfill(3)} {cam[index_cam]}'] = int(
                    cam[index_length])
        self.cameras = camera_names
        print(f'{len(camera_names)} listados.')

    # RETORNA A LISTA COM TODOS OS DADOS DO OBJETO
    def get_list(self):
        return {
            'cameras': self.cameras,
            'rolls_size': self.rolls_size,
            'rolls_used': self.rolls_used,
            'scraps': self.scraps,
            'organization': self.organization,
        }

    # FUNÇÃO CHAMADA POR install_organizer(self) -> DEFINE O MELHOR GRUPO DE CAMERAS POR ROLO # noqa E051
    def define_cam(self, cam_list, rolls_size):
        best_combination = {}
        best_value = 0
        # Inicia um loop que gera a quantidade de intens que podem ser combinados # noqa E051
        for i in range(1, len(cam_list)+1):
            # usando o itertools gera todas as combinações possíveis
            # i é o tamanho das combinações
            for combination in combinations(cam_list.items(), i):
                # gera a variavel com o valor da soma dos valores de cada combinação # noqa E051
                value = sum([v for k, v in combination])
                # testa se o valor é menor igual ao rolo e maior que o melhor valor # noqa E051
                if value <= rolls_size and value >= best_value:
                    # atualiza lista e valores de comparação
                    best_combination = dict(combination)
                    best_value = value
                    # se o valor for igual ao tamanho do rolo retorna imediatamente # noqa E051
                    if value == rolls_size:
                        return best_combination
                    # if i > 5:
                    #    return best_combination
        # retorna a melhor combinação
        return best_combination

    # DEFINE A ORGANIZAÇÃO GERAL DE INSTALAÇÃO
    def install_organizer(self):
        # recupera a lista de cameras
        cam_list = self.cameras.copy()
        organizer = {}
        roll = 0
        # realiza a função enquanto houver itens dentro da lista de cameras
        while cam_list:
            # numera o rolo
            roll += 1
            # se o cumprimento da camera for excedente ao rolo
            if list(cam_list.values())[0] > self.rolls_size:
                organizer[f'Rolo nº {str(roll).zfill(3)} Excedente'] = {
                    list(cam_list.keys())[0]: int(list(cam_list.values())[0])
                }
                # adiciona os excessos
                organizer[f'Rolo nº {str(roll).zfill(3)} Excedente'][
                    'Sobra'] = f'Excedente {self.rolls_size - int(list(cam_list.values())[0])}'
                # elimina item da lista
                del cam_list[list(cam_list.keys())[0]]
            else:
                # acha a melhor combinação de cameras para menor sobra o possível
                defined = self.define_cam(cam_list, self.rolls_size)
                # atribui a melhor combinação a lista organizada
                organizer[f'Rolo nº {str(roll).zfill(3)}'] = defined
                # deleta todos os itens da lista de cameras disponíveis
                for cam in defined.keys():
                    del cam_list[cam]
                # adiciona as sobras
                organizer[f'Rolo nº {str(roll).zfill(3)}']['Sobra'] = self.rolls_size - \
                    sum(defined.values())
        # define a organização do objeto, rolos usados e sobras
        self.organization = organizer
        self.rolls_used = roll
        self.scraps = [scrap['Sobra'] for scrap in organizer.values()]
        # retorna a lista organizada dos rolos com cada camera e sobras
        return organizer


tb_name = 'Teste.xlsx'

user = InstallationOtimized()
user.table_cameras(tb_name)
pprint.pprint(user.get_list()['cameras'])
user.install_organizer()
pprint.pprint(user.get_list())
