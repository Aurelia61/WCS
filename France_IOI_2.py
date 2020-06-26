nb_notes = int(input())
somme_notes = 0

for note in range(nb_notes):
    note_obtenue = int(input())
    print(note_obtenue)
    somme_notes += note_obtenue
print(somme_notes)  