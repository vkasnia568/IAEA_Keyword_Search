"""
IAEA Document Keyword Search
Simple Python Project for SGIM Internship Application
No external libraries required - Pure Python
"""

import os
import re
from pathlib import Path

# -------------------------------------------------
# 1. Read all documents from folder
# -------------------------------------------------
def load_documents(folder_path):
    """Load all .txt files from documents folder"""
    documents = {}
    folder = Path(folder_path)
    
    for file_path in folder.glob("*.txt"):
        with open(file_path, 'r', encoding='utf-8') as f:
            documents[file_path.name] = f.read()
    
    return documents

# -------------------------------------------------
# 2. Simple Keyword Search Algorithm
# -------------------------------------------------
def keyword_search(query, documents):
    """
    Search for query keywords in documents
    Returns ranked results based on keyword frequency
    """
    # Clean and split query into keywords
    query_keywords = query.lower().split()
    
    results = []
    
    for doc_name, doc_content in documents.items():
        doc_lower = doc_content.lower()
        
        # Count how many times each keyword appears
        total_matches = 0
        keyword_matches = {}
        
        for keyword in query_keywords:
            count = doc_lower.count(keyword)
            if count > 0:
                total_matches += count
                keyword_matches[keyword] = count
        
        if total_matches > 0:
            results.append({
                'document': doc_name,
                'total_matches': total_matches,
                'keyword_details': keyword_matches,
                'preview': doc_content[:200] + "..."
            })
    
    # Sort by total matches (highest first)
    results.sort(key=lambda x: x['total_matches'], reverse=True)
    
    return results

# -------------------------------------------------
# 3. Simple Relevance Score (0 to 100%)
# -------------------------------------------------
def calculate_relevance(match_count, max_possible):
    """Convert match count to percentage score"""
    if max_possible == 0:
        return 0
    return min(100, int((match_count / max_possible) * 100))

# -------------------------------------------------
# 4. Extract Key Terms (Simplified NER)
# -------------------------------------------------
def extract_key_terms(text):
    """
    Extract nuclear safeguards related terms
    Simple dictionary-based approach - No ML required
    """
    safeguards_terms = {
        'countries': ['iran', 'brazil', 'argentina', 'russia', 'china', 'usa', 
                     'france', 'uk', 'india', 'pakistan', 'north korea', 'israel'],
        'materials': ['uranium', 'plutonium', 'yellowcake', 'heavy water', 'centrifuge'],
        'facilities': ['natanz', 'yongbyon', 'bushehr', 'reactor', 'enrichment'],
        'organizations': ['iaea', 'un', 'board of governors', 'safeguards']
    }
    
    text_lower = text.lower()
    found_terms = []
    
    for category, terms in safeguards_terms.items():
        for term in terms:
            if term in text_lower:
                found_terms.append({
                    'term': term.title(),
                    'category': category
                })
    
    return found_terms

# -------------------------------------------------
# 5. Main Program
# -------------------------------------------------
def main():
    print("\n" + "="*60)
    print("⚛️  IAEA DOCUMENT KEYWORD SEARCH PROTOTYPE")
    print("="*60)
    print("Built for: SGIM-State Infrastructure Analysis Section")
    print("Internship Application - Simple Python Similarity Search")
    print("="*60)
    
    # Load documents
    docs = load_documents("documents")
    
    if not docs:
        print("\n❌ Error: No documents found in 'documents/' folder!")
        print("Please create .txt files in the documents folder.")
        return
    
    print(f"\n✅ Loaded {len(docs)} documents:")
    for doc_name in docs.keys():
        print(f"   📄 {doc_name}")
    
    print("\n" + "-"*60)
    print("Type your search query (or 'quit' to exit)")
    print("Example queries: 'Iran centrifuges', 'IAEA safeguards', 'nuclear Brazil'")
    print("-"*60)
    
    while True:
        # Get user query
        query = input("\n🔍 Search Query: ").strip()
        
        if query.lower() == 'quit':
            print("\n👋 Thank you for using IAEA Document Search!")
            break
        
        if not query:
            print("⚠️  Please enter a search query.")
            continue
        
        # Perform search
        results = keyword_search(query, docs)
        
        if not results:
            print(f"\n❌ No documents found matching: '{query}'")
            continue
        
        # Display results
        print(f"\n✅ Found {len(results)} relevant document(s):")
        print("-"*60)
        
        # Find max matches for relevance calculation
        max_matches = results[0]['total_matches'] if results else 1
        
        for i, result in enumerate(results, 1):
            relevance = calculate_relevance(result['total_matches'], max_matches)
            
            print(f"\n📊 Result #{i} - {result['document']}")
            print(f"   Relevance Score: {relevance}%")
            print(f"   Keyword Matches: {result['keyword_details']}")
            print(f"   Preview: {result['preview']}")
            
            # Show extracted key terms
            key_terms = extract_key_terms(docs[result['document']])
            if key_terms:
                print(f"   🔑 Key Terms Found:")
                for term_info in key_terms[:5]:  # Show top 5
                    print(f"      • {term_info['term']} ({term_info['category']})")
        
        print("\n" + "-"*60)

# -------------------------------------------------
# Run Program
# -------------------------------------------------
if __name__ == "__main__":
    main()