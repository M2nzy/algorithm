def solution(string):
    answer = []
    for i in range(1, len(string)+1):
        result = ""
        prev = ""
        cur = ""
        stack = []
        cnt = 1
        for s in string:
            stack.append(s)
            if len(stack) == i:
                cur = ''.join(stack)
                # 비어있다면 처음 나오는 문자열
                if prev == "":
                    prev = cur
                    cnt = 1
                elif cur == prev:
                    cnt += 1
                    prev = cur
                else:
                    #다른 문자열 나왔으니 이때까지 세던건 문자열 만들어줘야함
                    if cnt > 1:
                        result += str(cnt)
                    result += prev
                    #만든 후 다시 세기
                    prev = cur
                    cnt = 1
                stack = []
                
        if stack: # 문자열 남아있다면
            if cnt > 1:
                result += str(cnt)
            # 그 전 문자열 붙여주고, 현재 남은 문자 다 붙여줌
            result += prev
            result += ''.join(stack)
        else:
            if cnt > 1:
                result += str(cnt)
            # 남은 문자가 없으니 그 전 문자열만 붙여줌
            result += prev
            
        answer.append(len(result))
    return min(answer)