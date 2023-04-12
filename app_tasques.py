#!/usr/bin/python3

class App_tasques():
    def __init__(self):
        self._llista = []

    def afegeix_tasca(self, tasca_nova):
        self._llista.append(tasca_nova)

    def llegir_tasques(self):
        return self._llista
