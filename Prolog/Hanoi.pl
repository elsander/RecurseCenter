%% print statement
move(1, X, Y, _) :-
	write('Move top disk from '),
	write(X),
	write(' to '),
	write(Y),
	nl.

%% height, left, right, center
move(N, X, Y, Z) :-
	%% I'm not sure if this is necessary since Prolog should hit
	%% the previous rule before this one
	N > 1,
	%% We're moving a disc from the left so we need to decrement the total?
	M is N - 1,
	%% left goes to center
	move(M, X, Z, Y),
	move(1, X, Y, _),
	move(M, Z, Y, X).