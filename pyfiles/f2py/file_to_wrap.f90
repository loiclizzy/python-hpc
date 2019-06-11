subroutine sum_squares(A, res)
    implicit none
    real, dimension(:) :: A
    real :: res
    integer :: i, N

    N = size(A)
    res = 0.

    do i=1, N
        res = res + A(i)*A(i)
    end do

end subroutine