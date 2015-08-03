%% it's a valid set for row, col, or block if all are different.
set([A|[B|[C|D]]]) :-
	A =\= B,
	A =\= C,
	A =\= D,
	B =\= C,
	B =\= D,
	C =\= D.
valid([]).
valid([Head|Tail]) :-
	%%	set(Head),
	fd_all_different(Head),
	valid(Tail).

%% check if between 1 and 4.
ok([], _, _).
ok([Head|Tail], Low, High) :-
	Head =< High,
	Head >= Low,
	ok(Tail, Low, High).

sudoku(Puzzle, Solution) :-
	Solution = Puzzle,
	Puzzle = [A, B, C, D,
		  E, F, G, H,
		  I, J, K, L,
		  M, N, O, P],
	%% make sure everything is between 1 and 4
	fd_domain(Puzzle, 1, 4),
	%% rows
	Row1 = [A,B,C,D],
	Row2 = [E,F,G,H],
	Row3 = [I,J,K,L],
	Row4 = [M,N,O,P],
	%% columns
	Col1 = [A,E,I,M],
	Col2 = [B,F,J,N],
	Col3 = [C,G,K,O],
	Col4 = [D,H,L,P],
	%% blocks
	Sq1 = [A,B,E,F],
	Sq2 = [C,D,G,H],
	Sq3 = [I,J,M,N],
	Sq4 = [K,L,O,P],
	%% is everything valid?
	valid([Row1, Row2, Row3, Row4,
	       Col1, Col2, Col3, Col4,
	       Sq1, Sq2, Sq3, Sq4]).
	