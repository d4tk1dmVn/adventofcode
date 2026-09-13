input = "input.txt"
wire_to_evaluate = 'a'

expression_list = []
with open(input, 'r') as file:
    for line in file:
        expression_list.append(line.strip().split())

def parse_expression(expression):
    if len(expression) == 3 and expression[0].isnumeric():
        return { 'value' : int(expression[0]) }
    if len(expression) == 3:
        operator = 'ASS'
        operands = [expression[0]]
    elif len(expression[:-2]) == 2:
        # NOT case
        operator = 'NOT'
        operands = [expression[1]]
    else:
        operator = expression[1]
        operands = expression[0:3:2]
    operands = [int(x) if x.isnumeric() else x for x in operands]
    return { 'operator' : operator, 'operands': operands }

def all_operands_evaluated(operands, results):
      return all(w in results for w in operands if isinstance(w,str))

def evaluate(expression, results):
    wires = expression['operands']
    values = [results[w] if isinstance(w, str) else w for w in wires]
    match expression['operator']:
        case 'ASS':
            return values[0]
        case 'NOT':
            return ~values[0] & 0xFFFF
        case 'OR':
            return values[0] | values[1]
        case 'AND':
            return values[0] & values[1]
        case 'LSHIFT':
            return values[0] << values[1]
        case 'RSHIFT':
            return values[0] >> values[1]
        case _:
            print("CRITICAL ERROR: unknown operator found")
            exit(1)

def filter_retry_operands(operands, results):
    return [o for o in operands if isinstance(o, str) and o not in results]

def parse_input(expression_list, overrides):
    operations = {}
    results = {}

    for expression in expression_list:
        cur_wire = expression[-1]
        if cur_wire in overrides:
            results[cur_wire] = overrides[cur_wire]
            continue
        parsed = parse_expression(expression)
        if 'value' in parsed:
            results[cur_wire] = parsed['value']
        elif 'operands' in parsed and all_operands_evaluated(parsed['operands'], results):
            value = evaluate(parsed, results)
            results[cur_wire] = value
        else:
            operations[cur_wire] = parsed
    return [operations, results]

def pop_and_requeue(operands, wire_queue):
    for o in operands:
        if o in wire_queue: wire_queue.pop(o)
        wire_queue[o] = 0

def evaluate_circuit(parsed_input):
    operations, results = parsed_input
    wire_queue = { wire_to_evaluate : 0 }
    while wire_queue != {}:
        cur_wire = wire_queue.popitem()[0]
        cur_expr = operations[cur_wire]
        if all_operands_evaluated(cur_expr['operands'], results):
            value = evaluate(cur_expr, results)
            results[cur_wire] = value
        else:
            wire_queue[cur_wire] = 0
            non_evaluated_operands = filter_retry_operands(cur_expr['operands'], results)
            pop_and_requeue(non_evaluated_operands, wire_queue)

    return results[wire_to_evaluate]

part_one_parsed_input = parse_input(expression_list, {})
first_a_value = evaluate_circuit(part_one_parsed_input)
print(f"The value for expression a is {first_a_value}")
part_two_parsed_input= parse_input(expression_list, { 'b' : first_a_value})
second_a_value = evaluate_circuit(part_two_parsed_input)
print(f"The value for expression a is {second_a_value}")
