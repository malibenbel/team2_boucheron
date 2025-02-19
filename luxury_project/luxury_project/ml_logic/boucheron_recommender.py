import streamlit as st
import pandas as pd
def boucheron_recommender():
    # Load dataset
    file_path = "PM_extract_Jan_2025_10_brands.csv"
    df = pd.read_csv(file_path, sep=';')

    # Keep only Boucheron brand
    df = df[df['brand'] == 'Boucheron']

    # Convert price to numeric (in case of errors)
    df["price"] = pd.to_numeric(df["price"], errors='coerce')

    # Streamlit App Title
    st.title("⌚ Boucheron Watch Recommender")

    # Sidebar for user input
    st.sidebar.header("📌 Select Your Preferences")

    # User selects a price range
    min_price, max_price = st.sidebar.slider(
        "Select Price Range (in original currency)", 
        int(df["price"].min()), int(df["price"].max()), 
        (int(df["price"].min()), int(df["price"].max()))
    )

    # User selects a country
    country_options = df["country"].unique()    
    selected_country = st.sidebar.selectbox("Select Country", country_options)

    # User selects a currency
    currency_options = df[df["country"] == selected_country]["currency"].unique()
    selected_currency = st.sidebar.selectbox("Select Currency", currency_options)

    # User selects a collection
    collection_options = df[df["country"] == selected_country]["collection"].unique()
    selected_collection = st.sidebar.selectbox("Select Collection", collection_options)

    # User chooses how many recommendations they want
    num_recommendations = st.sidebar.slider("Number of Recommendations", 1, 10, 5)

    # Filter dataset based on selections
    filtered_df = df[
        (df["price"] >= min_price) & 
        (df["price"] <= max_price) & 
        (df["country"] == selected_country) & 
        (df["currency"] == selected_currency) & 
        (df["collection"] == selected_collection)
    ]

    # Display results
    st.subheader(f"💎 Recommended Watches ({num_recommendations} shown)")
    if not filtered_df.empty:
        for i, row in filtered_df.head(num_recommendations).iterrows():
            st.markdown(f"""
            **{row['reference_code']}**  
            💰 **Price:** {row['price']} {row['currency']}  
            🌍 **Country:** {row['country']}  
            🔗 [View Watch]({row['url']})  
            """)
    else:
        st.warning("No watches found for the selected filters. Try adjusting the price range, country, or collection.")

    # Footer
    st.markdown("🔍 *Refine your search on the sidebar!*")
    
    return None
    # python -m streamlit run boucheron_recommender.p