%% To source a file, use Consult('fname.pl').
%% Facts start with a lowercase letter and end with a period.
likes(alice, bob).
likes(alice, carol).
likes(bob, carol).
likes(james, mary).
likes(mary, james).

%% Variables start with an uppercase letter
%% likes(alice, Who) will query this file and return a person that alice likes.
%% Similar to a query language like SQL in this way!

%% Rules
%% X and Y are love_compatible if X likes Y and Y likes X.
love_compatible(X, Y) :- likes(X, Y), likes(Y, X).

%% Note that if there are multiple matches to a query, typing
%% a semicolon will find the next match.

food_type(velveeta, cheese).
food_type(ritz, cracker).
food_type(spam, meat).
food_type(sausage, meat).
food_type(jolt, soda).
food_type(twinkie, dessert).

flavor(sweet, dessert).
flavor(sweet, soda).
flavor(savory, meat).
flavor(savory, cheese).

%% Y is a flavor of food X if Z is X's food type and Y is Z's flavor.
food_flavor(X, Y) :- food_type(X, Z), flavor(Y, Z).