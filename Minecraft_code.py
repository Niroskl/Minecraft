<!doctype html>
<html lang="he">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>מוקד 105 - משחק</title>
  <style>
    :root{--bg:#0f1724;--card:#0b1220;--accent:#06b6d4;--text:#e6eef6;}
    *{box-sizing:border-box;font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;}
    body{margin:0;min-height:100vh;background:linear-gradient(180deg,#021124 0%, #052033 100%);color:var(--text);display:flex;align-items:center;justify-content:center;padding:20px;direction:rtl}
    .app{width:100%;max-width:900px;background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));border-radius:14px;padding:22px;box-shadow:0 10px 30px rgba(2,6,23,0.6)}
    header{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
    h1{margin:0;font-size:20px}
    .stats{display:flex;gap:12px;align-items:center}
    .stat{background:rgba(255,255,255,0.03);padding:8px 12px;border-radius:10px;font-size:14px}
    main{display:grid;grid-template-columns:1fr 360px;gap:18px}
    .card{background:var(--card);padding:16px;border-radius:12px;min-height:220px}
    .scenario-title{font-weight:700;margin-bottom:8px}
    .scenario-text{font-size:16px;line-height:1.45;margin-bottom:12px}
    .choices{display:flex;flex-direction:column;gap:10px}
    .choice{background:rgba(255,255,255,0.03);padding:12px;border-radius:10px;border:2px solid transparent;cursor:pointer;font-size:15px}
    .choice:hover{transform:translateY(-3px)}
    .choice.correct{border-color:rgba(34,197,94,0.8);background:linear-gradient(90deg, rgba(34,197,94,0.08), rgba(255,255,255,0.01))}
    .choice.wrong{border-color:rgba(239,68,68,0.8);background:linear-gradient(90deg, rgba(239,68,68,0.04), rgba(255,255,255,0.01))}
    .right-now{font-weight:700;margin-bottom:6px;}
    .timer-bar{height:10px;background:rgba(255,255,255,0.06);border-radius:999px;overflow:hidden;margin-bottom:12px}
    .timer-fill{height:100%;width:100%;background:linear-gradient(90deg,var(--accent),#4f46e5)}
    .side{display:flex;flex-direction:column;gap:12px}
    .log{background:rgba(255,255,255,0.02);padding:12px;border-radius:10px;max-height:260px;overflow:auto;font-size:14px}
    .controls{display:flex;gap:8px}
    button{background:var(--accent);border:none;color:#022;padding:8px 12px;border-radius:10px;font-weight:700;cursor:pointer}
    button.secondary{background:transparent;border:1px solid rgba(255,255,255,0.06);color:var(--text);font-weight:600}
    .footer{margin-top:14px;text-align:center;color:rgba(230,238,246,0.6);font-size:13px}
    .center{display:flex;align-items:center;justify-content:center}
    .overlay{position:fixed;inset:0;background:rgba(1,6,12,0.6);display:flex;align-items:center;justify-content:center}
    .modal{background:#071226;padding:20px;border-radius:12px;max-width:520px;width:94%}
    .bigscore{font-size:36px;font-weight:800;margin:10px 0}
    .small{font-size:14px;color:rgba(230,238,246,0.7)}
    @media (max-width:800px){
      main{grid-template-columns:1fr; }
      .side{order:2}
    }
  </style>
</head>
<body>
  <div class="app" role="application" aria-label="משחק מוקד 105">
    <header>
      <h1>מוקד 105 — תרגול מהיר</h1>
      <div class="stats">
        <div class="stat">נקודות: <span id="score">0</span></div>
        <div class="stat">שלב: <span id="level">1</span></div>
        <div class="stat">זמן לכל שיחה: <span id="timePer">15</span> שניות</div>
      </div>
    </header>

    <main>
      <section>
        <div class="card" id="scenarioCard" aria-live="polite">
          <div class="right-now">שיחה #<span id="roundNum">1</span></div>
          <div class="scenario-title" id="scenarioTitle">ממתין לתרחיש...</div>
          <div class="scenario-text" id="scenarioText">לחץ "התחל" כדי לקבל שיחה.</div>

          <div class="timer-bar" aria-hidden="true">
            <div class="timer-fill" id="timerFill" style="width: 100%"></div>
          </div>

          <div class="choices" id="choices"></div>
        </div>

        <div class="footer">
          הוראות: קרא את התרחיש ובחר את הפעולה המיידית הנכונה. זה משחק חינוכי בלבד — אם יש מצב חירום אמיתי, התקשר/י לגורמי החירום המתאימים.
        </div>
      </section>

      <aside class="side">
        <div class="card">
          <div style="display:flex;align-items:center;justify-content:space-between">
            <div>
              <div style="font-weight:800;font-size:18px">יומן שיחות</div>
              <div style="font-size:13px;color:rgba(230,238,246,0.7)">רשומות אחרונות של התגובות שלך</div>
            </div>
            <div>
              <button id="startBtn">התחל</button>
            </div>
          </div>

          <div class="log" id="log" aria-live="polite" style="margin-top:12px">אין עדיין שיחות.</div>

          <div style="margin-top:12px" class="controls">
            <button class="secondary" id="settingsBtn">הגדרות</button>
            <button class="secondary" id="resetBtn">אפס משחק</button>
          </div>
        </div>

        <div class="card center">
          <div>
            <div style="font-weight:700">הסבר ניקוד</div>
            <div style="margin-top:8px" class="small">תשובה נכונה בזמן — +100 נקודות. תשובה נכונה מהר במיוחד — בונוס. תשובה שגויה או פסק זמן — -50 נקודות.</div>
          </div>
        </div>
      </aside>
    </main>
  </div>

  <!-- תבניות מודאל -->
  <div id="modalRoot" style="display:none"></div>

  <script>
    // רשימת תרחישים (הוסף עוד לפי רצון)
    const SCENARIOS = [
      {
        title: "התעלפות פתאומית",
        text: "שולח התקשר/ה: 'אדם נפל והאיש אינו מגיב, נשמע נשימה לא סדירה'. מה עושים קודם?",
        choices: [
          { text: "שואלים אם האדם נושם ובודקים תגובה - מתקרבים בזהירות", correct: true },
          { text: "מבקשים ממישהו אחר לקחת את האופניים של הקרוב ולרוץ לבית החולים", correct: false },
          { text: "שולחים צילום של המקום לאנשי מדיה חברתית", correct: false },
          { text: "ממליצים למתקשר לשים מים על האדם ולקפא את הראש במים", correct: false }
        ]
      },
      {
        title: "כאבי חזה",
        text: "שולח התקשר/ה: 'אדם מבוגר מתלונן על לחץ כבד בחזה והזעה קרה'. מה הבחירה הנכונה?",
        choices: [
          { text: "להמליץ לשכב ולהישאר רגועים ולחכות לאמבולנס; לשאול על נשימה ודופק", correct: true },
          { text: "להציע לתת תרופה שאינך יודע מה היא", correct: false },
          { text: "לספר בדיחה כדי לשכך את המתח", correct: false },
          { text: "להנחות את המתקשר לנסוע במהירות לבית החולים בעצמו", correct: false }
        ]
      },
      {
        title: "שריפה בדירה",
        text: "שולח התקשר/ה: 'עשן בבית, קהל מתכנס, יש דלתות נעולות'. מה צריך לומר ראשון?",
        choices: [
          { text: "להוציא כוחות כיבוי בשטח ולהעביר מיקום מדויק והאם יש לכודים", correct: true },
          { text: "להמליץ להיכנס לחדר עם הכי הרבה עשן כי שם יש יותר אוויר", correct: false },
          { text: "לבקש מהמתקשר לצלם וידאו של האש ולשלוח", correct: false },
          { text: "להמליץ לפתוח את החלונות ולשפוך מים מכלי אחסון קטנים", correct: false }
        ]
      },
      {
        title: "ילד ננעל ברכב",
        text: "שולח התקשר/ה: 'ילד ננעל ברכב בחנייה והטמפרטורה חמה'. מה ההנחיה הראשונית?",
        choices: [
          { text: "לשאול גיל הילד, רמת הכרה ומצב נשימה ולהודיע שיש לקרוא אמבולנס וחילוץ תוך כדי ניסיון להגיע לחלון", correct: true },
          { text: "להציע לפתוח את הרכב בכוח בלי לבדוק מצב בטיחות", correct: false },
          { text: "להמליץ לפוצץ שמשה כדי להוציא את הילד מיד", correct: false },
          { text: "לומר להמתין שעה ולראות אם הילד ישתחרר מבודק האוטופילוט", correct: false }
        ]
      },
      // ניתן להוסיף עוד תרחישים...
    ];

    // מצב המשחק
    let score = 0;
    let round = 0;
    let level = 1;
    let timePerQuestion = 15; // שניות, ישתנה לפי שלב
    let timer = null;
    let timeLeft = timePerQuestion;
    let currentScenario = null;

    // אלמנטים
    const scoreEl = document.getElementById('score');
    const levelEl = document.getElementById('level');
    const timePerEl = document.getElementById('timePer');
    const roundNumEl = document.getElementById('roundNum');
    const scenarioTitleEl = document.getElementById('scenarioTitle');
    const scenarioTextEl = document.getElementById('scenarioText');
    const choicesEl = document.getElementById('choices');
    const timerFillEl = document.getElementById('timerFill');
    const logEl = document.getElementById('log');
    const startBtn = document.getElementById('startBtn');
    const resetBtn = document.getElementById('resetBtn');
    const settingsBtn = document.getElementById('settingsBtn');

    function shuffleArray(a){
      for(let i=a.length-1;i>0;i--){
        const j=Math.floor(Math.random()*(i+1));
        [a[i],a[j]]=[a[j],a[i]];
      }
      return a;
    }

    function pickScenario(){
      // בחר תרחיש אקראי; אפשר להרחיב לדרגות קושי לפי level
      const choices = [...SCENARIOS];
      const idx = Math.floor(Math.random()*choices.length);
      return JSON.parse(JSON.stringify(choices[idx])); // העתק עמוק
    }

    function startRound(){
      clearInterval(timer);
      round++;
      roundNumEl.textContent = round;
      // שינויים דינמיים: מקטין זמן ככל שהשלב עולה
      timePerQuestion = Math.max(6, 15 - Math.floor((level-1)/1.5)); // דוגמה
      timeLeft = timePerQuestion;
      timePerEl.textContent = timePerQuestion;
      timerFillEl.style.width = '100%';

      currentScenario = pickScenario();
      scenarioTitleEl.textContent = currentScenario.title;
      scenarioTextEl.textContent = currentScenario.text;

      // הצגת אפשרויות מסודרות אקראית
      const choices = shuffleArray(currentScenario.choices.map(c => ({...c})));
      choicesEl.innerHTML = '';
      choices.forEach((c, idx) => {
        const btn = document.createElement('button');
        btn.className = 'choice';
        btn.textContent = (idx+1) + ". " + c.text;
        btn.onclick = () => handleChoice(c, btn);
        choicesEl.appendChild(btn);
      });

      // התחל טיימר
      timer = setInterval(() => {
        timeLeft -= 0.1;
        const pct = Math.max(0, timeLeft / timePerQuestion) * 100;
        timerFillEl.style.width = pct + '%';
        if(timeLeft <= 0){
          clearInterval(timer);
          handleTimeout();
        }
      },100);
    }

    function handleChoice(choiceObj, btnEl){
      // מנטר תשובה פעם אחת בלבד
      if(!btnEl || btnEl.disabled) return;
      // נטרל כפתורים
      const all = choicesEl.querySelectorAll('button');
      all.forEach(b => b.disabled = true);

      clearInterval(timer);

      const isCorrect = !!choiceObj.correct;
      if(isCorrect){
        // ציון: זמן שנותר משפיע על בונוס
        const base = 100;
        const bonus = Math.round(Math.max(0, timeLeft) * 5); // בונוס על מהירות
        score += base + bonus;
        btnEl.classList.add('correct');
        appendLog(`שאלה ${round}: תשובה נכונה (+${base}+${bonus}) — ${currentScenario.title}`);
      } else {
        score -= 50;
        btnEl.classList.add('wrong');
        appendLog(`שאלה ${round}: תשובה שגויה (-50) — ${currentScenario.title}`);
      }
      updateDisplay();

      // סימון תשובה נכונה אם המשתמש טעה
      if(!isCorrect){
        // הדגיש את הכפתור הנכון
        const allBtns = choicesEl.querySelectorAll('button');
        allBtns.forEach(b => {
          if(b !== btnEl && b.textContent.includes(getCorrectTextForCurrent())) {
            b.classList.add('correct');
          }
        });
      }

      // קידום שלב פשוט אחרי מספר סיבובים
      if(round % 5 === 0){
        level++;
        appendLog(`עולים לשלב ${level} — זמן לכל שיחה קוצר.`);
      }

      // המתנה קצרה ואז שאלה הבאה
      setTimeout(() => {
        startRound();
      }, 1200);
    }

    function handleTimeout(){
      // הפסד עקב זמן
      score -= 50;
      appendLog(`שאלה ${round}: פסק זמן (-50) — ${currentScenario.title}`);
      updateDisplay();
      const all = choicesEl.querySelectorAll('button');
      all.forEach(b => b.disabled = true);
      // הדגש תשובה נכונה
      all.forEach(b => {
        if(b.textContent.includes(getCorrectTextForCurrent())) b.classList.add('correct');
      });
      setTimeout(() => {
        startRound();
      }, 1200);
    }

    function getCorrectTextForCurrent(){
      if(!currentScenario) return '';
      const correct = currentScenario.choices.find(c => c.correct);
      return correct ? correct.text.slice(0,12) : ''; // שימוש בחיתוך כדי התאמה חלקית
    }

    function appendLog(text){
      const time = new Date().toLocaleTimeString('he-IL');
      const entry = document.createElement('div');
      entry.style.padding = '6px 0';
      entry.innerHTML = `<strong>[${time}]</strong> ${escapeHtml(text)}`;
      logEl.prepend(entry);
      // שמירת 30 רשומות מקסימום
      while(logEl.childElementCount > 40) logEl.removeChild(logEl.lastChild);
    }

    function updateDisplay(){
      scoreEl.textContent = Math.max(0, score);
      levelEl.textContent = level;
    }

    function escapeHtml(str){
      return str.replace(/[&<>"']/g, (m) => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
    }

    // כפתורי ממשק
    startBtn.addEventListener('click', () => {
      startBtn.disabled = true;
      startBtn.textContent = 'רץ...';
      if(round === 0) {
        appendLog('המשחק התחיל! בהצלחה.');
      } else {
        appendLog('המשחק הוזן מחדש.');
      }
      startRound();
    });

    resetBtn.addEventListener('click', () => {
      clearInterval(timer);
      score = 0; round = 0; level = 1;
      startBtn.disabled = false;
      startBtn.textContent = 'התחל';
      updateDisplay();
      roundNumEl.textContent = 0;
      scenarioTitleEl.textContent = 'ממתין לתרחיש...';
      scenarioTextEl.textContent = 'לחץ "התחל" כדי לקבל שיחה.';
      choicesEl.innerHTML = '';
      timerFillEl.style.width = '100%';
      logEl.innerHTML = 'המשחק אופס.';
    });

    settingsBtn.addEventListener('click', () => {
      showModalSettings();
    });

    // מודאל של הגדרות
    function showModalSettings(){
      const root = document.getElementById('modalRoot');
      root.innerHTML = `
        <div class="overlay" id="overlay">
          <div class="modal" role="dialog" aria-modal="true">
            <div style="display:flex;justify-content:space-between;align-items:center">
              <div style="font-weight:800">הגדרות משחק</div>
              <div><button id="closeModal">סגור</button></div>
            </div>
            <div style="margin-top:12px">
              <label style="display:block;margin-bottom:8px">זמן התחלתי לכל שיחה (שניות): <input id="inputTime" type="number" min="6" max="30" value="${timePerQuestion}" style="width:80px;margin-inline-start:8px"></label>
              <div style="margin-top:10px">
                <button id="saveSettings">שמור</button>
              </div>
              <div style="margin-top:10px;font-size:13px;color:rgba(230,238,246,0.7)">שינוי זה ישפיע על סיבוב חדש (לא על סיבוב רץ).</div>
            </div>
          </div>
        </div>
      `;
      root.style.display = 'block';
      document.getElementById('closeModal').onclick = () => { root.style.display='none'; root.innerHTML=''; };
      document.getElementById('overlay').onclick = (e) => { if(e.target.id === 'overlay'){ root.style.display='none'; root.innerHTML=''; } };
      document.getElementById('saveSettings').onclick = () => {
        const val = parseInt(document.getElementById('inputTime').value||timePerQuestion);
        if(Number.isFinite(val) && val >= 6 && val <= 30){
          timePerQuestion = val;
          timePerEl.textContent = timePerQuestion;
          root.style.display='none';
          root.innerHTML='';
          appendLog(`הגדרות נשמרו: זמן לכל שאלה = ${timePerQuestion}s`);
        } else {
          alert('בחר ערך בין 6 ל-30 שניות.');
        }
      };
    }

    // התחלת מצב התחלתי
    updateDisplay();

    // הערת בטיחות קטנה בתחתית הקוד
    console.log("משחק מוקד 105: המשחק הוא סימולציה בלבד. במצב חירום אמיתי התקשר לגורמי החירום.");
  </script>
</body>
</html>
