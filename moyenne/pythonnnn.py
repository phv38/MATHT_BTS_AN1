


def tableaunote(): 
    note=[(),(),()]
    note.insert(0,input("ajouter une note de math" ))
    note.insert(1,input("ajouter une note de sisr" ))
    note.insert(2,input("ajouter une note de cyber" ))
    print(f'la note de math est {note[0]} la note de sisr est {note[1]} la note de cyber est {note[2]}')

def tableaumatiere():
    matiere=[("math",3),("sisr",12),("cyber",14)]
    print(f'Le coef de {matiere[0][0]} est {matiere[0][1]} Le coef de {matiere[1][0]} est {matiere[1][1]} Le coef de {matiere[2][0]} est {matiere[2][1]} ')



tableaunote()
tableaumatiere()






