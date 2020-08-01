n = int(input())
queue = list(map(int,input().split()))

stack = []
fix_order = 1
keep_tracking = True
is_order = True

while (keep_tracking):
    q1 = queue[0] if len(queue) > 0 else -1
    s1 = stack[-1] if len(stack) > 0 else -1

    if q1 == fix_order:
        del queue[0]
        fix_order = fix_order + 1
        continue

    if s1 == fix_order:
        stack.pop()
        fix_order = fix_order + 1
        continue

    if q1 != -1:
        del queue[0]
        stack.append(q1)
        continue

    # DONE
    if q1 == -1 and s1 == -1:
        keep_tracking = False
        continue

    #Can't order
    if q1 == -1 and s1 != fix_order:
        keep_tracking = False
        is_order = False
        
if is_order == False:
    print('no')
else:
    print('yes')

