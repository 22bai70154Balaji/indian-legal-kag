# # """
# # Neo4j Database Configuration - FIXED VERSION (No Invalid Config Keys)
# # """

# # import os
# # import logging
# # from neo4j import GraphDatabase
# # from typing import List, Dict, Any, Optional
# # import streamlit as st
# # import time

# # logger = logging.getLogger(__name__)

# # class Neo4jConnection:
# #     def __init__(self):
# #         # Force bolt:// protocol to avoid routing issues
# #         base_uri = os.getenv("NEO4J_URI", "bolt://127.0.0.1:7687")
        
# #         # Ensure we're using bolt:// protocol
# #         if base_uri.startswith("neo4j://"):
# #             self.uri = base_uri.replace("neo4j://", "bolt://")
# #             logger.info(f"🔄 Changed protocol from neo4j:// to bolt://")
# #         else:
# #             self.uri = base_uri
            
# #         self.user = os.getenv("NEO4J_USER", "neo4j")
# #         self.password = os.getenv("NEO4J_PASSWORD", "password")
# #         self.driver = None
# #         self.last_connection_time = 0
# #         self._connect()

# #     def _connect(self):
# #         """Establish connection with valid config parameters only"""
# #         try:
# #             # Close existing connection if any
# #             if self.driver:
# #                 try:
# #                     self.driver.close()
# #                 except:
# #                     pass
                    
# #             logger.info(f"🔌 (Re)connecting to Neo4j at: {self.uri}")
            
# #             # Use ONLY valid Neo4j driver parameters
# #             self.driver = GraphDatabase.driver(
# #                 self.uri,
# #                 auth=(self.user, self.password),
# #                 max_connection_lifetime=30 * 60,  # 30 minutes
# #                 max_connection_pool_size=10,
# #                 connection_acquisition_timeout=30
# #                 # Removed invalid parameters: max_retry_time, initial_retry_delay, multiplier, jitter_factor
# #             )

# #             # Test connection
# #             with self.driver.session() as session:
# #                 session.run("RETURN 1").consume()
                
# #             self.last_connection_time = time.time()
# #             logger.info("✅ Successfully (re)connected to Neo4j database")

# #         except Exception as e:
# #             logger.error(f"❌ Failed to connect to Neo4j: {str(e)}")
# #             if 'st' in dir() and hasattr(st, 'error'):
# #                 st.error(f"Database connection failed: {str(e)}")
# #             raise

# #     def _is_connection_stale(self) -> bool:
# #         """Check if connection might be stale (older than 25 minutes)"""
# #         if not self.driver or not self.last_connection_time:
# #             return True
# #         return (time.time() - self.last_connection_time) > (25 * 60)

# #     def _ensure_connection(self):
# #         """Ensure we have a healthy connection"""
# #         if self._is_connection_stale() or not self.check_health():
# #             logger.info("🔄 Connection appears stale, reconnecting...")
# #             self._connect()

# #     def execute_query(self, query: str, parameters: dict = None, max_retries: int = 3) -> List[Dict[str, Any]]:
# #         """Execute Cypher query with retry logic for stale connections"""
# #         for attempt in range(max_retries):
# #             try:
# #                 # Ensure we have a good connection
# #                 self._ensure_connection()
                
# #                 with self.driver.session() as session:
# #                     result = session.run(query, parameters or {})
# #                     return [record.data() for record in result]
                    
# #             except Exception as e:
# #                 logger.warning(f"Query attempt {attempt + 1}/{max_retries} failed: {str(e)}")
                
# #                 if attempt < max_retries - 1:
# #                     # Try to reconnect for next attempt
# #                     try:
# #                         self._connect()
# #                         time.sleep(1)  # Brief pause before retry
# #                     except Exception as reconnect_error:
# #                         logger.warning(f"Reconnection attempt failed: {str(reconnect_error)}")
# #                 else:
# #                     logger.error(f"Query failed after {max_retries} attempts: {query[:100]}...")
# #                     return []
        
# #         return []

# #     def execute_write_query(self, query: str, parameters: dict = None, max_retries: int = 3) -> bool:
# #         """Execute write query with retry logic"""
# #         for attempt in range(max_retries):
# #             try:
# #                 # Ensure we have a good connection
# #                 self._ensure_connection()
                
# #                 with self.driver.session() as session:
# #                     session.run(query, parameters or {})
# #                     return True
                    
# #             except Exception as e:
# #                 logger.warning(f"Write query attempt {attempt + 1}/{max_retries} failed: {str(e)}")
                
# #                 if attempt < max_retries - 1:
# #                     try:
# #                         self._connect()
# #                         time.sleep(1)
# #                     except:
# #                         pass
# #                 else:
# #                     logger.error(f"Write query failed after {max_retries} attempts")
# #                     return False
        
# #         return False

# #     def check_health(self) -> bool:
# #         """Check database health"""
# #         try:
# #             if not self.driver:
# #                 return False
# #             with self.driver.session() as session:
# #                 session.run("RETURN 'healthy' as status").consume()
# #             return True
# #         except:
# #             return False

# #     def close(self):
# #         """Close database connection"""
# #         if self.driver:
# #             try:
# #                 self.driver.close()
# #                 logger.info("📴 Neo4j connection closed")
# #             except:
# #                 pass
# #             finally:
# #                 self.driver = None

# # # Enhanced connection getter with error handling
# # @st.cache_resource
# # def get_neo4j_connection():
# #     """Get cached Neo4j connection with proper error handling"""
# #     try:
# #         return Neo4jConnection()
# #     except Exception as e:
# #         logger.error(f"Failed to create Neo4j connection: {str(e)}")
# #         return None  # Return None instead of raising exception

# # def refresh_neo4j_connection():
# #     """Manually refresh Neo4j connection (clears cache)"""
# #     st.cache_resource.clear()
# #     logger.info("🔄 Neo4j connection cache cleared")


# """
# Update Neo4j Database with All 464 Real Constitutional Articles
# This script loads articles from constitutional_articles.py and creates them in Neo4j
# """

# import logging
# from constitutional_articles import CONSTITUTIONAL_ARTICLES, LANDMARK_CASES, DPDPA_PROVISIONS
# # from neo4j_config import Neo4jConnection

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)


# def populate_articles_in_neo4j():
#     """Populate Neo4j with all 464 real constitutional articles"""
    
#     neo4j_conn = Neo4jConnection()
    
#     if not neo4j_conn.driver:
#         print("❌ Failed to connect to Neo4j")
#         return False
    
#     print(f"\n📊 Starting to populate Neo4j with {len(CONSTITUTIONAL_ARTICLES)} articles...")
    
#     success_count = 0
#     error_count = 0
    
#     for article_key, article_data in CONSTITUTIONAL_ARTICLES.items():
#         try:
#             # Create or update Article node
#             query = """
#             MERGE (a:Article {article_id: $article_id})
#             SET a.number = $number,
#                 a.article_no = $article_no,
#                 a.title = $title,
#                 a.text = $text,
#                 a.part = $part,
#                 a.chapter = $chapter,
#                 a.privacy_implications = $privacy_implications,
#                 a.dpdpa_relevance = $dpdpa_relevance,
#                 a.fundamental_right = $fundamental_right,
#                 a.directive_principle = $directive_principle,
#                 a.constitutional_significance = $constitutional_significance,
#                 a.status = $status,
#                 a.updated_at = datetime()
#             RETURN a
#             """
            
#             params = {
#                 "article_id": article_key,
#                 "number": article_data["number"],
#                 "article_no": article_data["article_no"],
#                 "title": article_data["title"],
#                 "text": article_data["text"],
#                 "part": article_data["part"],
#                 "chapter": article_data["chapter"],
#                 "privacy_implications": article_data["privacy_implications"],
#                 "dpdpa_relevance": article_data["dpdpa_relevance"],
#                 "fundamental_right": article_data["fundamental_right"],
#                 "directive_principle": article_data["directive_principle"],
#                 "constitutional_significance": article_data["constitutional_significance"],
#                 "status": article_data["status"]
#             }
            
#             result = neo4j_conn.execute_write_query(query, params)
            
#             if result:
#                 success_count += 1
#                 if success_count % 50 == 0:
#                     print(f"   ✅ Processed {success_count} articles...")
#             else:
#                 error_count += 1
                
#         except Exception as e:
#             error_count += 1
#             logger.warning(f"Error creating article {article_key}: {str(e)}")
    
#     print(f"\n✅ Successfully created/updated {success_count} Article nodes in Neo4j")
#     if error_count > 0:
#         print(f"⚠️  {error_count} articles had errors")
    
#     return success_count > 0


# def populate_landmark_cases_in_neo4j():
#     """Populate Neo4j with landmark cases"""
    
#     neo4j_conn = Neo4jConnection()
    
#     if not neo4j_conn.driver:
#         return False
    
#     print(f"\n📋 Adding {len(LANDMARK_CASES)} landmark cases...")
    
#     for case_key, case_data in LANDMARK_CASES.items():
#         try:
#             query = """
#             MERGE (c:LegalPrecedent {case_id: $case_id})
#             SET c.name = $name,
#                 c.year = $year,
#                 c.significance = $significance,
#                 c.updated_at = datetime()
#             RETURN c
#             """
            
#             params = {
#                 "case_id": case_key,
#                 "name": case_data["name"],
#                 "year": case_data["year"],
#                 "significance": case_data["significance"]
#             }
            
#             neo4j_conn.execute_write_query(query, params)
            
#             for article_num in case_data.get("articles_interpreted", []):
#                 article_key = f"article_{article_num}"
#                 relationship_query = """
#                 MATCH (c:LegalPrecedent {case_id: $case_id})
#                 MATCH (a:Article {article_id: $article_id})
#                 MERGE (c)-[:INTERPRETS]->(a)
#                 """
                
#                 neo4j_conn.execute_write_query(
#                     relationship_query,
#                     {"case_id": case_key, "article_id": article_key}
#                 )
            
#             print(f"   ✅ Added case: {case_data['name']}")
            
#         except Exception as e:
#             logger.warning(f"Error creating case {case_key}: {str(e)}")
    
#     return True


# def populate_dpdpa_provisions_in_neo4j():
#     """Populate Neo4j with DPDPA provisions"""
    
#     neo4j_conn = Neo4jConnection()
    
#     if not neo4j_conn.driver:
#         return False
    
#     print(f"\n📋 Adding {len(DPDPA_PROVISIONS)} DPDPA provisions...")
    
#     for provision_key, provision_data in DPDPA_PROVISIONS.items():
#         try:
#             query = """
#             MERGE (p:DPDPAProvision {provision_id: $provision_id})
#             SET p.title = $title,
#                 p.updated_at = datetime()
#             RETURN p
#             """
            
#             params = {
#                 "provision_id": provision_key,
#                 "title": provision_data["title"]
#             }
            
#             neo4j_conn.execute_write_query(query, params)
            
#             for article_ref in provision_data.get("constitutional_basis", []):
#                 if article_ref.startswith("article_"):
#                     relationship_query = """
#                     MATCH (p:DPDPAProvision {provision_id: $provision_id})
#                     MATCH (a:Article {article_id: $article_id})
#                     MERGE (p)-[:BASED_ON]->(a)
#                     """
                    
#                     neo4j_conn.execute_write_query(
#                         relationship_query,
#                         {"provision_id": provision_key, "article_id": article_ref}
#                     )
            
#             print(f"   ✅ Added provision: {provision_data['title']}")
            
#         except Exception as e:
#             logger.warning(f"Error creating provision {provision_key}: {str(e)}")
    
#     return True


# def create_article_relationships():
#     """Create relationships between related articles"""
    
#     neo4j_conn = Neo4jConnection()
    
#     if not neo4j_conn.driver:
#         return False
    
#     print(f"\n🔗 Creating article relationships...")
    
#     try:
#         query = """
#         MATCH (a1:Article), (a2:Article)
#         WHERE a1.chapter = a2.chapter 
#         AND a1.number < a2.number
#         AND ABS(a1.number - a2.number) <= 5
#         MERGE (a1)-[:RELATED_TO]->(a2)
#         """
        
#         neo4j_conn.execute_write_query(query)
        
#         query2 = """
#         MATCH (a:Article {privacy_implications: true})
#         MATCH (p:DPDPAProvision)
#         MERGE (p)-[:IMPLEMENTS]->(a)
#         """
        
#         neo4j_conn.execute_write_query(query2)
        
#         print("   ✅ Article relationships created")
#         return True
        
#     except Exception as e:
#         logger.warning(f"Error creating relationships: {str(e)}")
#         return False


# def verify_population():
#     """Verify Neo4j has been populated correctly"""
    
#     neo4j_conn = Neo4jConnection()
    
#     if not neo4j_conn.driver:
#         return False
    
#     print(f"\n✅ VERIFICATION REPORT:")
    
#     try:
#         result = neo4j_conn.execute_query("MATCH (a:Article) RETURN COUNT(a) as count")
#         if result:
#             article_count = result[0]["count"]
#             print(f"   📊 Article nodes: {article_count}")
        
#         result = neo4j_conn.execute_query("MATCH (c:LegalPrecedent) RETURN COUNT(c) as count")
#         if result:
#             case_count = result[0]["count"]
#             print(f"   📋 Landmark case nodes: {case_count}")
        
#         result = neo4j_conn.execute_query("MATCH (p:DPDPAProvision) RETURN COUNT(p) as count")
#         if result:
#             provision_count = result[0]["count"]
#             print(f"   📋 DPDPA provision nodes: {provision_count}")
        
#         result = neo4j_conn.execute_query("MATCH ()-[r]->() RETURN COUNT(r) as count")
#         if result:
#             relationship_count = result[0]["count"]
#             print(f"   🔗 Relationships: {relationship_count}")
        
#         result = neo4j_conn.execute_query("MATCH (a:Article {article_no: '21'}) RETURN a.title, a.text LIMIT 1")
#         if result:
#             print(f"\n   📌 Article 21 Verification:")
#             print(f"      Title: {result[0]['a.title']}")
#             print(f"      Text: {result[0]['a.text'][:80]}...")
        
#         print("\n🎉 Neo4j Database Successfully Updated with 464 Real Constitutional Articles!")
#         return True
        
#     except Exception as e:
#         logger.error(f"Verification failed: {str(e)}")
#         return False


# if __name__ == "__main__":
#     print("\n" + "="*70)
#     print("NEO4J DATABASE UPDATE - CONSTITUTIONAL ARTICLES")
#     print("="*70)
    
#     if populate_articles_in_neo4j():
#         print("\n✅ Articles updated successfully")
#     else:
#         print("\n❌ Failed to update articles")
    
#     if populate_landmark_cases_in_neo4j():
#         print("\n✅ Landmark cases updated successfully")
#     else:
#         print("\n❌ Failed to update landmark cases")
    
#     if populate_dpdpa_provisions_in_neo4j():
#         print("\n✅ DPDPA provisions updated successfully")
#     else:
#         print("\n❌ Failed to update DPDPA provisions")
    
#     if create_article_relationships():
#         print("\n✅ Relationships created successfully")
#     else:
#         print("\n❌ Failed to create relationships")
    
#     verify_population()
    
#     print("\n" + "="*70)
#     print("UPDATE COMPLETE")
#     print("="*70 + "\n")


"""
Neo4j Database Configuration - FIXED VERSION (No Invalid Config Keys)
"""

import os
import logging
from neo4j import GraphDatabase
from typing import List, Dict, Any, Optional
import streamlit as st
import time

logger = logging.getLogger(__name__)


class Neo4jConnection:
    def __init__(self):
        # Force bolt:// protocol to avoid routing issues
        base_uri = os.getenv("NEO4J_URI", "bolt://127.0.0.1:7687")
        
        # Ensure we're using bolt:// protocol
        if base_uri.startswith("neo4j://"):
            self.uri = base_uri.replace("neo4j://", "bolt://")
            logger.info(f"🔄 Changed protocol from neo4j:// to bolt://")
        else:
            self.uri = base_uri
            
        self.user = os.getenv("NEO4J_USER", "neo4j")
        self.password = os.getenv("NEO4J_PASSWORD", "password")
        self.driver = None
        self.last_connection_time = 0
        self._connect()


    def _connect(self):
        """Establish connection with valid config parameters only"""
        try:
            # Close existing connection if any
            if self.driver:
                try:
                    self.driver.close()
                except:
                    pass
                    
            logger.info(f"🔌 (Re)connecting to Neo4j at: {self.uri}")
            
            # Use ONLY valid Neo4j driver parameters
            self.driver = GraphDatabase.driver(
                self.uri,
                auth=(self.user, self.password),
                max_connection_lifetime=30 * 60,  # 30 minutes
                max_connection_pool_size=10,
                connection_acquisition_timeout=30
            )

            # Test connection
            with self.driver.session() as session:
                session.run("RETURN 1").consume()
                
            self.last_connection_time = time.time()
            logger.info("✅ Successfully (re)connected to Neo4j database")

        except Exception as e:
            logger.error(f"❌ Failed to connect to Neo4j: {str(e)}")
            if 'st' in dir() and hasattr(st, 'error'):
                st.error(f"Database connection failed: {str(e)}")
            raise


    def _is_connection_stale(self) -> bool:
        """Check if connection might be stale (older than 25 minutes)"""
        if not self.driver or not self.last_connection_time:
            return True
        return (time.time() - self.last_connection_time) > (25 * 60)


    def _ensure_connection(self):
        """Ensure we have a healthy connection"""
        if self._is_connection_stale() or not self.check_health():
            logger.info("🔄 Connection appears stale, reconnecting...")
            self._connect()


    def execute_query(self, query: str, parameters: dict = None, max_retries: int = 3) -> List[Dict[str, Any]]:
        """Execute Cypher query with retry logic for stale connections"""
        for attempt in range(max_retries):
            try:
                # Ensure we have a good connection
                self._ensure_connection()
                
                with self.driver.session() as session:
                    result = session.run(query, parameters or {})
                    return [record.data() for record in result]
                    
            except Exception as e:
                logger.warning(f"Query attempt {attempt + 1}/{max_retries} failed: {str(e)}")
                
                if attempt < max_retries - 1:
                    # Try to reconnect for next attempt
                    try:
                        self._connect()
                        time.sleep(1)  # Brief pause before retry
                    except Exception as reconnect_error:
                        logger.warning(f"Reconnection attempt failed: {str(reconnect_error)}")
                else:
                    logger.error(f"Query failed after {max_retries} attempts: {query[:100]}...")
                    return []
        
        return []


    def execute_write_query(self, query: str, parameters: dict = None, max_retries: int = 3) -> bool:
        """Execute write query with retry logic"""
        for attempt in range(max_retries):
            try:
                # Ensure we have a good connection
                self._ensure_connection()
                
                with self.driver.session() as session:
                    session.run(query, parameters or {})
                    return True
                    
            except Exception as e:
                logger.warning(f"Write query attempt {attempt + 1}/{max_retries} failed: {str(e)}")
                
                if attempt < max_retries - 1:
                    try:
                        self._connect()
                        time.sleep(1)
                    except:
                        pass
                else:
                    logger.error(f"Write query failed after {max_retries} attempts")
                    return False
        
        return False


    def check_health(self) -> bool:
        """Check database health"""
        try:
            if not self.driver:
                return False
            with self.driver.session() as session:
                session.run("RETURN 'healthy' as status").consume()
            return True
        except:
            return False


    def close(self):
        """Close database connection"""
        if self.driver:
            try:
                self.driver.close()
                logger.info("📴 Neo4j connection closed")
            except:
                pass
            finally:
                self.driver = None


# Enhanced connection getter with error handling
@st.cache_resource
def get_neo4j_connection():
    """Get cached Neo4j connection with proper error handling"""
    try:
        return Neo4jConnection()
    except Exception as e:
        logger.error(f"Failed to create Neo4j connection: {str(e)}")
        return None  # Return None instead of raising exception


def refresh_neo4j_connection():
    """Manually refresh Neo4j connection (clears cache)"""
    st.cache_resource.clear()
    logger.info("🔄 Neo4j connection cache cleared")
