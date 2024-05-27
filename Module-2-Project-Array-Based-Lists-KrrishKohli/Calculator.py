import ArrayStack


class Calculator:
    def __init__(self):
        self.dict = None

    def balanced_parens(self, s: str) -> bool:
        """
        This function checks if the string s contains balanced parentheses
        :param s: str type; the string to be checked
        :return: bool type; True if the string s contains balanced parentheses
        """
        stack = ArrayStack.ArrayStack()
        for c in s:
            if c == "(":
                stack.push(c)
            elif c == ")":
                if stack.size() == 0:
                    return False
                else:
                    stack.pop()
        return stack.size() == 0
        return True
        