from itertools import combinations


def solution(orders, course):
    answer = []
    for n in course:
        candidates = []
        new_menu = {}
        for menu in orders:
            menu_list = list(menu)
            for li in combinations(menu_list, n):
                # 정렬해서
                new = ''.join(sorted(li))
                if new not in candidates:
                    candidates.append(new)
                else:
                    # 두번 일 때
                    if new not in new_menu.keys():
                        new_menu[new] = 2
                    # 두번 이상일 때
                    else:
                        new_menu[new] += 1
        sort_menu = sorted(new_menu.items(), key=lambda x: (-x[1], x[0]))
        if len(sort_menu):
            M = sort_menu[0][1]
        while sort_menu:
            menu, cnt = sort_menu.pop()
            if cnt == M:
                answer.append(menu)
    return sorted(answer)


print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
