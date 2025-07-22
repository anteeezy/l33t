def interpreter(ast):
    print("interpreting..")
    for node in ast:
        if node["type"] == "print_statement":
            print(node["value"])
        else:
            raise RuntimeError(f"Unknown statement type: {node['type']}")

