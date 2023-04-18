#!usr/bin/python3

import app_tasques
import tasca

def main():
    t = None
    la_app = app_tasques.App_tasques()

    la_app.afegeix_tasca(tasca.Tasca(None, "Escombrar les escales"))
    la_app.afegeix_tasca(tasca.Tasca(None, "Portar el cotxe a la ITV"))

    for t in la_app.llegir_tasques():
        print(t)

    if t:
        t.done = True
        la_app.modifica_tasca(t)
        print("tasca modificada")
    
    for t in la_app.llegir_tasques():
        print(t)
    if t:
        la_app.esborra_tasca(t.id)
        print("tasca esborrada")


if __name__== "__main__":
    main()


