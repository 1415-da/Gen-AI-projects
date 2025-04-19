import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
import base64

# Set page config
st.set_page_config(page_title="LinkedIn Post Generator", layout="centered")

# Apply custom style
def set_custom_style():
    st.markdown("""
        <style>
            body {
                background-color: #e6ecf5;
            }
            .stApp {
                background-color: #ffffff;
                padding: 2rem;
                border-radius: 12px;
                box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
                font-family: 'Segoe UI', sans-serif;
                color: #111;
            }
            h1 {
                color: #0e76a8;
                text-align: center;
                font-weight: 700;
            }
            .custom-label {
                font-size: 18px !important;
                font-weight: 700 !important;
                color: #0e76a8 !important;
                margin-bottom: 0.2rem;
                display: block;
            }
            .stSelectbox label {
                display: none;
            }
            .stButton>button {
                background-color: #0e76a8;
                color: white;
                font-weight: 600;
                font-size: 16px;
                border-radius: 10px;
                padding: 10px 20px;
            }
            .post-box {
                background-color: #f7f9fc;
                padding: 20px;
                border-radius: 10px;
                font-weight: 600;
                color: #222;
                font-size: 16px;
                line-height: 1.6;
                margin-top: 10px;
            }
            .download-button a {
                text-decoration: none;
                color: white;
                background-color: #0e76a8;
                padding: 10px 15px;
                border-radius: 8px;
                display: inline-block;
                margin-top: 10px;
                font-weight: 600;
            }
        </style>
    """, unsafe_allow_html=True)

# Download utility
def generate_download_link(text, filename="linkedin_post.txt"):
    b64 = base64.b64encode(text.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="{filename}">Download your post</a>'
    st.markdown(f'<div class="download-button">{href}</div>', unsafe_allow_html=True)

# App UI
def main():
    set_custom_style()

    st.markdown("<h1>LinkedIn Post Generator</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #333;'>Generate professional LinkedIn posts quickly and easily with the power of AI</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()

    length_options = ["Short", "Medium", "Long"]
    language_options = ["English", "Hinglish"]

    with col1:
        st.markdown("<label class='custom-label'>Topic</label>", unsafe_allow_html=True)
        selected_tag = st.selectbox("", options=tags, label_visibility="collapsed")

    with col2:
        st.markdown("<label class='custom-label'>Length</label>", unsafe_allow_html=True)
        selected_length = st.selectbox("", options=length_options, label_visibility="collapsed")

    with col3:
        st.markdown("<label class='custom-label'>Language</label>", unsafe_allow_html=True)
        selected_language = st.selectbox("", options=language_options, label_visibility="collapsed")

    st.markdown("---")

    if st.button("Generate Post"):
        with st.spinner("Crafting your LinkedIn magic..."):
            post = generate_post(selected_length, selected_language, selected_tag)

            # Custom styled section heading
            st.markdown(
                """
                <div style='background-color: #e1f5fe; padding: 10px; border-radius: 8px; margin-top: 20px;'>
                    <h4 style='color:#0e76a8; font-weight:700; margin: 0;'>Here’s your post:</h4>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Styled post output
            st.markdown(f"<div class='post-box'>{post}</div>", unsafe_allow_html=True)

            # Download button
            generate_download_link(post)

# Run app
if __name__ == "__main__":
    main()
