'''
1、pop函数：移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
2、栈的原理：先入后出，与字典配合使用
例：‘([)]’ ==>先进来的是‘(’，则其对应的‘)’必须最后出
    ‘([])’ ==>先进‘(’，接着再进‘[’，之后进入‘]’，与对应的括号消除，最后进入‘)’与第一个消除，结果为空，表明有效

'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dict_brackets={'(':')',
                       '[':']',
                       '{':'}'}
        for i in s:
            if i in dict_brackets:
                stack.append(i)
                continue
            if stack and dict_brackets[stack[-1]]==i:
                stack.pop()
            else:
                return False
        if not stack:
            return True
        else:
            return False
