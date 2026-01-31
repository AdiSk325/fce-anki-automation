#!/usr/bin/env python3
"""
FCE Anki Local Generator
Generates Anki flashcards using Ollama's llama3 model for FCE vocabulary.
"""

import json
import csv
import re
import ollama
from typing import Dict, List


def clean_json_string(json_str: str) -> str:
    """
    Clean and fix common JSON formatting issues from LLM output.
    
    Args:
        json_str: Raw JSON string from the model
        
    Returns:
        Cleaned JSON string
    """
    # Remove markdown code blocks if present
    json_str = re.sub(r'```json\s*', '', json_str)
    json_str = re.sub(r'```\s*$', '', json_str)
    
    # Remove any leading/trailing whitespace
    json_str = json_str.strip()
    
    # Fix common escape issues
    json_str = json_str.replace('\n', ' ')
    
    return json_str


def read_words_from_file(filename: str) -> List[str]:
    """
    Read words from the input file.
    
    Args:
        filename: Path to the file containing words
        
    Returns:
        List of words/phrases
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            words = [line.strip() for line in f if line.strip()]
        return words
    except FileNotFoundError:
        print(f"Błąd: Plik '{filename}' nie został znaleziony.")
        print(f"Utwórz plik '{filename}' i dodaj słowa (jedno słowo/fraza na linię).")
        return []
    except Exception as e:
        print(f"Błąd podczas odczytu pliku: {e}")
        return []


def generate_flashcard(word: str) -> Dict[str, str]:
    """
    Generate a flashcard for a given word using Ollama's llama3 model.
    
    Args:
        word: The word or phrase to create a flashcard for
        
    Returns:
        Dictionary with sentence, translation, and definition
    """
    prompt = f"""Create a JSON object for learning the English word/phrase "{word}" for FCE exam preparation.

The JSON should have exactly these fields:
1. "sentence": An English sentence using the word with Cloze deletion format {{{{c1::{word}}}}}
2. "translation": Polish translation of the entire sentence
3. "definition": Polish definition/explanation of the word

Example format:
{{
  "sentence": "The team showed great {{{{c1::resilience}}}} after losing the first game.",
  "translation": "Zespół wykazał się wielką odpornością po przegraniu pierwszego meczu.",
  "definition": "odporność, zdolność do powrotu do formy po trudnościach"
}}

Now create a similar JSON for the word/phrase: "{word}"

Return ONLY the JSON object, no additional text."""

    try:
        response = ollama.chat(
            model='llama3',
            messages=[{
                'role': 'user',
                'content': prompt
            }]
        )
        
        # Extract the response content
        response_text = response['message']['content']
        
        # Clean the JSON string
        cleaned_json = clean_json_string(response_text)
        
        # Parse JSON
        flashcard_data = json.loads(cleaned_json)
        
        # Validate required fields
        required_fields = ['sentence', 'translation', 'definition']
        if not all(field in flashcard_data for field in required_fields):
            raise ValueError(f"Brakujące pola w odpowiedzi dla słowa '{word}'")
        
        return flashcard_data
        
    except json.JSONDecodeError as e:
        print(f"Błąd parsowania JSON dla słowa '{word}': {e}")
        print(f"Odpowiedź modelu: {response_text[:200]}")
        return None
    except Exception as e:
        print(f"Błąd podczas generowania fiszki dla '{word}': {e}")
        return None


def extract_word_from_cloze(sentence: str) -> str:
    """
    Extract the word from a Cloze deletion format.
    
    Args:
        sentence: Sentence with Cloze format {{c1::word}}
        
    Returns:
        Extracted word
    """
    match = re.search(r'\{\{c1::([^}]+)\}\}', sentence)
    if match:
        return match.group(1)
    return ""


def save_to_csv(flashcards: List[Dict[str, str]], output_file: str):
    """
    Save flashcards to CSV file for Anki import.
    
    Args:
        flashcards: List of flashcard dictionaries
        output_file: Path to output CSV file
    """
    try:
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            
            # Write header (matching Anki note type fields)
            writer.writerow(['Text', 'Translation', 'Definition', 'Word'])
            
            # Write flashcard data
            for card in flashcards:
                word = extract_word_from_cloze(card['sentence'])
                writer.writerow([
                    card['sentence'],
                    card['translation'],
                    card['definition'],
                    word
                ])
        
        print(f"\nPomyślnie zapisano {len(flashcards)} fiszek do pliku '{output_file}'")
        print(f"Możesz teraz zaimportować ten plik do Anki.")
        
    except Exception as e:
        print(f"Błąd podczas zapisywania do CSV: {e}")


def main():
    """Main function to orchestrate flashcard generation."""
    print("=" * 60)
    print("FCE Anki Local Generator - Generator fiszek z Ollama")
    print("=" * 60)
    
    input_file = 'slowka.txt'
    output_file = 'import_to_anki.csv'
    
    # Read words from file
    print(f"\nOdczytywanie słów z pliku '{input_file}'...")
    words = read_words_from_file(input_file)
    
    if not words:
        print("Brak słów do przetworzenia. Kończenie programu.")
        return
    
    print(f"Znaleziono {len(words)} słów do przetworzenia.")
    
    # Check if Ollama is available
    try:
        print("\nSprawdzanie połączenia z Ollama...")
        ollama.list()
        print("✓ Połączenie z Ollama nawiązane")
    except Exception as e:
        print(f"✗ Błąd połączenia z Ollama: {e}")
        print("Upewnij się, że Ollama jest uruchomiona i model llama3 jest dostępny.")
        print("Uruchom: ollama run llama3")
        return
    
    # Generate flashcards
    flashcards = []
    print(f"\nGenerowanie fiszek...")
    
    for i, word in enumerate(words, 1):
        print(f"\n[{i}/{len(words)}] Przetwarzanie: '{word}'")
        flashcard = generate_flashcard(word)
        
        if flashcard:
            flashcards.append(flashcard)
            print(f"  ✓ Wygenerowano fiszkę")
        else:
            print(f"  ✗ Nie udało się wygenerować fiszki")
    
    # Save to CSV
    if flashcards:
        print("\n" + "=" * 60)
        save_to_csv(flashcards, output_file)
        print("=" * 60)
    else:
        print("\nNie wygenerowano żadnych fiszek. Sprawdź błędy powyżej.")


if __name__ == "__main__":
    main()
