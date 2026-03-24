from db.neo4j_conn import Neo4jConnection


def run_query(query):
    conn = Neo4jConnection()
    result = conn.run_query(query)
    conn.close()
    return result


# 🔍 extract name from input
def extract_name(user_input):
    names = ["amit", "rahul", "priya"]
    for name in names:
        if name in user_input:
            return name.capitalize()
    return None


def generate_response(user_input):
    user_input = user_input.lower()
    name = extract_name(user_input)

    # 🔥 COMPLEX QUERY: friend + work
    if "friend" in user_input and "work" in user_input:
        query = f"""
        MATCH (p:Person {{name: '{name}'}})-[:FRIEND]->(f)-[:WORKS_AT]->(c)
        RETURN f.name AS person, c.name AS result
        """
        data = run_query(query)

        if data:
            return "\n".join([f"{r['person']} works at {r['result']}" for r in data])
        else:
            return "No matching data found."

    # FRIEND of specific person
    elif "friend" in user_input and name:
        query = f"""
        MATCH (p:Person {{name: '{name}'}})-[:FRIEND]->(f)
        RETURN p.name AS person, f.name AS result
        """
        data = run_query(query)

        return "\n".join([f"{r['person']} → {r['result']}" for r in data]) or "No data"

    # WORK
    elif "work" in user_input or "company" in user_input:
        query = """
        MATCH (p:Person)-[:WORKS_AT]->(c)
        RETURN p.name AS person, c.name AS result
        """
        data = run_query(query)

        return "\n".join([f"{r['person']} works at {r['result']}" for r in data])

    # CITY
    elif "live" in user_input or "city" in user_input:
        query = """
        MATCH (p:Person)-[:LIVES_IN]->(c)
        RETURN p.name AS person, c.name AS result
        """
        data = run_query(query)

        return "\n".join([f"{r['person']} lives in {r['result']}" for r in data])

    # STUDY
    elif "study" in user_input or "college" in user_input:
        query = """
        MATCH (p:Person)-[:STUDIED_AT]->(c)
        RETURN p.name AS person, c.name AS result
        """
        data = run_query(query)

        return "\n".join([f"{r['person']} studied at {r['result']}" for r in data])

    # GREETING
    elif "hi" in user_input or "hello" in user_input:
        return "Hello! Ask me smart questions 😎"

    return "Try asking: 'friend of amit' or 'who works where'"