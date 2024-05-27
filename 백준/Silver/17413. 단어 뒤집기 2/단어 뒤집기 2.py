import sys

# 입력을 받습니다.
S = sys.stdin.readline().strip()

# 결과를 저장할 리스트와 태그와 단어를 분리할 리스트입니다.
answer = []
arr = []

# 태그가 있는지 확인합니다.
while '<' in S:
    indexLeft = S.find('<')
    indexRight = S.find('>')
    
    # 태그 이전의 단어를 추가합니다.
    if indexLeft != 0:
        arr.append(S[:indexLeft])
    # 태그를 추가합니다.
    arr.append(S[indexLeft:indexRight+1])
    S = S[indexRight+1:]

# 태그가 없는 경우 남은 단어를 추가합니다.
if S:
    arr.append(S)

# arr 리스트를 순회하며 단어를 뒤집습니다.
for i in arr:
    if '<' in i and '>' in i:
        # 태그가 포함된 부분은 뒤집지 않습니다.
        answer.append(i)
    else:
        # 태그가 아닌 단어 부분을 공백으로 나누어 뒤집습니다.
        words = i.split(' ')
        for j in range(len(words)):
            answer.append(words[j][::-1])
            if j != len(words) - 1:
                answer.append(' ')

# 결과를 출력합니다.
print(''.join(answer))
