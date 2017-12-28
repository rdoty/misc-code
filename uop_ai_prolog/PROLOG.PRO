domains
  chrlst = char*

predicates
   operand(chrlst)
   opratr(char)
   wff(chrlst)
   apnd(chrlst,chrlst,chrlst)
   string_chlist(string,chrlst)
   check_wff(chrlst)

goal
   makewindow(1,2,5,"Check your WFF",10,10,15,50),
   nl, write ("Enter expression to be considered:"),
   cursor(2,1), readln(Expression), nl,
   string_chlist(Expression,List), check_wff(List).

clauses
   operand(['p']).
   operand(['q']).
   operand(['r']).

   opratr('c').
   opratr('a').
   opratr('i').
   opratr('e').

   wff(L) if operand(L).

   wff(['n'|T]) if wff(T).

   wff([H|T]) if opratr(H) and apnd(E1,E2,T) and
                wff(E1) and wff(E2).

   apnd([],L,L).
   apnd([X|L1],L2,[X|L3]) if apnd(L1,L2,L3).

   string_chlist("",[]).
   string_chlist(S, [H|T]) if frontchar(S,H,S1), string_chlist(S1,T).

   check_wff(List) if wff(List) and wff(List)
             and write(" is a wff."),nl.
   check_wff(List) if not(wff(List)) and wff(List)
             and write(" is not a wff."),nl.

wff([])
wff([H|T]) if write(H) and wff(T).
