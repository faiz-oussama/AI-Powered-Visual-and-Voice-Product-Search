from langdetect import detect, detect_langs
import json
import requests
import time
import os

file_path = 'static/formatted_products.json'
with open(file_path, 'r', encoding='utf-8') as f:
    products = json.load(f)

def translate_to_tamazight(text):
    try:
        if not text:
            return ""

        # SerpAPI search endpoint
        url = "https://serpapi.com/search.json"
        
        # Format query to specifically look for Tamazight/Berber translations
        query = f"translate {text} to Tamazight Berber"
        
        params = {
            "q": query,
            "hl": "en",
            "gl": "ma",  # Morocco location for better Tamazight results
            "api_key": "64840e2807615ab0e1bafb65bf56fb7109a148be1293400b6419aad00a228681"
        }

        response = requests.get(url, params=params)
        response.raise_for_status()
        
        result = response.json()
        
        # Try to find translation in knowledge graph or organic results
        if 'knowledge_graph' in result:
            if 'description' in result['knowledge_graph']:
                return result['knowledge_graph']['description']
                
        if 'organic_results' in result:
            for item in result['organic_results'][:3]:  # Check first 3 results
                if 'snippet' in item:
                    # Look for patterns that might indicate a translation
                    snippet = item['snippet'].lower()
                    if 'translation:' in snippet or 'in tamazight:' in snippet:
                        # Extract the part after the indicator
                        parts = snippet.split('translation:' if 'translation:' in snippet else 'in tamazight:')
                        if len(parts) > 1:
                            return parts[1].strip()
        
        return text  # Return original if no translation found

    except Exception as e:
        print(f"Translation error for text '{text}': {e}")
        return text

print(f"Starting translation of {len(products)} products...")

for i, product in enumerate(products):
    print(f"Translating product {i+1}/{len(products)}")
    
    if 'category' in product:
        product['category_tz'] = translate_to_tamazight(product['category'])
        print(f"Category: {product['category']} -> {product['category_tz']}")
    
    if 'description' in product:
        product['description_tz'] = translate_to_tamazight(product['description'])
        print(f"Description: {product['description']} -> {product['description_tz']}")
    
    # Add a delay to respect rate limits
    time.sleep(2)  # Increased delay for search queries

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print("Translation completed! File updated with Tamazight translations")