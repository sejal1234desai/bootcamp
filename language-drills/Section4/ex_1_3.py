#3. store_funcs_list

funcs = [abs, str, hex]

results = [f(-42) for f in funcs]
print(results)  # Output: [42, '-42', '-0x2a']
