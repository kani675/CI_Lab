(defun fact2 ( n ) ;;function for recursive mentod
( if ( = n 0 ) 1
( * n ( fact2( - n 1 ) ) )
)
)
