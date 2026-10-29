import ast, unittest 
from rules.custom_rules import YamlLoadRule

class TestYamlLoad(unittest.TestCase):
    """ Unit test class for testing pickle_loads
    """

    def tearDown(self):
        result = self._outcome.result
        if not any(error for test, error in result.errors + result.failures if test == self):
            print(f"\n {self._testMethodName} passed!\n\n")

    def test_yaml_load(self):
        source = """
import yaml
yaml.load('!!python/object/apply:posix_system ["id"]')
        """
        mast = ast.parse(source)
        urljoin_class = YamlLoadRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == "PYT005", "Wrong rule ID found."
    
    def test_load(self):
        source = """
from yaml import load
load('!!python/object/apply:posix_system ["id"]')        
"""
        mast = ast.parse(source)
        urljoin_class = YamlLoadRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == "PYT005", "Wrong rule ID found."

    def test_yaml_load_asyl(self):
        source = """
from yaml import load as yl
yl('!!python/object/apply:posix_system ["id"]')        
"""       
        mast = ast.parse(source)
        urljoin_class = YamlLoadRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == "PYT005", "Wrong rule ID found."

    def test_yaml_loads_safe(self):
        source = """
import yaml
yaml.loads('!!python/object/apply:posix_system ["id"]')
        """
        mast = ast.parse(source)
        urljoin_class = YamlLoadRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == None, "Wrong rule ID found."
    
    def test_loads_safe(self):
        source = """
from yaml import loads
loads('!!python/object/apply:posix_system ["id"]')        
"""
        mast = ast.parse(source)
        urljoin_class = YamlLoadRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == None, "Wrong rule ID found."

    def test_yaml_loads_asyl_safe(self):
        source = """
from yaml import loads as yl
yl('!!python/object/apply:posix_system ["id"]')        
"""       
        mast = ast.parse(source)
        urljoin_class = YamlLoadRule()
        urljoin_class.visit(mast)
        assert urljoin_class.findings.get_finding('id') == None, "Wrong rule ID found."
 

if __name__ == "__main__":
    unittest.main()
