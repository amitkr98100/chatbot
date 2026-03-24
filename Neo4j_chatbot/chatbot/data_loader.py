from db.neo4j_conn import Neo4jConnection


def load_data():
    conn = Neo4jConnection()

    # 1️⃣ Delete old data
    conn.run_query("MATCH (n) DETACH DELETE n")

    # 2️⃣ Create nodes
    conn.run_query("MERGE (:Person {name: 'Amit'})")
    conn.run_query("MERGE (:Person {name: 'Rahul'})")
    conn.run_query("MERGE (:Person {name: 'Priya'})")
    conn.run_query("MERGE (:Person {name: 'Sneha'})")

    conn.run_query("MERGE (:Company {name: 'Google'})")
    conn.run_query("MERGE (:Company {name: 'Microsoft'})")

    conn.run_query("MERGE (:City {name: 'Delhi'})")
    conn.run_query("MERGE (:City {name: 'Mumbai'})")

    conn.run_query("MERGE (:College {name: 'IIT Delhi'})")
    conn.run_query("MERGE (:College {name: 'Delhi University'})")

    # 3️⃣ Create relationships
    conn.run_query("""
    MATCH (a:Person {name:'Amit'}), (b:Person {name:'Rahul'})
    MERGE (a)-[:FRIEND]->(b)
    """)

    conn.run_query("""
    MATCH (a:Person {name:'Rahul'}), (b:Person {name:'Priya'})
    MERGE (a)-[:FRIEND]->(b)
    """)

    conn.run_query("""
    MATCH (a:Person {name:'Priya'}), (b:Person {name:'Sneha'})
    MERGE (a)-[:FRIEND]->(b)
    """)

    conn.run_query("""
    MATCH (a:Person {name:'Amit'}), (c:Company {name:'Google'})
    MERGE (a)-[:WORKS_AT]->(c)
    """)

    conn.run_query("""
    MATCH (a:Person {name:'Rahul'}), (c:Company {name:'Microsoft'})
    MERGE (a)-[:WORKS_AT]->(c)
    """)

    conn.run_query("""
    MATCH (a:Person {name:'Priya'}), (c:Company {name:'Google'})
    MERGE (a)-[:WORKS_AT]->(c)
    """)

    conn.run_query("""
    MATCH (a:Person {name:'Amit'}), (c:City {name:'Delhi'})
    MERGE (a)-[:LIVES_IN]->(c)
    """)

    conn.run_query("""
    MATCH (a:Person {name:'Rahul'}), (c:City {name:'Mumbai'})
    MERGE (a)-[:LIVES_IN]->(c)
    """)

    conn.run_query("""
    MATCH (a:Person {name:'Priya'}), (c:City {name:'Delhi'})
    MERGE (a)-[:LIVES_IN]->(c)
    """)

    conn.run_query("""
    MATCH (a:Person {name:'Sneha'}), (c:City {name:'Mumbai'})
    MERGE (a)-[:LIVES_IN]->(c)
    """)

    conn.run_query("""
    MATCH (a:Person {name:'Amit'}), (c:College {name:'IIT Delhi'})
    MERGE (a)-[:STUDIED_AT]->(c)
    """)

    conn.run_query("""
    MATCH (a:Person {name:'Rahul'}), (c:College {name:'Delhi University'})
    MERGE (a)-[:STUDIED_AT]->(c)
    """)

    conn.run_query("""
    MATCH (a:Person {name:'Priya'}), (c:College {name:'IIT Delhi'})
    MERGE (a)-[:STUDIED_AT]->(c)
    """)

    conn.close()

    print("✅ Data Loaded Successfully")