from brownie import $name_pascal_case$

def main():
    sources = $name_pascal_case$.get_verification_info()['standard_json_input']['sources']
    keys = list(sources.keys())
    keys = sorted(keys, key=lambda x: -1 if x != '$name_pascal_case$.sol' else 1)
    with open('$name_pascal_case$Flattened.sol', 'w') as f:
        for key in keys:
            f.write(sources[key]['content'])
            f.write("\n\n")
    print("Done.")
