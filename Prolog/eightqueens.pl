valid_queen((Row, Col)) :-
	Range = [1,2,3,4,5,6,7,8],
	member(Row, Range),
	member(Col, Range).
valid_board([]).
valid_board([Head|Tail]) :-
	valid_queen(Head),
	valid_board(Tail).

%% get rows, cols, diagonal.
rows([], []).
rows([(Row, _)|QueensTail], [Row|RowsTail]) :-
	rows(QueensTail, RowsTail).
cols([], []).
cols([(_, Col)|QueensTail], [Col|ColsTail]) :-
	rows(QueensTail, ColsTail).
%% NE-SW and SE-NW diags must be handled separately.
diags1([], []).
diags1([(Row, Col)|QueensTail], [Diag|DiagsTail]) :-
	Diag is Row - Col,
	diags1(QueensTail, DiagsTail).
diags2([], []).
diags2([(Row, Col)|QueensTail], [Diag|DiagsTail]) :-
	Diag is Row + Col,
	diags1(QueensTail, DiagsTail).

eight_queens(Board) :-
	length(Board, 8),
	valid_board(Board),
	rows(Board, Rows),
	cols(Board, Cols),
	diags1(Board, Diag1),
	diags2(Board, Diag2),
	fd_all_different(Rows),
	fd_all_different(Cols),
	fd_all_different(Diag1),
	fd_all_different(Diag2).
	