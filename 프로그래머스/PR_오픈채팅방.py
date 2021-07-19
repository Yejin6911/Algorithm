def solution(record):
    id_name = {}
    result = []
    for r in record:
        r = r.split()
        if r[0] == "Enter" or r[0] == "Change":
            id_name[r[1]] = r[2]
        result.append([r[0], r[1]])
    answer = []
    for r in result:
        nickname = id_name[r[1]]
        if r[0] == "Enter":
            answer.append(nickname+"님이 들어왔습니다.")
        elif r[0] == "Leave":
            answer.append(nickname+"님이 나갔습니다.")
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
                "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
