import streamlit as st

import datetime

# 제목
st.title("🌸 향기로 알아보는 나의 공감 유형")
st.write("향기를 고르면 감정 그래프와 함께 나의 공감 유형을 테스트해볼 수 있어요.")

# 향기 선택
choice = st.selectbox("가장 좋아하는 향기를 선택하세요:", ["라벤더", "민트", "오렌지"])

# 향기별 감정 이미지 및 공감 이미지 불러오기
if choice == "라벤더":
    st.subheader("💜 라벤더 감정 반응")
    st.image("lavender_chart.png.png", caption="라벤더 감정 그래프", use_container_width=True)
    st.image("lavender.jpg", caption="라벤더 향기 이미지", use_container_width=True)
    st.info("💡 라벤더 향은 이완과 감성, 정서적 안정감을 높여주며 공감 능력과 정서적 민감성을 자극합니다.")

elif choice == "민트":
    st.subheader("💚 민트 감정 반응")
    st.image("mint_chart.png.png", caption="민트 감정 그래프", use_container_width=True)
    st.image("mint.jpg", caption="민트 향기 이미지", use_container_width=True)
    st.info("💡 민트 향은 집중력과 명료함을 주어 감정적 거리를 유지하면서 이성적 공감을 가능하게 합니다.")

else:
    st.subheader("🧡 오렌지 감정 반응")
    st.image("orange_chart.png.png", caption="오렌지 감정 그래프", use_container_width=True)
    st.image("orange.jpg", caption="오렌지 향기 이미지", use_container_width=True)
    st.info("💡 오렌지 향은 따뜻하고 명랑한 기분을 유도하여 친밀한 공감과 긍정적 에너지 전달에 도움을 줍니다.")

# 공감 테스트
st.divider()
st.subheader("💗 공감 성향 자가 테스트")
st.write("공감이란 다른 사람의 감정을 알아차리고 함께 느끼는 능력입니다. 이 테스트를 통해 나의 공감 성향을 알아보세요.")

questions = [
    "1. 친구가 슬프다고 말하면 내 마음도 무거워진다.",
    "2. 감정이입이 쉬운 편이다.",
    "3. 영화나 책을 보며 눈물이 나는 편이다.",
    "4. 타인의 기분 변화를 잘 눈치챈다.",
    "5. 뉴스에서 슬픈 장면을 보면 감정이 쉽게 흔들린다."
]

score = 0
for q in questions:
    answer = st.radio(q, ["예", "아니오"], key=q)
    if answer == "예":
        score += 1

# 결과 출력 및 저장
st.divider()
if st.button("✨ 나의 공감 결과 보기"):
    st.subheader("📊 당신의 공감 유형")

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result_text = ""

    if score >= 4:
        result_text = "감수성이 풍부한 공감형"
        st.success("💜 당신은 감수성이 풍부한 공감형!")
        st.write("감정을 민감하게 포착하고 깊이 느끼며 타인을 잘 이해하는 사람입니다. 이러한 성향은 예술, 상담, 간호, 교육 등 정서적 공감이 중요한 분야에서 강점으로 작용합니다.")
    elif score >= 2:
        result_text = "균형 잡힌 공감형"
        st.info("🧡 당신은 균형 잡힌 공감형")
        st.write("이성적 판단과 감정적 공감을 조화롭게 사용하는 타입입니다. 상황에 따라 적절한 공감 반응을 보이며 인간관계에서 조율의 달인이 될 수 있습니다.")
    else:
        result_text = "이성 중심의 분석형"
        st.warning("💚 당신은 이성 중심의 분석형")
        st.write("감정보다는 논리와 사실을 중심으로 사고하는 유형입니다. 공감 표현은 적을 수 있지만, 실제로는 실용적인 도움을 주는 데 능숙합니다.")