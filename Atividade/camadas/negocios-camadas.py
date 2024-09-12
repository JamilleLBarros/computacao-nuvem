from camada_dados import CamadaDados

class CamadaNegocios:
    def __init__(self):
        self.dados = CamadaDados()

    def adicionar_contato(self, nome, telefone):
        if not nome or not telefone:
            raise ValueError("Nome e telefone são obrigatórios")
        return self.dados.adicionar_contato(nome, telefone)

    def adicionar_compromisso(self, descricao, data, contato_id=None):
        if not descricao or not data:
            raise ValueError("Descrição e data são obrigatórios")
        return self.dados.adicionar_compromisso(descricao, data, contato_id)

    def listar_contatos(self):
        return self.dados.listar_contatos()

    def listar_compromissos(self):
        compromissos = self.dados.listar_compromissos()
        return [
            {
                'id': c[0],
                'descricao': c[1],
                'data': c[2],
                'contato': {'id': c[3], 'nome': c[4]} if c[3] else None
            }
            for c in compromissos
        ]