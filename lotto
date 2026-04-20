import streamlit as st
import random
import io

def ball_color(num):
    if num <= 10:
        return "#f44336"
    if num <= 20:
        return "#ff9800"
    if num <= 30:
        return "#ffeb3b"
    if num <= 40:
        return "#03a9f4"
    return "#8bc34a"

def draw_one_set(with_bonus: bool):
    pool = list(range(1, 46))
    random.shuffle(pool)
    main = sorted(pool[:6])
    bonus = None
    if with_bonus:
        bonus = random.choice(pool[6:])
    return {"main": main, "bonus": bonus}

def format_sets_text(sets):
    lines = []
    for i, s in enumerate(sets, start=1):
        main_str = ", ".join(str(n) for n in s["main"])
        if s.get("bonus") is not None:
            lines.append(f"#{i}: {main_str} (보너스: {s['bonus']})")
        else:
            lines.append(f"#{i}: {main_str}")
    return "\n".join(lines)

def render_sets_html(sets):
    html = '<div style="font-family:Arial, sans-serif; max-width:900px;">'
    for idx, s in enumerate(sets, start=1):
        html += (
            '<div style="display:flex; align-items:center; gap:8px; '
            'margin:8px 0; padding:10px; background:#fff; border-radius:8px; '
            'box-shadow:0 1px 3px rgba(0,0,0,0.06);">'
        )
        html += f'<div style="font-weight:600; min-width:48px; text-align:center">#{idx}</div>'
        for n in s["main"]:
            color = ball_color(n)
            text_color = "#222" if 21 <= n <= 30 else "#fff"
            html += (
                f'<div style="width:48px; height:48px; border-radius:50%; background:{color}; '
                f'color:{text_color}; display:flex; align-items:center; justify-content:center; '
                f'font-weight:700; box-shadow:0 2px 4px rgba(0,0,0,0.15); margin-right:6px;">{n}</div>'
            )
        if s.get("bonus") is not None:
            html += '<div style="margin-left:8px; margin-right:6px; font-size:90%;">보너스</div>'
            html += (
                f'<div style="width:48px; height:48px; border-radius:50%; background:#fff9db; color:#222; '
                f'border:3px solid gold; display:flex; align-items:center; justify-content:center; '
                f'font-weight:700;">{s["bonus"]}</div>'
            )
        html += '</div>'
    html += '</div>'
    return html

st.set_page_config(page_title="로또 번호 추첨기", layout="centered")
st.title("로또 번호 추첨기")

col1, col2 = st.columns([2,1])
with col1:
    sets = st.number_input("세트 수", min_value=1, max_value=10, value=1, step=1)
with col2:
    with_bonus = st.checkbox("보너스 포함", value=False)

col_btns = st.columns([1,1,1])
with col_btns[0]:
    if st.button("추첨하기"):
        results = [draw_one_set(with_bonus) for _ in range(sets)]
        st.session_state["results"] = results
with col_btns[1]:
    if st.button("결과 복사(클립보드)"):
        if "results" not in st.session_state:
            st.warning("먼저 추첨하세요.")
        else:
            text = format_sets_text(st.session_state["results"])
            st.markdown(
                f"""
                <script>
                (async function() {{
                  try {{
                    await navigator.clipboard.writeText({repr(text)});
                    alert('결과가 클립보드에 복사되었습니다.');
                  }} catch (e) {{
                    var ok = prompt('클립보드 접근이 제한되어 자동 복사가 실패했습니다. 아래 텍스트를 직접 복사하세요:', {repr(text)});
                  }}
                }})();
                </script>
                """,
                unsafe_allow_html=True,
            )
with col_btns[2]:
    if st.button("파일 다운로드(.txt)"):
        if "results" not in st.session_state:
            st.warning("먼저 추첨하세요.")
        else:
            text = format_sets_text(st.session_state["results"])
            buffer = io.BytesIO()
            buffer.write(text.encode("utf-8"))
            buffer.seek(0)
            st.download_button("다운로드 시작", data=buffer, file_name="lotto_results.txt", mime="text/plain")

st.markdown("---")
if "results" in st.session_state:
    st.markdown(render_sets_html(st.session_state["results"]), unsafe_allow_html=True)
    st.markdown("**텍스트 형식:**")
    st.code(format_sets_text(st.session_state["results"]), language="text")
else:
    st.info("추첨 버튼을 눌러 로또 번호를 생성하세요.")
