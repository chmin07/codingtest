# 1. 스킬 트리에서 관련 없는 스펠링은 뺀다
# 2. 관련없는 스펠링을 빼고 남은 스펠링 그룹과 스킬의 리스트를 비교
# 3. 반복문 돌려서 각각이 일치하면 가능한 스킬트리 개수 +1

def solution(skill, skill_trees):
    answer =0 
    for str in skill_trees:
        temp=[]
        ok=True

        for i in str:
            if skill.find(i) != -1:
                temp += i

        for j in range(len(temp)):
            if skill[j] != temp[j]:
                ok=False
                break

        if ok ==True:
            answer +=1

    return answer
