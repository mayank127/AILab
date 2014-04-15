value(a,1).
value(b,0).
value(c,0).
value(d,0).
value(e,1).


ckt_elem(and1).
type(and1, andGate).
inputs(and1,3).

ckt_elem(and2).
type(and2, andGate).
inputs(and2,3).

ckt_elem(and3).
type(and3, andGate).
inputs(and3,3).

ckt_elem(and4).
type(and4, andGate).
inputs(and4,3).

ckt_elem(and5).
type(and5, andGate).
inputs(and5,3).

ckt_elem(and6).
type(and6, andGate).
inputs(and6,3).

ckt_elem(and7).
type(and7, andGate).
inputs(and7,3).

ckt_elem(and8).
type(and8, andGate).
inputs(and8,3).

ckt_elem(and9).
type(and9, andGate).
inputs(and9,3).

ckt_elem(and10).
type(and10, andGate).
inputs(and10,3).

ckt_elem(or1).
type(or1, orGate).
inputs(or1, 10).

connected(in(1,and1), a).
connected(in(2,and1), b).
connected(in(3,and1), c).

connected(in(1,and2), a).
connected(in(2,and2), b).
connected(in(3,and2), d).

connected(in(1,and3), a).
connected(in(2,and3), b).
connected(in(3,and3), e).

connected(in(1,and4), a).
connected(in(2,and4), c).
connected(in(3,and4), d).

connected(in(1,and5), a).
connected(in(2,and5), c).
connected(in(3,and5), e).

connected(in(1,and6), a).
connected(in(2,and6), d).
connected(in(3,and6), e).

connected(in(1,and7), b).
connected(in(2,and7), c).
connected(in(3,and7), d).

connected(in(1,and8), b).
connected(in(2,and8), c).
connected(in(3,and8), e).

connected(in(1,and9), b).
connected(in(2,and9), d).
connected(in(3,and9), e).

connected(in(1,and10), c).
connected(in(2,and10), d).
connected(in(3,and10), e).

connected(in(1,or1), out(and1)).
connected(in(2,or1), out(and2)).
connected(in(3,or1), out(and3)).
connected(in(4,or1), out(and4)).
connected(in(5,or1), out(and5)).
connected(in(6,or1), out(and6)).
connected(in(7,or1), out(and7)).
connected(in(8,or1), out(and8)).
connected(in(9,or1), out(and9)).
connected(in(10,or1), out(and10)).

wire(y).
connected(y, out(or1)).






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


