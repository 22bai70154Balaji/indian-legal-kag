"""
Populate Neo4j with all 464 Constitutional Articles
Run: python run_populate.py
"""

import sys
import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

sys.path.insert(0, '.')

from config.constitutional_articles import CONSTITUTIONAL_ARTICLES

# Get credentials from .env
uri = os.getenv("NEO4J_URI", "bolt://127.0.0.1:7687")
user = os.getenv("NEO4J_USER", "neo4j")
password = os.getenv("NEO4J_PASSWORD", "12345678")

print(f"\n🔌 Connecting to Neo4j at {uri}...")
print(f"   User: {user}\n")

try:
    driver = GraphDatabase.driver(uri, auth=(user, password))
    
    # Test connection
    with driver.session() as session:
        session.run("RETURN 1")
    print("✅ Connected to Neo4j successfully!\n")
    
except Exception as e:
    print(f"❌ Failed to connect: {str(e)}")
    print(f"   Check your credentials in .env file")
    exit(1)

print("="*70)
print("NEO4J DATABASE UPDATE - CONSTITUTIONAL ARTICLES")
print("="*70 + "\n")

print(f"📊 Populating {len(CONSTITUTIONAL_ARTICLES)} articles...\n")

success = 0
errors = 0

for article_key, article_data in CONSTITUTIONAL_ARTICLES.items():
    query = """
    MERGE (a:Article {article_id: $article_id})
    SET a.number = $number,
        a.article_no = $article_no,
        a.title = $title,
        a.text = $text,
        a.part = $part,
        a.chapter = $chapter,
        a.status = $status
    RETURN a
    """
    
    params = {
        "article_id": article_key,
        "number": article_data["number"],
        "article_no": article_data["article_no"],
        "title": article_data["title"],
        "text": article_data["text"],
        "part": article_data["part"],
        "chapter": article_data["chapter"],
        "status": article_data["status"]
    }
    
    try:
        with driver.session() as session:
            session.run(query, params)
        success += 1
        if success % 50 == 0:
            print(f"✅ Processed {success} articles...")
    except Exception as e:
        errors += 1
        print(f"⚠️  Error on {article_key}: {str(e)}")

print(f"\n✅ Successfully populated {success} articles!")
if errors > 0:
    print(f"⚠️  {errors} errors occurred")

# Verify
try:
    with driver.session() as session:
        result = session.run("MATCH (a:Article) RETURN COUNT(a) as count")
        for record in result:
            count = record['count']
            print(f"📊 Total articles in Neo4j: {count}")
            
        result = session.run("MATCH (a:Article {article_no: '21'}) RETURN a.title LIMIT 1")
        for record in result:
            print(f"✅ Article 21: {record['a.title']}")
            
except Exception as e:
    print(f"Verification error: {str(e)}")

print("\n" + "="*70)
print("COMPLETE! ✅")
print("="*70 + "\n")

driver.close()
