def solution(str1, str2):
    split_1 = []
    split_2 = []
    for i in range(len(str1)-1):
        now = str1[i:i+2]
        if now.isalpha():
            now = now.lower()
            split_1.append(now)
    for i in range(len(str2)-1):
        now = str2[i:i+2]
        if now.isalpha():
            now = now.lower()
            split_2.append(now)
    split_1.sort()
    split_2.sort()
    inter = []
    union = []
    if len(split_1) < len(split_2):
        inter = [split_2.remove(x) for x in split_1 if x in split_2]
    else:
        inter = [split_1.remove(x) for x in split_2 if x in split_1]
    union = split_1+split_2
    if len(union) == 0:
        answer = 65536
    else:
        answer = int((len(inter)/len(union))*65536)
    return answer


print(solution("FRANCE", "french"))
