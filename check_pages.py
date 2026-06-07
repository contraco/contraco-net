with open(r'C:/Users/FrankMeltke/OneDrive - CONTRACO USA/Documents/GitHub/contraco/insights.html', 'r', encoding='utf-8') as f:
    content = f.read()

last_card = '<article class="insight-card">\n                        <div class="insight-header">\n                            <div class="insight-meta">Executive Guide | 16 min read</div>'

new_cards = '''<article class="insight-card">
                        <div class="insight-header">
                            <div class="insight-meta">Research Hub | 12 min read</div>
                            <h3 class="insight-title">Strategic Intelligence</h3>
                            <p class="insight-excerpt">Research-grade analysis on AI strategy, pricing psychology and organisational design from 28 years at the frontlines of transformation. contraco's intelligence frameworks for leaders navigating the AI era.</p>
                        </div>
                        <div class="insight-content">
                            <div class="insight-tags">
                                <span class="tag">AI Strategy</span>
                                <span class="tag">Research</span>
                                <span class="tag">Frameworks</span>
                            </div>
                            <a href="https://contraco.net/strategic-intelligence.html" class="insight-cta">
                                Explore the research
                                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M5 12h14M12 5l7 7-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
                                </svg>
                            </a>
                        </div>
                    </article>
                    <article class="insight-card">
                        <div class="insight-header">
                            <div class="insight-meta">Global Markets Guide | 14 min read</div>
                            <h3 class="insight-title">Cultural Adaptation in Digital Transformation</h3>
                            <p class="insight-excerpt">Why transformation fails across borders and how to fix it. contraco's cultural adaptation framework for localising AI and digital transformation across markets with fundamentally different organisational cultures.</p>
                        </div>
                        <div class="insight-content">
                            <div class="insight-tags">
                                <span class="tag">Cultural Adaptation</span>
                                <span class="tag">Global Markets</span>
                                <span class="tag">Digital Transformation</span>
                            </div>
                            <a href="https://contraco.net/cultural-adaptation-guide.html" class="insight-cta">
                                Read the guide
                                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M5 12h14M12 5l7 7-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
                                </svg>
                            </a>
                        </div>
                    </article>
                    ''' + last_card

if last_card in content:
    content = content.replace(last_card, new_cards)
    with open(r'C:/Users/FrankMeltke/OneDrive - CONTRACO USA/Documents/GitHub/contraco/insights.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("FIXED")
else:
    print("NOT FOUND")
