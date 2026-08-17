import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="เกมร้องเพลงตามคำ",
    page_icon="🎤",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------- คลังคำศัพท์ -----------------
words_start_th = [
    "ก็", "เก็บ", "กี่", "ก่อน", "การ", "กลับ", "เขา", "ขอ", "ความ", "คน", "แค่", 
    "คำ", "เคย", "คอย", "ใคร", "คุณ", "คิด", "คืน", "งาม", "เจ็บ", "จริง", "จาก", 
    "จำ", "ใจ", "จะ", "จิต", "ฉัน", "ชอบ", "เชื่อ", "ใช่", "ชีวิต", "ช่วง", "ชื่น", "เด็ก", 
    "ได้", "ดอก", "ดั่ง", "ดาว", "เดือน", "ดู", "เดี๋ยว", "ตั้งแต่", "ตอน", "ตาย", "ตื่น", "แต่", 
    "ต่อ", "ตราบ", "ถ้า", "ถาม", "ถึง", "ทำไม", "ทาง", "ที่", "ท่ามกลาง", "ทำ", "ทุก", "เธอ", "ทรมาน", 
    "ใน", "นอก", "นาน", "นี่", "นั่น", "หน้า", "หนู", "นึก", "บน", "บาง", "บ่", "บท", 
    "บอก", "แปลก", "ไป", "เปลี่ยน", "ปล่อย", "เป็น", "ปิด", "เปิด", "ปาก", "ปี", "ผม", "ผ่าน", 
    "ผู้", "ผิด", "ฝาก", "ฝน", "เพื่อน", "เพื่อ", "เพลง", "เพราะ", "พบ", "พี่", "พอ", 
    "พรุ่งนี้", "เพิ่ง", "ฟัง", "แฟน", "ภาพ", "ภูมิ", "เมื่อ", "มา", "มี", "เหมือน", "มัน", "แม้", "ไม่", 
    "ยัง", "ยอม", "ยาม", "ยิ่ง", "ยิ้ม", "รอ", "แล้ว", "วัน", "สิ่ง", "หมด", "หยุด", "อยาก", "อยู่", "อาจ"
]

words_start_en = [
    "You", "I", "Baby", "Never", "When", "Don't", "If", "Why", "Every", "Look", 
    "Please", "Tell", "Say", "Hey", "Let", "Sometimes", "Maybe", "Without", 
    "Nobody", "Cause", "Just", "Forever", "Before", "Nothing", "Somebody", 
    "Another", "Listen", "Remember", "Hold"
]

words_contain_th = [
    "ก็", "เก็บ", "กี่", "ก่อน", "การ", "กลับ", "เขา", "ขอ", "ความ", "คน", "แค่", 
    "คำ", "เคย", "คอย", "โคตร", "ใคร", "คุณ", "คิด", "คืน", "งาม", "เจ็บ", "จริง", "จาก", 
    "จำ", "ใจ", "จะ", "จิต", "ฉัน", "ชอบ", "เชื่อ", "ใช่", "ชีวิต", "ช่วง", "ชะตา", "ชื่น", "เด็ก", 
    "ได้", "ดอก", "ดั่ง", "ดาว", "เดือน", "ดู", "เดี๋ยว", "ตั้งแต่", "ตอน", "ตาย", "ตื่น", "แต่", 
    "ต่อ", "ตราบ", "ถ้า", "ถาม", "ถึง", "ทำไม", "ทาง", "ที่", "ท่ามกลาง", "ทำ", "ทุก", "เธอ", "ทรมาน", 
    "ใน", "นอก", "นาน", "นิทาน", "นี่", "นั่น", "หน้า", "หนู", "นึก", "บน", "บาง", "บ่", "บท", 
    "บอก", "แปลก", "ไป", "เปลี่ยน", "ปล่อย", "เป็น", "ปิด", "เปิด", "ปาก", "ปี", "ผม", "ผ่าน", 
    "ผู้", "ผิด", "ฝาก", "ฝน", "พายุ", "เพื่อน", "เพื่อ", "เพลง", "เพราะ", "พบ", "พี่", "พอ", 
    "พรุ่งนี้", "เพิ่ง", "ฟัง", "ฟ้า", "แฟน", "ภาพ", "ภูมิ", "เมื่อ", "มา", "มี", "เหมือน", "มัน", "แม้", "ไม่", 
    "ยัง", "ยอม", "ยาม", "ยิ่ง", "ยิ้ม", "ยื้อ", "รอ", "ฤดู", "แล้ว", "วัน", "วิ่ง", "สิ่ง", "เสียง", "แสง", 
    "หมด", "หยุด", "หัวใจ", "อยาก", "อยู่", "อาจ"
]

words_contain_en = [
    "Amazing", "Admire", "Adult", "Away", "Adore", "And", "Another", "Apart", "Across", 
    "Believe", "Bear", "Because", "Begin", "Better", "Both", "Best", "Bad", "Burn", 
    "Cat", "Can", "Call", "Cold", "Cool", "Calm", "Sad", "Mad", "You", "I", "Baby", "Never", 
    "When", "Don't", "If", "Why", "Every", "Look", "Please", "Tell", "Say", "Hey", "Let", 
    "Sometimes", "Maybe", "Without", "Nobody", "Cause", "Just", "Forever", "Before", "Nothing", 
    "Somebody", "Another", "Listen", "Remember", "Hold", "Love", "Heart", "Rain", "Night", "Tonight", 
    "Eyes", "Sky", "Fire", "Home", "World", "Star", "Dream", "Time", "Mind", "Tears", "Dance", "Crazy", 
    "Alone", "Sun", "Life", "Call", "Forever", "Shadow", "Magic", "Secret"
]

# ปลดล็อกขอบหน้าจอ Streamlit ให้อิสระ 100%
st.markdown("""
    <style>
    header[data-testid="stHeader"], section[data-testid="stSidebar"] {
        display: none !important;
    }
    .stApp {
        background: linear-gradient(135deg, #d3e1e8 0%, #e0d7ec 40%, #eddcf5 75%, #ded0ea 100%) !important;
    }
    .main .block-container {
        padding: 0 !important;
        max-width: 100% !important;
        margin: 0 !important;
    }
    iframe {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
        z-index: 1 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- HTML / CSS / JS Responsive Application -----------------
html_code = f"""
<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<style>
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        user-select: none;
        -webkit-tap-highlight-color: transparent;
    }}

    body {{
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
        min-height: 100vh;
        width: 100vw;
        background: transparent;
        padding: 5vh 0 4vh 0;
        overflow-y: auto;
        overflow-x: hidden;
    }}

    /* การ์ดเกมหลัก (การ์ดบน) */
    .card {{
        width: 90%;
        max-width: 820px;
        min-height: 480px;
        background: rgba(255, 255, 255, 0.58);
        backdrop-filter: blur(30px);
        -webkit-backdrop-filter: blur(30px);
        border-radius: 28px;
        border: 1.5px solid rgba(255, 255, 255, 0.85);
        box-shadow: 0 15px 40px rgba(90, 70, 110, 0.08);
        padding: 24px 35px 35px 35px;
        position: relative;
        display: flex;
        flex-direction: column;
        align-items: center;
    }}

    /* แถบเมนูด้านบนสุด */
    .top-bar {{
        width: 100%;
        display: flex;
        justify-content: flex-end;
        align-items: center;
        height: 32px;
        margin-bottom: 5px;
    }}

    .menu-btn {{
        font-size: 24px;
        background: transparent;
        border: none;
        color: #2D283E;
        cursor: pointer;
        line-height: 1;
        padding: 4px;
    }}

    /* แถว Heading + ปุ่ม ⇄ */
    .heading-wrapper {{
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        margin-bottom: 15px;
        width: 100%;
    }}

    .heading-title {{
        font-size: 22px;
        font-weight: 700;
        color: #2D283E;
        text-align: center;
        white-space: nowrap;
    }}

    /* ปุ่มสลับโหมด ⇄ */
    .switch-btn {{
        background: rgba(255, 255, 255, 0.75);
        color: #2D283E;
        border: 1.5px solid rgba(45, 40, 62, 0.25);
        font-size: 15px;
        font-weight: 700;
        border-radius: 10px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
        width: 32px;
        height: 28px;
        flex-shrink: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.2s ease;
    }}

    .switch-btn:hover {{
        background: #FFFFFF;
        border-color: #2D283E;
        transform: scale(1.08);
    }}

    /* แถบปุ่มภาษา TH / EN */
    .lang-wrapper {{
        display: flex;
        gap: 10px;
        justify-content: center;
    }}

    .lang-btn {{
        border-radius: 16px;
        font-weight: 700;
        padding: 4px 18px;
        font-size: 13px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.06);
        cursor: pointer;
        transition: all 0.2s ease;
    }}

    .lang-btn.inactive {{
        background-color: #FFFFFF;
        color: #2D283E;
        border: none;
    }}

    .lang-btn.active {{
        background-color: rgba(45, 40, 62, 0.20);
        color: #2D283E;
        border: 1.5px solid #2D283E;
    }}

    /* กล่องข้อความคำสุ่ม */
    .word-text {{
        flex: 1;
        width: 100%;
        font-size: 64px;
        font-weight: 800;
        color: #2D283E;
        letter-spacing: 1px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 20px 0;
        word-break: break-word;
        transition: font-size 0.2s ease, opacity 0.2s ease;
    }}

    /* สถานะเมื่อแสดงข้อความเริ่มต้น "เริ่มสุ่มคำได้เลย !" */
    .word-text.placeholder {{
        font-size: 34px;
        font-weight: 600;
        color: #8C849E;
        letter-spacing: 0px;
    }}

    /* ปุ่มสุ่มคำใหม่ */
    .random-btn {{
        background-color: #3E3848;
        color: #FFFFFF;
        border-radius: 100px;
        border: none;
        padding: 10px 40px;
        font-size: 15px;
        font-weight: 500;
        box-shadow: 0 4px 12px rgba(0,0,0,0.12);
        cursor: pointer;
        transition: background-color 0.2s ease, transform 0.1s ease;
    }}

    .random-btn:hover {{
        background-color: #635C6E;
    }}

    .random-btn:active {{
        transform: scale(0.98);
    }}

    /* การ์ดวิธีเล่นเกม (การ์ดแยกด้านล่าง) */
    .instruction-card {{
        width: 90%;
        max-width: 820px;
        margin-top: 18px;
        background: rgba(255, 255, 255, 0.48);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border: 1.5px solid rgba(255, 255, 255, 0.8);
        border-radius: 22px;
        padding: 16px 28px;
        color: #4C455A;
        font-size: 13.5px;
        line-height: 1.6;
        box-shadow: 0 10px 30px rgba(90, 70, 110, 0.05);
        display: flex;
        flex-direction: column;
        align-items: center;
    }}

    .instruction-header {{
        font-weight: 700;
        color: #2D283E;
        margin-bottom: 8px;
        font-size: 14.5px;
    }}

    .instruction-list {{
        margin: 0;
        padding-left: 20px;
        width: 100%;
        max-width: 620px;
    }}

    .instruction-list li {{
        margin-bottom: 3px;
    }}

    .icon-badge {{
        display: inline-block;
        padding: 0 5px;
        font-size: 12px;
        background: rgba(45, 40, 62, 0.09);
        border-radius: 5px;
        font-weight: bold;
        color: #2D283E;
        vertical-align: baseline;
    }}

    /* ----------------- Modal Popup เพิ่มคำ (ธีมสว่าง Glassmorphism) ----------------- */
    .modal-overlay {{
        position: fixed;
        top: 0; 
        left: 0; 
        width: 100vw; 
        height: 100vh;
        background: rgba(45, 40, 62, 0.22);
        display: none;
        align-items: center;
        justify-content: center;
        z-index: 9999;
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        padding: 20px;
    }}

    .modal-card {{
        background: rgba(255, 255, 255, 0.88);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        color: #2D283E;
        padding: 26px 28px;
        border-radius: 24px;
        width: 100%;
        max-width: 390px;
        border: 1.5px solid rgba(255, 255, 255, 0.95);
        box-shadow: 0 20px 45px rgba(90, 70, 110, 0.14);
    }}

    .modal-title {{
        font-size: 19px;
        font-weight: 700;
        color: #2D283E;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 6px;
    }}

    .modal-label {{
        font-size: 13px;
        font-weight: 600;
        margin: 10px 0 6px 0;
        color: #554F66;
    }}

    .modal-input, .modal-select {{
        width: 100%;
        padding: 9px 14px;
        background: rgba(255, 255, 255, 0.9);
        color: #2D283E;
        border: 1.5px solid rgba(45, 40, 62, 0.15);
        border-radius: 12px;
        font-size: 14px;
        outline: none;
        margin-bottom: 12px;
        transition: all 0.2s ease;
    }}

    .modal-input:focus, .modal-select:focus {{
        border-color: #2D283E;
        background: #FFFFFF;
        box-shadow: 0 0 0 3px rgba(45, 40, 62, 0.08);
    }}

    .modal-input::placeholder {{
        color: #A09BAE;
    }}

    .modal-actions {{
        display: flex;
        gap: 10px;
        margin-top: 18px;
    }}

    .modal-btn {{
        flex: 1;
        padding: 10px 0;
        border-radius: 14px;
        border: none;
        cursor: pointer;
        font-weight: 600;
        font-size: 14px;
        transition: all 0.2s ease;
    }}

    .modal-save {{ 
        background: #3E3848; 
        color: #FFFFFF; 
        box-shadow: 0 4px 12px rgba(62, 56, 72, 0.2);
    }}
    .modal-save:hover {{ 
        background: #5A5266; 
    }}

    .modal-close {{ 
        background: rgba(45, 40, 62, 0.08); 
        color: #2D283E; 
    }}
    .modal-close:hover {{ 
        background: rgba(45, 40, 62, 0.15); 
    }}

    /* ----------------- กฎ Responsive สำหรับหน้าจอมือถือ (<= 600px) ----------------- */
    @media (max-width: 600px) {{
        body {{
            padding: 3vh 0 3vh 0;
        }}
        .card {{
            width: 92%;
            min-height: 480px;
            padding: 18px 18px 26px 18px;
            border-radius: 24px;
        }}
        .top-bar {{
            height: 28px;
            margin-bottom: 2px;
        }}
        .menu-btn {{
            font-size: 22px;
        }}
        .heading-wrapper {{
            margin-bottom: 12px;
            gap: 6px;
        }}
        .heading-title {{
            font-size: 15px;
            line-height: 1.2;
        }}
        .switch-btn {{
            width: 28px;
            height: 26px;
            font-size: 12px;
        }}
        .word-text {{
            font-size: 52px;
            padding: 15px 0;
        }}
        .word-text.placeholder {{
            font-size: 25px;
        }}
        .random-btn {{
            width: 85%;
            padding: 12px 0;
            font-size: 16px;
        }}
        .instruction-card {{
            width: 92%;
            margin-top: 14px;
            padding: 14px 16px;
            font-size: 12px;
            border-radius: 20px;
        }}
        .instruction-list {{
            padding-left: 16px;
        }}
    }}
</style>
</head>
<body>

<!-- 1. การ์ดเกมหลัก -->
<div class="card">
    <div class="top-bar">
        <button class="menu-btn" onclick="openModal()">☰</button>
    </div>

    <div class="heading-wrapper">
        <div class="heading-title" id="headingText">🎤 ร้องเพลงที่ขึ้นต้นด้วยคำว่า...</div>
        <button class="switch-btn" onclick="toggleMode()" title="คลิกเพื่อสลับโหมด">⇄</button>
    </div>

    <div class="lang-wrapper">
        <button class="lang-btn active" id="btnTH" onclick="setLang('TH')">TH</button>
        <button class="lang-btn inactive" id="btnEN" onclick="setLang('EN')">EN</button>
    </div>

    <div class="word-text placeholder" id="displayWord">เริ่มสุ่มคำได้เลย !</div>

    <button class="random-btn" onclick="randomWord()">สุ่มคำใหม่</button>
</div>

<!-- 2. การ์ดวิธีเล่นเกม (แยกกล่องด้านล่าง) -->
<div class="instruction-card">
    <div class="instruction-header">🎤 วิธีเล่นเกม 🎮</div>
    <ol class="instruction-list">
        <li>เลือกโหมดระหว่าง "ร้องเพลงที่ขึ้นต้นด้วยคำว่า..." กับ "ร้องเพลงที่มีคำว่า..."</li>
        <li>เลือกภาษาของเพลง</li>
        <li>กดปุ่มสุ่มคำใหม่</li>
        <li>หากต้องการเพิ่มคำ กดที่เมนู <span class="icon-badge">☰</span> แล้วเพิ่มคำที่ต้องการ</li>
    </ol>
</div>

<!-- Modal Popup (ธีมสว่าง) -->
<div class="modal-overlay" id="modalOverlay">
    <div class="modal-card">
        <div class="modal-title">➕ เพิ่มคำศัพท์ใหม่</div>
        
        <div class="modal-label">เลือกโหมดเกม:</div>
        <select class="modal-select" id="addMode">
            <option value="start">ขึ้นต้นด้วยคำว่า...</option>
            <option value="contain">มีคำว่า...ในเพลง</option>
        </select>

        <div class="modal-label">เลือกภาษา:</div>
        <select class="modal-select" id="addLang">
            <option value="TH">ภาษาไทย (TH)</option>
            <option value="EN">English (EN)</option>
        </select>

        <div class="modal-label">พิมพ์คำศัพท์ (คั่นด้วยจุลภาคได้):</div>
        <input type="text" class="modal-input" id="addWordInput" placeholder="เช่น รัก, ฝัน, เธอ">

        <div class="modal-actions">
            <button class="modal-btn modal-close" onclick="closeModal()">ยกเลิก</button>
            <button class="modal-btn modal-save" onclick="saveNewWords()">บันทึก</button>
        </div>
    </div>
</div>

<script>
    const words = {{
        start_th: {json.dumps(words_start_th, ensure_ascii=False)},
        start_en: {json.dumps(words_start_en, ensure_ascii=False)},
        contain_th: {json.dumps(words_contain_th, ensure_ascii=False)},
        contain_en: {json.dumps(words_contain_en, ensure_ascii=False)}
    }};

    let currentMode = "start";
    let currentLang = "TH";

    function resetToPrompt() {{
        const wordEl = document.getElementById("displayWord");
        wordEl.innerText = "เริ่มสุ่มคำได้เลย !";
        wordEl.classList.add("placeholder");
    }}

    function updateView() {{
        const heading = document.getElementById("headingText");
        heading.innerText = currentMode === "start" ? "🎤 ร้องเพลงที่ขึ้นต้นด้วยคำว่า..." : "🎤 ร้องเพลงที่มีคำว่า...";
        
        document.getElementById("btnTH").className = currentLang === "TH" ? "lang-btn active" : "lang-btn inactive";
        document.getElementById("btnEN").className = currentLang === "EN" ? "lang-btn active" : "lang-btn inactive";
        
        resetToPrompt();
    }}

    function toggleMode() {{
        currentMode = currentMode === "start" ? "contain" : "start";
        updateView();
    }}

    function setLang(lang) {{
        if (currentLang !== lang) {{
            currentLang = lang;
            updateView();
        }}
    }}

    function randomWord() {{
        const poolKey = `${{currentMode}}_${{currentLang.toLowerCase()}}`;
        const pool = words[poolKey];
        if (pool && pool.length > 0) {{
            const randIndex = Math.floor(Math.random() * pool.length);
            const wordEl = document.getElementById("displayWord");
            wordEl.innerText = pool[randIndex];
            wordEl.classList.remove("placeholder");
        }}
    }}

    function openModal() {{
        document.getElementById("modalOverlay").style.display = "flex";
    }}

    function closeModal() {{
        document.getElementById("modalOverlay").style.display = "none";
        document.getElementById("addWordInput").value = "";
    }}

    function saveNewWords() {{
        const input = document.getElementById("addWordInput").value.trim();
        if (!input) return;

        const mode = document.getElementById("addMode").value;
        const lang = document.getElementById("addLang").value.toLowerCase();
        const poolKey = `${{mode}}_${{lang}}`;

        const newItems = input.split(",").map(w => w.trim()).filter(w => w);
        words[poolKey].push(...newItems);

        currentMode = mode;
        currentLang = document.getElementById("addLang").value;
        
        const heading = document.getElementById("headingText");
        heading.innerText = currentMode === "start" ? "🎤 ร้องเพลงที่ขึ้นต้นด้วยคำว่า..." : "🎤 ร้องเพลงที่มีคำว่า...";
        document.getElementById("btnTH").className = currentLang === "TH" ? "lang-btn active" : "lang-btn inactive";
        document.getElementById("btnEN").className = currentLang === "EN" ? "lang-btn active" : "lang-btn inactive";

        const wordEl = document.getElementById("displayWord");
        wordEl.innerText = newItems[newItems.length - 1];
        wordEl.classList.remove("placeholder");

        closeModal();
    }}
</script>
</body>
</html>
"""

components.html(html_code, height=950)
