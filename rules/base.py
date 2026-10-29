import ast
from .models import RuleBreak, Findings

class BaseRule(ast.NodeVisitor):
    """ Base Rule class which will be inherited by rules.
    """
    def __init__(self):
        self.rulebreak = RuleBreak(
            id="PYB001",
            message="Default error message for base class",
            func=[],
            args=[],
            arg_pos = -1
        )
        self.findings = Findings()
        self.import_calls = {}

    def _get_string_args(self, node_arg) -> str:
        """ Get args as strings.

            Args:
                node_arg (ast.arguments): The argument from the ast to check against.

            Returns:
                str: Returns the arg as a string from the node, otherwise an empty string.
        """
        if isinstance(node_arg, ast.Constant) and isinstance(node_arg.value, str):
            return node_arg.value
        # This needs to be here for older python versions.
        elif isinstance(node_arg, ast.Str):
            return node_arg.s
        return str()

    def _find_parts_iter(self, node):
        """ Find function parts iteratively.

            Args:
                node (ast.Call): The AST expression representing a function, method, or class invocation.

            Returns:
                list: Returns a list of found function parts.
        """
        curr = node.func
        func_parts = []

        while isinstance(curr, ast.Attribute):
            # In os.path.join curr.attr is 'join'.
            func_parts.append(curr.attr)
            # Curr.value is then os.path, using the example above.
            curr = curr.value

        if not isinstance(curr, ast.Name):
            return []

        func_parts.append(curr.id)
        func_parts.reverse()
        
        return func_parts

    def _find_func(self, node):
        """ Find the function, in the node, defined by the rule.

            Args:
                node (ast.Call): The AST expression representing a function, method, or class invocation.

            Returns:
                bool: True if found, false if not.
        """
        parts = self._find_parts_iter(node)
        
        if not parts:
            return False
       
        if parts[0] in self.import_calls:
            parts = self.import_calls[parts[0]] + parts[1:]
        return self.rulebreak.func == parts

    def _find_arg(self, node):
        """ Find the args, in the node, defined by the rule.

            Args:
                node (ast.Call): The AST expression representing a function, method, or class invocation.
            
            Returns:
                bool: True if found, false if not.
        """
        if not self.rulebreak.args:
            return True

        pos = self.rulebreak.arg_pos
        if 0 <= pos < len(node.args):
            arg_get = self._get_string_args(node.args[pos])
            if not arg_get:
                return False
            if len(self.rulebreak.args) == 1:
                if arg_get.startswith(self.rulebreak.args[0]):
                    return True
            else:
                for arg_ in self.rulebreak.args:
                    if arg_get.startswith(arg_):
                        return True
        else:
            for kw in node.keywords:
                if kw.arg in self.rulebreak.args:
                    if isinstance(kw.value, ast.Constant):
                        return kw.value.value is True
        return False
 
    def visit_Module(self, node):
        """ Visits a Module node within the AST and gets all imports for the file.

            Args:
                node (ast.Module): The AST expression representing the Python module.
        """
        for child in node.body:
            if not isinstance(child, ast.ImportFrom) and not isinstance(child, ast.Import):
                continue
            for alias in child.names:
                local_name = alias.asname if alias.asname else alias.name
                import_names = []
                if isinstance(child, ast.ImportFrom):
                    import_names = child.module.split('.')
                    import_names.append(alias.name)
                if isinstance(child, ast.Import):
                    import_names = alias.name.split('.')
                self.import_calls[local_name] = import_names

        self.generic_visit(node)

    def visit_Call(self, node):
        """ Visits a Call node within the AST and checks if the rule's function name(s) and arg(s) are present.
            If they are update our findings and post it to the console.
        
            Args:
                node (ast.Call): The AST expression representing a function, method, or class invocation.
        """
        if self._find_arg(node) and self._find_func(node):
            self.findings.add(self.rulebreak.id, self.rulebreak.message, node.lineno, node.col_offset)
        self.generic_visit(node)

    def print_findings(self):
        """ Print the findings list.
        """
        if self.findings:
            print(self.findings)

