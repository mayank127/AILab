value(x1,1).
value(x2,0).
value(c1,0).


ckt_elem(a1).
type(a1, xorGate).
inputs(a1,2).

ckt_elem(a2).
type(a2, xorGate).
inputs(a2, 2).

ckt_elem(a3).
type(a3, andGate).
inputs(a3, 2).

ckt_elem(a4).
type(a4, orGate).
inputs(a4,2).

ckt_elem(a5).
type(a5, andGate).
inputs(a5,2).

ckt_elem(a6).
type(a6, orGate).
inputs(a6,2).

connected(in(1,a1), x1).
connected(in(2,a1), x2).

connected(in(1,a2), out(a1)).
connected(in(2,a2), c1).

connected(in(1,a3), x1).
connected(in(2,a3), x2).


connected(in(1,a4), x1).
connected(in(2,a4), x2).

connected(in(1,a5), out(a4)).
connected(in(2,a5), c1).

connected(in(1,a6), out(a3)).
connected(in(2,a6), out(a5)).



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


