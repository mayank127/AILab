value(x1,_).
value(x2,_).
value(c1,_).


ckt_elem(a1).
type(a1, xorGate).
ckt_elem(a2).
type(a2, xorGate).
ckt_elem(a3).
type(a3, andGate).
ckt_elem(a4).
type(a4, orGate).
ckt_elem(a5).
type(a5, andGate).
ckt_elem(a6).
type(a6, orGate).

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

wire(y1).
wire(y2).
connected(out(a2), y1).
connected(out(a6), y2).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

are_connected(T1, T2) :- connected(T1, T2), !.
are_connected(T1, T2) :- connected(T2, T1), !.

wire(T) :- value(T, _).
wire(out(G)) :- ckt_elem(G).
wire(in(N,G)) :- ckt_elem(G), elem_def(G, I), N =< I, N > 0.

elem_def(G, 1) :- ckt_elem(G), type(G, notGate).
elem_def(G, 2) :- ckt_elem(G).



signal(T, 1) :- value(T, 1), !.
signal(T, 0) :- value(T, 0), !.
signal(T, 1) :- value(T, 0), !, fail.
signal(T, 0) :- value(T, 1), !, fail.


signal(out(G), 1) :- type(G, andGate), signal(in(1,G), 1), signal(in(2,G), 1).
signal(out(G), 0) :- type(G, andGate), signal(in(1,G), 0); type(G, andGate), signal(in(2,G), 0).


signal(out(G), 1) :- type(G, orGate), signal(in(1,G), 1); type(G, orGate), signal(in(2,G), 1).
signal(out(G), 0) :- type(G, orGate), signal(in(1,G), 0), signal(in(2,G), 0).


signal(out(G), 1) :- type(G, notGate), signal(in(1,G), 0).
signal(out(G), 0) :- type(G, notGate), signal(in(1,G), 1).


signal(out(G), 1) :- type(G, xorGate), signal(in(1,G), 1), signal(in(2,G), 0); type(G, xorGate), signal(in(1,G), 0), signal(in(2,G), 1).
signal(out(G), 0) :- type(G, xorGate), signal(in(1,G), 1), signal(in(2,G), 1); type(G, xorGate), signal(in(1,G), 0), signal(in(2,G), 0).

signal(out(_), _) :- !, fail.
signal(T, V) :- wire(T), wire(T2), T\=T2, are_connected(T, T2), !, signal(T2, V).


