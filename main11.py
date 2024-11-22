import json

def task() -> float:
    
    with open('input.json', 'r') as f:
        data = json.load(f)

   
    total_sum = 0.0

    
    for item in data:
        score = item.get('score', 0)
        weight = item.get('weight', 1) 
        total_sum += score * weight

   
    return round(total_sum, 3)


print(task())