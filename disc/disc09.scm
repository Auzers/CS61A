; Return whether there are n perfect squares with no repeats that sum to total

(define (fit total n)
    (define (f total n k)
        (if (and (= n 0) (= total 0))
            #t
        (if (< total (* k k))
            #f
        (or (f total n (+ 1 k)) (f (- total (* k k)) (- n 1) (+ 1 k)))
        )))
    (f total n 1))



 (define with-list
        (list
            '(a b)
            'c
            'd
            '(e)
        )
    )
    ; (draw with-list)  ; Uncomment this line to draw with-list

;;; Return a list of pairs containing the elements of s.
    ;;;
    ;;; scm> (pair-up '(3 4 5 6 7 8))
    ;;; ((3 4) (5 6) (7 8))
    ;;; scm> (pair-up '(3 4 5 6 7 8 9))
    ;;; ((3 4) (5 6) (7 8 9))
(define (pair-up s)
    (if (<= (length s) 3)
        (list s)
        (cons (list (car s) (car (cdr s))) (pair-up(cdr (cdr s))))
    ))

(expect (pair-up '(3 4 5 6 7 8)) ((3 4) (5 6) (7 8)) )
(expect (pair-up '(3 4 5 6 7 8 9)) ((3 4) (5 6) (7 8 9)) )