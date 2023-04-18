#user/bin/python3
import json
class Tasca ():
    """
    tasca.py conté la classe de Tasca que es la classe principal de la  nostra apl
    """
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @ property 
    def persistencia (self):
       return self._persistencia
    
    @persistencia.setter
    def persistencia (self, valor):
        self._persistencia = valor 

    @property
    def titol(self):
        return self._titol
    @titol.setter
    def titol(self, valor):
        self._titol = str(valor).strip()

    @property
    def done(self):
        return self._done
    @done.setter
    def done(self, valor):
        self._done = valor

    def __init__(self, persistencia, titol, done=False, id=None):
        # assert issubclass(type(persistencia), src.app_todo.persistencia_tasca.Persistencia_tasca) 
            # self._persistencia = persistencia

        """
        la funció strip() treu els espais sobrants 
        del darrera i del començament d'una cadena de text.
        """

        self._titol = str(titol).strip()
        self._done = done
        self._id = id   

    def desa(self):
        resultat = self._persistencia.desa(self)
        if resultat:
            self._id = resultat.id
        return resultat

    def __str__(self):
        resultat = {'id': self._id, 'titol': self._titol, 'done': self._done}
        return json.dumps(resultat)
