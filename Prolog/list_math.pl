count(0,[]).
count(Count, [Head|Tail]) :- count(TailCount, Tail), Count is TailCount + 1.

sum(0,[]).
sum(Total, [Head|Tail]) :- sum(Sum, Tail), Total is Head + Sum.

average(Average, List) :- sum(Sum, List), count(Count, List), Average is Sum/Count.

%% Prolog doesn't think of these things as functions!
%% Prolog thinks of these statements as logical rules to follow.
%% I might want to call count as count(What, [1,2,3]) to learn the
%% length of a list, but Prolog is trying to PROVE that the count of
%% [1,2,3] is What. This rule holds when What = 3, so Prolog returns
%% What = 3.

%% Append function.
%% Holy crap.
concatenate([], List, List).
concatenate([Head|Tail1], List, [Head|Tail2]) :- concatenate(Tail1, List, Tail2).

%% Fibonacci Sequence.
%% Tail recursive.
fib(0, A, _, A).
fib(N, A, B, F) :- N1 is N - 1, Sum is A + B, fib(N1, B, Sum, F).
fib(N, F) :- fib(N, 0, 1, F).	%for calling convenience I think.

%% Factorial: my first Prolog program :)
fact(1, A, A).
fact(N, Running, F) :- N1 is N - 1, Running2 is Running * N, fact(N1, Running2, F).
fact(N, F) :- fact(N, 1, F).

%% reverse a list using an accumulator
reverse([H|T], A, R) :- reverse(T, [H|A], R).
reverse([], A, A).

%% find the smallest element of a list
listmin([Min], Min). %we found the smallest
listmin([H, K|T], Min):-
	H =< K, 
	listmin([H|T], Min).	%keep H since it's smaller
listmin([H, K|T], Min):-
	H > K, 
	listmin([K|T], Min).	%keep K since it's smaller

%% sort elements of a list
%% alias for calling
insert_sort(List, Sorted) :- i_sort(List, [], Sorted).
%% if list empty, accumulator is fully sorted.
i_sort([], Acc, Acc).
i_sort([H|T], Acc, Sorted) :-
	%% inserting head into accumulator gives new accumulator
	insert(H, Acc, NAcc),
	%% inserting tail into new accumulator gives final sorted list
	i_sort(T, NAcc, Sorted).
insert(X, [Y|T], [Y|NT]) :-
	%% X is not lowest value, so inserting X into tail gives new
	%% tail to accumulator.
	X > Y,
	insert(X, T, NT).
%% X is lower than Y, so it must go at the beginning of the accumulator.
insert(X, [Y|T], [X, Y|T]) :- X =< Y.
%% insert value into empty accumulator
insert(X, [], [X]).