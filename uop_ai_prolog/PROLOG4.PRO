domains
	symbol_list = symbol*
	
predicates
	member(symbol,symbol_list)
	
clauses
	member(H,[H|_]).
	member(X,[_|T]) if member(X,T).