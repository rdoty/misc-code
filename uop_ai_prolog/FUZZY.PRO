database
	truth(real)
	thresh(real)
	
predicates
	init_fuzzy	fuzzy(real)	threshold(real)	
	f_OR	f_AND	p_OR	p_AND	f_NOT
	
	fuzzy_max(real, real, real)
	fuzzy_min(real, real, real)
	
clauses

	/* Init_fuzzy must be called before any
	   fuzzy operators or predicates are used.
	   It sets the initial search threshold to
	   which fuzzy truth values are compared.*/
	
	init_fuzzy :- asserta(thresh(0.01)).
	
	/* Fuzzy is used to specify a particular
	   fuzzy truth value, or to retrieve the
	   current truth value.               */
	   
	fuzzy(Truth) :- bound(Truth),
			asserta(truth(Truth)),
			retract(thresh(Thresh)),
			asserta(thresh(Thresh)), !,
			Truth >= Thresh.
			
	fuzzy(Truth) :- retract(truth(Truth)),
			asserta(truth(Truth)), !.
			
	/* Threshold sets or retrieves the search
	   threshold used by the Fuzzy Logic
	   operations. If a call to FUZZY or the
	   result of a Fuzzy Logic operator results
	   in a truth value less than the threshold,
	   the predicate or operator will fail.   */
	   
	threshold(Truth) :- bound(Truth),
			    retract(thresh(_)),
			    asserta(thresh(Truth)),
			    retract(truth(Current)),   
			    asserta(truth(Current)),
			    !,Current >= Truth.
			    
	threshold(Truth) :- retract(thresh(Truth)),
			    asserta(thresh(Truth)),
			    !.
			    
	/* Fuzzy logic contains five basic
	   operators: fuzzy-AND, fuzzy_OR,
	   probablity-AND, probability-OR, and
	   NOT. In this Turbo Prolog impleentation,
	   these are represented by f-AND, f-OR,
	   p-AND, p-OR, and f-NOT respectively.
	   "f-NOT" is used to avoid conflicting
	   with the Turbo Prolog predicate "NOT."
	   Since Turbo Prolog does not support
	   true operator definition, the Fuzzy
	   Logic operators are used syntactically
	   as predicates, in the order specified
	   by Reverse Polish Notation (RPN). For
	   example, the clause
	   
	   	woof :- fuzzy(0.6), fuzzy(0.7),
	   		p-AND, fuzzy(0.4), p-OR.
	   		
	   represents the Fuzzy Logic expression
	   
	   	(0.6 p-AND 0.7) p-OR 0.4
	   	
	   Note that only predicates which use
	   Fuzzy Logic will generate fuzzy truth
	   value operands. Other predicates,
	   including those built into Turbo
	   Prolog, do not generate fuzzy truth
	   values. Hence, the clause
	   
	   	woof(X,Y) :- fuzzy(0.6), X > Y,
	   	             f-AND.
	   	             
	   is incorrect since f-AND requires two
	   operands, but only one (from the FUZZY
	   predicate) has been generated.      */
	   
	f_OR :- retract(truth(X)),
	        retract(truth(Y)),!,
	        fuzzy_max(X, Y, Z), fuzzy(Z), !.
	f_AND :- retract(truth(X)),
	         retract(truth(Y)),!,
	         fuzzy_min(X, Y, Z), fuzzy(Z), !.
	p_OR :- retract(truth(X)),
		retract(truth(Y)), !,
		Z = X + Y - (X * Y), fuzzy(Z), !.
	p_AND :- retract(truth(X)),
		 retract(truth(Y)),!,
		 Z = X * Y, fuzzy(Z), !.
	f_NOT :- retract(truth(X)), !,
		 Z = 1 - X, fuzzy(Z), !.
		 
	     /* Local predicates used by the
	        fuzzy operators           */
	        
	     fuzzy_max(X, Y, Z) :- X >= Y, !, Z = X.
	     fuzzy_max(_, Y, Z) :- Z = Y.
	     
	     fuzzy_min(X, Y, Z) :- X <= Y, !, Z = X.
	     fuzzy_min(_, Y, Z) :- Z = Y.    