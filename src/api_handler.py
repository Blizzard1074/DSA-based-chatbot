import requests
import json

class DictionaryAPIHandler:
    def __init__(self, cache_file='../data/dictionary_cache.json'):
        self.cache_file = cache_file
        self.load_cache()

    def load_cache(self):
        try:
            with open(self.cache_file, 'r') as f:
                self.cache = json.load(f)
        except FileNotFoundError:
            self.cache = {}

    def save_cache(self):
        with open(self.cache_file, 'w') as f:
            json.dump(self.cache, f, indent=4)

    def fetch_word_data(self, word):
        if word in self.cache:
            return self.cache[word]

        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)
        if response.status_code == 200:
            word_data = response.json()
            self.cache[word] = word_data
            self.save_cache()
            return word_data
        else:
            return None

    def get_synonyms(self, word):
        word_data = self.fetch_word_data(word)
        if word_data:
            synonyms = []
            meanings = word_data[0].get('meanings', [])
            for meaning in meanings:
                for definition in meaning.get('definitions', []):
                    synonyms.extend(definition.get('synonyms', []))
            return synonyms
        return []

