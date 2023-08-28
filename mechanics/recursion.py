def recursion(command, in_bracket = False):
    from execution import execution
    pointer = 0
    divided = list()
    while pointer < len(command):
        if command[pointer] in ['@', '$']: 
            cut = pointer   
            is_bracket = False        
            bracket = 0

            while cut < len(command) and command[cut] not in [' ', '\\', ','] or bracket > 0:
                if command[cut] == '(': 
                    bracket += 1
                    if not is_bracket: is_bracket = cut
                if command[cut] == ')': 
                    bracket -= 1
                    if bracket == 0: break
                cut += 1    

            if cut == len(command): cut += 1
            if is_bracket and bracket == 0:
                mechanic = command[pointer:][:is_bracket - pointer]
                args = recursion(command[is_bracket + 1:][:cut - 1 - is_bracket], in_bracket = True)
                out = execution(mechanic, args = args)
                divided.append(out)              
            else: 
                out = execution(command[pointer:][:cut - pointer])
                divided.append(out)

            if cut < len(command) and command[cut] == '\\': cut += 1
            command = command[:pointer] + str(out) + command[cut:]

        pointer += 1
    if in_bracket: return divided
    return command    