class ManipulacaoArquivo:
    def __init__(self, arquivo=None, modo='r', codificacao='UTF-8'):
        self.__arquivo = arquivo
        self.__modo    = modo
        self.__codificacao = codificacao    
        
    def obter_dados(self):
        try:
            arquivo = open(self.__arquivo, self.__modo, encoding=self.__codificacao)    
        except:
            return 'Erro ao ler o arquivo'
        else:
            return arquivo.read()
        finally:
            arquivo.close()

    def separar_dados_obtidos(self):
        dados_obtidos = self.obter_dados()
        return dados_obtidos.split()
    
    def exportar_calculo_media(self):
        try:
            arquivo_entrada = open(self.__arquivo, self.__modo, encoding=self.__codificacao)
            arquivo_saida   = open("g://Meu Drive//VIDA//IFRN//PEOO//AULAS//codigo//arquivos_fluxo//text//medias.txt", "w", encoding=self.__codificacao) 
            for linha in arquivo_entrada:
                partes = linha.split()
                nome = partes[0]
                notas = [int(nota) for nota in partes[1:]]
                
                media = sum(notas) / len(notas)
                
                arquivo_saida.write(f"{nome}: {media:.2f}\n")
        except:
            return 'Erro ao gerar ou exportar arquivo'
        finally:
            arquivo_entrada.close()
            arquivo_saida.close()