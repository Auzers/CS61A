(define (over-or-under num1 num2) (cond ((> num1 num2) 1) ((< num1 num2) -1) (else 0)))

(define (make-adder num) (lambda (x) (+ num x)))

(define (composed f g) (lambda (x) (f(g x))) )

(define (repeat f n) (if(< n 1) (lambda (x) x) (composed f (repeat f (- n 1)))))

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b)
  (if (= a b)
      a
      (gcd (if (> a b) (- a b) a) (if (> a b) b (- b a)))))
