import os
import json

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="A deep historical exploration of the {title} during World War II.">
    <title>{title} - Echoes of Conflict</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../battle-detail.css">
</head>
<body>
    <div class="background-overlay"></div>
    
    <nav class="navbar">
        <a href="../index.html" class="nav-home-link">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <line x1="19" y1="12" x2="5" y2="12"></line>
                <polyline points="12 19 5 12 12 5"></polyline>
            </svg>
            Back to Timeline
        </a>
        <span style="font-family: var(--font-heading); font-weight: 700; font-size: 1.2rem; color: var(--accent);">ECHOES OF CONFLICT</span>
    </nav>

    <header class="hero-detail">
        <img src="../{image}" alt="{title}" class="hero-detail-bg">
        <div class="hero-detail-content">
            <span class="hero-date">{date}</span>
            <h1 class="hero-title">{title}</h1>
        </div>
    </header>

    <main class="container">
        <article class="content-section">
            {chapters_html}
        </article>

        <aside class="sidebar">
            <div class="stat-card">
                <h3 class="stat-card-title">Battle Statistics</h3>
                <div class="stat-item">
                    <span class="stat-label">Date</span>
                    <span class="stat-value">{date}</span>
                </div>
                <div class="stat-item">
                    <span class="stat-label">Location</span>
                    <span class="stat-value">{location}</span>
                </div>
                <div class="stat-item">
                    <span class="stat-label">Result</span>
                    <span class="stat-value outcome">{result}</span>
                </div>
                <div class="stat-item">
                    <span class="stat-label">Strategic Impact</span>
                    <span class="stat-value">{outcome}</span>
                </div>
                <div class="stat-item">
                    <span class="stat-label">Allied Commanders</span>
                    <span class="stat-value">{allied_commanders}</span>
                </div>
                <div class="stat-item">
                    <span class="stat-label">Axis Commanders</span>
                    <span class="stat-value">{axis_commanders}</span>
                </div>
                <div class="stat-item">
                    <span class="stat-label">Allied Forces</span>
                    <span class="stat-value">{allied_forces}</span>
                </div>
                <div class="stat-item">
                    <span class="stat-label">Axis Forces</span>
                    <span class="stat-value">{axis_forces}</span>
                </div>
                <div class="stat-item">
                    <span class="stat-label">Allied Casualties</span>
                    <span class="stat-value">{allied_casualties}</span>
                </div>
                <div class="stat-item">
                    <span class="stat-label">Axis Casualties</span>
                    <span class="stat-value">{axis_casualties}</span>
                </div>
            </div>
        </aside>
    </main>

    <div class="container" style="padding-top: 0; padding-bottom: 0;">
        <nav class="page-navigation">
            {prev_button_html}
            {next_button_html}
        </nav>
    </div>

    <footer>
        <p>A historical exploration project. Created by Arjun Divecha.</p>
    </footer>
</body>
</html>
"""

def generate_chapters(chapters):
    html = []
    for ch in chapters:
        ch_title = ch.get("title", "")
        ch_content = ch.get("content", [])
        paragraphs_html = ""
        for p in ch_content:
            # Check if it's a sidebar box
            if isinstance(p, dict) and p.get("type") == "sidebar":
                paragraphs_html += f'''
                <div class="sidebar-box">
                    <h4>{p.get("title")}</h4>
                    <p>{p.get("text")}</p>
                </div>
                '''
            elif isinstance(p, dict) and p.get("type") == "sources":
                sources_html = ""
                for src in p.get("items", []):
                    sources_html += f'''
                    <li class="source-item">
                        <a href="{src.get("url")}" target="_blank" rel="noopener noreferrer" class="source-link">
                            {src.get("title")}
                            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-left: 2px;">
                                <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                                <polyline points="15 3 21 3 21 9"></polyline>
                                <line x1="10" y1="14" x2="21" y2="3"></line>
                            </svg>
                        </a>
                        <span class="source-desc">{src.get("desc")}</span>
                    </li>
                    '''
                paragraphs_html += f'<ul class="sources-list">{sources_html}</ul>'
            elif isinstance(p, dict) and p.get("type") == "map":
                paragraphs_html += f'''
                <div class="battle-map-container">
                    <img src="{p.get("url")}" alt="{p.get("alt")}" class="battle-map-img">
                    <p class="battle-map-caption"><strong>Figure:</strong> {p.get("caption")}</p>
                </div>
                '''
            else:
                paragraphs_html += f'<p>{p}</p>'
        
        html.append(f'''
        <section class="chapter" id="{ch_title.lower().replace(' ', '-').replace('&', 'and')}">
            <h2 class="chapter-title">{ch_title}</h2>
            {paragraphs_html}
        </section>
        ''')
    return "\\n".join(html)

def main():
    data_dir = "data"
    out_dir = "battles"
    os.makedirs(out_dir, exist_ok=True)
    
    # Chronological ordering of battles
    order = [
        "poland", "britain", "barbarossa", "pearl-harbor", "midway", 
        "stalingrad", "d-day", "bulge", "iwo-jima", "berlin"
    ]
    
    # Load all battle data
    battles_data = {}
    for filename in os.listdir(data_dir):
        if filename.endswith(".json"):
            bid = filename[:-5]
            with open(os.path.join(data_dir, filename), "r", encoding="utf-8") as f:
                battles_data[bid] = json.load(f)
                
    for i, bid in enumerate(order):
        if bid not in battles_data:
            print(f"Warning: {bid} not found in data folder.")
            continue
            
        data = battles_data[bid]
        
        # Navigation buttons
        prev_button_html = ""
        if i > 0:
            prev_id = order[i-1]
            prev_title = battles_data[prev_id]["title"]
            prev_button_html = f'''
            <a href="{prev_id}.html" class="nav-btn prev">
                <span class="nav-btn-label">Previous Battle</span>
                <span class="nav-btn-title">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="19" y1="12" x2="5" y2="12"></line>
                        <polyline points="12 19 5 12 12 5"></polyline>
                    </svg>
                    {prev_title}
                </span>
            </a>
            '''
            
        next_button_html = ""
        if i < len(order) - 1:
            next_id = order[i+1]
            next_title = battles_data[next_id]["title"]
            next_button_html = f'''
            <a href="{next_id}.html" class="nav-btn next">
                <span class="nav-btn-label">Next Battle</span>
                <span class="nav-btn-title">
                    {next_title}
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="5" y1="12" x2="19" y2="12"></line>
                        <polyline points="12 5 19 12 12 19"></polyline>
                    </svg>
                </span>
            </a>
            '''
            
        # Chapters HTML
        chapters_html = generate_chapters(data.get("chapters", []))
        
        # Render the template
        html_content = TEMPLATE.format(
            title=data.get("title", ""),
            date=data.get("date", ""),
            location=data.get("location", ""),
            result=data.get("result", ""),
            outcome=data.get("outcome", ""),
            allied_commanders=data.get("allied_commanders", ""),
            axis_commanders=data.get("axis_commanders", ""),
            allied_forces=data.get("allied_forces", ""),
            axis_forces=data.get("axis_forces", ""),
            allied_casualties=data.get("allied_casualties", ""),
            axis_casualties=data.get("axis_casualties", ""),
            image=data.get("image", ""),
            chapters_html=chapters_html,
            prev_button_html=prev_button_html,
            next_button_html=next_button_html
        )
        
        out_path = os.path.join(out_dir, f"{bid}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Generated {out_path}")

if __name__ == "__main__":
    main()
