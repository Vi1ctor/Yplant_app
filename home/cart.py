import joblib
from sklearn.metrics import confusion_matrix

class CARTlgoritm:
    def __init__(self, modelo_path):
        # Carrega o modelo treinado a partir do caminho especificado
        self.modelo_cart = joblib.load(modelo_path)

    def fazer_previsao(self, dados_entrada):
        # Faz uma previsão com base nos dados de entrada
        previsao = self.modelo_cart.predict([dados_entrada])
        return previsao
    
    def calcular_matriz_confusao(self, valores_reais, previsoes, labels=None):
        matriz_confusao = confusion_matrix(valores_reais, previsoes, labels=labels)
        return matriz_confusao