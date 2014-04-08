value(x,_).
value(y,_).

ckt_elem(a).
type(a, orGate).
inputs(a,2).
wire(x).
wire(y).
connected(in(1,a), x).
connected(in(2,a), y).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

are_connected(T1, T2) :- connected(T1, T2), !.
are_connected(T1, T2) :- connected(T2, T1), !.


wire(in(N,G)) :- ckt_elem(G), elem_def(G, I), N =< I, N > 0.
wire(out(G)) :- ckt_elem(G).
%wire(T) :- signal(T, _).

elem_def(G, 1) :- ckt_elem(G), type(G, notGate).
elem_def(G, N) :- inputs(G, N).


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

signal(out(_), _) :- !.
signal(T, V) :- wire(T), wire(T2), T\=T2, are_connected(T, T2), !, signal(T2, V).


