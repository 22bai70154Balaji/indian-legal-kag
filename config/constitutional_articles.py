# """
# Simple Constitutional Articles - GUARANTEED TO WORK
# All 395 articles loaded without external dependencies
# """

# def create_all_articles():
#     """Create all 395 constitutional articles - no external files needed"""
    
#     articles = {}
    
#     # Key articles with real content
#     important_articles = {
#         1: ("Name and territory of the Union", "India, that is Bharat, shall be a Union of States."),
#         12: ("Definition", "In this part, the State includes the Government and Parliament of India."),
#         14: ("Equality before law", "The State shall not deny to any person equality before the law."),
#         19: ("Freedom of speech etc.", "All citizens shall have the right to freedom of speech and expression."),
#         21: ("Protection of life and personal liberty", "No person shall be deprived of his life or personal liberty except according to procedure established by law."),
#         32: ("Right to constitutional remedies", "The right to move the Supreme Court is guaranteed."),
#         243: ("Definitions - Panchayats", "In this Part, Gram Sabha means a body consisting of persons registered in electoral rolls."),
#         356: ("President's rule", "If the President is satisfied that government of State cannot be carried on, he may assume functions."),
#         368: ("Power to amend Constitution", "Parliament may amend by way of addition, variation or repeal any provision.")
#     }
    
#     # Create all 395 articles
#     for i in range(1, 396):
#         article_key = f"article_{i}"
        
#         if i in important_articles:
#             title, text = important_articles[i]
#         else:
#             title = f"Article {i}"
#             text = f"Constitutional provision {i}"
        
#         # Determine part
#         if 1 <= i <= 4:
#             part = "I"
#         elif 5 <= i <= 11:
#             part = "II"  
#         elif 12 <= i <= 35:
#             part = "III"
#         elif 36 <= i <= 51:
#             part = "IV"
#         elif 52 <= i <= 151:
#             part = "V"
#         elif 152 <= i <= 237:
#             part = "VI"
#         else:
#             part = "Other"
            
#         # Determine chapter
#         if 12 <= i <= 35:
#             chapter = "Fundamental Rights"
#         elif 36 <= i <= 51:
#             chapter = "Directive Principles"
#         else:
#             chapter = "Constitutional Provisions"
        
#         articles[article_key] = {
#             "number": i,
#             "title": title,
#             "text": text,
#             "part": part,
#             "chapter": chapter,
#             "privacy_implications": i in [14, 19, 21, 32],
#             "dpdpa_relevance": "critical" if i == 21 else "low",
#             "fundamental_right": 12 <= i <= 35,
#             "directive_principle": 36 <= i <= 51,
#             "constitutional_significance": "landmark" if i in [14, 19, 21, 32, 368] else "important",
#             "landmark_cases": [],
#             "privacy_scope": []
#         }
    
#     return articles

# # Load all articles
# CONSTITUTIONAL_ARTICLES = create_all_articles()

# # Basic landmark cases
# LANDMARK_CASES = {
#     "kesavananda_bharati": {
#         "name": "Kesavananda Bharati v. State of Kerala",
#         "year": 1973,
#         "significance": "Basic Structure Doctrine",
#         "articles_interpreted": [368]
#     },
#     "maneka_gandhi": {
#         "name": "Maneka Gandhi v. Union of India", 
#         "year": 1978,
#         "significance": "Expanded Article 21",
#         "articles_interpreted": [21]
#     },
#     "puttaswamy": {
#         "name": "Justice K.S. Puttaswamy v. Union of India",
#         "year": 2017, 
#         "significance": "Right to Privacy",
#         "articles_interpreted": [21]
#     }
# }

# # Basic DPDPA provisions
# DPDPA_PROVISIONS = {
#     "section_3": {
#         "title": "Applicability of Act",
#         "constitutional_basis": ["article_21"]
#     },
#     "section_5": {
#         "title": "Grounds for processing personal data", 
#         "constitutional_basis": ["article_21"]
#     }
# }

# print(f"✅ LOADED: {len(CONSTITUTIONAL_ARTICLES)} Constitutional Articles")
# print(f"✅ LOADED: {len(LANDMARK_CASES)} Landmark Cases") 
# print(f"✅ LOADED: {len(DPDPA_PROVISIONS)} DPDPA Provisions")
# print("🎉 Your Indian Legal KAG System is Ready!")


# """
# Constitutional Articles - Complete with Real Text from Indian Constitution
# Data source: GitHub - Yash-Handa/The_Constitution_Of_India
# """

# import json
# import os
# from typing import Dict, List


# def load_constitution_from_json(json_path: str = "COI.json") -> List[Dict]:
#     """Load constitution from downloaded JSON file"""
#     if not os.path.exists(json_path):
#         raise FileNotFoundError(
#             f"❌ {json_path} not found. Download it using:\n"
#             "curl -o COI.json https://raw.githubusercontent.com/Yash-Handa/The_Constitution_Of_India/master/COI.json"
#         )
    
#     with open(json_path, 'r', encoding='utf-8') as f:
#         coi_data = json.load(f)
    
#     # COI.json structure: [articles_array, parts_array, schedules_array]
#     return coi_data[0]  # Return articles array


# def extract_article_text(article: Dict) -> str:
#     """Extract full text from article object with clauses and subclauses"""
#     text_parts = []
    
#     # Add article description if present
#     if article.get("ArtDesc"):
#         text_parts.append(article["ArtDesc"])
    
#     # Add clauses if present
#     if article.get("Clauses"):
#         for clause in article["Clauses"]:
#             if clause.get("Status") == "Omitted":
#                 continue
                
#             clause_text = f"({clause['ClauseNo']}) {clause['ClauseDesc']}"
            
#             # Add sub-clauses if present
#             if clause.get("SubClauses"):
#                 for sub_clause in clause["SubClauses"]:
#                     if sub_clause.get("Status") != "Omitted":
#                         clause_text += f" ({sub_clause['SubClauseNo']}) {sub_clause['SubClauseDesc']}"
            
#             # Add follow-up text if present
#             if clause.get("FollowUp"):
#                 clause_text += f" {clause['FollowUp']}"
            
#             text_parts.append(clause_text)
    
#     # Add explanations if present
#     if article.get("Explanations"):
#         for explanation in article["Explanations"]:
#             text_parts.append(f"Explanation {explanation['ExplanationNo']}: {explanation['Explanation']}")
    
#     return " ".join(text_parts).strip()


# def determine_part(article_num: int) -> str:
#     """Determine constitutional part based on article number"""
#     part_ranges = {
#         "I": (1, 4), "II": (5, 11), "III": (12, 35), "IV": (36, 51),
#         "IVA": (51, 51), "V": (52, 151), "VI": (152, 237),
#         "VII": (238, 238), "VIII": (239, 242), "IX": (243, 243),
#         "IXA": (243, 243), "IXB": (243, 243), "X": (244, 244),
#         "XI": (245, 263), "XII": (264, 300), "XIII": (301, 307),
#         "XIV": (308, 323), "XIVA": (323, 323), "XV": (324, 329),
#         "XVI": (330, 342), "XVII": (343, 351), "XVIII": (352, 360),
#         "XIX": (361, 367), "XX": (368, 368), "XXI": (369, 392),
#         "XXII": (393, 395)
#     }
    
#     for part, (start, end) in part_ranges.items():
#         if start <= article_num <= end:
#             return part
#     return "Other"


# def create_all_articles(json_path: str = "COI.json") -> Dict:
#     """Create all constitutional articles with real text from COI.json"""
    
#     # Load constitution data
#     raw_articles = load_constitution_from_json(json_path)
    
#     articles = {}
#     article_count = 0
#     omitted_count = 0
    
#     for raw_article in raw_articles:
#         # Skip preamble (ArtNo: 0)
#         art_no = raw_article.get("ArtNo", "")
#         if art_no == "0" or not art_no:
#             continue
        
#         # Handle omitted articles
#         is_omitted = raw_article.get("Status") == "Omitted"
        
#         # Extract article number (handle cases like "31A", "31B", "21A")
#         try:
#             numeric_part = ''.join(filter(str.isdigit, art_no))
#             if not numeric_part:
#                 continue
#             article_num = int(numeric_part)
#         except:
#             continue
        
#         if article_num < 1 or article_num > 395:
#             continue
        
#         article_key = f"article_{article_num}"
        
#         # Extract full text with all clauses and subclauses
#         if is_omitted:
#             article_text = f"[Omitted by the Constitution]"
#             omitted_count += 1
#         else:
#             article_text = extract_article_text(raw_article)
#             if not article_text:
#                 article_text = f"Article {article_num} text not available"
        
#         article_title = raw_article.get("Name", f"Article {article_num}")
        
#         # Determine chapter and significance
#         if 12 <= article_num <= 35:
#             chapter = "Fundamental Rights"
#             subheading = raw_article.get("SubHeading", "Fundamental Rights")
#         elif 36 <= article_num <= 51:
#             chapter = "Directive Principles"
#             subheading = "Directive Principles of State Policy"
#         else:
#             chapter = "Constitutional Provisions"
#             subheading = raw_article.get("SubHeading", "")
        
#         # Privacy and DPDPA relevance
#         privacy_articles = [14, 19, 21, 32]
#         landmark_articles = [14, 19, 21, 32, 243, 356, 368]
        
#         articles[article_key] = {
#             "number": article_num,
#             "article_no": art_no,  # Original article number (e.g., "31A")
#             "title": article_title,
#             "text": article_text,
#             "part": determine_part(article_num),
#             "chapter": chapter,
#             "subheading": subheading,
#             "privacy_implications": article_num in privacy_articles,
#             "dpdpa_relevance": "critical" if article_num == 21 else ("moderate" if article_num in privacy_articles else "low"),
#             "fundamental_right": 12 <= article_num <= 35 and not is_omitted,
#             "directive_principle": 36 <= article_num <= 51,
#             "constitutional_significance": "landmark" if article_num in landmark_articles else "important",
#             "status": "Omitted" if is_omitted else "Active",
#             "landmark_cases": [],
#             "privacy_scope": []
#         }
        
#         article_count += 1
    
#     print(f"\n✅ Successfully created {article_count} articles")
#     print(f"   - Active articles: {article_count - omitted_count}")
#     print(f"   - Omitted articles: {omitted_count}")
#     return articles


# # Load all articles when module is imported
# try:
#     CONSTITUTIONAL_ARTICLES = create_all_articles()
#     print(f"✅ LOADED: {len(CONSTITUTIONAL_ARTICLES)} Constitutional Articles with REAL text")
    
#     # Show sample articles to verify
#     print("\n📋 Sample Articles (verifying real content):")
#     for art_key in ["article_1", "article_21", "article_14"]:
#         if art_key in CONSTITUTIONAL_ARTICLES:
#             art = CONSTITUTIONAL_ARTICLES[art_key]
#             print(f"\n{art['article_no']}. {art['title']}")
#             print(f"   Status: {art['status']}")
#             print(f"   Text preview: {art['text'][:120]}...")
            
# except FileNotFoundError as e:
#     print(str(e))
#     print("\n⚠️  Creating empty dictionary for now...")
#     CONSTITUTIONAL_ARTICLES = {}
# except Exception as e:
#     print(f"❌ Error loading articles: {str(e)}")
#     CONSTITUTIONAL_ARTICLES = {}


# # Landmark cases
# LANDMARK_CASES = {
#     "kesavananda_bharati": {
#         "name": "Kesavananda Bharati v. State of Kerala",
#         "year": 1973,
#         "significance": "Basic Structure Doctrine",
#         "articles_interpreted": [368]
#     },
#     "maneka_gandhi": {
#         "name": "Maneka Gandhi v. Union of India",
#         "year": 1978,
#         "significance": "Expanded Article 21",
#         "articles_interpreted": [21]
#     },
#     "puttaswamy": {
#         "name": "Justice K.S. Puttaswamy v. Union of India",
#         "year": 2017,
#         "significance": "Right to Privacy",
#         "articles_interpreted": [21]
#     }
# }


# # DPDPA provisions
# DPDPA_PROVISIONS = {
#     "section_3": {
#         "title": "Applicability of Act",
#         "constitutional_basis": ["article_21"]
#     },
#     "section_5": {
#         "title": "Grounds for processing personal data",
#         "constitutional_basis": ["article_21"]
#     }
# }


# if CONSTITUTIONAL_ARTICLES:
#     print(f"✅ LOADED: {len(LANDMARK_CASES)} Landmark Cases")
#     print(f"✅ LOADED: {len(DPDPA_PROVISIONS)} DPDPA Provisions")
#     print("\n🎉 Your Indian Legal KAG System is Ready with REAL Constitutional Text!\n")

# """
# Constitutional Articles - ALL 395 Articles with Real Text
# Data source: GitHub - civictech-India/constitution-of-india
# """

# import json
# import os
# from typing import Dict, List


# def load_constitution_from_json(json_path: str = "constitution_complete.json") -> List[Dict]:
#     """Load complete constitution from civictech-India JSON"""
#     if not os.path.exists(json_path):
#         raise FileNotFoundError(
#             f"❌ {json_path} not found. Download using:\n"
#             "curl -o constitution_complete.json https://raw.githubusercontent.com/civictech-India/constitution-of-india/main/constitution_of_india.json"
#         )
    
#     with open(json_path, 'r', encoding='utf-8') as f:
#         data = json.load(f)
    
#     # This JSON is a simple array of article objects
#     return data


# def determine_part(article_num: int) -> str:
#     """Determine constitutional part"""
#     part_ranges = {
#         "I": (1, 4), "II": (5, 11), "III": (12, 35), "IV": (36, 51),
#         "V": (52, 151), "VI": (152, 237), "VIII": (239, 242),
#         "IX": (243, 243), "X": (244, 244), "XI": (245, 263),
#         "XII": (264, 300), "XIII": (301, 307), "XIV": (308, 323),
#         "XV": (324, 329), "XVI": (330, 342), "XVII": (343, 351),
#         "XVIII": (352, 360), "XIX": (361, 367), "XX": (368, 368),
#         "XXI": (369, 392), "XXII": (393, 395)
#     }
#     for part, (start, end) in part_ranges.items():
#         if start <= article_num <= end:
#             return part
#     return "Other"


# def create_all_articles(json_path: str = "constitution_complete.json") -> Dict:
#     """Create all 395 constitutional articles from complete dataset"""
#     raw_articles = load_constitution_from_json(json_path)
    
#     articles = {}
#     article_count = 0
#     omitted_count = 0
    
#     for raw_article in raw_articles:
#         art_no = raw_article.get("article")
        
#         # Skip preamble (article 0)
#         if art_no == 0:
#             continue
        
#         # Handle article numbers (int or string like "21A")
#         if isinstance(art_no, str):
#             try:
#                 numeric_part = ''.join(filter(str.isdigit, art_no))
#                 article_num = int(numeric_part) if numeric_part else 0
#             except:
#                 continue
#         else:
#             article_num = art_no
        
#         if article_num < 1 or article_num > 395:
#             continue
        
#         article_key = f"article_{article_num}"
#         article_title = raw_article.get("title", f"Article {article_num}")
#         article_text = raw_article.get("description", "")
        
#         # Check if omitted/repealed
#         is_omitted = "Rep." in article_text or "Omitted" in article_text or "[" in article_title[:10]
#         if is_omitted:
#             omitted_count += 1
        
#         # Determine chapter
#         if 12 <= article_num <= 35:
#             chapter = "Fundamental Rights"
#         elif 36 <= article_num <= 51:
#             chapter = "Directive Principles"
#         elif 52 <= article_num <= 151:
#             chapter = "The Union"
#         elif 152 <= article_num <= 237:
#             chapter = "The States"
#         elif 243 <= article_num <= 243:
#             chapter = "Panchayats and Municipalities"
#         elif 245 <= article_num <= 263:
#             chapter = "Relations between Union and States"
#         elif 352 <= article_num <= 360:
#             chapter = "Emergency Provisions"
#         elif 368 == article_num:
#             chapter = "Amendment of Constitution"
#         else:
#             chapter = "Constitutional Provisions"
        
#         privacy_articles = [14, 19, 21, 32]
#         landmark_articles = [14, 19, 21, 32, 243, 356, 368]
        
#         articles[article_key] = {
#             "number": article_num,
#             "article_no": str(art_no),
#             "title": article_title,
#             "text": article_text,
#             "part": determine_part(article_num),
#             "chapter": chapter,
#             "privacy_implications": article_num in privacy_articles,
#             "dpdpa_relevance": "critical" if article_num == 21 else ("moderate" if article_num in privacy_articles else "low"),
#             "fundamental_right": 12 <= article_num <= 35 and not is_omitted,
#             "directive_principle": 36 <= article_num <= 51,
#             "constitutional_significance": "landmark" if article_num in landmark_articles else "important",
#             "status": "Omitted" if is_omitted else "Active",
#             "landmark_cases": [],
#             "privacy_scope": []
#         }
#         article_count += 1
    
#     print(f"\n✅ Successfully created {article_count} articles")
#     print(f"   - Active articles: {article_count - omitted_count}")
#     print(f"   - Omitted articles: {omitted_count}")
#     return articles


# # Load all articles
# try:
#     CONSTITUTIONAL_ARTICLES = create_all_articles()
#     print(f"✅ LOADED: {len(CONSTITUTIONAL_ARTICLES)} Constitutional Articles with REAL text")
#     print("\n📋 Sample Articles:")
#     for art_key in ["article_1", "article_21", "article_243", "article_368"]:
#         if art_key in CONSTITUTIONAL_ARTICLES:
#             art = CONSTITUTIONAL_ARTICLES[art_key]
#             print(f"\n{art['article_no']}. {art['title']}")
#             print(f"   Status: {art['status']}")
#             print(f"   Text: {art['text'][:100]}...")
# except FileNotFoundError as e:
#     print(str(e))
#     CONSTITUTIONAL_ARTICLES = {}
# except Exception as e:
#     print(f"❌ Error: {str(e)}")
#     CONSTITUTIONAL_ARTICLES = {}

# LANDMARK_CASES = {
#     "kesavananda_bharati": {"name": "Kesavananda Bharati v. State of Kerala", "year": 1973, "articles_interpreted": [368]},
#     "maneka_gandhi": {"name": "Maneka Gandhi v. Union of India", "year": 1978, "articles_interpreted": [21]},
#     "puttaswamy": {"name": "Justice K.S. Puttaswamy v. Union of India", "year": 2017, "articles_interpreted": [21]}
# }

# DPDPA_PROVISIONS = {
#     "section_3": {"title": "Applicability of Act", "constitutional_basis": ["article_21"]},
#     "section_5": {"title": "Grounds for processing personal data", "constitutional_basis": ["article_21"]}
# }

# if CONSTITUTIONAL_ARTICLES:
#     print(f"✅ LOADED: {len(LANDMARK_CASES)} Landmark Cases")
#     print(f"✅ LOADED: {len(DPDPA_PROVISIONS)} DPDPA Provisions")
#     print("\n🎉 C-KAG System Ready with ALL 395 Constitutional Articles!\n")


"""
Constitutional Articles - ALL 395+ Articles with Real Text
Data source: GitHub - civictech-India/constitution-of-india
Properly handles article variants (21A, 31A, 243A-243ZG, etc.)
"""

import json
import os
from typing import Dict, List


def load_constitution_from_json(json_path: str = "constitution_complete.json") -> List[Dict]:
    """Load complete constitution from civictech-India JSON"""
    if not os.path.exists(json_path):
        raise FileNotFoundError(
            f"❌ {json_path} not found. Download using:\n"
            "curl -o constitution_complete.json https://raw.githubusercontent.com/civictech-India/constitution-of-india/main/constitution_of_india.json"
        )
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    return data


def determine_part(article_num: int) -> str:
    """Determine constitutional part based on article number"""
    part_ranges = {
        "I": (1, 4), "II": (5, 11), "III": (12, 35), "IV": (36, 51),
        "V": (52, 151), "VI": (152, 237), "VIII": (239, 242),
        "IX": (243, 243), "X": (244, 244), "XI": (245, 263),
        "XII": (264, 300), "XIII": (301, 307), "XIV": (308, 323),
        "XV": (324, 329), "XVI": (330, 342), "XVII": (343, 351),
        "XVIII": (352, 360), "XIX": (361, 367), "XX": (368, 368),
        "XXI": (369, 392), "XXII": (393, 395)
    }
    for part, (start, end) in part_ranges.items():
        if start <= article_num <= end:
            return part
    return "Other"


def normalize_article_number(art_no) -> tuple:
    """
    Normalize article number to extract numeric part and preserve original format
    Returns: (article_key, numeric_part, original_article_no)
    Example: "21A" -> ("article_21A", 21, "21A")
    Example: 368 -> ("article_368", 368, 368)
    """
    if isinstance(art_no, str):
        # Extract numeric part for sorting/comparison
        numeric_part = ''.join(filter(str.isdigit, art_no))
        article_num = int(numeric_part) if numeric_part else 0
        article_key = f"article_{art_no}"  # Preserve original (21A, 31A, etc)
    else:
        # Integer article number
        article_num = art_no
        article_key = f"article_{art_no}"
    
    return article_key, article_num, art_no


def create_all_articles(json_path: str = "constitution_complete.json") -> Dict:
    """Create all 395+ constitutional articles from complete dataset"""
    raw_articles = load_constitution_from_json(json_path)
    
    articles = {}
    article_count = 0
    omitted_count = 0
    
    for raw_article in raw_articles:
        art_no = raw_article.get("article")
        
        # Skip preamble (article 0)
        if art_no == 0:
            continue
        
        # Normalize article number (handles both int and string formats)
        article_key, article_num, original_art_no = normalize_article_number(art_no)
        
        # Only process articles 1-395
        if article_num < 1 or article_num > 395:
            continue
        
        article_title = raw_article.get("title", f"Article {art_no}")
        article_text = raw_article.get("description", "")
        
        # Check if omitted/repealed (look for "Rep." or "Omitted" in the text)
        is_omitted = ("Rep." in article_text or 
                     "Omitted" in article_text or 
                     "repealed" in article_text.lower())
        
        if is_omitted:
            omitted_count += 1
        
        # Determine chapter based on article number
        if 12 <= article_num <= 35:
            chapter = "Fundamental Rights"
        elif 36 <= article_num <= 51:
            chapter = "Directive Principles"
        elif 52 <= article_num <= 151:
            chapter = "The Union"
        elif 152 <= article_num <= 237:
            chapter = "The States"
        elif 243 <= article_num <= 243:
            chapter = "Panchayats and Municipalities"
        elif 245 <= article_num <= 263:
            chapter = "Relations between Union and States"
        elif 264 <= article_num <= 300:
            chapter = "Finance, Property, Contracts"
        elif 301 <= article_num <= 307:
            chapter = "Trade, Commerce"
        elif 308 <= article_num <= 323:
            chapter = "Services"
        elif 324 <= article_num <= 329:
            chapter = "Elections"
        elif 330 <= article_num <= 342:
            chapter = "Special Provisions"
        elif 343 <= article_num <= 351:
            chapter = "Official Language"
        elif 352 <= article_num <= 360:
            chapter = "Emergency Provisions"
        elif 361 <= article_num <= 367:
            chapter = "Miscellaneous"
        elif article_num == 368:
            chapter = "Amendment of Constitution"
        elif 369 <= article_num <= 392:
            chapter = "Temporary, Transitional"
        elif 393 <= article_num <= 395:
            chapter = "Short title, Commencement"
        else:
            chapter = "Constitutional Provisions"
        
        # Mark privacy-critical and landmark articles
        privacy_articles = [14, 19, 21, 32]
        landmark_articles = [14, 19, 21, 32, 243, 356, 368]
        
        articles[article_key] = {
            "number": article_num,
            "article_no": str(original_art_no),  # Keep original format (21A, 31A, etc)
            "title": article_title,
            "text": article_text,
            "part": determine_part(article_num),
            "chapter": chapter,
            "privacy_implications": article_num in privacy_articles,
            "dpdpa_relevance": "critical" if article_num == 21 else ("moderate" if article_num in privacy_articles else "low"),
            "fundamental_right": 12 <= article_num <= 35 and not is_omitted,
            "directive_principle": 36 <= article_num <= 51,
            "constitutional_significance": "landmark" if article_num in landmark_articles else "important",
            "status": "Omitted" if is_omitted else "Active",
            "landmark_cases": [],
            "privacy_scope": []
        }
        
        article_count += 1
    
    print(f"\n✅ Successfully created {article_count} articles")
    print(f"   - Active articles: {article_count - omitted_count}")
    print(f"   - Omitted articles: {omitted_count}")
    return articles


# Load all articles when module is imported
try:
    CONSTITUTIONAL_ARTICLES = create_all_articles()
    print(f"✅ LOADED: {len(CONSTITUTIONAL_ARTICLES)} Constitutional Articles with REAL text")
    
    # Show sample articles to verify
    print("\n📋 Sample Articles (verifying real content):")
    
    sample_articles = [
        ("article_1", "Article 1: Union Territory"),
        ("article_21", "Article 21: Right to Life"),
        ("article_21A", "Article 21A: Right to Education"),
        ("article_243", "Article 243: Panchayats"),
        ("article_368", "Article 368: Amendment Power")
    ]
    
    for art_key, label in sample_articles:
        if art_key in CONSTITUTIONAL_ARTICLES:
            art = CONSTITUTIONAL_ARTICLES[art_key]
            print(f"\n{label}")
            print(f"   Status: {art['status']}")
            print(f"   Text: {art['text'][:120]}...")
        else:
            print(f"\n{label} - NOT FOUND")
            
except FileNotFoundError as e:
    print(str(e))
    print("\n⚠️  Creating empty dictionary...")
    CONSTITUTIONAL_ARTICLES = {}
except Exception as e:
    print(f"❌ Error loading articles: {str(e)}")
    import traceback
    traceback.print_exc()
    CONSTITUTIONAL_ARTICLES = {}


# Landmark cases
LANDMARK_CASES = {
    "kesavananda_bharati": {
        "name": "Kesavananda Bharati v. State of Kerala",
        "year": 1973,
        "significance": "Basic Structure Doctrine",
        "articles_interpreted": [368]
    },
    "maneka_gandhi": {
        "name": "Maneka Gandhi v. Union of India",
        "year": 1978,
        "significance": "Expanded Article 21",
        "articles_interpreted": [21]
    },
    "puttaswamy": {
        "name": "Justice K.S. Puttaswamy v. Union of India",
        "year": 2017,
        "significance": "Right to Privacy",
        "articles_interpreted": [21]
    }
}


# DPDPA provisions
DPDPA_PROVISIONS = {
    "section_3": {
        "title": "Applicability of Act",
        "constitutional_basis": ["article_21"]
    },
    "section_5": {
        "title": "Grounds for processing personal data",
        "constitutional_basis": ["article_21"]
    }
}


if CONSTITUTIONAL_ARTICLES:
    print(f"✅ LOADED: {len(LANDMARK_CASES)} Landmark Cases")
    print(f"✅ LOADED: {len(DPDPA_PROVISIONS)} DPDPA Provisions")
    print("\n🎉 C-KAG System Ready with ALL 395+ Constitutional Articles!\n")
