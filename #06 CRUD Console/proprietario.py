import pessoa

class proprietario(pessoa.pessoa):
    def __repr__(self): 
        return "ID:%s nome:%s datanasc:%s" % (self.id, self.nome, self.datanasc)