/**
 * AI Study Planner - Frontend Application
 * Handles form submission, API calls, and UI state management
 */

(function() {
    'use strict';

    // ============================================
    // DOM Elements
    // ============================================
    const elements = {
        form: document.getElementById('studyForm'),
        topicInput: document.getElementById('topicInput'),
        submitBtn: document.getElementById('submitBtn'),
        loading: document.getElementById('loading'),
        results: document.getElementById('results'),
        error: document.getElementById('error'),
        errorMessage: document.getElementById('errorMessage'),
        quickTopics: document.querySelectorAll('.quick-topic'),
        cards: {
            explanation: document.getElementById('explanationContent'),
            simplified: document.getElementById('simplifiedContent'),
            fact: document.getElementById('factContent'),
            questions: document.getElementById('questionsContent')
        }
    };

    // ============================================
    // State Management
    // ============================================
    let state = {
        isLoading: false,
        currentTopic: null
    };

    // ============================================
    // Utility Functions
    // ============================================
    
    /**
     * Converts markdown text to HTML
     * Supports: headers, bold, italic, lists, code blocks, inline code, blockquotes
     */
    function formatText(text) {
        if (!text) return '';
        
        let html = text;
        
        // Escape HTML to prevent XSS
        html = html.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
        
        // Code blocks (```code```)
        html = html.replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>');
        
        // Inline code (`code`)
        html = html.replace(/`([^`]+)`/g, '<code class="inline-code">$1</code>');
        
        // Headers (### Header, ## Header, # Header)
        html = html.replace(/^### (.+)$/gm, '<h4>$1</h4>');
        html = html.replace(/^## (.+)$/gm, '<h3>$1</h3>');
        html = html.replace(/^# (.+)$/gm, '<h2>$1</h2>');
        
        // Bold (**text**)
        html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
        
        // Italic (*text*)
        html = html.replace(/\*(.+?)\*/g, '<em>$1</em>');
        
        // Blockquotes (> text)
        html = html.replace(/^&gt; (.+)$/gm, '<blockquote>$1</blockquote>');
        
        // Horizontal rules (---)
        html = html.replace(/^---$/gm, '<hr>');
        
        // Unordered lists (- item or * item)
        html = html.replace(/^[\-\*] (.+)$/gm, '<li>$1</li>');
        html = html.replace(/(<li>.*<\/li>\n?)+/g, '<ul>$&</ul>');
        
        // Ordered lists (1. item)
        html = html.replace(/^\d+\. (.+)$/gm, '<li>$1</li>');
        
        // Process paragraphs and line breaks
        const lines = html.split('\n');
        let result = '';
        let inList = false;
        let inCodeBlock = false;
        
        for (let i = 0; i < lines.length; i++) {
            const line = lines[i];
            
            // Track code blocks
            if (line.includes('<pre><code>')) {
                inCodeBlock = true;
            }
            if (line.includes('</code></pre>')) {
                inCodeBlock = false;
                result += line + '\n';
                continue;
            }
            
            // Skip processing inside code blocks
            if (inCodeBlock) {
                result += line + '\n';
                continue;
            }
            
            // Handle list items
            if (line.includes('<li>')) {
                inList = true;
                result += line + '\n';
                continue;
            }
            
            // Close list if we're no longer in list items
            if (inList && !line.includes('<li>')) {
                inList = false;
            }
            
            // Handle headers (already formatted)
            if (line.match(/^<h[2-4]>/)) {
                result += line + '\n';
                continue;
            }
            
            // Handle blockquotes
            if (line.includes('<blockquote>')) {
                result += line + '\n';
                continue;
            }
            
            // Handle horizontal rules
            if (line.includes('<hr>')) {
                result += line + '\n';
                continue;
            }
            
            // Empty lines become paragraph breaks
            if (line.trim() === '') {
                result += '\n';
                continue;
            }
            
            // Regular text becomes paragraph
            if (line.trim()) {
                result += `<p>${line}</p>\n`;
            }
        }
        
        // Clean up multiple newlines
        result = result.replace(/\n{3,}/g, '\n\n');
        
        // Wrap consecutive blockquotes
        result = result.replace(/(<blockquote>.*<\/blockquote>\n?)+/g, '<div class="blockquote-group">$&</div>');
        
        return result;
    }

    /**
     * Animates an element with a given animation class
     */
    function animateElement(element, animationClass) {
        return new Promise(resolve => {
            element.classList.add(animationClass);
            element.addEventListener('animationend', () => {
                element.classList.remove(animationClass);
                resolve();
            }, { once: true });
        });
    }

    /**
     * Delays execution for a specified duration
     */
    function delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    // ============================================
    // UI State Functions
    // ============================================
    
    /**
     * Sets the loading state of the application
     */
    function setLoading(isLoading) {
        state.isLoading = isLoading;
        
        elements.loading.classList.toggle('hidden', !isLoading);
        elements.results.classList.add('hidden');
        elements.error.classList.add('hidden');
        
        elements.submitBtn.disabled = isLoading;
        elements.topicInput.disabled = isLoading;
        
        if (isLoading) {
            elements.submitBtn.querySelector('.btn-text').textContent = 'Generating...';
        } else {
            elements.submitBtn.querySelector('.btn-text').textContent = 'Generate';
        }
    }

    /**
     * Displays an error message to the user
     */
    function showError(message) {
        elements.errorMessage.textContent = message;
        elements.error.classList.remove('hidden');
        elements.loading.classList.add('hidden');
        
        // Add shake animation
        animateElement(elements.error, 'shake');
    }

    /**
     * Shows the results section with staggered card animations
     */
    async function showResults(data) {
        setLoading(false);
        
        // Populate content
        elements.cards.explanation.innerHTML = formatText(data.explanation);
        elements.cards.simplified.innerHTML = formatText(data.simplified);
        elements.cards.fact.innerHTML = formatText(data.fact);
        elements.cards.questions.innerHTML = formatText(data.questions);
        
        // Show results container
        elements.results.classList.remove('hidden');
        
        // Add staggered animation to cards
        const cards = elements.results.querySelectorAll('.result-card');
        cards.forEach((card, index) => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';
            
            setTimeout(() => {
                card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            }, index * 100);
        });
        
        // Smooth scroll to results
        await delay(100);
        elements.results.scrollIntoView({ 
            behavior: 'smooth', 
            block: 'start' 
        });
    }

    // ============================================
    // API Functions
    // ============================================
    
    /**
     * Sends the topic to the API and retrieves the study plan
     */
    async function generateStudyPlan(topic) {
        const response = await fetch('/api/study-plan', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ topic })
        });
        
        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.detail || `HTTP error! status: ${response.status}`);
        }
        
        return response.json();
    }

    // ============================================
    // Event Handlers
    // ============================================
    
    /**
     * Handles form submission
     */
    async function handleSubmit(event) {
        event.preventDefault();
        
        if (state.isLoading) return;
        
        const topic = elements.topicInput.value.trim();
        if (!topic) {
            elements.topicInput.focus();
            return;
        }
        
        state.currentTopic = topic;
        setLoading(true);
        
        try {
            const data = await generateStudyPlan(topic);
            await showResults(data);
        } catch (err) {
            console.error('Error generating study plan:', err);
            showError(err.message || 'Failed to generate study plan. Please try again.');
        }
    }

    /**
     * Handles quick topic button clicks
     */
    function handleQuickTopicClick(event) {
        const button = event.currentTarget;
        const topic = button.dataset.topic;
        
        if (topic && !state.isLoading) {
            elements.topicInput.value = topic;
            elements.topicInput.focus();
            
            // Add visual feedback
            button.style.transform = 'scale(0.95)';
            setTimeout(() => {
                button.style.transform = '';
            }, 150);
        }
    }

    /**
     * Clears error when input is focused
     */
    function handleInputFocus() {
        elements.error.classList.add('hidden');
    }

    /**
     * Handles keyboard navigation for quick topics
     */
    function handleQuickTopicKeydown(event) {
        if (event.key === 'Enter' || event.key === ' ') {
            event.preventDefault();
            handleQuickTopicClick(event);
        }
    }

    // ============================================
    // Initialization
    // ============================================
    
    /**
     * Initialize the application
     */
    function init() {
        // Form submission
        elements.form.addEventListener('submit', handleSubmit);
        
        // Input focus handler
        elements.topicInput.addEventListener('focus', handleInputFocus);
        
        // Quick topic buttons
        elements.quickTopics.forEach(button => {
            button.addEventListener('click', handleQuickTopicClick);
            button.addEventListener('keydown', handleQuickTopicKeydown);
        });
        
        // Keyboard shortcut: Enter to submit
        elements.topicInput.addEventListener('keydown', (event) => {
            if (event.key === 'Enter' && !event.shiftKey) {
                // Allow default form submission
            }
        });
        
        // Add entrance animations
        document.querySelectorAll('.header, .search-form').forEach((el, index) => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            
            setTimeout(() => {
                el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                el.style.opacity = '1';
                el.style.transform = 'translateY(0)';
            }, index * 100);
        });
        
        // Focus input on page load
        setTimeout(() => {
            elements.topicInput.focus();
        }, 600);
    }

    // Start the application when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
