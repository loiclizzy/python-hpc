subroutine sum_squares(A, res)
    implicit none
    real, dimension(:), intent(in) :: A
    real, intent(out) :: res
    integer :: i, N

    N = size(A)
    res = 0.

    do i=1, N
        res = res + A(i)*A(i)
    end do

end subroutine


real function sum_squares_as_func(A)
    implicit none
    real, dimension(:), intent(in) :: A
    integer :: i, N

    N = size(A)
    sum_squares_as_func = 0.

    do i=1, N
        sum_squares_as_func = sum_squares_as_func + A(i)*A(i)
    end do

end function