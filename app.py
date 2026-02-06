import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Doctor Please Help 🩺💗", layout="centered")

html("""
<style>
    * {
        box-sizing: border-box;
    }

    body {
        margin: 0;
        background: linear-gradient(180deg, #ff69b4, #ff85c1);
        font-family: "Segoe UI", sans-serif;
        -webkit-tap-highlight-color: transparent;
    }

    .screen {
        min-height: 100vh;
        display: none;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 20px;
    }

    .active {
        display: flex;
    }

    .card {
        background: white;
        padding: 28px 22px;
        border-radius: 22px;
        width: 100%;
        max-width: 420px;
        text-align: center;
        box-shadow: 0 16px 36px rgba(0,0,0,0.18);
    }

    h2 {
        color: #ff2f92;
        margin-bottom: 12px;
        font-size: 22px;
    }

    p, li {
        color: #444;
        font-size: 16px;
        line-height: 1.5;
    }

    ul {
        text-align: left;
        padding-left: 18px;
        margin: 10px 0;
    }

    .buttons {
        margin-top: 20px;
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
        justify-content: center;
        width: 100%;
        max-width: 420px;
    }

    button {
        padding: 14px 22px;
        border-radius: 14px;
        border: none;
        background: linear-gradient(135deg, #ff69b4, #ff85c1);
        color: white;
        font-size: 15px;
        font-weight: 600;
        cursor: pointer;
        box-shadow: 0 6px 16px rgba(255,105,180,0.55);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
        min-width: 120px;
    }

    button:active {
        transform: scale(0.97);
        box-shadow: 0 4px 12px rgba(255,105,180,0.4);
    }

    .checkbox {
        text-align: left;
        margin-top: 10px;
        color: #444;
        font-size: 15px;
    }

    .checkbox input {
        margin-right: 8px;
        transform: scale(1.1);
    }

    .pink-screen {
        position: fixed;
        inset: 0;
        background: #ff69b4;
        display: none;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: white;
        text-align: center;
        padding: 24px;
        z-index: 9999;
    }

    .pink-screen h1 {
        font-size: 26px;
        margin-bottom: 12px;
    }

    .pink-screen p {
        font-size: 16px;
        opacity: 0.95;
    }

    .retry {
        margin-top: 26px;
        background: white;
        color: #ff2f92;
        padding: 14px 26px;
        border-radius: 16px;
        font-weight: 700;
    }

    @media (max-width: 360px) {
        h2 { font-size: 20px; }
        p, li { font-size: 15px; }
        button { font-size: 14px; }
    }
</style>


<div id="p1" class="screen active">
    <div class="card">
        <h2>Welcome Dr. Aditi 🌸</h2>
        <p>We urgently need your medical expertise 🩺💗</p>
    </div>
    <div class="buttons">
        <button onclick="go(2)">✨ Start Case ✨</button>
    </div>
</div>

<div id="p2" class="screen">
   <div class="card">
    <h2>🗂 Case History</h2>

    <p><b>Name:</b> Aryan</p>
    <p><b>Age:</b> 23</p>
    <p><b>Profession:</b> Engineer (overthinks everything 🧠)</p>
    <p><b>Hobby:</b> Cooking comfort food with extra care 👨‍🍳</p>
    <p><b>Primary Complaint:</b> Missing someone way too much 👉🏻👈🏻</p>
    <p><b>Trigger:</b> One message from her 💬</p>
    <p><b>Prognosis:</b> Improves instantly with attention 💗</p>
</div>

    <div class="buttons">
        <button onclick="go(3)">Next ➡️</button>
    </div>
</div>

<div id="p3" class="screen">
    <div class="card">
        <h2>🩺 Symptoms</h2>
        <ul>
            <li>Zoning out 🥲</li>
            <li>Smiling at phone 🫠</li>
            <li>Thinking all day 🤦🏻‍♂️</li>
            <li>Heartbeat increases on notifications 💓</li>
        </ul>
    </div>
    <div class="buttons">
        <button onclick="go(4)">Proceed 💊</button>
    </div>
</div>

<div id="p4" class="screen">
    <div class="card">
        <h2>💖 Prescription</h2>

        <div class="checkbox"><input type="checkbox"> Cute pictures 📸</div>
        <div class="checkbox"><input type="checkbox"> Meet someday 🫂</div>
        <div class="checkbox"><input type="checkbox"> Maybe Video calls 📱</div>
        <div class="checkbox"><input type="checkbox"> Voice notes 🎧</div>
        <div class="checkbox"><input type="checkbox"> Cute Dosa dates ☕🍰</div>
     <p id="error" style="
    color:#ff2f92;
    font-weight:600;
    margin-top:16px;
    display:none;
"></p>


    </div>
     
    <div class="buttons">
        <button onclick="validate()">Submit Prescription</button>
    </div>
</div>

<div id="p5" class="screen">
    <div class="card">
        <h2>🥺 Final Question</h2>
        <p>Will you treat this patient <b>forever</b>?</p>
    </div>
    <div class="buttons">
        <button onclick="yes()">YES 🧿</button>
        <button onclick="nope('maybe')">Maybe 😏</button>
        <button onclick="nope('no')">No 🙃</button>
    </div>
</div>

<div class="pink-screen" id="pink">
    <h1 id="msg"></h1>
    <p>This page refuses to continue without a YES 🧿</p>
    <button class="retry" onclick="retry()">Retry 💗</button>
</div>

<script>
    function go(n) {
        document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
        document.getElementById('p' + n).classList.add('active');
        heart();
    }

    
    function validate() {
    const checks = document.querySelectorAll('#p4 input[type="checkbox"]');
    const errorBox = document.getElementById("error");

    const cuteErrors = [
        "Doctor 😌 please don’t miss any medicine… this patient is very serious 💗",
        "Uh-oh 🩺💔 incomplete prescription detected! Patient still missing you badly.",
        "Emergency alert 🚨💗 All doses must be given, doctor!",
        "Doctor, half treatment won’t work here… full care required 😏💖",
        "Patient condition critical 😔 missing a few very important medicines!",
        "Oops 😌 looks like dosage is incomplete… please prescribe everything"
    ];

    if ([...checks].every(c => c.checked)) {
        errorBox.style.display = "none";
        go(5);
    } else {
        const msg = cuteErrors[Math.floor(Math.random() * cuteErrors.length)];
        errorBox.innerText = msg;
        errorBox.style.display = "block";
    }
}



    function yes() {
        heart();
        alert("💖 THANK YOU DOCTOR\\nPatient saved for life!");
    }

    function nope(type) {
        document.getElementById("pink").style.display = "flex";
        document.getElementById("msg").innerText =
            type === "maybe"
            ? "Patient needs you… badly 🥺💗"
            : "Emergency! Doctor please reconsider 😭💘";
    }

    function retry() {
        document.getElementById("pink").style.display = "none";
    }

    function heart() {
        const h = document.createElement("div");
        h.innerHTML = "💗";
        h.style.position = "fixed";
        h.style.left = Math.random() * 100 + "vw";
        h.style.bottom = "0";
        h.style.fontSize = "22px";
        h.style.animation = "float 2s ease-out forwards";
        document.body.appendChild(h);
        setTimeout(() => h.remove(), 2000);
    }

    const style = document.createElement("style");
    style.innerHTML = `
        @keyframes float {
            0% { transform: translateY(0); opacity: 1; }
            100% { transform: translateY(-140px); opacity: 0; }
        }
    `;
    document.head.appendChild(style);
</script>
""", height=1000)
