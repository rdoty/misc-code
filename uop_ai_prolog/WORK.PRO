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
domains
  attribute = attr(string,string,string)
  list = attribute*

database
  class(symbol,list,list)
  %       name,must,can

predicates
  start
  learn(symbol)
  restrict(list,list,list,list)
  generalize(list,list,list,list,list)
  add(attribute,list,list)
  member(attribute,list)
  append(list,list,list)
  example(symbol,list,list)
  nearmiss(symbol,list,list)
  remove(attribute,list,list)
  reconcile(list,list,list)
  disp_knowledge
  writelistt(list,integer)

goal
  makewindow(1,7,7,"Entry Screen",1,1,24,79),
  start.

clauses
  start :-
  	write ("learn or display? (L/D) "),
	readln(Q),
	Q=l,
	write("Class name: "),
	readln(Name),
	assert(class(Name,[],[])),
	learn(Name).

  start :-
	disp_knowledge.

  learn(ClassName) :-
  	example(ClassName,[],E),
  	retract(class(ClassName,R,C)),
  	generalize(E,C,Can,R,R2),
  	nearmiss(ClassName,[],M),
  	restrict(E,M,R2,Req),
  	reconcile(Req,Can,Newcan),
  	assert(class(ClassName,Req,Newcan)),!,
  	write("More? (Y/N) "),
  	readln(Q), Q=y,
  	learn(ClassName).

  example(Name,L,E) :-
  	write("E: Subject: "),
  	readln(S),
  	S<>" ",
  	write("E: Verb: "),
  	readln(V),
  	write("E: Object: "),
  	readln(O),
  	add(attr(S,V,O),L,E2),
  	example(Name,E2,E).
  example(_,E,E).

  nearmiss(Name,L,E) :-
  	write("M: Subject: "),
  	readln(S),
  	S<>" ",
  	write("M: Verb: "),
  	readln(V),
  	write("M: Object: "),
  	readln(O),
  	add(attr(S,V,O),L,E2),
  	example(Name,E2,E).
  nearmiss(_,E,E).

  restrict(_,[],Req,Req).
  restrict(E,[M|Mt],Req,Req2) :-
  	remove(M,E,Et),
  	restrict(Et,Mt,Req,Req2).
  	restrict(E,[attr(S,V,O)|Mt],Req,Req2) :-
  	fronttoken(V,_,V2),
  	frontchar(V2,_,V3),
  	remove(attr(S,V3,O),E,Et),
  	add(attr(S,V3,O),Req,R),
  	restrict(Et,Mt,R,Req2).
  restrict(_,_,Req,Req).
  generalize([],C,C,R,R).
  generalize([attr(S,V,O)|Et],C,C2,R,R2) :-
  	member(attr(_,V,O),R),
  	remove(attr(X,V,O),R,T),
  	X<>S,
  	fronttoken(Nc,"_",X),
  	fronttoken(NewClass,8,Nc),
  	add(attr(NewClass,V,O),T,T2),
  	generalize(Et,C,C2,T2,R2).
  generalize([attr
