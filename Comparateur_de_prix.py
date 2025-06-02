import requests      #Pour envoyer des requêtes HTTP
from bs4 import BeautifulSoup   # Pour parser le HTML
import pandas as pd    # Pour stocker les données
import time     # Pour gérer des pauses (anti-blocage)

def scraper_coinafrique(max_pages=10):
    base_url = 'https://ci.coinafrique.com/categorie/appartements'
    annonces = []

    for page in range(1, max_pages + 1):
        url = f"{base_url}?page={page}"
        print(f"Scraping de la page {page}...")
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Erreur sur la page {page}: {e}")
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        cartes = soup.select('div.card-content.top-ads-listing-content.card-content-flex')
        if not cartes:
            print("Aucune annonce trouvée, arrêt du scraping.")
            break

        for carte in cartes:
            titre = carte.select_one('p.card-title.activator.orange-text')
            titre_text = titre.get_text(strip=True) if titre else ''

            prix_tag = carte.select_one('p.card-price')
            prix_text = prix_tag.get_text(strip=True) if prix_tag else ''

            localisation_tag = carte.select_one('p.card-location')
            localisation_text = localisation_tag.get_text(strip=True) if localisation_tag else ''

            lien_tag = carte.find_parent('a')
            lien = 'https://ci.coinafrique.com' + lien_tag['href'] if lien_tag and lien_tag.has_attr('href') else ''

            annonces.append({
                'Titre': titre_text,
                'Prix': prix_text,
                'Localisation': localisation_text,
                'Lien': lien
            })

        time.sleep(1)  # pause anti-blocage

    df = pd.DataFrame(annonces)
    df.to_csv('annonces_coinafrique_10pages.csv', index=False, encoding='utf-8')
    print(f"Scraping terminé. {len(annonces)} annonces enregistrées dans annonces_coinafrique_10pages.csv")

if __name__ == "__main__":
    scraper_coinafrique(10)
