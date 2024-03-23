import sys 
import re
ex = sys.stdin.readline().strip()
result = 0

if(len(ex) > 50):
    sys.exit()
    
else:
    if "-" not in ex:
        newex = ex.split("+")
        for i in range(len(newex)):
            # while(True):
            #     if newex[i][0] == "0":
            #         tmp = newex[i]
            #         tmp = tmp[1:]
            #         newex[i] = tmp
            #     else:
            #         break

            result += int(newex[i])

        print(result)

    elif "+" not in ex:
        newex = ex.split("-")
        for i in range(len(newex)):
            # while(True):
            #     if newex[i][0] == "0":
            #         tmp = newex[i]
            #         tmp = tmp[1:]
            #         newex[i] = tmp
            #     else:
            #         break
            if i == 0:
                result += int(newex[i])
            else:
                result -= int(newex[i])
        print(result)

    else:
        flag = 0
        for i in range(len(ex)):
            if ex[i] == "-":
                if flag == 0:
                    flag = -1
                    newex = ex[:i+1]+ "(" + ex[i+1:] + ")"
                    result = eval(newex)
                elif flag == -1:    
                    continue


            elif ex[i] == "+":
                if flag == -1:
                    flag = 0

        print(result)
