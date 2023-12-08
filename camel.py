camel = input("camelCase: ").strip()

def snake(camel):
    ans = ''
    for cap in range(len(camel)):
        if cap > 0 and camel[cap].isupper():
            ans += "_"

        ans += camel[cap].lower()
    print(ans)

snake(camel)
