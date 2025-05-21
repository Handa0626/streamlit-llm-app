from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# 専門家のシステムメッセージ定義
EXPERT_PROMPTS = {
    "医師": "あなたは経験豊富な内科医です。医学的な質問に対して専門的かつわかりやすく回答してください。",
    "弁護士": "あなたは熟練した企業法務弁護士です。法的な観点から正確で丁寧に回答してください。",
    "エンジニア": "あなたはソフトウェア開発に精通したエンジニアです。技術的な質問には具体的かつ分かりやすく説明してください。"
}

# LLMに入力して応答を得る関数
def get_llm_response(user_input: str, expert_type: str) -> str:
    system_prompt = EXPERT_PROMPTS[expert_type]
    chat = ChatOpenAI()

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ]

    response = chat.invoke(messages)
    return response.content

# Streamlit UI構築
def main():
    st.title("💬 専門家AIに質問してみよう")
    st.write("""
        このWebアプリでは、あなたの質問に対して、選択した専門分野のAIが専門的な立場から回答します。
        
        使い方:
        1. 下の入力欄に質問を入力してください。
        2. 回答してほしい専門家の種類を選んでください。
        3. 「送信」ボタンを押すと、専門家AIからの回答が表示されます。
    """)

    # 専門家選択
    expert_type = st.radio("回答してほしい専門家を選んでください:", list(EXPERT_PROMPTS.keys()))

    # ユーザー入力
    user_input = st.text_area("質問を入力してください:")

    # 回答表示
    if st.button("送信"):
        if user_input.strip() == "":
            st.warning("質問を入力してください。")
        else:
            with st.spinner("AIが回答を生成中です..."):
                response = get_llm_response(user_input, expert_type)
            st.success("✅ 回答が得られました:")
            st.write(response)

if __name__ == "__main__":
    main()