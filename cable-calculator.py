class CalculadoraInstalacao:
    def __init__(self):
        self.metragens = []
        self.tamanhos_rolos = []
        self.qtd_cameras = {}

    def definir_metragens_cameras(self):
        print("Digite as possíveis metragens de câmeras (separadas por vírgula):")
        metragens_str = input().strip()
        self.metragens = [int(m.strip()) for m in metragens_str.split(",")]
        print(f"Metragens de câmeras definidas: {self.metragens}\n")

    def definir_tamanhos_rolos(self):
        print("Digite os possíveis tamanhos de rolos (separados por vírgula):")
        tamanhos_str = input().strip()
        self.tamanhos_rolos = [int(t.strip()) for t in tamanhos_str.split(",")]
        print(f"Tamanhos de rolos definidos: {self.tamanhos_rolos}\n")

    def definir_qtd_cameras(self):
        print("Digite a quantidade de câmeras para cada metragem:")
        for metragem in self.metragens:
            qtd = int(input(f"{metragem} metros: "))
            self.qtd_cameras[metragem] = qtd
        print(f"Quantidade de câmeras definida: {self.qtd_cameras}\n")

    def obter_informacoes(self):
        return {
            "metragens": self.metragens,
            "tamanhos_rolos": self.tamanhos_rolos,
            "qtd_cameras": self.qtd_cameras
        }


calc = CalculadoraInstalacao()
calc.definir_metragens_cameras()
calc.definir_tamanhos_rolos()
calc.definir_qtd_cameras()
info = calc.obter_informacoes()
