import json

ctx = {"name": "老王"}
print(type(ctx))

result = json.dumps(ctx)
print(type(result))

result1 = json.loads(result)
print(result1)
print(type(result1))
