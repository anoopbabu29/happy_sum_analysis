from typing import Dict, List, Tuple
from copy import deepcopy
import matplotlib.pyplot as plt

list_trails: Dict[int, List[int]] = dict()
count_trails: Dict[int, int] = dict()
is_happy_trails: Dict[int, bool] = dict()

def happy_sum(n: int, prev_trail: List[int] = []) -> Tuple[bool, int, List[int]]:
    global list_trails
    global count_trails
    global is_happy_trails

    SSD: int = sum([int(digit) * int(digit) for digit in str(n)])
    
    # If it is 1, then return true
    if n == 1:
        prev_trail.append(n)
        return True, n, prev_trail
    
    # If recursive function sees the value before (if loops), then false
    if n in list_trails:
        prev_trail = prev_trail + list_trails[n]
        return is_happy_trails[n], n, prev_trail
    elif n in prev_trail:
        return False, n, prev_trail

    prev_trail.append(n)

    return happy_sum(SSD, prev_trail)	 # check new number


def rotate_left(arr: List[int], is_pop: bool, n: int = 1) -> List[int]:
    for _ in range(n):
        if is_pop:
            arr.pop(0)
        else:
            arr.append(arr.pop(0))
    
    return arr


def update_trails(n: int, is_happy_sum: bool, loop_num: int, prev_trail: List[int]) -> None:
    global count_trails
    global list_trails
    global is_happy_trails

    reached_loop_num: bool = False
    swapping_trail: List[int] = deepcopy(prev_trail)

    for point in prev_trail:
        if point == loop_num:
            reached_loop_num = True

        if not point in is_happy_trails:
            is_happy_trails[point] = is_happy_sum

        if point in count_trails:
            count_trails[point] += 1
        else:
            count_trails[point] = 1

        if not point in list_trails:
            list_trails[point] = deepcopy(swapping_trail)

        prev_num = point
        swapping_trail = rotate_left(swapping_trail, is_happy_sum or not reached_loop_num)


def max_len_dict_list(dict_list: Dict[int, List[int]]) -> Tuple[List[int], int]:
    curr_max: int = 0
    curr_ind: List[int] = [0]
    
    for key in dict_list.keys():
        this_len: int = len(dict_list[key])
        if curr_max < this_len:
            curr_max = this_len
            curr_ind = [key]
        elif curr_max == this_len:
            curr_ind.append(key)

    return curr_ind, curr_max


def print_dict(pass_dict) -> None:
    for i in sorted(pass_dict.keys()):
        print(f'{i}: {pass_dict[i]}')
    print()


def print_res(n: int, is_happy_trails: Dict[int, bool], count_trails: Dict[int, int], list_trails: Dict[int, List[int]], is_mat_plot: bool = False) -> None:
    if is_mat_plot:
        plt.scatter(is_happy_trails.keys(), is_happy_trails.values())
        plt.show()

        num_happy: int = sum([1 if is_happy_trails[key] else 0 for key in is_happy_trails.keys()])
        num_unhappy: int = sum([0 if is_happy_trails[key] else 1 for key in is_happy_trails.keys()])
        plt.bar(['happy', 'unhappy'], [num_happy, num_unhappy])
        plt.show()

        plt.bar(list_trails.keys(), [len(val) for val in list_trails.values()])
        plt.show()

        max_nums, max_trail_len = max_len_dict_list(list_trails)
        print(f'Nums w/ Longest Trail:')
        for val in max_nums:
            print(val)
        print(f'Length of Longest Trail: {max_trail_len}')

        print(f'Num Happy: {num_happy}')
        print(f'Num Unhappy: {num_unhappy}')
        print(f'Ratio: {num_happy/num_unhappy}')
    
    else:
        print('--------------------------------------------------')
        print('--------------------------------------------------')
        print(f'{n}:')
        print('--------------------------------------------------')
        print(f'is_happy_trails:')
        print_dict(is_happy_trails)

        print(f'count_trails:')
        print_dict(count_trails)

        print(f'list_trails:')
        print_dict(list_trails)

        max_nums, max_trail_len = max_len_dict_list(list_trails)
        print(f'Nums w/ Longest Trail:')
        for val in max_nums:
            print(val)
        print(f'Length of Longest Trail: {max_trail_len}')
        
        print('--------------------------------------------------')
        print('--------------------------------------------------\n')


def happy_sum_n(n: int) -> None:
    global is_happy_trails
    global count_trails
    global list_trails

    for i in range(n + 1):
        is_sum, loop_num, trail = happy_sum(i, [])
        update_trails(i, is_sum, loop_num, trail)

    print_res(n, is_happy_trails, count_trails, list_trails)
    print_res(n, is_happy_trails, count_trails, list_trails, True)


def main() -> None:
    happy_sum_n(1000)


if __name__ == '__main__':
    main()

