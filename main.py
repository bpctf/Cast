import argparse, ast, rules

def parse_args():
    """ Parse arguments by the CLI.

        Returns:
            parse_args(ArgumentParser.Namespace): A Namespace object which returns the arguments from the CLI.
    """
    parser = argparse.ArgumentParser(prog="Cast", description="Custom AST.")
    parser.add_argument('filename', help="The file to parse through.")
    return parser.parse_args()

if __name__ == "__main__":
    parser = parse_args()
    list_of_classes = rules.get_all_classes()
    
    with open(parser.filename) as f:
        source = f.read()
    
    mast = ast.parse(source)
    
    print(f"Checking file {parser.filename}. . .\n")
    
    for my_class in list_of_classes:
        my_class.visit(mast)
        my_class.print_findings()
