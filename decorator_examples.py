def lowercase_decorator(function):
    def lowercasewapper():
        original_result = function()
        modified_result = original_result.lower()
        return modified_result
    return lowercasewapper
@lowercase_decorator
def sayHello():
    return "HELLO"



print(sayHello())


