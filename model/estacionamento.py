from model.vaga import Vaga


class Estacionamento:
    def __init__(self):
        self.vagas = [Vaga(num+1) for num in range(10)]
        self.historico = []

    def estacionar(self, veiculo, num_vaga):
        vaga = self.vagas[num_vaga]
        vaga.ocupada = True
        vaga.ocupar(veiculo)
        self.historico.append({"acao": "entrada", "placa": veiculo.placa})
    
    def retirar(self, num_vaga, num_horas):
        vaga = self.vagas[num_vaga - 1]
        veiculo = vaga.liberar()
        tarifa = veiculo.calcular_tarifa(num_horas)
        self.historico.append({"acao": "saida", "placa": veiculo.placa, "valor": tarifa})
    
    def relatorio(self):
        pass














# import json

# from model.vaga import Vaga


# class Estacionamento:
#     def __init__(self, total_vagas=10):
#         self.vagas = [Vaga(i+1) for i in range(total_vagas)]
#         self.historico = []

#     def estacionar(self, veiculo, numero_vaga):
#         vaga = self.vagas[numero_vaga - 1]
#         vaga.ocupar(veiculo)
#         self.historico.append({"acao": "entrada", "placa": veiculo.placa})

#     def retirar(self, numero_vaga, horas):
#         vaga = self.vagas[numero_vaga - 1]
#         veiculo = vaga.liberar()
#         tarifa = veiculo.calcular_tarifa(horas)
#         self.historico.append({
#             "acao": "saida",
#             "placa": veiculo.placa,
#             "valor": tarifa
#         })
#         return tarifa

#     def relatorio(self):
#         ocupadas = sum(1 for v in self.vagas if v.ocupada)
#         livres = len(self.vagas) - ocupadas
#         return {"ocupadas": ocupadas, "livres": livres}

#     def salvar_historico(self, arquivo="historico.json"):
#         with open(arquivo, "w") as f:
#             json.dump(self.historico, f, indent=4)
