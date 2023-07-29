from dataclasses import dataclass
import re, math

@dataclass
class Monkey:
    id: int
    items: list
    operation: str
    test: int
    true_throw: int
    false_throw: int
    items_inspected: int

monkeys = []

contents: str
with open("input.txt") as f:
    contents = f.read()

monkey_predictions = contents.split("\n\n")
for monkey_prediction in monkey_predictions:
    monkey_details = monkey_prediction.splitlines()

    monkey_id = int(re.search("\d+", monkey_details[0]).group(0))
    monkey_items = [int(i) for i in re.search("\d.*", monkey_details[1]).group(0).split(", ")]
    monkey_operation = re.search("old.*", monkey_details[2]).group(0)
    monkey_test = int(re.search("\d+", monkey_details[3]).group(0))
    monkey_true = int(re.search("\d+", monkey_details[4]).group(0))
    monkey_false = int(re.search("\d+", monkey_details[5]).group(0))

    monkeys.append(Monkey(monkey_id, monkey_items, monkey_operation, monkey_test, monkey_true, monkey_false, 0))

lcm = math.lcm(*[i.test for i in monkeys])

for round in range(10000):
    monkey: Monkey
    for monkey in monkeys:
        # print(f"Monkey {monkey.id}:")
        i = 0
        while i < len(monkey.items):
            # print(f"\tMonkey inspects an item with a worry level of {monkey.items[i]}.")
            monkey.items[i] = eval(monkey.operation.replace("old", str(monkey.items[i])))
            # print(f"\t\tWorry level goes to {monkey.items[i]}.")
            monkey.items[i] %= lcm
            # print(f"\t\tMonkey gets bored with item. Worry level is divided by 3 to {monkey.items[i]}.")
            
            target: int
            if monkey.items[i] % monkey.test == 0:
                # print(f"\t\tCurrent worry level is divisible by {monkey.test}.")
                # print(f"\t\tItem with worry level {monkey.items[i]} is thrown to monkey {monkey_true}")
                target = monkey.true_throw
            else:
                # print(f"\t\tCurrent worry level is not divisible by {monkey.test}.")
                # print(f"\t\tItem with worry level {monkey.items[i]} is thrown to monkey {monkey_false}")
                target = monkey.false_throw
            target_monkey: Monkey
            target_monkey_index = 0
            for target_monkey in monkeys:
                if target_monkey.id == target:
                    target_monkey_index = monkeys.index(target_monkey)
                    break
            monkey.items_inspected += 1
            monkeys[target_monkey_index].items.append(monkey.items.pop(i))
    # print(f"After round {round + 1}, the monkeys are holding items with these worry levels:")
    # for monkey in monkeys:
    #     print(f"Monkey {monkey.id}: {', '.join(map(str, monkey.items))}")
    # print()

most_business = 0
busiest_monkey = -1
for monkey in monkeys:
    print(f"Monkey {monkey.id} inspected items {monkey.items_inspected} times.")
    if monkey.items_inspected > most_business:
        most_business = monkey.items_inspected
        busiest_monkey = monkeys.index(monkey)

second_most_business = 0
second_busiest_monkey = -1
for monkey in monkeys:
    if monkeys.index(monkey) != busiest_monkey and monkey.items_inspected > second_most_business:
        second_most_business = monkey.items_inspected
        second_busiest_monkey = monkeys.index(monkey)

print(f"\nMonkey business: {most_business * second_most_business}")