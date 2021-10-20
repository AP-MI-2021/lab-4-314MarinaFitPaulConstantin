def AfisNegative(list):
    """
    Afiseaza numerele negative din lista citita
    :param list: lsita de numere citita
    :return: afiseaza numerele negative din lista
    """
    for i in range(len(list)):
        if list[i] < 0:
            print(list[i])


def NrMinCuCifraN(list, j):
    """
    Cauta si afiseaza cel mai mic număr care are ultima cifră egală cu o cifră citită
    :param list: lsita de numere intregi citita
    :param j: numar intreg citit de la tastatura
    :return: Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită
    """
    for i in range(len(list)):
        k = list[i]
        if k % 10 == j:
            minim = k
            break
    for i in range(len(list)):
        k = list[i]
        if k % 10 == j:
            if minim > k:
                minim = k
    return minim

def veri_Prime(n):
    """
    verifica daca un numar e prim
    :param n: numar din lista citita
    :return: True, daca n e prim, False in caz contrar
    """
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, n // 2):
        if n % i == 0:
            return False
    return True

def test_verif_Prime():
    assert veri_Prime(3) is True
    assert veri_Prime(5) is True

def SuperPrime(list):
    """
    verifica daca un numar e superprim si il afiseaza
    :param list: lista de nr intregi
    :return: afiseaza numerele superprime
    """

    for i in range(len(list)):
        putere = 1
        k = list[i]
        if list[i] > 0:
            ok = 1
            while k != 0:
                k //= 10
                putere *= putere
            while putere > 0:
                if veri_Prime(list[i] // putere):
                    putere = putere // 10
                else:
                    ok = 0
                    break
            if ok == 1:
                print(list[i])

def main():
    while True:
        list = []
        n: int = int(input("Dati numar de elemente : "))
        for i in range(n):
            list.append(int(input("Dati elemente : ")))
        ''' testele sa le trec aici '''
        print("1. Afișarea tuturor numerelor negative nenule din listă: ")
        print("2. Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită.")
        print("3. Afișarea tuturor numerelor din listă care sunt superprime.")
        print("4. Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu"
              "CMMDC-ul lor și numerele negative au cifrele în ordine inversă.")
        print("x. Iesire")
        optiune = input("Dati optiune : ")
        if optiune == "1":
            print(AfisNegative(list))
        elif optiune == "2":
            j = int(input("Dati numar: "))
            print(NrMinCuCifraN(list, j))
        elif optiune == "3":
            print(SuperPrime(list))
        elif optiune == "x":
            break
        else:
            print("Optiune gresita, reincercati.")


main()
