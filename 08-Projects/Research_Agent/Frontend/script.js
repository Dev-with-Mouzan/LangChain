const API_BASE = '/api';
const messagesEl = document.getElementById('messages');
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const statusDot = document.getElementById('status-dot');
const statusText = document.getElementById('status-text');
const versionDisplay = document.getElementById('version-display');
const typingIndicator = document.getElementById('typing-indicator');
const welcomeScreen = document.getElementById('welcome-screen');
const suggestions = document.getElementById('suggestions');

let isProcessing = false;

// ─── Auto-resize textarea ───
userInput.addEventListener('input', () => {
    userInput.style.height = 'auto';
    userInput.style.height = Math.min(userInput.scrollHeight, 200) + 'px';
    sendBtn.disabled = !userInput.value.trim();
    sendBtn.classList.toggle('active', userInput.value.trim().length > 0);
});

userInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        chatForm.dispatchEvent(new Event('submit'));
    }
});

// ─── Suggestion chips ───
suggestions.addEventListener('click', (e) => {
    const chip = e.target.closest('.suggestion-chip');
    if (chip) {
        userInput.value = chip.dataset.prompt;
        userInput.dispatchEvent(new Event('input'));
        chatForm.dispatchEvent(new Event('submit'));
    }
});

// ─── Health check ───
async function checkHealth() {
    try {
        const res = await fetch(`${API_BASE}/health`);
        if (res.ok) {
            statusDot.className = 'status-dot online';
            statusText.textContent = 'Online';
        } else {
            statusDot.className = 'status-dot offline';
            statusText.textContent = 'Offline';
        }
    } catch {
        statusDot.className = 'status-dot offline';
        statusText.textContent = 'Offline';
    }
}

async function checkVersion() {
    try {
        const res = await fetch(`${API_BASE}/version`);
        if (res.ok) {
            const data = await res.json();
            versionDisplay.textContent = data.version || '—';
        }
    } catch {
        versionDisplay.textContent = '—';
    }
}

// ─── Formatting ───
function formatText(text) {
    let formatted = text
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;');

    formatted = formatted.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
    formatted = formatted.replace(/`([^`]+)`/g, '<code>$1</code>');
    formatted = formatted.replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>');
    formatted = formatted.replace(/\n/g, '<br>');

    return formatted;
}

// ─── Message rendering ───
function addMessage(text, role) {
    welcomeScreen?.classList.add('hidden');

    const div = document.createElement('div');
    div.className = `message ${role}`;

    const avatar = document.createElement('div');
    avatar.className = 'avatar';
    avatar.textContent = role === 'user' ? '👤' : '🤖';

    const bubble = document.createElement('div');
    bubble.className = 'bubble';

    const pEl = document.createElement('p');
    pEl.innerHTML = formatText(text);
    bubble.appendChild(pEl);

    div.appendChild(avatar);
    div.appendChild(bubble);
    messagesEl.appendChild(div);
    messagesEl.scrollTop = messagesEl.scrollHeight;
}

function createAgentBubble() {
    welcomeScreen?.classList.add('hidden');

    const div = document.createElement('div');
    div.className = 'message agent';

    const avatar = document.createElement('div');
    avatar.className = 'avatar';
    avatar.textContent = '🤖';

    const bubble = document.createElement('div');
    bubble.className = 'bubble';
    const pEl = document.createElement('p');

    bubble.appendChild(pEl);
    div.appendChild(avatar);
    div.appendChild(bubble);
    messagesEl.appendChild(div);
    messagesEl.scrollTop = messagesEl.scrollHeight;

    return pEl;
}

function setProcessing(state) {
    isProcessing = state;
    sendBtn.disabled = state || !userInput.value.trim();
    userInput.disabled = state;
    typingIndicator.classList.toggle('active', state);
}

// ─── Send message ───
async function sendMessage(question) {
    if (isProcessing) return;

    addMessage(question, 'user');
    userInput.value = '';
    userInput.style.height = 'auto';
    sendBtn.disabled = true;
    sendBtn.classList.remove('active');
    setProcessing(true);

    const pEl = createAgentBubble();

    try {
        const res = await fetch(`${API_BASE}/get_response`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question }),
        });

        if (!res.ok) {
            const errText = await res.text();
            throw new Error(errText || `HTTP ${res.status}`);
        }

        const reader = res.body.getReader();
        const decoder = new TextDecoder();
        let answer = '';

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            answer += decoder.decode(value, { stream: true });
            pEl.innerHTML = formatText(answer);
            messagesEl.scrollTop = messagesEl.scrollHeight;
        }
    } catch (err) {
        pEl.innerHTML = formatText(`**Error:** ${err.message}`);
    } finally {
        setProcessing(false);
        userInput.focus();
    }
}

// ─── Events ───
chatForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const question = userInput.value.trim();
    if (question && !isProcessing) {
        sendMessage(question);
    }
});

document.getElementById('new-chat-btn').addEventListener('click', () => {
    messagesEl.querySelectorAll('.message').forEach(el => el.remove());
    welcomeScreen?.classList.remove('hidden');
    userInput.value = '';
    userInput.style.height = 'auto';
    sendBtn.disabled = true;
    sendBtn.classList.remove('active');
    userInput.focus();
});

// ─── Theme toggle ───
const themeToggle = document.getElementById('theme-toggle');
const themeLabel = document.getElementById('theme-label');

function setTheme(isLight) {
    document.documentElement.classList.toggle('light-theme', isLight);
    themeLabel.textContent = isLight ? 'Dark' : 'Light';
    localStorage.setItem('theme', isLight ? 'light' : 'dark');
}

themeToggle.addEventListener('click', () => {
    const isLight = !document.documentElement.classList.contains('light-theme');
    setTheme(isLight);
});

const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'light') {
    setTheme(true);
}

// ─── Init ───
checkHealth();
checkVersion();
setInterval(checkHealth, 15000);
