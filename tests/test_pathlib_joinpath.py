import ast, unittest 
from rules.custom_rules import PathJoinRule

class TestPathlibJoinPath(unittest.TestCase):
    """ Unit test class for testing pickle_loads
    """

    def tearDown(self):
        result = self._outcome.result
        if not any(error for test, error in result.errors + result.failures if test == self):
            print(f"\n {self._testMethodName} passed!\n\n")

    def test_pathlib_Path_joinpath(self):
        source = """
import pathlib
pathlib.Path.joinpath("~/dev", "/root")
        """
        mast = ast.parse(source)
        urljoin_class = PathJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == "PYT004", "Wrong rule ID found."
    
    def test_Path_joinpath(self):
        source = """
from pathlib import Path
Path.joinpath("~/dev", "/root")
        """
        mast = ast.parse(source)
        urljoin_class = PathJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == "PYT004", "Wrong rule ID found."

    def test_joinpath(self):
        source = """
from pathlib.Path import joinpath
joinpath("~/dev", "/root")
        """
        mast = ast.parse(source)
        urljoin_class = PathJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == "PYT004", "Wrong rule ID found."
    
    def test_pathlib_Path_asp(self):
        source = """
import pathlib.Path as p
p.joinpath("~/dev", "/root")
        """
        mast = ast.parse(source)
        urljoin_class = PathJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == "PYT004", "Wrong rule ID found."

    def test_pathlib_Path_joinpath_safe(self):
        source = """
import pathlib
pathlib.Path.joinpath("~/dev", "python")
        """
        mast = ast.parse(source)
        urljoin_class = PathJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == None, "Wrong rule ID found."
    
    def test_Path_joinpath_safe(self):
        source = """
from pathlib import Path
Path.joinpath("~/dev", "python")
        """
        mast = ast.parse(source)
        urljoin_class = PathJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == None, "Wrong rule ID found."

    def test_joinpath_safe(self):
        source = """
from pathlib.Path import joinpath
joinpath("~/dev", "python")
        """
        mast = ast.parse(source)
        urljoin_class = PathJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == None, "Wrong rule ID found."
    
    def test_pathlib_Path_asp_safe(self):
        source = """
import pathlib.Path as p
p.joinpath("~/dev", "python")
        """
        mast = ast.parse(source)
        urljoin_class = PathJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == None, "Wrong rule ID found."

if __name__ == "__main__":
    unittest.main()
