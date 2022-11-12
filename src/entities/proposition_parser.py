class PropositionParser:
    def __init__(self, proposition):
        self.proposition = proposition
    
    def validate_proposition(self):
        if self.proposition == "":
            return False
        elif self.proposition[0] in ['∨', '∧']:
            return False
        return True
         