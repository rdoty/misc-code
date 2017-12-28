predicates
	children(symbol,symbol,symbol)
	parent(symbol,symbol,symbol)
	gparent(symbol,symbol,symbol)
	fcousin(symbol,symbol)
clauses
       children(arthur,guinivere,gawain).
       children(arthur,guinivere,red).
       children(gawain,brunhilde,fawn).
       children(gawain,brunhilde,dawn).
       children(red,hypatia,lance).
       children(red,hypatia,george).
       parent(C,F,M) if children(F,M,C).
       gparent(GF,GM,C) if parent(C,F,M) and children(GF,GM,F).
       sibling(Pa,Pb) if parent(Pa,F,M) and parent(Pb,F,M) and Pa<>Pb.
       fcousin(P,Fc) if parent(P,F,M) and sibling(F,U) and children(U,A,Fc).
