const inputEl = document.getElementById("user-input");
const toneEl = document.getElementById("tone-select");
const btnEl = document.getElementById("generate-btn");
const outputSection = document.getElementById("output-section");
const outputContent = document.getElementById("output-content");
const copyBtn = document.getElementById("copy-btn");

btnEl.addEventListener("click", handleGenerate);
inputEl.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && e.shiftKey) {
    e.preventDefault();
    handleGenerate();
  }
});

async function handleGenerate() {
  const topic = inputEl.value.trim();
  if (!topic) return;

  outputSection.hidden = true;
  setLoading(true);

  try {
    const res = await fetch("http://127.0.0.1:8000/generate_prompt", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_input: topic, tone: toneEl.value }),
    });

    if (!res.ok) {
      const errText = await res.text();
      throw new Error(errText || `HTTP ${res.status}`);
    }

    const data = await res.json();
    outputContent.textContent = data.generated_prompt;
    outputSection.hidden = false;
  } catch (err) {
    outputContent.textContent = `Error: ${err.message}`;
    outputSection.hidden = false;
  } finally {
    setLoading(false);
  }
}

function setLoading(loading) {
  btnEl.disabled = loading;
  if (loading) {
    btnEl.innerHTML = '<span class="loader"></span> Generating...';
  } else {
    btnEl.textContent = "Generate Prompt";
  }
}

copyBtn.addEventListener("click", async () => {
  try {
    await navigator.clipboard.writeText(outputContent.textContent);
    const orig = copyBtn.textContent;
    copyBtn.textContent = "Copied!";
    setTimeout(() => { copyBtn.textContent = orig; }, 2000);
  } catch {
    copyBtn.textContent = "Failed to copy";
    setTimeout(() => { copyBtn.textContent = "Copy to Clipboard"; }, 2000);
  }
});
