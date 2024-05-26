import streamlit as st
import requests


# Apply custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Load custom CSS
local_css("style.css")


# Function to fetch data from API and parse JSON
def fetch_data(endpoint):
    try:
        response = requests.get(endpoint)
        response.raise_for_status()  # Check HTTP response status
        return response.json()
    except requests.exceptions.HTTPError as e:
        st.error(f"HTTP error occurred: {e}")
    except ValueError as e:
        st.error(f"Error decoding JSON: {e}")
    return []


# Helper function to post data to API
def post_data(endpoint, data):
    try:
        response = requests.post(endpoint, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        st.error(f"HTTP error occurred: {e}")
    except ValueError as e:
        st.error(f"Error decoding JSON: {e}")
    return {}


# Helper function to delete data from API
def delete_data(endpoint):
    try:
        response = requests.delete(endpoint)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as e:
        st.error(f"HTTP error occurred: {e}")
    return None


# Display form to create flower
def display_create_flower():
    st.title("Create Flower")
    st.markdown("### Enter the details of the flower")
    col1, col2 = st.columns(2)
    with col1:
        name_supplier = st.text_input("Supplier Name", "")
        name = st.text_input("Flower Name", "")
        type_of_farm = st.text_input("Type", "")
        variant = st.text_input("Variant", "")
    with col2:
        price = st.number_input("Price", min_value=0.0, format="%.2f")
        country = st.text_input("Country", "")
        blooming_season = st.text_input("Blooming Season", "")

    if st.button("Create Flower"):
        if not name_supplier or not name:
            st.error("Supplier Name and Flower Name are required")
        else:
            flower_data = {
                "name": name,
                "type": type_of_farm,
                "variant": variant,
                "price": price,
                "country": country,
                "blooming_season": blooming_season,
            }
            result = post_data(f"http://127.0.0.1:8000/create_flower/{name_supplier}", flower_data)
            st.success(f"Flower created: {result}")


# Display form to delete flower
def display_delete_flower():
    st.title("Delete Flower")
    st.markdown("### Enter the details of the flower to delete")
    col1, col2 = st.columns(2)
    with col1:
        name_supplier = st.text_input("Supplier Name to delete from", "")
    with col2:
        flower_name = st.text_input("Flower Name to delete", "")

    if st.button("Delete Flower"):
        if not name_supplier or not flower_name:
            st.error("Supplier Name and Flower Name are required")
        else:
            delete_endpoint = f"http://127.0.0.1:8000/delete_flower/{name_supplier}/{flower_name}"
            result = delete_data(delete_endpoint)
            if result and result.status_code == 204:
                st.success(f"Flower {flower_name} deleted successfully")
            else:
                st.error(f"Failed to delete flower {flower_name}")


# Display all flowers
def display_all_flowers():
    st.title("All Flowers")
    flowers = fetch_data('http://127.0.0.1:8000/get_all_flowers')
    if not flowers:
        st.warning("No flowers data available or failed to fetch data.")
        return
    for flower in flowers:
        with st.expander(f"Flower: {flower['name']} (ID: {flower['id']})"):
            st.markdown(f"- Price: {flower['price']}")
            st.markdown(f"- Country: {flower['country']}")
            st.markdown(f"- Variant: {flower['variant']}")
            st.markdown(f"- Type: {flower['type']}")
            st.markdown(f"- Blooming Season: {flower['blooming_season']}")


# Display all suppliers
def display_all_suppliers():
    st.title("All Suppliers")
    suppliers = fetch_data('http://127.0.0.1:8000/get_all_supplier')
    if not suppliers:
        st.warning("No suppliers data available or failed to fetch data.")
        return
    for supplier in suppliers:
        with st.expander(f"Supplier: {supplier['name']} (ID: {supplier['id']})"):
            st.markdown(f"- Address: {supplier['address']}")
            st.markdown(f"- Type of Farm: {supplier['type_of_farm']}")


# Display all flowers for each supplier
def display_all_flowers_for_suppliers():
    st.title("All Flowers for Each Supplier")
    suppliers = fetch_data('http://127.0.0.1:8000/get_all_flowers_for_suppliers')
    if not suppliers:
        st.warning("No suppliers or flowers data available or failed to fetch data.")
        return
    for supplier in suppliers:
        with st.expander(f"{supplier['name']} (ID: {supplier['id']})"):
            st.markdown(f"Address: {supplier['address']}")
            st.markdown(f"Type of Farm: {supplier['type_of_farm']}")
            if supplier['flowers']:
                for flower in supplier['flowers']:
                    st.markdown(f"**Flower: {flower['name']} (ID: {flower['id']})**")
                    st.markdown(f"- Country: {flower['country']}")
                    st.markdown(f"- Blooming Season: {flower['blooming_season']}")
                    st.markdown(f"- Price: {flower['price']}")
                    st.markdown(f"- Type: {flower['type']}")
                    st.markdown(f"- Variant: {flower['variant']}")
            else:
                st.markdown("No flowers available for this supplier")


# Display seasonal flowers
def display_seasonal_flowers(seasonal):
    st.title(f"Flowers for Season: {seasonal}")
    flowers = fetch_data(f'http://127.0.0.1:8000/get_seasonal_flowers/{seasonal}')
    if not flowers:
        st.warning(f"No flowers data available for the season: {seasonal}")
        return
    for flower in flowers:
        with st.expander(f"Flower: {flower['name']} (ID: {flower['id']})"):
            st.markdown(f"- Price: {flower['price']}")
            st.markdown(f"- Country: {flower['country']}")
            st.markdown(f"- Blooming Season: {flower['blooming_season']}")


# Display flowers by country
def display_flowers_by_country(country):
    st.title(f"Flowers for Country: {country}")
    flowers = fetch_data(f'http://127.0.0.1:8000/get_flowers_for_country/{country}')
    if not flowers:
        st.warning(f"No flowers data available for the country: {country}")
        return
    for flower in flowers:
        with st.expander(f"Flower: {flower['name']} (ID: {flower['id']})"):
            st.markdown(f"- Price: {flower['price']}")
            st.markdown(f"- Country: {flower['country']}")
            st.markdown(f"- Blooming Season: {flower['blooming_season']}")


# Display all vendors
def display_all_vendors():
    st.title("All Vendors")
    vendors = fetch_data('http://127.0.0.1:8000/get_all_vendors')
    if not vendors:
        st.warning("No vendors data available or failed to fetch data.")
        return
    for vendor in vendors:
        with st.expander(f"Vendor: {vendor['name']} (ID: {vendor['id']})"):
            st.markdown(f"- Address: {vendor['address']}")


# Display matching suppliers
def display_matching_suppliers():
    st.title("Matching Suppliers")

    # Input field to get vendor ID
    vendor_id = st.text_input("Enter Vendor ID:")

    if vendor_id:
        try:
            response = requests.get(f'http://127.0.0.1:8000/get_matching_suppliers/{vendor_id}')
            response.raise_for_status()  # Raise an error for bad status codes
            suppliers = response.json()
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to fetch data: {e}")
            return

        if not suppliers:
            st.warning("No matching suppliers data available.")
            return

        for supplier in suppliers:
            st.subheader(f"Supplier: {supplier['name']} (ID: {supplier['id']})")
    else:
        st.info("Please enter a Vendor ID to fetch matching suppliers.")


# Display vendors with filtering options
def display_get_vendors():
    st.title("Get Vendors")
    sort = st.checkbox("Sort vendors")
    variant = st.text_input("Enter variant", "")

    # Create an empty dictionary for parameters
    params = {}
    if sort:
        params['sort'] = "true"
    if variant:
        params['variant'] = variant

    # Create query string
    url = 'http://127.0.0.1:8000/get_vendors'
    if params:
        params_str = "&".join(f"{key}={value}" for key, value in params.items())
        url = f"{url}?{params_str}"

    vendors = fetch_data(url)

    if not vendors:
        st.warning("No vendors data available or failed to fetch data.")
        return
    for vendor in vendors:
        with st.expander(f"Vendor: {vendor['name']} (ID: {vendor['id']})"):
            st.markdown(f"- Address: {vendor['address']}")


# Main function for Streamlit app
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose a page", [
        "Create Flower",
        "Delete Flower",
        "All Flowers",
        "All Suppliers",
        "All Vendors",
        "Flowers for Each Supplier",
        "Seasonal Flowers",
        "Flowers by Country",
        "Matching Suppliers"
    ])

    if page == "All Flowers":
        display_all_flowers()
    elif page == "All Suppliers":
        display_all_suppliers()
    elif page == "Flowers for Each Supplier":
        display_all_flowers_for_suppliers()
    elif page == "Seasonal Flowers":
        seasonal = st.sidebar.text_input("Enter the season", "spring")
        if seasonal:
            display_seasonal_flowers(seasonal)
    elif page == "Flowers by Country":
        country = st.sidebar.text_input("Enter the country", "USA")
        if country:
            display_flowers_by_country(country)
    elif page == "All Vendors":
        display_all_vendors()
    elif page == "Create Flower":
        display_create_flower()
    elif page == "Delete Flower":
        display_delete_flower()
    elif page == "Get Vendors":
        display_get_vendors()
    elif page == "Matching Suppliers":
        display_matching_suppliers()


if __name__ == '__main__':
    main()

# To run this app, use: streamlit run app.py
