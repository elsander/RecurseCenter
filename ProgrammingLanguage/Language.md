Language will have:
- Booleans (#t and #f)
- Numbers (ints, floats, signed and unsigned)
- symbols (function names, variables, control statments)
- Lists

	(define x 3)
	(if (> 4 3)
		x
		y)
	(lambda (x y)
		(define z (+ x y))
		z)

lambdas can be nested.

Given a parser, work through building a language to make them parse
