let sessionId = Math.random().toString(36).substring(7);
let history = [];

// Theme Management
const savedTheme = localStorage.getItem('theme') || 'dark';
document.documentElement.setAttribute('data-theme', savedTheme);

document.getElementById('themeToggle').addEventListener('click', toggleTheme);

function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
}

// Character Count
const queryInput = document.getElementById('query');
const charCount = document.getElementById('charCount');

queryInput.addEventListener('input', () => {
    charCount.textContent = queryInput.value.length;
});

// Keyboard Shortcuts
document.addEventListener('keydown', (e) => {
    // Ctrl+K or Cmd+K to focus input
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        queryInput.focus();
        queryInput.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
    
    // Ctrl+Shift+T to toggle theme
    if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key === 'T') {
        e.preventDefault();
        toggleTheme();
    }
});

// Enter to submit
queryInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        getExplanation();
    }
});

// Explanation Logic
async function getExplanation() {
    const role = document.getElementById('role').value;
    const query = queryInput.value.trim();

    if (!query) {
        showError('Please enter a question');
        queryInput.focus();
        return;
    }

    const loading = document.getElementById('loading');
    const results = document.getElementById('results');
    const explainBtn = document.getElementById('explainBtn');

    loading.classList.add('active');
    results.classList.remove('active');
    results.style.display = 'none';
    explainBtn.disabled = true;
    explainBtn.querySelector('.btn-label').textContent = 'Thinking...';

    try {
        const response = await fetch('/explain', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query, role, session_id: sessionId })
        });

        if (!response.ok) {
            const errData = await response.json().catch(() => ({}));
            throw new Error(errData.detail || 'Failed to get explanation');
        }

        const data = await response.json();

        document.getElementById('whatContent').textContent = data.response.what || 'No explanation available';
        document.getElementById('howContent').textContent = data.response.how || 'No explanation available';
        document.getElementById('whyContent').textContent = data.response.why || 'No explanation available';

        loading.classList.remove('active');
        results.style.display = 'flex';
        
        requestAnimationFrame(() => {
            results.classList.add('active');
            results.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });

        addToHistory(role, query);

    } catch (error) {
        loading.classList.remove('active');
        showError(error.message);
    } finally {
        explainBtn.disabled = false;
        explainBtn.querySelector('.btn-label').textContent = 'Explain';
    }
}

function showError(message) {
    document.querySelectorAll('.error').forEach(el => el.remove());

    const errorDiv = document.createElement('div');
    errorDiv.className = 'error';
    errorDiv.innerHTML = `
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"/>
            <line x1="15" y1="9" x2="9" y2="15"/>
            <line x1="9" y1="9" x2="15" y2="15"/>
        </svg>
        ${message}
    `;
    
    document.querySelector('.input-card').prepend(errorDiv);
    setTimeout(() => {
        errorDiv.style.opacity = '0';
        errorDiv.style.transform = 'translateY(-8px)';
        setTimeout(() => errorDiv.remove(), 200);
    }, 4500);
}

function addToHistory(role, query) {
    history.unshift({ role, query });
    if (history.length > 10) history.pop();
    renderHistory();
}

function renderHistory() {
    const container = document.getElementById('history');
    const emptyState = document.getElementById('emptyHistory');

    if (history.length === 0) {
        container.innerHTML = '';
        emptyState.style.display = 'flex';
        return;
    }

    emptyState.style.display = 'none';
    container.innerHTML = history.map((item, i) => `
        <div class="history-item" onclick="reuseHistory(${i})" role="button" tabindex="0">
            <span class="history-role">${item.role}</span>
            <span class="history-query">${escapeHtml(item.query)}</span>
        </div>
    `).join('');
}

function reuseHistory(index) {
    const item = history[index];
    document.getElementById('role').value = item.role;
    queryInput.value = item.query;
    charCount.textContent = item.query.length;
    queryInput.focus();
    queryInput.scrollTo(0, 0);
}

function clearHistory() {
    history = [];
    renderHistory();
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
