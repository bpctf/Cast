import ast, unittest 
from rules.custom_rules import OsJoinRule

class TestOsPathJoin(unittest.TestCase):
    """ Unit test class for testing pickle_loads
    """

    def tearDown(self):
        result = self._outcome.result
        if not any(error for test, error in result.errors + result.failures if test == self):
            print(f"\n {self._testMethodName} passed!\n\n")

    def test_os_path_join(self):
        source = """
import os
os.path.join("~/dev", "/root")
        """
        mast = ast.parse(source)
        urljoin_class = OsJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == "PYT003", "Wrong rule ID found."
    
    def test_path_join(self):
        source = """
from os import path
path.join("~/dev", "/root")
        """
        mast = ast.parse(source)
        urljoin_class = OsJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == "PYT003", "Wrong rule ID found."

    def test_join(self):
        source = """
from os.path import join
join("~/dev", "/root")
        """
        mast = ast.parse(source)
        urljoin_class = OsJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == "PYT003", "Wrong rule ID found."
    
    def test_os_path_asp(self):
        source = """
import os.path as p
p.join("~/dev", "/root")
        """
        mast = ast.parse(source)
        urljoin_class = OsJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == "PYT003", "Wrong rule ID found."

    def test_os_path_join_safe(self):
        source = """
import os
os.path.join("~/dev", "python")
        """
        mast = ast.parse(source)
        urljoin_class = OsJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == None, "Wrong rule ID found."
    
    def test_path_join_safe(self):
        source = """
from os import path
path.join("~/dev", "python")
        """
        mast = ast.parse(source)
        urljoin_class = OsJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == None, "Wrong rule ID found."

    def test_join_safe(self):
        source = """
from os.path import join
join("~/dev", "python")
        """
        mast = ast.parse(source)
        urljoin_class = OsJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == None, "Wrong rule ID found."
    
    def test_os_path_asp_safe(self):
        source = """
import os.path as p
p.join("~/dev", "python")
        """
        mast = ast.parse(source)
        urljoin_class = OsJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == None, "Wrong rule ID found."

if __name__ == "__main__":
    unittest.main()
