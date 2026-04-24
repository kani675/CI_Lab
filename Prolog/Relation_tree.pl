% RELATION TREE:
male(john). male(bob). male(jim). male(tom). male(fred). male(scott).
male(steve). male(jack). male(rich). male(mike). male(harry).
female(mary). female(carol). female(patty). female(alice). female(barbara).
female(valerie). female(cindy). female(linda). female(donna). female(rachel).
female(jane).
spouse(john, mary).
spouse(bob, mary).
spouse(patty, john).
spouse(tom, alice).
spouse(fred, valerie).
spouse(barbara, scott).
spouse(linda, steve).
spouse(jack, donna).
spouse(rich, rachel).
married(X,Y) :- spouse(X,Y).
married(X,Y) :- spouse(Y,X).
father(john, tom).
father(john, linda).
father(john, carol).
father(bob, jim).
father(tom, barbara).
father(tom, valerie).
father(fred, jane).
father(scott, cindy).
father(steve, jack).
father(steve, rich).
father(jack, mike).
father(rich, harry).
mother(mary, tom).
mother(mary, linda).
mother(mary, jim).
mother(patty, carol).
mother(alice, barbara).
mother(alice, valerie).
mother(valerie, jane).
mother(barbara, cindy).
mother(linda, jack).
mother(linda, rich).
mother(donna, mike).
mother(rachel, harry).
parent(X,Y) :- father(X,Y).
parent(X,Y) :- mother(X,Y).
sibling(X, Y) :- 
    father(F, X), father(F, Y), 
    X \= Y.
brother(X,Y) :- sibling(X,Y), male(X).
sister(X,Y) :- sibling(X,Y), female(X).
grandparent(X,Y) :- parent(X,Z), parent(Z,Y).
grandfather(X,Y) :- grandparent(X,Y), male(X).
grandmother(X,Y) :- grandparent(X,Y), female(X).
grandchild(X,Y) :- grandparent(Y,X).
grandson(X,Y) :- grandchild(X,Y), male(X).
granddaughter(X,Y) :- grandchild(X,Y), female(X).
uncle(X,Y) :- brother(X,Z), parent(Z,Y).
aunt(X,Y) :- sister(X,Z), parent(Z,Y).
cousin(X,Y) :
    parent(A,X),
    parent(B,Y),
    sibling(A,B),
    X \= Y.
nephew(X,Y) :- male(X), (uncle(Y,X); aunt(Y,X)).
niece(X,Y) :- female(X), (uncle(Y,X); aunt(Y,X)).
relation(X, Y) :- 
    (   sibling(X, Y)     -> write(X), write(' is the sibling of '), write(Y)
    ;   parent(X, Y)      -> write(X), write(' is the parent of '), write(Y)
    ;   parent(Y, X)      -> write(X), write(' is the child of '), write(Y)
    ;   grandparent(X, Y) -> write(X), write(' is the grandparent of '), 
write(Y)
    ;   grandchild(X, Y)  -> write(X), write(' is the grandchild of '), write(Y)
    ;   uncle(X, Y)       -> write(X), write(' is the uncle of '), write(Y)
    ;   aunt(X, Y)        -> write(X), write(' is the aunt of '), write(Y)
    ;   cousin(X, Y)      -> write(X), write(' is the cousin of '), write(Y)
    ;   nephew(X, Y)      -> write(X), write(' is the nephew of '), write(Y)
    ;   niece(X, Y)       -> write(X), write(' is the niece of '), write(Y)
    ;   % If none of the above match:
        write('No relation found between '), write(X), write(' and '), write(Y)
    ), nl.
