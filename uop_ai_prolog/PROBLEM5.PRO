/*
    MIT License

    Copyright (c) 2017 Rick Doty

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

    Written in 1989 at the University of the Pacific
*/
predicates
  transform(string)
  start
  is_and_or(symbol)
  opposite(symbol,symbol)

goal
	start.

clauses
    start :-
	write("Enter expression:"),nl,
	readln(E),
	transform(E).

	transform(S) :- %associative
	fronttoken(S,T,S1),
	T = "(",
	fronttoken(S1,P,S2),
	fronttoken(S2,Op,S3),
	is_and_or(Op),
	fronttoken(S3,Q,S4),
	fronttoken(S4,")",S5),
	fronttoken(S5,Op2,S6),
	Op2=Op,
	fronttoken(S6,R,_),
	write(P," ",Op,"(",Q," ",Op2," ",R,")"),
	nl.

	transform(S) :- %DeMorgan's
	 fronttoken(S,T,S1),
	 T = "not",
	 fronttoken(S1,"(",S1a),
	 fronttoken(S1a,P,S2),
	 fronttoken(S2,Op,S3),
	 is_and_or(Op),
	 opposite(Op,Op2),
	 fronttoken(S3,Q,S4),
	 fronttoken(S4,")",_),
	 write("not ",P," ",Op2," not ",Q),
	 nl.

	is_and_or(O) :-
 	 O = "and".
	is_and_or(O) :-
	 O = "or".

	opposite(O,P) :-
	 O = "and",
	 P = "or".

	opposite(O,P) :-
	 O = "or",
	 P = "and".
