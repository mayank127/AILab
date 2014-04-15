value(a,1).
value(b,1).
value(c,0).
value(d,1).
value(e,1).

ckt_elem(xor1).
type(xor1, xorGate).
inputs(xor1,2).

ckt_elem(xor2).
type(xor2, xorGate).
inputs(xor2,2).

ckt_elem(or1).
type(or1, orGate).
inputs(or1, 2).

ckt_elem(nor1).
type(nor1, notGate).

connected(in(1,xor1), a).
connected(in(2,xor1), e).

connected(in(1,xor2), b).
connected(in(2,xor2), d).

connected(in(1,or1), out(xor1)).
connected(in(2,or1), out(xor2)).

connected(in(1, nor1), out(or1)).

wire(y).
connected(y, out(nor1)).



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

are_connected(T1, T2) :- connected(T1, T2), !.
are_connected(T1, T2) :- connected(T2, T1), !.

wire(T) :- value(T, _).
wire(out(G)) :- ckt_elem(G).
wire(in(N,G)) :- ckt_elem(G), elem_def(G, I), N =< I, N > 0.

elem_def(G, 1) :- ckt_elem(G), type(G, notGate), !.
elem_def(G, N) :- inputs(G,N).


all(G, X) :- elem_def(G, I), check_val(G, I, X).
check_val(_, 0, _) :- !.
check_val(G, N, X) :- signal(in(N, G), X), M is N-1, check_val(G, M, X).

xor(X,Y,0) :- X==Y, !.
xor(X,Y,1) :- X\=Y, !.

check_count_val(_,0,0) :- !.
check_count_val(_,0,1) :- !, fail.
check_count_val(G, N, O) :- signal(in(N,G), X), M is N-1, check_count_val(G, M, O1), xor(O1, X, O).
count(G) :- elem_def(G, I), check_count_val(G, I, 1).

signal(T, 1) :- value(T, 1), !.
signal(T, 0) :- value(T, 0), !.
signal(T, 1) :- value(T, 0), !, fail.
signal(T, 0) :- value(T, 1), !, fail.


signal(out(G), 1) :- type(G, andGate), all(G, 1).
signal(out(G), 0) :- type(G, andGate), \+all(G, 1).


signal(out(G), 0) :- type(G, orGate), all(G,0).
signal(out(G), 1) :- type(G, orGate), \+all(G,0).


signal(out(G), 1) :- type(G, notGate), signal(in(1,G), 0).
signal(out(G), 0) :- type(G, notGate), signal(in(1,G), 1).


signal(out(G), 1) :- type(G, xorGate), count(G).
signal(out(G), 0) :- type(G, xorGate), \+count(G).

signal(out(_), _) :- !, fail.
signal(T, V) :- wire(T), wire(T2), T\=T2, are_connected(T, T2), !, signal(T2, V).

