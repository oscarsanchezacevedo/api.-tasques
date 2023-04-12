#!usr/bin/python3

import app_tasques
import tasca

def main():
    la_app = app_tasques.App_tasques()

    la_app.afegeix_tasca(tasca.Tasca(None, "Escombrar les escales"))
    la_app.afegeix_tasca(tasca.Tasca(None, "Portar el cotxe a la ITV"))

    for t in la_app.llegir_tasques():
        print(t)

if __name__== "__main__":
    main()


