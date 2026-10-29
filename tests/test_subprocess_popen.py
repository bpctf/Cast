import ast, rules, unittest 
from rules.custom_rules import PopenRule

class TestSubprocessPOpen(unittest.TestCase):
    """ Unit test class for testing subprocess popen
    """

    def tearDown(self):
        result = self._outcome.result
        if not any(error for test, error in result.errors + result.failures if test == self):
            print(f"\n {self._testMethodName} passed!\n\n")

    def test_subprocess_popen_shell(self):
        source = """
import subprocess
subprocess.Popen("calc", shell=True)
        """
        mast = ast.parse(source)
        popen_class = PopenRule()
        popen_class.visit(mast)
        assert popen_class.findings.get_finding('id') == "PYT001", "Wrong rule ID found"

    def test_subprocess_popen_noshell(self):
        source = """
import subprocess
subprocess.Popen("calc")
        """
        mast = ast.parse(source)
        popen_class = PopenRule()
        popen_class.visit(mast)
        assert popen_class.findings.get_finding('id') == None, "Default rule not found when it should be."

    def test_subprocess_popen_shell_false(self):
        source = """
import subprocess
subprocess.Popen("calc", shell=False)
        """
        mast = ast.parse(source)
        popen_class = PopenRule()
        popen_class.visit(mast)
        assert popen_class.findings.get_finding('id') == None, "Default rule not found when it should be."



if __name__ == "__main__":
    unittest.main()

