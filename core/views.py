from django.shortcuts import render
from neo4j import GraphDatabase

# Setup Neo4j driver
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "Neo4jdesktop"))

def home(request):
    return render(request, 'core/home.html')

def result(request):
    user_input = request.GET.get("query")
    search_type = request.GET.get("type")

    with driver.session() as session:
        if search_type == "disease":
            data = session.run("""
                MATCH (d:Disease {name: $query})<-[:TREATS]-(m:Medicine),
                      (d)<-[:ABOUT]-(p:ResearchPaper)-[:WRITTEN_BY]->(r:Researcher)
                RETURN d.name AS disease, m.name AS medicine, p.title AS title,
                       r.name AS author, r.affiliation AS affiliation,
                       p.link AS link, p.overview AS overview
            """, {"query": user_input}).single()
        else:
            data = session.run("""
                MATCH (m:Medicine {name: $query})-[:TREATS]->(d:Disease),
                      (d)<-[:ABOUT]-(p:ResearchPaper)-[:WRITTEN_BY]->(r:Researcher)
                RETURN d.name AS disease, m.name AS medicine, p.title AS title,
                       r.name AS author, r.affiliation AS affiliation,
                       p.link AS link, p.overview AS overview
            """, {"query": user_input}).single()

    return render(request, 'core/result.html', {"data": data})



