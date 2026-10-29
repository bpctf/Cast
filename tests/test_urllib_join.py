import ast, unittest 
from rules.custom_rules import UrlJoinRule

class TestUrllibJoin(unittest.TestCase):
    """ Unit test class for testing pickle_loads
    """

    def tearDown(self):
        result = self._outcome.result
        if not any(error for test, error in result.errors + result.failures if test == self):
            print(f"\n {self._testMethodName} passed!\n\n")

    def test_urllib_parse_urljoin(self):
        source = """
import urllib
urllib.parse.urljoin("https://www.google.com", "https://www.evil.com")
        """
        mast = ast.parse(source)
        urljoin_class = UrlJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == "PYT006", "Wrong rule ID found."

    def test_parse_urljoin(self):
        source = """
from urllib import parse
parse.urljoin("https://www.google.com", "https://www.evil.com")
        """
        mast = ast.parse(source)
        urljoin_class = UrlJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == "PYT006", "Wrong rule ID found."

    def test_parse_urljoin_asp(self):
        source = """
from urllib import parse as p
p.urljoin("https://www.google.com", "https://www.evil.com")
        """
        mast = ast.parse(source)
        urljoin_class = UrlJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == "PYT006", urljoin_class.findings.get_finding('id')#"Wrong rule ID found."

    def test_urljoin(self):
        source = """
from urllib.parse import urljoin
urljoin("https://www.google.com", "https://www.evil.com")
        """
        mast = ast.parse(source)
        urljoin_class = UrlJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == "PYT006", "Wrong rule ID found."

    def test_urllib_parse_urljoin_safe(self):
        source = """
import urllib
urllib.parse.urljoin("https://www.google.com", "search")
        """
        mast = ast.parse(source)
        urljoin_class = UrlJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == None, "Wrong rule ID found."

    def test_parse_urljoin_safe(self):
        source = """
from urllib import parse
parse.urljoin("https://www.google.com", "search")
        """
        mast = ast.parse(source)
        urljoin_class = UrlJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == None, "Wrong rule ID found."
    
    def test_parse_urljoin_asp_safe(self):
        source = """
from urllib import parse as p
p.urljoin("https://www.google.com", "search")
        """
        mast = ast.parse(source)
        urljoin_class = UrlJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == None, "Wrong rule ID found."
    
    def test_urljoin_safe(self):
        source = """
from urllib.parse import urljoin
urljoin("https://www.google.com", "search")
        """
        mast = ast.parse(source)
        urljoin_class = UrlJoinRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == None, "Wrong rule ID found."

if __name__ == "__main__":
    unittest.main()
