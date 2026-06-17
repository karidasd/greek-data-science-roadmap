# 🏛️ Ελληνικά Open Data Sources (Portfolio Goldmine)

Όταν χτίζεις ένα Portfolio, το να χρησιμοποιείς το `Titanic Dataset` ή το `Iris Dataset` δεν εντυπωσιάζει πλέον κανέναν. Οι Hiring Managers θέλουν να δουν ότι μπορείς να διαχειριστείς **πραγματικά, ακατάστατα δεδομένα** (messy data) που έχουν Business Value για την Ελληνική αγορά.

Εδώ είναι μια λίστα με πηγές δεδομένων για να φτιάξεις τα δικά σου "Greek-Flavored" projects:

## 1. 📊 Οικονομία & Κοινωνία
* **[ΕΛΣΤΑΤ (Ελληνική Στατιστική Αρχή)](https://www.statistics.gr/):** Η απόλυτη πηγή για πληθωρισμό, ανεργία, ΑΕΠ, και δημογραφικά στοιχεία.
  * *Ιδέα για Project:* Ένα Power BI dashboard που δείχνει την εξέλιξη της ανεργίας ανά περιφέρεια και ηλικιακή ομάδα την τελευταία 10ετία.
* **[data.gov.gr](https://data.gov.gr/):** Το επίσημο portal ανοικτών δεδομένων του Ελληνικού Κράτους. Περιέχει APIs για εμβολιασμούς, συνταγογραφήσεις, εισιτήρια μουσείων κ.ά.
  * *Ιδέα για Project:* Python script που τραβάει τα καθημερινά δεδομένα κίνησης στους δρόμους της Αθήνας και προβλέπει το μποτιλιάρισμα με Prophet.

## 2. ⚡ Ενέργεια & Περιβάλλον
* **[ΑΔΜΗΕ / ΔΕΔΔΗΕ / ΡΑΕ](https://www.admie.gr/):** Δεδομένα για το ενεργειακό μείγμα της Ελλάδας (πόσο ρεύμα παράγεται από αιολικά vs λιγνίτη).
  * *Ιδέα για Project:* Time-series forecasting (XGBoost/LSTM) για την πρόβλεψη της ζήτησης ρεύματος στην Ελλάδα τον επόμενο μήνα.
* **[Meteo.gr / Εθνικό Αστεροσκοπείο](https://meteo.gr/):** Δεδομένα θερμοκρασιών και ακραίων καιρικών φαινομένων.

## 3. 📜 Νομοθεσία & Κράτος
* **[Διαύγεια (Diavgeia API)](https://diavgeia.gov.gr/api/help):** Όλες οι κρατικές αποφάσεις και δαπάνες αναρτώνται εδώ. Το API είναι ανοιχτό.
  * *Ιδέα για Project:* Ένα RAG (Retrieval-Augmented Generation) bot με LangChain όπου ο χρήστης ρωτάει "Πόσα χρήματα ξόδεψε ο Δήμος Αθηναίων για φωτισμό το 2023;" και το bot βρίσκει το σωστό PDF και απαντάει.

## 4. 🏠 Real Estate & E-commerce
* **Web Scraping (Spitogatos, XE.gr, Skroutz):** Αν και δεν υπάρχουν επίσημα APIs, η συλλογή δεδομένων με BeautifulSoup ή Selenium είναι εξαιρετικό skill.
  * *Ιδέα για Project:* Scraper που μαζεύει τιμές ενοικίων στο κέντρο της Αθήνας και φτιάχνει έναν διαδραστικό χάρτη με Folium που δείχνει πού είναι τα "φθηνά" διαμερίσματα.

* **[e-katanalotis.gov.gr](https://e-katanalotis.gov.gr/):** Η πλατφόρμα με τιμές από σούπερ μάρκετ και καύσιμα.
  * *Ιδέα για Project:* Σύγκριση "Καλαθιού του Νοικοκυριού" ανάμεσα σε 3 αλυσίδες και δημιουργία Dashboard Πληθωρισμού.

## 5. 📦 Kaggle Greek Datasets
* **[Kaggle Search: Greece](https://www.kaggle.com/datasets?search=greece):**
  Στο Kaggle υπάρχουν έτοιμα καθαρισμένα datasets (π.χ. Airbnb listings in Athens, OASA bus routes, Greek fires). 
  * *Ιδέα για Project:* Εξαιρετικό μέρος για να βρείτε έτοιμα CSVs αν δεν θέλετε να χτίσετε δικούς σας scrapers.

---

## ⚖️ The "Scraping Ethics" (Και πώς να μη φάτε IP Ban)
Πολλά ελληνικά sites (π.χ. efood, Spitogatos, Car.gr) **δεν** δίνουν Public API. Ο μόνος τρόπος να πάρετε δεδομένα είναι το Web Scraping (με BeautifulSoup ή Selenium).
**ΠΡΟΣΟΧΗ:** 
1. Πάντα να ελέγχετε το `robots.txt` του site (π.χ. `spitogatos.gr/robots.txt`). Σας λέει τι επιτρέπεται και τι απαγορεύεται.
2. Βάλτε `time.sleep(2)` ανάμεσα στα requests σας! Αν στείλετε 1.000 requests σε 1 δευτερόλεπτο, όχι μόνο θα φάτε ban από το firewall τους (π.χ. Cloudflare), αλλά ίσως ρίξετε και τον server τους (DDoS attack), το οποίο διώκεται ποινικά.
3. Μην κάνετε scrape προσωπικά δεδομένα (GDPR!).

---

## ⌨️ Code Snippets (Πώς "χτυπάμε" τα Ελληνικά APIs)

Το να ξέρετε να καλείτε ένα REST API είναι βασικό skill. Δείτε ένα απλό παράδειγμα σε Python για το πώς παίρνουμε δεδομένα από τη Διαύγεια χωρίς να κατεβάζουμε χειροκίνητα PDFs:

### Παράδειγμα: API της Διαύγειας (Python)
```python
import requests
import pandas as pd

# Αναζήτηση των τελευταίων 50 αποφάσεων (π.χ. Δήμος Αθηναίων / Ενδεικτικό Query)
# Δείτε το documentation στο diavgeia.gov.gr/api/help
url = "https://diavgeia.gov.gr/opendata/search?q=organizationUid:50024&size=50"
headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Μετατροπή του JSON response κατευθείαν σε Pandas DataFrame
    df = pd.DataFrame(data['decisions'])
    print(f"✅ Βρέθηκαν {len(df)} αποφάσεις.")
    # Εμφάνιση του θέματος και της ημερομηνίας των πρώτων 3
    print(df[['subject', 'issueDate']].head(3))
else:
    print(f"❌ Σφάλμα API: HTTP {response.status_code}")
```
*Tip: Χρησιμοποιήστε το AI (π.χ. ChatGPT) δίνοντάς του το documentation URL ενός API και ζητήστε του να σας γράψει τον Python wrapper!*

---
💡 **Pro Tip:** Χρησιμοποιήστε το [Greek-Data-Kit](https://github.com/karidasd/Greek-Data-Kit) που είναι ήδη φτιαγμένο για να διευκολύνει την άντληση πολλών από αυτά τα δεδομένα!

---

## 🚀 Πώς να φιλοξενήσετε το Portfolio σας (Δωρεάν)
Το να έχετε απλά τον κώδικα στο GitHub είναι καλό. Το να στείλετε ένα link στον Hiring Manager με ένα **live web app** που μπορεί να πατήσει κουμπιά και να δει γραφήματα είναι 10 φορές καλύτερο. Ορίστε πώς θα "ανεβάσετε" τα ελληνικά projects σας δωρεάν:

1. **Streamlit Community Cloud:** Ιδανικό για Data Analysts/Scientists. Γράφετε ένα απλό Python script (`app.py`) με το `streamlit`, το κάνετε push στο GitHub, και το Streamlit το μετατρέπει σε Web App δωρεάν.
2. **Vercel / Netlify:** Ιδανικά αν έχετε φτιάξει ένα dashboard με καθαρή HTML/JS ή React. Απίστευτα γρήγορο deploy.
3. **Render:** Αν το project σας είναι ένα Backend API (π.χ. ένα FastAPI που δέχεται τετραγωνικά και περιοχή και προβλέπει τιμές ενοικίων), το Render παρέχει δωρεάν hosting για web services. Το free tier "κοιμάται" μετά από 15 λεπτά αδράνειας, αλλά για portfolio είναι τέλειο!
