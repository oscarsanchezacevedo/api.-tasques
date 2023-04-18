#!/usr/bin/python3
import persistencia_tasca_sqlite

RUTA_BD = "todo_list.db"
class App_tasques():
    def __init__(self):
        self._persistencia_tasques = persistencia_tasca_sqlite.Persitencia_tasca_sqlite(RUTA_BD)

    def afegeix_tasca(self, tasca_nova):
        tasca_nova.persistencia = self._persistencia_tasques
        tasca_nova.desa()

    def llegir_tasques(self):
        return self._persistencia_tasques.get_list()
