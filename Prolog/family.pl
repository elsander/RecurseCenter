father(zeb, john_boy_sr).
father(john_boy_sr, john_boy_jr).

%% When you have multiple clauses that make up a rule,
%% only one needs to be true for the rule to be true.
ancestor(X, Y) :- father(X, Y).
ancestor(X, Y) :- father(X, Z), ancestor(Z, Y).

%% tail recursion optimization: position the recursive subgoal
%% at the end of the recursive rule, and Prolog can optimize
%% to discard the call stack and keep memory use constant.