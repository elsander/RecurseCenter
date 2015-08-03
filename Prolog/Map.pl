different(red, green). different(green, red).
different(blue, red). different(red, blue).
different(blue, green). different(green, blue).

coloring(Alabama, Mississippi, Georgia, Tennessee, Florida) :-
	different(Mississippi, Tennessee),
	different(Mississippi, Alabama),
	different(Alabama, Tennessee),
	different(Alabama, Mississippi),
	different(Alabama, Georgia),
	different(Alabama, Florida),
	different(Georgia, Florida),
	different(Georgia, Tennessee).

	