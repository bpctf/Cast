## Cast

Cast — a Python AST-based security analysis tool built to explore static analysis, rule design, testing, and threat modeling.

## Features

- AST-based analysis: Parses Python source code to inspect its structure without executing it.

- Custom security rules: Uses individual rule classes to identify potentially unsafe function calls and arguments.

- Import resolution: Accounts for common import patterns and aliases when matching function calls.

- Dynamic rule discovery: Loads custom rules to make extending the tool with additional checks easier.

## What it does

Cast analyzes Python files to find pre-determined rules that can be malicious or have unintended behaviour.

## Example

If your Python file contains os.path.join('Desktop', '/root'), Cast will flag it as a potential issue.

On Linux systems, os.path.join() returns '/root' because the second argument is an absolute path. This overrides the preceding path, 'Desktop', rather than joining the two paths together.

This can lead to unexpected path handling if the application assumes the resulting path will remain inside the intended directory.

## How To Use

To use Cast you can call `python main.py /path/to/file`. To run all the tests you can use `python -m unittest discover -s tests`. There is an example file you can run with `python main.py tests/vulntest.py`.

## Security Rules

|  ID  | Rule                              |
|------|-----------------------------------|
|PYB001|Base                               |
|PYT001|POpen with Shell                   |
|PYT002|Pickle.loads                       |
|PYT003|os.path.join with root arg         |
|PYT004|pathlib.Path.joinpath with root arg|
|PYT005|yaml.load                          |
|PYT006|urllib.parse.urljoin with root arg |

## How It Works

1. Parse: Cast parses the target Python file into an AST.

2. Discover rules: Custom rule classes are loaded and initialized.

3. Analyze: Each rule examines relevant AST nodes and checks for configured functions and arguments.

4. Report: When a rule's conditions match, Cast reports a finding.

Cast parses the analyzed source code rather than executing it. This helps avoid the risks associated with running untrusted source code during analysis, but does not guarantee that the analysis process itself is free from security risks.

## Testing

35 tests passed.

## Limitations

Cast is an experimental static analysis tool with several limitations:

- No runtime analysis: Cast does not execute the analyzed code or observe its runtime behavior.

- Limited data-flow analysis: Cast does not comprehensively track values through variables, function calls, or execution paths.

- False positives and false negatives: A suspicious pattern may be safe in context, while a vulnerability may exist without matching any current rule.

- Limited import resolution: Import handling supports common patterns but may not cover every valid Python import structure.

- Context-dependent findings: Detecting a function call alone is not enough to establish that an application is vulnerable.

- Cast is intended to supplement code review and security testing, not replace them.

- Currently does not account for pathlib usage of:
```python
from pathlib import Path

Path("/base").joinpath("/root")
```

## Future Improvements

- Expand the collection of security rules.

- Improve analysis of dynamic values and import patterns.

- Test rule limitations and document potential bypasses.

- Explore integration into CI/CD pipelines.

- Improve command-line usability and diagnostic output.

## Motivation

Cast was developed as a practical exploration of Python ASTs, static analysis, and application security. The goal is to build an extensible foundation for detecting potentially unsafe coding patterns while exploring the limitations of rule-based security analysis.
