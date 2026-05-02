import rdflib
import glob
import os

def run_eeat_query():
    g = rdflib.Graph()
    data_dir = "data"
    
    if not os.path.exists(data_dir):
        print(f"[ ERROR ]: Data directory not found.")
        return

    # Load all verified JSON-LD data
    for file in glob.glob(os.path.join(data_dir, "*.jsonld")):
        try:
            g.parse(file, format="json-ld")
        except Exception as e:
            print(f"[ ERROR ]: Failed to parse {file}: {e}")

    query = """
    PREFIX padi: <https://gitandu.com/padi/>
    PREFIX trust: <https://gitandu.com/padi/trust/>
    PREFIX asqa: <https://www.asqa.gov.au/standards/>

    SELECT ?pillar ?credential ?standard_mapping
    WHERE {
      ?subject trust:pillar ?pillar .
      OPTIONAL { ?subject trust:credential ?credential . }
      OPTIONAL { ?subject asqa:competencyUnit ?standard_mapping . }
      OPTIONAL { ?subject asqa:aqfLevel ?standard_mapping . }
    }
    ORDER BY ?pillar
    """
    
    print("\n--- [ PADI E-E-A-T VERIFICATION REPORT ] ---")
    results = g.query(query)
    for row in results:
        pillar = str(row.pillar)
        cred = str(row.credential) if row.credential else "N/A"
        mapping = str(row.standard_mapping) if row.standard_mapping else "N/A"
        print(f"Pillar: {pillar:12} | Credential: {cred:25} | ASQA/AQF: {mapping}")

if __name__ == "__main__":
    run_eeat_query()
