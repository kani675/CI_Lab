%Calculator program
calculator(N1, N2, '+', R) :- R is N1 + N2.
calculator(N1, N2, '-', R) :- R is N1 - N2.
calculator(N1, N2, '*', R) :- R is N1 * N2.
calculator(N1, N2, '/', R) :- N2 =\= 0, R is N1 / N2.
calculator(N1, N2, '%', R) :- N2 =\= 0, R is N1 mod N2.
run :
    write('Enter N1: '),
    read(N1),
    write('Enter N2: '),
    read(N2),
    write('Enter operator (+, -, *, / , %): '),
    read(Op),
    % Ensure the operator is matched correctly
    (calculator(N1, N2, Op, Result) ->
        format('Result = ~w~n', [Result])
    ;   
        write('Calculation failed :-  n2=0.'), nl
    ).
