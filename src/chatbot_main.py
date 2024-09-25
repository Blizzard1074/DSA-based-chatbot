import json
import requests

# Path to the dictionary cache
cache_file_path = 'dictionary_cache.json'

# Load the dictionary cache
try:
    with open(cache_file_path, 'r') as cache_file:
        dictionary_cache = json.load(cache_file)
except FileNotFoundError:
    dictionary_cache = {}

# List of words to ignore for definitions
ignore_words = ["i", "to", "the", "a", "an", "and", "but", "or", "so", "for", "of", "on", "in", "is", "am", "are", "be"]

def fetch_word_data(word):
    """Fetch word data from the local cache or external dictionary API."""
    word = word.lower()

    # First, check the local cache
    if word in dictionary_cache:
        return dictionary_cache[word]

    # If not found in cache, fetch from API
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    
    if response.status_code == 200:
        word_data = response.json()

        # Cache the word data locally for future use
        dictionary_cache[word] = word_data
        
        # Update the dictionary cache file
        with open(cache_file_path, 'w') as cache_file:
            json.dump(dictionary_cache, cache_file, indent=4)

        return word_data
    else:
        return None

def choose_best_definition(word_data):
    """Choose the best definition for the word based on conversational context."""
    # Assuming word_data is the JSON response from the dictionary API
    for entry in word_data:
        for meaning in entry['meanings']:
            if meaning['partOfSpeech'] in ['adjective', 'verb']:
                return meaning['definitions'][0]['definition'], meaning['partOfSpeech']
    # Default to the first definition if no adjectives/verbs found
    return word_data[0]['meanings'][0]['definitions'][0]['definition'], word_data[0]['meanings'][0]['partOfSpeech']

def generate_response(user_input):
    """Generate a response based on user input."""
    normalized_input = user_input.lower()

    # Check for common conversational phrases
    if normalized_input in ["hello", "hi"]:
        return "Ah, hello! It's great to see you! How can I assist you today?"
    elif normalized_input in ["how are you", "how's it going", "what's up"]:
        return "I'm just a bot, but I'm here to help! What about you?"
    elif normalized_input in ["what can you do", "tell me about yourself"]:
        return "I'm your friendly chatbot designed to help you learn new words and answer your questions! What word do you want to explore today?"

    # For words lookup
    words = normalized_input.split()
    responses = []
    
    for word in words:
        if word in ignore_words:
            continue  # Skip common words that don't need defining
        word_data = fetch_word_data(word)
        if word_data:
            definition, pos = choose_best_definition(word_data)
            responses.append(f"Ah, '{word}'! That's a {pos} meaning: {definition}. What else would you like to know?")
        else:
            responses.append(f"I'm not sure what '{word}' means. Can you try another word?")
    
    if responses:
        return " ".join(responses)
    
    return "I'm not sure how to respond to that. Could you ask about a specific word or phrase?"

if __name__ == "__main__":
    print("Welcome to the Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye! Have a great day!")
            break
        bot_response = generate_response(user_input)
        print(f"Bot: {bot_response}")
