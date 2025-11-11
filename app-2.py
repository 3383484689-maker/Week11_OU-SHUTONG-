import streamlit as st
from openai import OpenAI

# -------------------------------
# 🌸 1. Page Settings
# -------------------------------
st.set_page_config(page_title="🎭 Role-based Chatbot", layout="centered")

st.title("🎭 Role-based Chatbot")
st.caption("Ask creative questions and get advice from your AI mentor.")

# -------------------------------
# 🌸 2. Connect to OpenAI
# -------------------------------
# ✅ IMPORTANT: You must set your OpenAI API key in Streamlit Cloud Secrets:
# Settings → Secrets → Add: OPENAI_API_KEY = "your-api-key"
client = OpenAI()

# -------------------------------
# 🌸 3. Role Selection
# -------------------------------
roles = {
    "🎬 Film Director": "You are a professional film director who gives insightful and practical advice about filmmaking, cinematography, and storytelling.",
    "🎨 Art Critic": "You are an experienced art critic who analyzes artworks in a poetic and profound way.",
    "🎭 Theatre Designer": "You are a stage and performance designer specializing in spatial composition, lighting, and movement.",
    "💃 Choreographer": "You are a creative dance instructor who gives emotional and physical advice about choreography and body movement.",
    "📷 Photographer": "You are a photography mentor who discusses lighting, framing, and composition in detail."
}

selected_role = st.selectbox("Choose your role:", list(roles.keys()))
role_instruction = roles[selected_role]

# -------------------------------
# 🌸 4. Initialize Chat Session
# -------------------------------
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": role_instruction}]

# -------------------------------
# 🌸 5. Chat Interface
# -------------------------------
user_input = st.chat_input("Ask your question...")
if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state["messages"]
        )
        reply = response.choices[0].message.content
        st.session_state["messages"].append({"role": "assistant", "content": reply})

# -------------------------------
# 🌸 6. Display Messages
# -------------------------------
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").write(msg["content"])

# -------------------------------
# 🌸 7. Footer
# -------------------------------
st.markdown("---")
st.markdown("👨‍🏫 **Made for Arts & Advanced Big Data — Week 11 Role-based Chatbot Practice**")
