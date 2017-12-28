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
  wordlist=symbol*
database
  curr_response(string)
  substitute(symbol,symbol)
predicates
  words(string,wordlist)
  patient(string)
  doctor(string)
  respond(string)
  print_list(wordlist)
  converse
  purge
goal
  makewindow(1,7,7,"I am ELIZA",1,0,24,80),
  assert(curr_response("")),
  assert(substitute("I","YOU")),
  assert(substitute("YOU","ME")),
  assert(substitute("MYSELF","YOURSELF")),
  assert(substitute("WE","YOU")),
  assert(substitute("OUR","YOUR")),
  assert(substitute("YOURSELF","ME")),
  assert(substitute("WAS","WERE")),
  assert(substitute("YOU","I")),
  assert(substitute("YOUR","MY")),
  assert(substitute("ME","YOU")),
  assert(substitute("MY","YOUR")),
  assert(substitute("AM","ARE")),
  assert(substitute("ARE","AM")),
  assert(substitute("I","YOU")),
  write("The doctor is IN, how may I help?"),nl,
  write("(PUT A PERIOD AT THE END)"),nl,
  converse,
  write("Please come again!").
clauses
  converse :-
   curr_response(S),
   S="QUIT.",
   purge.

  converse :-
   patient(S),
   doctor(S),
   converse.

  words(S,[H|T]) :-
   fronttoken(S,H,S1),!,

  words(S1,T).
  words(_,[]).

  patient(S) :-
   write("-> "),
   readln(L),
   upper_lower(S,L),
   assert(curr_response(S)).

  doctor(S) :-
   words(S,L),
   L=[_|["THINK"|_]],
   write("WHY DO "),
   respond(S).

  doctor(S) :-
   words(S,L),
   L=["I"|["FEEL"|_]],
   write("FOR WHAT REASON DO "),
   respond(S).

  doctor(S) :-
   words(S,L),
   L=["I"|["HATE"|_]],
   write("THIS SHOULD BE EXPLORED.  WHY DO YOU HAVE HATRED?"),nl.

  doctor(S) :-
   words(S,L),
   L=["I"|["HAVE"|T]],
   write("WHY DO YOU HAVE "),
   print_list(T).

  doctor(S) :-
   words(S,L),
   L=[_|["TAKE"|_]],
   write("WHY DO "),
   respond(S).

  doctor(S) :-
   words(S,L),
   L=[_|["DO"|_]],
   write("WHY DO "),
   respond(S).

  doctor(S) :-
   words(S,L),
   L=[N|["KNOW"|T]],
   write("HOW WELL DOES ",N,"  KNOW "),
   print_list(T).

  doctor(S) :-
   words(S,L),
   L=[_|["WAS"|_]],
   write("FOR WHAT REASON?"),nl.

  doctor(S) :-
   words(S,L),
   L=["HE"|[_|_]],
   write("AND THIS FACT ABOUT HIM DISTURBS YOU?").

  doctor(S) :-
   words(S,L),
   L=["SHE"|[_|_]],
   write("AND THIS FACT ABOUT HER DISTURBS YOU?").

  doctor(S) :-
   words(S,L),
   L=[_|["LOVE"|_]],
   write("THESE ARE GOOD FEELINGS TO HAVE.  ELABORATE USING DIFFERENT TERMS."),nl.

  doctor(S) :-
   words(S,L),
   L=["WHY"|[_|_]],
   write("I WOULD PHILOSOPHIZE ABOUT THIS, BUT I EXPECT YOU KNOW THE ANSWER."),nl.

  doctor(S) :-
   words(S,L),
   L=[_|["BOTHER"|_]],
   write("WHY DO "),
   respond(S),nl.

  doctor(S) :-
   words(S,L),
   L=["WHO"|[_|_]],
   write("LET'S ATTEMPT TO KEEP THE TOPIC ON YOU."),nl.

  doctor(S) :-
   words(S,L),
   L=["CAN"|[_|_]],
   write("INSTEAD OF ASKING QUESTIONS, PLEASE PRESENT YOUR PROBLEMS."),nl.

  doctor(S) :-
   words(S,L),
   L=["WHAT"|[_|_]],
   respond(S),
   write("(in your opinion)?"),nl.

  doctor(S) :-
   words(S,L),
   L=[_|["FRIEND"|_]],
   write("YOU SPEAK OF FRIENDS -- THEY ARE IMPORTANT TO YOU?"),nl.

  doctor(S) :-
   words(S,L),
   L=[""],
   write("Come again").

  doctor(S) :-
   words(S,L),
   L=["HOW"|[_|_]],
   write("LET'S NOT ASK HOW, WE WILL JUST TALK ABOUT YOU."),nl.

  doctor(S) :-
   words(S,L),
   L=["CORRECT"|[_|_]],
   write("I WAS HOPING I WAS.  PLEASE CONTINUE."),nl.

  doctor(S) :-
   words(S,L),
   L=["NO"|[_|_]],
   write("LET'S CONTINUE ON, PLEASE EXPRESS ANY OF YOUR CONCERNS."),nl.

  doctor(S) :-
   words(S,L),
   L=["YES"|[_|_]],
   write("I SEE.  EXPLAIN WHY IF YOU CAN. (IN THE FUTURE, TRY TO AVOID YES/NO ANSWERS)"),nl.

  doctor(S) :-
   words(S,L),
   L=["MAYBE"|[_|_]],
   write("Try to be more definitive when expressing yourself."),nl.

  doctor(S) :-
   words(S,L),
   L=[_|["DONT"|_]],
   write("Can you tell me why "),
   respond(S), write("?"),nl.

  doctor(S) :-
   words(S,L),
   L=["I"|["WAS"|_]],
   write("Can you tell me why "),
   respond(S), write("?"),nl.


  doctor(S) :-
   words(S,L),
   L=[_|["WERE"|_]],
   write("Can you tell me why "),
   respond(S), write("?"),nl.

  doctor(S) :-
   words(S,L),
   L=[_|["NEED"|_]],
   write("Yes, let's talk about these needs, especially why."),nl.

  doctor(S) :-
   words(S,L),
   L=["MY"|[H|_]],
   write("And this is bad for either you or the subject [THIS '",H,"']?"),nl.

  doctor(S) :-
   words(S,L),
   L=["IF"|[_|_]],
   write("Do you consider this a real possibility?"),nl.

  doctor(S) :-
   words(S,L),
   L=["BECAUSE"|[_|_]],
   write("Is this an adequate reason?"),nl.

  doctor(S) :-
   words(S,L),
   L=["I"|["AM"|T]],
   write("Does it bother you being "),
   print_list(T).

  doctor(S) :-
   words(S,L),
   L=[_|["CANT"|_]],
   respond(S),
   write("?  Are you sure an adequate effort has been put forth?"),nl.

  doctor(S) :-
   words(S,L),
   L=[_|["IS"|_]],
   write("Does it bother you that "),
   respond(S),nl.

  doctor(S) :-
   words(S,L),
   L=["YOU"|[_|_]],
   write("Enough about me, lets talk about you..."),nl.

  doctor(S) :-
   respond(S),
   write("?"),nl.

  respond(".").

  respond(S) :-
   fronttoken(S,T,S2),
   substitute(T,T2),
   write(T2," "),
   respond(S2).

  respond(S) :-
   fronttoken(S,T,S2),
   write(T," "),
   respond(S2).

  print_list(["."]).
  print_list([H|T]) :-
   write(H," "),
   print_list(T),write("?"),nl.

  purge :-
   retract(substitute(_,_)),
   fail.
  purge :-
   retract(curr_response(_)),fail.
  purge.
