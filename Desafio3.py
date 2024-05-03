class Heroi:
    def __init__(self,*, nome, idade, tipo):
        self._nome = nome
        self._idade = idade
        self._tipo = tipo

    def atacar(self):

        ataque = ''

        if self._tipo == 'mago':
            ataque = 'magia'
        elif self._tipo == 'guerreiro':
            ataque = 'espada'
        elif self._tipo == 'monge':
            ataque = 'artes marciais'
        elif self._tipo == 'ninja':
            ataque =  'shiriken'
        print(f"o {self._tipo} atacou usando {ataque}")

heroi1 = Heroi(nome='Avdol', idade=45, tipo='mago')

heroi1.atacar()
