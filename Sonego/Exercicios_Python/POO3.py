class BaseDeDados:
    def __init__(self):
        self.__dados = {}
    
    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id:nome}
        else:
            self.__dados['clientes'].update({id:nome})
    
    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)
    
    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

    @property
    def dados(self):
        return self.__dados
    
Base = BaseDeDados()
Base.inserir_clientes(12, 'joao')
Base.lista_clientes()
#Base.dados = 'Crientes'
Base.lista_clientes()
print(Base._BaseDeDados__dados)
print(Base.dados)
