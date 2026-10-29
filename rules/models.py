from dataclasses import dataclass

@dataclass
class RuleBreak:
    """ A collection of Rules to look for when scanning files.

        Attributes:
            id (str): The ID used to identify the rule.
            message (str): The message to post for the rule.
            func (list): List of functions to look for.
            args (list): List of arguments to look for.
            arg_pos (int): The position to look for arguments at.
    """
    id: str
    message: str
    func: list
    args: list
    arg_pos: int

@dataclass
class Finding:
    """ A collection of Findings to look for when scanning files.

        Attributes:
            id (str): The ID used to identify the rule.
            message (str): The message to post for the rule.
            line (int): The line the error is found at.
            column (int): The column the error is found at.
    """
    id: str
    message: str
    line: int
    column: int

class Findings():
    """ Findings of potential issues.
    """
    def __init__(self):
        self._findings = []

    def __bool__(self):
        """ Bool representation of the findings list.
        
            Returns:
                bool: True if there are findings, false otherwise.
        """
        return bool(self._findings)

    def __str__(self):
        """ String representation of the findings dictionary.
            
            Returns:
                str: A formatted string representation of the findings dictionary.
        """
        return"\n".join(f"Issue found!\n ID: {finding.id}\n Message: {finding.message}\n At line: {finding.line}\n At column: {finding.column}" for finding in self._findings)


    def add(self, rule_id, message, line, column):
        """ Add the findings object with new values to the list.

            Args:
                rule_id (str): The ID of the RuleBreak dataclass.
                message (str): The message used for the RuleBreak dataclass.
                line (int): The line number the issue can be found at.
                column (int): The column offset the issue can be found at.
        """
        self._findings.append(Finding(rule_id, message, line, column))

    def get_finding(self, entry):
        """ Get an entry of the findings object.
        
            Args:
                entry (str): The attribute of the findings object to return.

            Returns:
                int or str: The value of the findings dictionary entry.
        """
        for finding in self._findings:
            if not hasattr(finding, entry):
                raise AttributeError(f"Unknown attribute {entry} in dataclass")

            return getattr(finding, entry)


