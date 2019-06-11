module dtw_cort
    implicit none

    contains
        subroutine dtwdistance(s1, s2, dtw_result)
            ! Computes the dtw between s1 and s2 with distance the absolute distance
            doubleprecision, intent(in) :: s1(:), s2(:)
            doubleprecision, intent(out) :: dtw_result

            integer :: i, j
            integer :: len_s1, len_s2
            doubleprecision :: dist
            doubleprecision, allocatable :: dtw_mat(:, :)

            len_s1 = size(s1)
            len_s2 = size(s1)

            allocate(dtw_mat(len_s1, len_s2))

            dtw_mat(1, 1) = dabs(s1(1) - s2(1))

            do j = 2, len_s2
                dist = dabs(s1(1) - s2(j))
                dtw_mat(1, j) = dist + dtw_mat(1, j-1)
            end do

            do i = 2, len_s1
                dist = dabs(s1(i) - s2(1))
                dtw_mat(i, 1) = dist + dtw_mat(i-1, 1)
            end do

            ! Fill the dtw_matrix
            do i = 2, len_s1
                do j = 2, len_s2
                    dist = dabs(s1(i) - s2(j))
                    dtw_mat(i, j) = dist + dmin1(dtw_mat(i - 1, j), &
                                                 dtw_mat(i, j - 1), &
                                                 dtw_mat(i - 1, j - 1))
                end do
            end do

            dtw_result = dtw_mat(len_s1, len_s2)

        end subroutine dtwdistance

        doubleprecision function cort(s1, s2)
            ! Computes the cort between s1 and s2 (assuming they have the same length)
            doubleprecision, intent(in) :: s1(:), s2(:)

            integer :: len_s1, t
            doubleprecision :: slope_1, slope_2
            doubleprecision :: num, sum_square_x, sum_square_y

            len_s1 = size(s1)
            num = 0
            sum_square_x = 0
            sum_square_y = 0

            do t=1, len_s1 - 1
                slope_1 = s1(t + 1) - s1(t)
                slope_2 = s2(t + 1) - s2(t)
                num = num + slope_1 * slope_2
                sum_square_x = sum_square_x + slope_1 * slope_1
                sum_square_y = sum_square_y + slope_2 * slope_2
            end do

            cort = num / (dsqrt(sum_square_x*sum_square_y))

        end function cort


end module dtw_cort