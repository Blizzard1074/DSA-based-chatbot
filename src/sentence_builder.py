class SentenceBuilder:
    def __init__(self, trie, grammar_validator):
        self.trie = trie
        self.grammar_validator = grammar_validator

    def build_sentence(self, subject, verb, object_):
        # Validate subject-verb agreement
        if not self.grammar_validator.validate_subject_verb_agreement(subject, verb):
            return "Invalid sentence: subject-verb disagreement."
        
        # Construct basic sentence
        sentence = f"{subject.capitalize()} {verb} {object_}."
        return sentence

    def build_with_synonyms(self, word):
        synonyms = self.trie.search(word)
        if synonyms:
            synonym_sentence = f"Did you mean: {', '.join(synonyms)}?"
            return synonym_sentence
        else:
            return f"No synonyms found for {word}."
