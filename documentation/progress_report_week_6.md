## Progress report week 5

### What I have done this week?
  - Almost all main features for creating binary tree nodes are done
  - Brainstorming how to present binary tree. Probably printing binary tree as a string using pre tag.
  - Improved semantic tree result in UI
  - Working to get proper validator
  - Bugfix to double negation rule
  - Increased test coverage to 99%
  - Did peer review
  - Updated documentation

### How the software has progressed 
  - Features for semantic tree rules pretty much done. Left is to check if the path from the root to a leaf has a negation of proposition symbol as well as the proposition symbol.
 
### Problems
  - No new major problems, pretty clear plan what to do next
  - Getting software into production failed -> fly launch failed.

### Questions
  - Is proper proposition validator must or can I expect that tool is used with propositions that are written correctly?
  - Does this software need O-analysis? 
  
### Next week
  - Test more complex propositions
  - Refactoring
  - Improve UI
  - Add more tests
  - Setting up the proper proposition validator (?) (drafted one doesn't support negations)

Current proposition valídator draft (didn't want to add it to the code, since it's not working properly)

def validate_proposition(proposition):
        """ Validates that proposition is in correct format

        Args:
            proposition = proposition string

        Returns:
            Boolean variable

        """

        prev_char = proposition[0]
        depth = 0
        valid_chars = '()∨∧→↔¬abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ'

        if proposition[0] in ['∨', '∧', '→', '↔']:
            return f'Proposition clause cannot start with {proposition}'
        
        for char in proposition:
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
            elif char not in valid_chars:
                return f'Character {char} is not valid'
            elif char in ['∨', '∧', '→', '↔'] and prev_char in ['∨', '∧', '→', '↔']:
                return False
            elif char not in ['∨', '∧', '→', '↔', '(', ')'] and prev_char not in ['∨', '∧', '→', '↔', '(', ')']:
                return False 
            prev_char = char
            

        if depth != 0:        
            return 'Parenthesis missmatch' 
    
        return True


### Hours used
  -  11 hours
