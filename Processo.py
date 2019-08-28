processos = []
class Processos():
    def __init__(self, id_coordenador, id_processo, ativo=True):
       self.id_coordenador = id_coordenador
       self.id_processo = id_processo
       self.ativo = ativo
    
    def get_active(self):
       return self.ativo 
    
    def get_id_process(self):
        return self.id_processo

    def get_id_coordenador(self):
        return self.id_coordenador

    def set_id_coordenador(self, id_new_coordenador):
        self.id_coordenador = id_new_coordenador

    def call_all (self, id_called ):
        for j in processos:
            j.set_id_coordenador(id_called)      

    def printt(self):
        print("Coordenador {} Processo {} Ativo {}".format(self.id_coordenador, self.id_processo, self.ativo))

    def desativar(self):
        if (self.ativo):
            self.ativo = False
        else:
            self.ativo = True
        print("\nEstado do processo id {}, estado {}\n".format(self.id_processo, self.ativo))

    def eleicao(self):
        for i in processos:
            if (i.get_id_process() > self.id_processo):
                if (i.get_active()):
                    print("Processo {} saiu da eleição ".format(self.id_processo))
                    i.eleicao()
                    break
                if (self.id_coordenador == i.get_id_process()) and (i.get_active() == False):
                    self.id_coordenador = self.id_processo
                    print("\nNovo coordenador {}\n".format(self.id_processo))
                    i.call_all(self.id_processo)        

numero_de_processos = int(input("Digite o número de processos: "))
processo_eleicao = int(input("Digite o processo que vai pedir a eleição do novo coordenador: "))
count = 1

while(count <= numero_de_processos):
    process = Processos(numero_de_processos  , count )
    processos.append(process)
    count += 1
print("\nCoordenador atual, processos, se esta ativo \n")
for l in processos:
    
    l.printt()

processos[len(processos)-1].desativar()

print("\nProcessos que não podem concorrer \n ")
for k in processos:
    if k.get_id_process() == processo_eleicao:
        k.eleicao()
        break

print("Novo coordenador, processos, se esta ativo \n")

for h in processos:
    
    h.printt()