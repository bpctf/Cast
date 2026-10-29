import importlib, pkgutil, sys

def load_all_rules():
    """ Load all our custom rules into sys.modules.
    """
    # pkgutil.iter_modules returns a tuple of module_finder, name, and ispkg. We only need name.
    for _, name, _ in pkgutil.iter_modules(__path__):
        fname = f"{__name__}.{name}"
        
        # If the function is not loaded in sys.modules load it.
        if fname not in sys.modules:
            importlib.import_module(fname)

def get_all_classes():
    """ Return all the classes that inherit from BaseRule.

        Returns:
            list: List of all the BaseRule classes.
    """
    from .base import BaseRule
    # Load all the rule functions into the sys.modules.
    load_all_rules()
    # Create an empty list.
    list_of_rules = []
    # Find all BaseRule subclasses (all the classes in custom_rules.py)
    subclasses = BaseRule.__subclasses__()
    # Loop through them and add them to the list.
    for rule_class in subclasses:
        list_of_rules.append(rule_class())
    # Return the list.
    return list_of_rules
