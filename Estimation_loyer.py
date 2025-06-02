import streamlit as st
import pandas as pd

# Modèle simple d'estimation basé sur le nombre de chambres et la localisation
def estimation_loyer(chambres, localisation):
    # Tarifs indicatifs par chambre selon localisation (en CFA)
    tarifs = {
        'Abidjan': 40000,      # par chambre
        'Yamoussoukro': 25000,
        'Bouaké': 20000,
        'Autre': 15000
    }
    tarif_par_chambre = tarifs.get(localisation, tarifs['Autre'])
    
    estimation = chambres * tarif_par_chambre
    return estimation

def main():
    st.title("Estimation du loyer d'un appartement en Côte d'Ivoire")
    st.write("Entrez le nombre de chambres et la localisation pour estimer le loyer mensuel.")
    
    chambres = st.number_input("Nombre de chambres", min_value=1, max_value=10, value=1, step=1)
    localisation = st.selectbox("Localisation", ['Abidjan', 'Yamoussoukro', 'Bouaké', 'Autre'])
    
    if st.button("Estimer le loyer"):
        loyer = estimation_loyer(chambres, localisation)
        st.success(f"Loyer estimé : {loyer:,.0f} FCFA / mois")

if __name__ == "__main__":
    main()
