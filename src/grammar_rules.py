# grammar_rules.py
import json

class GrammarValidator:
    def __init__(self, grammar_file='../data/grammar_rules.json'):
        # Load grammar rules from a JSON file
        with open(grammar_file, 'r') as f:
            self.grammar_rules = json.load(f)

    def validate_subject_verb_agreement(self, subject, verb):
        """Validates subject-verb agreement based on grammar rules."""
        if subject in self.grammar_rules['subject_verb_agreement']['singular']:
            return verb in self.grammar_rules['verb_tenses']['present']
        elif subject in self.grammar_rules['subject_verb_agreement']['plural']:
            return verb in self.grammar_rules['verb_tenses']['past']
        return False

    def validate_adjective_noun_pairing(self, adjective, noun):
        """Validates adjective-noun pairing based on grammar rules."""
        return (adjective in self.grammar_rules['adjective_noun_pairing']['adjectives'] 
                and noun in self.grammar_rules['adjective_noun_pairing']['nouns'])

def apply_grammar_rules(subject, verb, adjective, noun):
    """Applies grammar rules using GrammarValidator."""
    validator = GrammarValidator()

    # Validate subject-verb agreement
    if not validator.validate_subject_verb_agreement(subject, verb):
        return f"Error: '{subject}' does not agree with the verb '{verb}'."

    # Validate adjective-noun pairing
    if not validator.validate_adjective_noun_pairing(adjective, noun):
        return f"Error: The adjective '{adjective}' does not pair correctly with the noun '{noun}'."

    return "Grammar is correct."
