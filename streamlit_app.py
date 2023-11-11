import matplotlib as plt
import matplotlib.pyplot as plt
import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Lab05 s22683",
    page_icon="🇯🇵",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None,
)

st.title("Lab05. Streamlit")

st.subheader("Przetwarzanie języka naturalnego")
st.text(
    "Aplikacja do analizy sentymentu w języku angielskim ocenia teksty pod kątem pozytywnego lub negatywnego tonu, zapewniając szybką analizę emocji.\nDodatkowo, umożliwia tłumaczenie tekstu z języka angielskiego na niemiecki."
)


def translate_to_german(text):
    with st.spinner("Wait for it..."):
        translator = pipeline(task="translation_en_to_de")
        translation = translator(text, max_length=50)[0]["translation_text"]
    st.balloons()
    return translation


# Funkcja do generowania wykresu kołowego
def generate_pie_chart(value, label):
    if label == "POSITIVE":
        positive_value = value
        negative_value = 1 - positive_value
    else:
        negative_value = value
        positive_value = 1 - negative_value

    fig, ax = plt.subplots(figsize=(7, 3.5))

    ax.pie(
        [positive_value, negative_value],
        labels=["Pozytywny", "Negatywny"],
        autopct="%1.1f%%",
        startangle=90,
        colors=["green", "red"],
    )

    ax.set_title("Wydźwięk emocjonalny")

    st.pyplot(fig=fig, use_container_width=False)


col11, _ = st.columns(2)

with col11:
    option = st.selectbox(
        "Opcje",
        [
            "Wydźwięk emocjonalny tekstu (eng)",
            "tłumaczenie na niemiecki",
        ],
    )
col12, col22 = st.columns(2)
text = ""
with col12:
    if option == "Wydźwięk emocjonalny tekstu (eng)":
        text = st.text_area(
            label="Wpisz tekst",
            placeholder="Wpisz tekst do oceny wydźwięku emocjonalnego",
        )
        if text:
            with st.spinner("Wait for it..."):
                classifier = pipeline("sentiment-analysis")
                answer = classifier(text)
                generate_pie_chart(answer[0]["score"], answer[0]["label"])
            st.balloons()
    elif option == "tłumaczenie na niemiecki":
        text = st.text_area(
            label="Angielski 🇬🇧", placeholder="Przetłumacz tekst na niemiecki"
        )
        if st.button("tłumacz"):
            translated_text = translate_to_german(text)
            with col22:
                st.text_area("Niemiecki 🇩🇪", translated_text, disabled=True)

st.text("Patryk Potera s22683")
