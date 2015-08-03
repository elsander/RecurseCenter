writtenby(pride_and_prejudice, austen).
writtenby(emma, austen).
writtenby(wuthering_heights, bronte).
writtenby(jane_eyre, bronte).
writtenby(mistborn, sanderson).

music(barrios, classical).
music(clapton, rock).
music(liz, covers).
music(mozart, classical).
genre(classical, piano).
genre(covers, guitar).
genre(covers, piano).
genre(rock, guitar).

plays(X, Y) :- music(X, Z), genre(Z, Y).
