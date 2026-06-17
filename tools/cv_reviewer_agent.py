import os
import sys
from openai import OpenAI

def read_cv(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"❌ Σφάλμα κατά την ανάγνωση του αρχείου: {e}")
        sys.exit(1)

def review_cv(cv_text, api_key):
    client = OpenAI(api_key=api_key)
    
    system_prompt = """
    Είσαι ένας αυστηρός αλλά δίκαιος Hiring Manager (Head of Data) σε μεγάλη Ελληνική εταιρεία (π.χ. Τράπεζα, e-commerce, Telco). 
    Διαβάζεις ένα Data Science / Data Analytics CV. 
    Ο ρόλος σου είναι να δώσεις αυστηρό feedback με βάση τις ανάγκες της αγοράς το 2026 (Agentic AI Era).
    Ψάχνεις για Business Impact, όχι απλά λίστες με εργαλεία.
    Δώσε το feedback σου στα Ελληνικά με bullet points.
    Χώρισε την κριτική σου σε:
    1. Τι είναι καλό (Δυνατά σημεία)
    2. Τι λείπει (Red Flags / Αδυναμίες)
    3. Actionable συμβουλές για την Ελληνική αγορά.
    """
    
    print("🤖 Ο AI Hiring Manager διαβάζει το CV σου...")
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Παρακαλώ αξιολόγησε το παρακάτω CV:\n\n{cv_text}"}
            ],
            temperature=0.7
        )
        print("\n" + "="*50)
        print("🎯 ΑΠΟΤΕΛΕΣΜΑ ΑΞΙΟΛΟΓΗΣΗΣ:")
        print("="*50 + "\n")
        print(response.choices[0].message.content)
        
    except Exception as e:
        print(f"❌ Σφάλμα κατά την επικοινωνία με το OpenAI API: {e}")

if __name__ == "__main__":
    print("🚀 Καλώς ήρθες στον AI CV Reviewer (Agentic Era 2026)")
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        api_key = input("🔑 Βάλε το OpenAI API Key σου (ξεκινάει από sk-...): ").strip()
        
    if len(sys.argv) < 2:
        print("\n⚠️ Χρήση: python cv_reviewer_agent.py <path_to_cv.txt_or_md>")
        print("💡 Παράδειγμα: python cv_reviewer_agent.py ../templates/data_science_cv_template.md")
        sys.exit(1)
        
    cv_path = sys.argv[1]
    cv_text = read_cv(cv_path)
    review_cv(cv_text, api_key)
