import ast, rules, unittest 
from rules.custom_rules import PickleRule

class TestPickleLoads(unittest.TestCase):
    """ Unit test class for testing pickle_loads
    """

    def tearDown(self):
        result = self._outcome.result
        if not any(error for test, error in result.errors + result.failures if test == self):
            print(f"\n {self._testMethodName} passed!\n\n")

    def test_pickle_loads(self):
        source = """
import pickle
pickle.loads("calc")
        """
        mast = ast.parse(source)
        pickle_loads_class = PickleRule()
        pickle_loads_class.visit(mast)
        assert pickle_loads_class.findings.get_finding('id') == "PYT002", "Wrong rule ID found."

    def test_pickle_loads_nopickle(self):
        source = """
from pickle import loads
loads("calc")
        """
        mast = ast.parse(source)
        pickle_loads_class = PickleRule()
        pickle_loads_class.visit(mast)
        assert pickle_loads_class.findings.get_finding('id') == "PYT002", "Wrong rule ID found."

if __name__ == "__main__":
    unittest.main()
