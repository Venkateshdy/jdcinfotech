import streamlit as st
import os

st.title("🧠 AI Website Generator")

business_name = st.text_input("Business Name")

industry = st.selectbox(
    "Industry",
    ["Restaurant", "Gym", "IT Company", "Salon", "Real Estate"]
)

pages = st.multiselect(
    "Select Pages",
    ["Home", "About", "Services", "Contact"]
)

style = st.selectbox(
    "Website Style",
    ["Modern", "Minimal", "Colorful"]
)

# =========================
# AGENTIC LOGIC (NO AI API)
# =========================

def generate_sitemap(prompt):
    return ["Home", "About", "Services", "Contact"]

def generate_content(prompt, sitemap):
    content = {}
    for page in sitemap:
        content[page] = f"This is the {page} section for {prompt}."
    return content

def generate_page_html(page, business_name):

    return f"""
    <html>
    <head>
        <title>{business_name} - {page}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>

            body {{
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f4f6f8;
            }}

            /* NAVBAR */
            nav {{
                background: #1f2937;
                color: white;
                padding: 15px;
                display: flex;
                justify-content: space-between;
            }}

            nav a {{
                color: white;
                margin-left: 15px;
                text-decoration: none;
            }}

            /* HERO */
            .hero {{
                background: linear-gradient(to right, #3b82f6, #6366f1);
                color: white;
                padding: 80px 20px;
                text-align: center;
            }}

            /* SECTION */
            .section {{
                padding: 40px;
                max-width: 900px;
                margin: auto;
                background: white;
                margin-top: 20px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}

            /* FOOTER */
            footer {{
                text-align: center;
                padding: 20px;
                margin-top: 40px;
                background: #1f2937;
                color: white;
            }}

        </style>
    </head>

    <body>

        <!-- NAVBAR -->
        <nav>
            <div><b>{business_name}</b></div>
            <div>
                <a href="home.html">Home</a>
                <a href="about.html">About</a>
                <a href="services.html">Services</a>
                <a href="contact.html">Contact</a>
            </div>
        </nav>

        <!-- HERO -->
        <div class="hero">
            <h1>{business_name}</h1>
            <p>Welcome to our {page} page</p>
        </div>

        <!-- CONTENT -->
        <div class="section">
            <h2>{page}</h2>
            <p>This is the {page} section of {business_name}. We provide high-quality services tailored to your needs.</p>
        </div>

        <!-- FOOTER -->
        <footer>
            <p>© 2026 {business_name}. All rights reserved.</p>
        </footer>

    </body>
    </html>
    """

# =========================
# MAIN FLOW
# =========================

if st.button("🚀 Generate Website"):

    if not business_name:
        st.warning("Please enter business name")

    elif not pages:
        st.warning("Please select at least one page")

    else:
        folder = business_name.replace(" ", "_").lower()
        os.makedirs(folder, exist_ok=True)

        for page in pages:
            file_path = f"{folder}/{page.lower()}.html"

            html = generate_page_html(page, business_name)

            with open(file_path, "w") as f:
                f.write(html)

        st.success("✅ Website created!")
        st.write(f"📁 Saved in: {folder}")

        # ✅ ZIP DOWNLOAD
        import zipfile

        zip_path = f"{folder}.zip"

        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for file in os.listdir(folder):
                zipf.write(f"{folder}/{file}")

        with open(zip_path, "rb") as f:
            st.download_button(
                "📥 Download Website",
                f,
                file_name=f"{folder}.zip"
            )