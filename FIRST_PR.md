# 🤝 The "My First PR" Guide

Καλώς ήρθες! Αν δεν έχεις συνεισφέρει ποτέ σε ένα Open Source project στο GitHub, αυτό το αποθετήριο (repo) είναι το ιδανικό μέρος για να ξεκινήσεις. Θα σε πάρουμε βήμα-βήμα.

## Βήμα 1: Fork το Repository
Στο πάνω δεξιά μέρος αυτής της σελίδας, θα δεις ένα κουμπί που λέει **"Fork"**. Πάτα το. 
Αυτό δημιουργεί ένα ακριβές αντίγραφο αυτού του repo στον δικό σου λογαριασμό GitHub (π.χ. `your_username/greek-data-science-roadmap`).

## Βήμα 2: Clone το δικό σου (Forked) Repo τοπικά
Άνοιξε το τερματικό σου (ή το Git Bash) και γράψε:
```bash
git clone https://github.com/YOUR_USERNAME/greek-data-science-roadmap.git
cd greek-data-science-roadmap
```

## Βήμα 3: Φτιάξε ένα νέο Branch
Μην κάνεις αλλαγές απευθείας στο `main`. Φτιάξε ένα κλαδί (branch) με ένα περιγραφικό όνομα:
```bash
git checkout -b add-my-new-resource
```

## Βήμα 4: Κάνε την αλλαγή σου
Για παράδειγμα, άνοιξε το αρχείο `resources.json` και πρόσθεσε ένα YouTube channel που σε βοήθησε. Ή διόρθωσε ένα ορθογραφικό λάθος στο `README.md`.

## Βήμα 5: Κάνε Commit
Αποθήκευσε το αρχείο και πήγαινε ξανά στο τερματικό:
```bash
git add .
git commit -m "Add great Python YouTube channel to resources"
```

## Βήμα 6: Κάνε Push
Ανέβασε την αλλαγή σου στο δικό σου repo στο GitHub:
```bash
git push origin add-my-new-resource
```

## Βήμα 7: Κάνε το Pull Request (PR)
1. Πήγαινε στη σελίδα του δικού σου repo στο GitHub.
2. Θα δεις ένα πράσινο κουμπί που λέει **"Compare & pull request"**. Πάτα το.
3. Γράψε μια μικρή περιγραφή για το τι άλλαξες (π.χ. "Πρόσθεσα αυτό το link γιατί είναι πολύ καλό για αρχάριους").
4. Πάτα **"Create pull request"**.

🎉 **ΣΥΓΧΑΡΗΤΗΡΙΑ!** Μόλις έκανες το πρώτο σου Pull Request. Μόλις το κάνω αποδοχή (Merge), ο κώδικάς σου θα αποτελεί επίσημο κομμάτι αυτού του repo και το όνομά σου θα φαίνεται στους Contributors!
