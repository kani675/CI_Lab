(defun AreaOfCircle()
(terpri) ;terminate printing
(princ "Enter the readius:")
(setq radius (read))     ;simple variable assignment stmt of lisp
(setq area (* 3.1416 radius radius ) )
(format t "Radius: = ~F~% Area = ~F" radius area ) 
)
