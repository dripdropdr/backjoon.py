#   priorities	    location	return
# [2, 1, 3, 2]	        2	      1
# [1, 1, 9, 1, 1, 1]	  0	      5

# 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다. 이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.

# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.

# 예를 들어, 4개의 문서(A, B, C, D)가 순서대로 인쇄 대기목록에 있고 중요도가 2 1 3 2 라면 C D A B 순으로 인쇄하게 됩니다.
# 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 알고 싶습니다. 위의 예에서 C는 1번째로, A는 3번째로 인쇄됩니다.
# 현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때, 
# 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.

from collections import deque
def solution(priorities, location):
    pri_queue = deque(priorities)
    print_stack = [] #프린트 몇 개 되었는지... 굳이 스택으로 안 하고 answer = 0부터 해서 더해줘도 될 듯

    while True:
        if pri_queue[0] == max(pri_queue):
            print_stack.append(pri_queue.popleft())
            if location == 0:
                return len(print_stack)
            else:
                location -= 1
        else:
            pri_queue.append(pri_queue.popleft())
            if location != 0:
                location -= 1
            else:
                location = len(pri_queue) - 1
                
# Sorted 된 내림차순 priorities 리스트 & enumerate로 job의 인덱스와 priorieties => 이 둘을 비교해가면서 출력될 때마다 answer+=1 하는 방법도 있음!
