import os
from jinja2 import Template

# ----------------------------------------------------------------------
# 1. Master CSS & HTML Template
# ----------------------------------------------------------------------
MASTER_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} | Dai Lab</title>
    <meta name="description" content="{{ description }}">
    <link rel="canonical" href="{{ page_url }}">
    <link rel="icon" type="image/svg+xml" href="images/logo.svg">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Dai Lab">
    <meta property="og:title" content="{{ title }} | Dai Lab">
    <meta property="og:description" content="{{ description }}">
    <meta property="og:url" content="{{ page_url }}">
    <meta property="og:image" content="{{ site_url }}images/og-image.jpg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:alt" content="Algae growing in tubular photobioreactors in the Dai Lab">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{{ title }} | Dai Lab">
    <meta name="twitter:description" content="{{ description }}">
    <meta name="twitter:image" content="{{ site_url }}images/og-image.jpg">
    {% if page_id == 'home' %}
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "ResearchOrganization",
        "name": "Dai Lab",
        "url": "{{ site_url }}",
        "logo": "{{ site_url }}images/logo.svg",
        "email": "{{ contact_email }}",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Bond Life Sciences Center, 1201 Rollins Street",
            "addressLocality": "Columbia",
            "addressRegion": "MO",
            "postalCode": "65211",
            "addressCountry": "US"
        },
        "parentOrganization": {
            "@type": "CollegeOrUniversity",
            "name": "University of Missouri"
        },
        "founder": {
            "@type": "Person",
            "name": "Susie Y. Dai",
            "jobTitle": "Professor",
            "sameAs": ["https://scholar.google.com/citations?user=jWERWWsAAAAJ", "https://www.linkedin.com/in/susie-dai"]
        }
    }
    </script>
    {% endif %}
    <style>
        :root {
            --primary: #0d5c3a;
            --primary-hover: #083c25;
            --accent-red: #800000;
            --bg-body: #ffffff;
            --bg-card: #f8f9fa;
            --text-dark: #212529;
            --text-muted: #6c757d;
            --border: #e9ecef;
            --max-width: 1100px;
        }

        * { box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
            line-height: 1.6;
            color: var(--text-dark);
            background-color: var(--bg-body);
            margin: 0;
            padding: 0;
        }

        /* Header Navigation */
        header {
            background-color: #ffffff;
            border-bottom: 3px solid var(--primary);
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
            position: sticky;
            top: 0;
            z-index: 1000;
        }
        .header-container {
            max-width: var(--max-width);
            margin: 0 auto;
            padding: 1.25rem 1.5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
        }
        .brand {
            display: flex;
            align-items: center;
            gap: 1.25rem;
        }
        .brand-logo {
            height: 110px;
            width: auto;
            object-fit: contain;
        }
        .brand h1 {
            margin: 0;
            font-size: 2.8rem;
            color: var(--primary);
            font-weight: 800;
            letter-spacing: -1px;
        }
        .header-container, .brand-logo, .brand h1 {
            transition: padding 0.25s ease, height 0.25s ease, font-size 0.25s ease;
        }
        header.scrolled .header-container { padding-top: 0.4rem; padding-bottom: 0.4rem; }
        header.scrolled .brand-logo { height: 48px; }
        header.scrolled .brand h1 { font-size: 1.7rem; }
        @media (prefers-reduced-motion: reduce) {
            .header-container, .brand-logo, .brand h1 { transition: none; }
        }
        nav { display: flex; gap: 1.5rem; margin-top: 0.5rem; }
        nav a {
            text-decoration: none;
            color: #555555;
            font-weight: 700;
            font-size: 0.95rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            padding-bottom: 0.25rem;
            transition: color 0.2s ease, border-bottom 0.2s ease;
        }
        nav a:hover, nav a.active {
            color: var(--primary);
            border-bottom: 2px solid var(--primary);
        }

        /* Hero Welcome Banner */
        /* Hero Welcome Banner Fix */
        .hero-banner {
            position: relative;
            width: 100%;
            height: 520px;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            background-color: #ffffff;
            margin-bottom: 2.5rem;
        }
        .hero-bg-img {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
            z-index: 1;
            filter: brightness(1.25) contrast(1.05);
        }
        .hero-overlay-dark {
            display: none;
        }
        .hero-logo-large {
            position: relative;
            z-index: 3;
            max-height: 320px;
            width: auto;
            max-width: 85%;
            filter: drop-shadow(0 4px 15px rgba(0, 0, 0, 0.4));
        }

        /* Main Layout Container */
        main {
            max-width: var(--max-width);
            margin: 2.5rem auto;
            padding: 0 1.5rem;
            min-height: 70vh;
        }

        /* Home Page Layout */
        .recruitment-banner {
            text-align: center;
            color: var(--accent-red);
            font-weight: 700;
            font-size: 1.15rem;
            margin-bottom: 2.5rem;
            line-height: 1.8;
            padding: 1rem;
        }
        .recruitment-actions {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 0.75rem;
            margin-top: 1rem;
        }
        .btn {
            display: inline-block;
            padding: 0.6rem 1.4rem;
            border-radius: 4px;
            font-size: 1rem;
            font-weight: 700;
            text-decoration: none;
            border: 2px solid var(--primary);
            transition: background-color 0.2s ease, color 0.2s ease;
        }
        .btn-primary { background-color: var(--primary); color: #ffffff; }
        .btn-primary:hover { background-color: var(--primary-hover); border-color: var(--primary-hover); }
        .btn-outline { background-color: #ffffff; color: var(--primary); }
        .btn-outline:hover { background-color: var(--primary); color: #ffffff; }

        /* Contact Page */
        .contact-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
            margin-bottom: 3rem;
        }
        @media (max-width: 800px) {
            .contact-grid { grid-template-columns: 1fr; }
        }
        .contact-card {
            background-color: #f4f5f7;
            border-radius: 8px;
            padding: 1.75rem 2rem;
        }
        .contact-card h2, .join-section h2 {
            color: var(--accent-red);
            font-size: 1.4rem;
            margin: 0 0 1rem 0;
        }
        .contact-card p { margin: 0 0 0.75rem 0; }
        .contact-card a, .join-section a:not(.btn) {
            color: var(--primary);
            font-weight: 600;
        }
        .contact-label {
            display: block;
            font-size: 0.8rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: var(--text-muted);
        }
        .join-section {
            border: 2px solid var(--accent-red);
            border-radius: 8px;
            padding: 1.75rem 2rem;
            scroll-margin-top: 180px;
        }
        .join-section ul { padding-left: 1.25rem; margin: 0.5rem 0 1.25rem 0; }
        .join-section li { margin-bottom: 0.4rem; }
        .platform-section {
            background-color: #f4f5f7;
            padding: 2.5rem 2rem;
            border-radius: 8px;
            margin-bottom: 3.5rem;
            text-align: center;
        }
        .platform-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 2rem;
            text-align: left;
        }
        @media (max-width: 800px) {
            .platform-grid { grid-template-columns: 1fr; }
        }
        .platform-card {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .platform-card img {
            width: 100%;
            height: 180px;
            object-fit: cover;
            border-radius: 6px;
            margin-bottom: 1.25rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        .platform-card p {
            margin: 0;
            font-size: 0.98rem;
            line-height: 1.6;
            color: #333333;
        }

        /* Lab Values Section */
        .values-section {
            background: linear-gradient(135deg, var(--primary) 0%, #127a4d 100%);
            border-radius: 10px;
            padding: 3rem 2rem;
            margin-bottom: 3.5rem;
            text-align: center;
            color: #ffffff;
        }
        .values-section h2 {
            font-size: 2rem;
            font-weight: 800;
            margin: 0 0 0.5rem 0;
            color: #ffffff;
        }
        .values-lead {
            font-size: 1.1rem;
            max-width: 720px;
            margin: 0 auto 2.25rem auto;
            color: rgba(255, 255, 255, 0.9);
        }
        .values-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 1.25rem;
        }
        @media (max-width: 900px) {
            .values-grid { grid-template-columns: repeat(2, 1fr); }
        }
        @media (max-width: 520px) {
            .values-grid { grid-template-columns: 1fr; }
            .values-section { padding: 2.25rem 1.25rem; }
        }
        .value-card {
            background-color: #ffffff;
            color: var(--text-dark);
            border-radius: 8px;
            padding: 1.75rem 1.25rem;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.12);
            transition: transform 0.2s ease;
        }
        .value-card:hover { transform: translateY(-4px); }
        @media (prefers-reduced-motion: reduce) {
            .value-card { transition: none; }
            .value-card:hover { transform: none; }
        }
        .value-icon {
            width: 56px;
            height: 56px;
            margin: 0 auto 1rem auto;
            border-radius: 50%;
            background-color: #e6f2ec;
            color: var(--primary);
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .value-icon svg {
            width: 28px;
            height: 28px;
            fill: none;
            stroke: currentColor;
            stroke-width: 2;
            stroke-linecap: round;
            stroke-linejoin: round;
        }
        .value-card h3 {
            font-size: 1.1rem;
            color: var(--accent-red);
            margin: 0 0 0.5rem 0;
        }
        .value-card p {
            font-size: 0.95rem;
            line-height: 1.6;
            margin: 0;
            color: #333333;
        }

        /* Research Page Specific Styling (Matching Reference) */
        .research-container {
            max-width: 980px;
            margin: 0 auto;
        }
        .research-section {
            margin-bottom: 4rem;
            text-align: center;
        }
        .research-title {
            color: var(--accent-red);
            font-size: 1.65rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            text-align: center;
        }
        .research-description {
            text-align: justify;
            color: #444444;
            font-size: 0.98rem;
            line-height: 1.75;
            margin-bottom: 2.5rem;
        }
        .research-description p {
            margin-bottom: 1rem;
        }
        .research-image-row {
            display: flex;
            justify-content: space-around;
            align-items: center;
            gap: 1.5rem;
            flex-wrap: wrap;
            margin-top: 1rem;
        }
        .research-image-row img {
            max-width: 31%;
            height: auto;
            max-height: 220px;
            object-fit: contain;
        }
        @media (max-width: 768px) {
            .research-image-row img {
                max-width: 100%;
                margin-bottom: 1rem;
            }
        }
        .full-banner-img {
            width: 100%;
            max-height: 320px;
            object-fit: cover;
            border-radius: 4px;
        }

        /* Team Page Specific Layout */
        .pi-container {
            display: flex;
            gap: 2.5rem;
            align-items: flex-start;
            margin-bottom: 2.5rem;
        }
        @media (max-width: 800px) {
            .pi-container { flex-direction: column; }
        }
        .pi-bio {
            flex: 1;
            font-size: 0.98rem;
            line-height: 1.7;
            color: #333333;
            text-align: justify;
        }
        .pi-photo { flex: 0 0 320px; }
        .pi-photo img {
            width: 100%;
            height: auto;
            border-radius: 4px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        .pi-links {
            text-align: center;
            margin: 2.5rem 0 3.5rem 0;
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
            font-size: 1.15rem;
        }
        .pi-links .podcast-label, .pi-links .linkedin-label {
            color: var(--accent-red);
            font-weight: 700;
            display: inline-block;
            margin-right: 0.5rem;
        }
        .pi-links a {
            color: #555555;
            text-decoration: none;
        }
        .pi-links a:hover {
            text-decoration: underline;
            color: var(--primary);
        }
        .section-heading-center {
            text-align: center;
            font-size: 1.75rem;
            font-weight: 700;
            color: #111111;
            margin: 3rem 0 2rem 0;
        }
        .team-images-stack {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 2rem;
            max-width: 100%;
            margin: 0 auto;
        }
        .team-images-stack img {
            max-width: 100%;
            height: auto;
            border-radius: 4px;
        }

        /* Publications Page Styling */
        .scholar-section {
            text-align: center;
            margin-top: 1rem;
            margin-bottom: 2rem;
        }
        .scholar-title {
            color: var(--accent-red);
            font-size: 1.25rem;
            font-weight: 700;
            margin-bottom: 0.25rem;
        }
        .scholar-link a {
            color: #222222;
            font-size: 1.15rem;
            text-decoration: none;
            word-break: break-all;
        }
        .scholar-link a:hover {
            text-decoration: underline;
            color: var(--primary);
        }
        .pub-tagline {
            text-align: center;
            font-size: 1.15rem;
            color: #333;
            margin-top: 2rem;
            margin-bottom: 2.5rem;
            font-weight: 500;
        }
        .pub-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1.75rem;
            align-items: start;
        }
        @media (max-width: 850px) {
            .pub-grid { grid-template-columns: 1fr; }
        }
        .pub-column {
            background-color: #ffffff;
            border-radius: 4px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            border: 1px solid var(--border);
        }
        .pub-column img {
            width: 100%;
            height: 150px;
            object-fit: cover;
            display: block;
        }
        .pub-column-title {
            background-color: #f4f5f7;
            padding: 1.25rem 1rem;
            text-align: center;
            font-weight: 700;
            font-size: 1.1rem;
            color: #111111;
            min-height: 75px;
            display: flex;
            align-items: center;
            justify-content: center;
            line-height: 1.35;
        }
        .pub-column-content {
            padding: 1.25rem 0.75rem;
        }
        .pub-column-content ol {
            padding-left: 1.25rem;
            margin: 0;
            font-size: 0.9rem;
            line-height: 1.6;
            color: #333333;
        }
        .pub-column-content li {
            margin-bottom: 1rem;
        }
        .pub-column-content a {
            color: #222222;
            text-decoration: none;
        }
        .pub-column-content a:hover {
            text-decoration: underline;
            color: var(--primary);
        }

        /* Gallery Layout */
        .gallery-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 2.5rem;
            max-width: 1000px;
            margin: 1rem auto;
        }
        .gallery-container img {
            width: 100%;
            height: auto;
            border-radius: 6px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        }

        /* Footer */
        footer {
            background-color: var(--bg-card);
            border-top: 1px solid var(--border);
            padding: 2rem 1.5rem;
            text-align: center;
            font-size: 0.85rem;
            color: var(--text-muted);
            margin-top: 4rem;
        }
    </style>
</head>
<body>
    <header>
        <div class="header-container">
            <div class="brand">
                <img src="images/logo.svg" alt="Dai Lab Logo" class="brand-logo">
                <h1>Dai Lab</h1>
            </div>
            <nav>
                <a href="index.html" {% if page_id == 'home' %}class="active"{% endif %}>Home</a>
                <a href="research.html" {% if page_id == 'research' %}class="active"{% endif %}>Research</a>
                <a href="publications.html" {% if page_id == 'publications' %}class="active"{% endif %}>Publications</a>
                <a href="team.html" {% if page_id == 'team' %}class="active"{% endif %}>Team</a>
                <a href="gallery.html" {% if page_id == 'gallery' %}class="active"{% endif %}>Gallery</a>
                <a href="contact.html" {% if page_id == 'contact' %}class="active"{% endif %}>Contact</a>
            </nav>
        </div>
    </header>

    
   {% if page_id == 'home' %}
    <div class="hero-banner">
        <img src="images/200L.jpg" alt="Dai Lab Welcome Image" class="hero-bg-img">
        <img src="images/logo.svg" alt="Dai Lab Logo" class="hero-logo-large">
    </div>
{% endif %}

    <main>
        {% if page_id == 'home' %}
            <div class="recruitment-banner">
                <div>We have immediate openings for post-doc and graduate students with microbiology, molecular biology, synthetic biology, biochemistry, electrochemistry and material sciences background.</div>
                <div class="recruitment-actions">
                    <a class="btn btn-primary" href="contact.html#join">How to apply</a>
                    <a class="btn btn-outline" href="mailto:{{ contact_email }}?subject={{ apply_subject | urlencode }}">Email the PI</a>
                </div>
            </div>

            <div class="platform-section">
                <h3 style="font-size: 1.5rem; font-weight: 700; margin-bottom: 2rem; color: #111;">Interdisciplinary Platforms for Biology, Chemistry, and Engineering</h3>
                <div class="platform-grid">
                    {% for p in platforms %}
                    <div class="platform-card">
                        <img src="{{ p.img }}" alt="Platform Image">
                        <p>{{ p.text }}</p>
                    </div>
                    {% endfor %}
                </div>
            </div>

            <div style="text-align: center; margin-bottom: 3.5rem;">
                <h2 style="color: var(--accent-red); font-size: 2rem; margin-bottom: 1.5rem;">News</h2>
                <div style="max-width: 900px; margin: 0 auto; display: flex; flex-direction: column; gap: 0.85rem;">
                    {% for item in news %}
                    <div style="font-size: 0.95rem; line-height: 1.6; color: #222;">{{ item | safe }}</div>
                    {% endfor %}
                </div>
            </div>

            <section class="values-section">
                <h2>Dai Lab Values</h2>
                <p class="values-lead">{{ values_lead }}</p>
                <div class="values-grid">
                    {% for val in values %}
                    <div class="value-card">
                        <div class="value-icon"><svg viewBox="0 0 24 24" aria-hidden="true">{{ val.icon | safe }}</svg></div>
                        <h3>{{ val.title }}</h3>
                        <p>{{ val.text }}</p>
                    </div>
                    {% endfor %}
                </div>
            </section>

        {% elif page_id == 'research' %}
            <div class="research-container">
                {% for sec in research_sections %}
                <div class="research-section">
                    <div class="research-title">{{ sec.title }}</div>
                    
                    <div class="research-description">
                        {% for p in sec.paragraphs %}
                        <p>{{ p }}</p>
                        {% endfor %}
                    </div>

                    {% if sec.banner %}
                        <div>
                            <img src="{{ sec.banner }}" alt="{{ sec.title }}" class="full-banner-img">
                        </div>
                    {% elif sec.images %}
                        <div class="research-image-row">
                            {% for img_path in sec.images %}
                            <img src="{{ img_path }}" alt="Research graphic">
                            {% endfor %}
                        </div>
                    {% endif %}
                </div>
                {% endfor %}
            </div>

        {% elif page_id == 'team' %}
            <div class="pi-container">
                <div class="pi-bio">
                    <p>{{ pi.bio }}</p>
                </div>
                <div class="pi-photo">
                    <img src="{{ pi.img }}" alt="{{ pi.name }}">
                </div>
            </div>

            <div class="pi-links">
                <div>
                    <span class="podcast-label">Podcast about the PI:</span>
                    <a href="{{ pi.podcast_url }}" target="_blank">{{ pi.podcast_url }}</a>
                </div>
                <div>
                    <span class="linkedin-label">Linkedin:</span>
                    <a href="{{ pi.linkedin_url }}" target="_blank">{{ pi.linkedin_url }}</a>
                </div>
            </div>

            <div class="section-heading-center">Group members</div>
            <div class="team-images-stack">
                <img src="{{ group_images.lab1 }}" alt="Group Members - Lab 1">
                <img src="{{ group_images.lab2 }}" alt="Group Members - Lab 2">
            </div>

        {% elif page_id == 'publications' %}
            <div class="scholar-section">
                <h2 style="color: var(--accent-red); font-size: 2rem; margin: 0 0 0.75rem 0;">Selected Publications</h2>
                <div class="scholar-link">
                    For the full list, see the <a href="{{ scholar_url }}" target="_blank" style="color: var(--primary); font-weight: 600; text-decoration: underline;">Google Scholar profile</a>.
                </div>
            </div>

            <div class="pub-tagline">
                {{ tagline }}
            </div>

            <div class="pub-grid">
                {% for pillar in pillars %}
                <div class="pub-column">
                    <img src="{{ pillar.img }}" alt="{{ pillar.title }}">
                    <div class="pub-column-title">
                        {{ pillar.title }}
                    </div>
                    <div class="pub-column-content">
                        <ol>
                            {% for paper in pillar.pub_list %}
                            <li>{{ paper | safe }}</li>
                            {% endfor %}
                        </ol>
                    </div>
                </div>
                {% endfor %}
            </div>

        {% elif page_id == 'gallery' %}
            <div class="gallery-container">
                {% for img in gallery_images %}
                <img src="{{ img }}" alt="Gallery Photo">
                {% endfor %}
            </div>

        {% elif page_id == 'contact' %}
            <div class="contact-grid">
                <div class="contact-card">
                    <h2>Get in touch</h2>
                    <p>
                        <span class="contact-label">Principal Investigator</span>
                        Dr. Susie Y. Dai, Professor
                    </p>
                    <p>
                        <span class="contact-label">Email</span>
                        <a href="mailto:{{ contact_email }}">{{ contact_email }}</a>
                    </p>
                    <p>
                        <span class="contact-label">Office</span>
                        Room 124, Christopher S. Bond Life Sciences Center<br>
                        1201 Rollins Street<br>
                        University of Missouri, Columbia, MO 65211
                    </p>
                    <p><a href="https://www.google.com/maps/search/?api=1&query=Bond+Life+Sciences+Center+1201+Rollins+St+Columbia+MO+65211" target="_blank" rel="noopener">View on map</a></p>
                </div>
                <div class="contact-card">
                    <h2>Affiliations</h2>
                    <p>
                        <span class="contact-label">Department</span>
                        <a href="https://engineering.missouri.edu/departments/chbme/" target="_blank" rel="noopener">Department of Chemical and Biomedical Engineering</a>
                    </p>
                    <p>
                        <span class="contact-label">Research center</span>
                        <a href="https://bondlsc.missouri.edu/labs/susie-dai/" target="_blank" rel="noopener">Christopher S. Bond Life Sciences Center</a>
                    </p>
                    <p>
                        <span class="contact-label">Publications</span>
                        <a href="https://scholar.google.com/citations?user=jWERWWsAAAAJ" target="_blank" rel="noopener">Google Scholar profile</a>
                    </p>
                </div>
            </div>

            <div class="join-section" id="join">
                <h2>Join the lab</h2>
                <p>We have immediate openings for <b>postdoctoral researchers</b> and <b>graduate students</b> with backgrounds in:</p>
                <ul>
                    {% for field in opening_fields %}
                    <li>{{ field }}</li>
                    {% endfor %}
                </ul>
                <p>To apply, email Dr. Dai with a short note on your research interests and your CV. Prospective graduate students should also apply to the <a href="https://engineering.missouri.edu/departments/chbme/" target="_blank" rel="noopener">Chemical and Biomedical Engineering graduate program</a>.</p>
                <a class="btn btn-primary" href="mailto:{{ contact_email }}?subject={{ apply_subject | urlencode }}">Email the PI</a>
            </div>
        {% endif %}
    </main>

    <footer>
        <p>&copy; Dai Lab — Department of Chemical and Biomedical Engineering; Bond Life Sciences Center, University of Missouri. All rights reserved.</p>
        <p><a href="contact.html" style="color: inherit;">Contact</a> &middot; <a href="mailto:{{ contact_email }}" style="color: inherit;">{{ contact_email }}</a></p>
    </footer>
    <script>
        // Shrink the sticky header once the reader scrolls down. The gap between the
        // two thresholds stops it flickering when the shrink itself shifts the page.
        (function () {
            var header = document.querySelector("header");
            function update() {
                var y = window.scrollY;
                if (y > 80) header.classList.add("scrolled");
                else if (y < 10) header.classList.remove("scrolled");
            }
            window.addEventListener("scroll", update, { passive: true });
            update();
        })();
    </script>
</body>
</html>
"""

# ----------------------------------------------------------------------
# 2. Central Site Data Structure
# ----------------------------------------------------------------------
SITE_URL = "https://www.dai-lab.com/"

SHARED = {
    "site_url": SITE_URL,
    "contact_email": "sydai@missouri.edu",
    "apply_subject": "Prospective lab member inquiry",
}

def pub(authors, title, journal, year, doi):
    return f'<b>{authors}</b>, <a href="https://doi.org/{doi}" target="_blank">{title}</a>, <i>{journal}</i>, {year}.'

def get_site_data():
    return {
        "index.html": {
            "page_id": "home",
            "title": "Welcome to the Dai Lab",
            "description": "The Dai Lab at the University of Missouri integrates synthetic biology, materials science, chemistry, and engineering for sustainable synthesis, PFAS and microplastic remediation, and environmental health.",
            "platforms": [
                {
                    "img": "images/main1.png",
                    "text": "We integrate synthetic biology, material science, chemistry and engineering approaches for sustainable synthesis and remediation."
                },
                {
                    "img": "images/main2.png",
                    "text": "We apply multiple bio/analytical platforms and data analytics to study and understand environmental chemical impacts on the environments and human population."
                },
                {
                    "img": "images/main3.png",
                    "text": "We care about our people. We outreach to communities with engineering intervention for a sustainable future."
                }
            ],
            "values_lead": "We value and welcome everyone’s unique contribution!",
            "values": [
                {
                    "title": "Think Broadly and Deeply",
                    "text": "We strive to think broadly and deeply, implementing novel ideas that advance science.",
                    "icon": '<path d="M9 18h6"/><path d="M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12.74V17h8v-2.26A7 7 0 0 0 12 2z"/>'
                },
                {
                    "title": "Serve the Community",
                    "text": "Our research serves the local community and the public.",
                    "icon": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>'
                },
                {
                    "title": "Rigor and Reproducibility",
                    "text": "We are dedicated to high-quality and reproducible research.",
                    "icon": '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>'
                },
                {
                    "title": "Inclusion and Collaboration",
                    "text": "Our lab fosters an inclusive and collaborative environment.",
                    "icon": '<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>'
                }
            ],
            "news": [
                "<b>September 2026</b>. Our collaborative work on renewable carbon fiber is published in <i>Matter</i> (with Joshua Yuan @ WashU). By adding lignin, an abundant waste product of paper pulping and biorefining, and guiding its crystallization with carbon nanotubes, the team cut petroleum-based PAN use by half and production costs by 25%, while substantially reducing carbon emissions. The resulting fiber meets automotive industry standards for strength and stiffness, opening the door to renewable carbon fiber for cars, aircraft, and wind turbines.",
                "<b>February 2026</b>. Our engineered algae for microplastic cleanup is featured by Mizzou Engineering, WashU, SciTechDaily, and other media outlets. The limonene-producing strain makes the cells water-repellent, so they clump together with microplastics and sink as easy-to-collect biomass. We are now scaling up with a 100-liter bioreactor prototype, with the goal of integrating the process into municipal wastewater treatment plants.",
                "<b>December 2025</b>. Our work on using engineered cyanobacteria to remediate and up-cycle microplastics is published in <i>Nature Communications</i>. The engineered strain removed 91.4% of microplastics within one hour while also taking up nutrients from wastewater. The captured microplastic-rich biomass can then be up-cycled into bioplastic composite films, turning a pollutant into a useful product.",
                "<b>August 2025</b>. We are very excited to have Dr. Kainan Chen join our lab as an Assistant Research Professor. Kainan is a long-time collaborator and a lead author on our CO2-to-bioplastics (<i>Chem</i>, 2022) and electro-biodiesel (<i>Joule</i>, 2024) work. He will help lead our research integrating electrocatalysis and synthetic biology for carbon upcycling.",
                "<b>July 2025</b>. Our collaborative work on a degradable bioplastic film is published in <i>Nature Communications</i> (with Joshua Yuan @ WashU). Inspired by the layered structure of plant leaves, the LEAFF film sandwiches cellulose between bioplastic layers to boost strength, transparency, and gas-barrier performance. The film fully degrades in ambient soil within about five weeks, offering a sustainable alternative for food packaging.",
                "<b>June 2025</b>. Welcome <b>Will Thives Santos</b>, our first graduate student at Mizzou! Will is a Mizzou graduate who is staying on as a Tiger to pursue graduate research with us. We are thrilled to have Will on the team.",
                "<b>November 2024</b>. Our lab has moved to the University of Missouri, Columbia, and is now located in the Bond Life Sciences Center. Dr. Dai joined the Department of Chemical and Biomedical Engineering, continuing our work on bioremediation, carbon upcycling, and environmental health. We look forward to new collaborations across Mizzou and the state of Missouri.",
                "<b>October 2024</b>. Our work on converting CO2 to biodiesel is published in <i>Joule</i>. By pairing a new zinc- and copper-based electrocatalyst with an engineered <i>Rhodococcus</i> strain, the system turns CO2 into lipids for biodiesel with 4.3% solar-to-fuel efficiency. This is about 45 times more efficient, and uses about 45 times less land, than soybean-based biodiesel. Congratulations, Kainan and the team!",
            ]
        },
        "research.html": {
            "page_id": "research",
            "title": "Research Areas",
            "description": "Dai Lab research: biological and material engineering for PFAS and microplastic remediation, electro-microbial conversion of CO2 to fuels and bioplastics, environmental surveillance, and community science.",
            "research_sections": [
                {
                    "title": "Biological and material engineering for remediation",
                    "paragraphs": [
                        "Nature maintains environmental balance through integrated biological and chemical processes that recycle waste efficiently. However, persistent contaminants such as PFAS and microplastics, along with excess nutrients like nitrogen and phosphate, challenge these natural systems. My research engineers and integrates biological platforms, including living fungi, algae, and bacteria, with bio-material development to remove and remediate emerging contaminants. Using systems biology and mechanistic analysis, we optimize bioremediation conditions and elucidate degradation pathways to design more efficient, scalable, and sustainable remediation technologies."
                    ],
                    "images": [
                        "images/remediation_pfas.png",
                        "images/remediation_photocatalysis.png",
                        "images/remediation_pathway.png"
                    ]
                },
                {
                    "title": "Integration of electrochemical process and synthetic biology",
                    "paragraphs": [
                        "The root cause of climate change is due to modern society's significant demand of energy and reliance on fossil energy. The natural photosynthesis cannot harvest enough solar energy for the current global energy consumption, when the majority photosynthesis inputs are used toward agriculture and infrastructure such as food, fiber and lumber. Our goal is to bypass photosynthesis to reach higher energy conversion rate, product yield, and pay off the carbon debt.",
                        "We integrate electrocatalysis and synthetic biology for high value product synthesis such as biplastics and fuels."
                    ],
                    "images": [
                        "images/electro_table.png",
                        "images/electro_reactor.png",
                        "images/electro_microbial.png"
                    ]
                },
                {
                    "title": "Environmental surveillance and health",
                    "paragraphs": [
                        "Environmental contaminants present health risks to human populations depending on the exposure routes. We are conducting bio-monitoring surveillance to understand population exposure to chemicals and toxic elements such as pesticides (neonicotinoids), environmental phenols ( BPA, BPF, BPS etc.), and heavy metals."
                    ],
                    "images": [
                        "images/surveillance_tap.jpg",
                        "images/Small molecule.png",
                        "images/PFAS.png"
                    ]
                },
                {
                    "title": "Community science, survey, and intervention",
                    "paragraphs": [
                        "Currently, we are working on an Arsenic Awareness Campaign in South Texas Counties."
                    ],
                    "banner": "images/community_water_banner.jpg"
                }
            ]
        },
        "publications.html": {
            "page_id": "publications",
            "title": "Selected Publications",
            "description": "Recent Dai Lab publications in Nature Communications, Joule, Chem, Matter, Green Chemistry, and more on sustainable manufacturing, remediation, and environmental monitoring.",
            "scholar_url": "https://tinyurl.com/scholarsusiedai",
            "tagline": "We integrate experiments and data analytics for synergized solutions",
            "pillars": [
                {
                    "title": "Sustainable Synthesis and Manufacturing",
                    "img": "images/pillar_synthesis.PNG",
                    "pub_list": [
                        pub("Li et al.", "Transforming renewable carbon fiber performance, economics, and sustainability via oriented crystallization design", "Matter", 2026, "10.1016/j.matt.2026.103001"),
                        pub("Dhatt et al.", "Biomimetic layered, ecological, advanced, multi-functional film for sustainable packaging", "Nature Communications", 2025, "10.1038/s41467-025-61693-2"),
                        pub("Chen et al.", "Electro-biodiesel empowered by co-design of microorganism and electrocatalysis", "Joule", 2025, "10.1016/j.joule.2024.10.001"),
                        pub("Li et al.", "Integrated design of multifunctional reinforced bioplastics (MReB) to synergistically enhance strength, degradability, and functionality", "Green Chemistry", 2025, "10.1039/d4gc02440k"),
                        pub("Zhou et al.", "Computational modeling-guided design of deep eutectic solvents for tailoring lignin chemistry during lignocellulose pretreatment", "Green Chemistry", 2025, "10.1039/d4gc06120a"),
                        pub("Zhang et al.", "Chem-bio interface design for rapid conversion of CO<sub>2</sub> to bioplastics in an integrated system", "Chem", 2022, "10.1016/j.chempr.2022.09.005"),
                        pub("Li et al.", "Lignin molecular design to transform green manufacturing", "Matter", 2022, "10.1016/j.matt.2022.07.011"),
                        pub("Long et al.", "Machine learning-informed and synthetic biology-enabled semi-continuous algal cultivation to unleash renewable fuel productivity", "Nature Communications", 2022, "10.1038/s41467-021-27665-y")
                    ]
                },
                {
                    "title": "Remediation and Recovery",
                    "img": "images/pillar_remediation.png",
                    "pub_list": [
                        pub("Zhang et al.", "Photocatalytic degradation of perfluorooctanoic acid under ambient conditions validated by duckweed as a sensitive ecotoxicity assay", "Journal of Hazardous Materials: Organics", 2026, "10.1016/j.hazmo.2026.100016"),
                        pub("Long et al.", "Remediation and upcycling of microplastics by algae with wastewater nutrient removal and bioproduction potential", "Nature Communications", 2025, "10.1038/s41467-025-67543-5"),
                        pub("Zhang et al.", "3D structure-functional design of a biomass-derived photocatalyst for antimicrobial efficacy and chemical degradation under ambient conditions", "Green Chemistry", 2024, "10.1039/d4gc01246a"),
                        pub("Santiago-Cruz et al.", "Carbon adsorbent properties impact hydrated electron activity and perfluorocarboxylic acid (PFCA) destruction", "ACS ES&amp;T Engineering", 2024, "10.1021/acsestengg.4c00211"),
                        pub("Wang et al.", "Microplastics removal in the aquatic environment via fungal pelletization", "Bioresource Technology Reports", 2023, "10.1016/j.biteb.2023.101545"),
                        pub("Yu et al.", "Genomic diversity and phenotypic variation in fungal decomposers involved in bioremediation of persistent organic pollutants", "Journal of Fungi", 2023, "10.3390/jof9040418"),
                        pub("Zhang et al.", "Design of biomass-based renewable materials for environmental remediation", "Trends in Biotechnology", 2022, "10.1016/j.tibtech.2022.09.011"),
                        pub("Li et al.", "Sustainable environmental remediation via biomimetic multifunctional lignocellulosic nano-framework", "Nature Communications", 2022, "10.1038/s41467-022-31881-5")
                    ]
                },
                {
                    "title": "Surveillance, Monitoring and Modeling",
                    "img": "images/pillar_surveillance.png",
                    "pub_list": [
                        pub("Jiang et al.", "The effects of federal incentives on the automotive market and greenhouse gas emissions", "Sustainable Futures", 2026, "10.1016/j.sftr.2026.102155"),
                        pub("Simmons et al.", "Iowa population exposures to metals and metalloids in well water", "Environmental Toxicology", 2026, "10.1002/tox.70005"),
                        pub("Chen et al.", "Life cycle assessment and social benefits of producing bioplastic polyhydroxyalkanoates (PHAs) via integrating electrochemical CO<sub>2</sub> conversion and microbial fermentation", "ACS Sustainable Chemistry &amp; Engineering", 2025, "10.1021/acssuschemeng.5c02891"),
                        pub("Mattson et al.", "Human biomonitoring without in-person interaction: public health engagements during the COVID-19 pandemic and future implications", "BMC Medical Research Methodology", 2024, "10.1186/s12874-024-02165-x"),
                        pub("Yu et al.", "Artificial intelligence-based HDX (AI-HDX) prediction reveals fundamental characteristics to protein dynamics: mechanisms on SARS-CoV-2 immune escape", "iScience", 2023, "10.1016/j.isci.2023.106282")
                    ]
                }
            ]
        },
        "team.html": {
            "page_id": "team",
            "title": "Lab Personnel",
            "description": "Meet Dr. Susie Dai, Professor of Chemical and Biomedical Engineering at the University of Missouri, and the members of the Dai Lab.",
            "pi": {
                "name": "Dr. Susie Dai",
                "img": "images/susie_dai.jpg",
                "bio": "Susie Dai received her BSc in Chemistry from Fudan University and PhD in Chemistry from Duke University, followed by postdoctoral training at Scripps Research Institute and Oak Ridge National Laboratory. She previously held research and leadership positions at university-based state agencies, including the Office of the Texas State Chemist and the Iowa State Hygienic Laboratory, integrating research with public service and regulatory science. She is currently a Professor at the University of Missouri, where her research integrates synthetic biology, protein engineering, catalysis, and materials science to advance sustainable biomanufacturing, carbon utilization, and environmental remediation. She has published broadly in journals including Joule, Chem, Nature Communications, PNAS, Advanced Science, and Angewandte Chemie.",
                "podcast_url": "https://www.peoplebehindthescience.com/dr-susie-dai/",
                "linkedin_url": "https://www.linkedin.com/in/susie-dai"
            },
            "group_images": {
                "lab1": "images/lab1.png",
                "lab2": "images/lab2.png"
            }
        },
        "gallery.html": {
            "page_id": "gallery",
            "title": "Gallery",
            "description": "Photos from the Dai Lab at the University of Missouri.",
            "gallery_images": [
                "images/gallary1.png",
                "images/gallary2.png"
            ]
        },
        "contact.html": {
            "page_id": "contact",
            "title": "Contact",
            "description": "Contact the Dai Lab at the Bond Life Sciences Center, University of Missouri. Openings for postdocs and graduate students.",
            "opening_fields": [
                "Microbiology",
                "Molecular biology",
                "Synthetic biology",
                "Biochemistry",
                "Electrochemistry",
                "Materials science"
            ]
        }
    }

# ----------------------------------------------------------------------
# 3. Execution & Build
# ----------------------------------------------------------------------
def build_site():
    site_data = get_site_data()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_img_dir = os.path.join(script_dir, "images")
    
    if not os.path.exists(target_img_dir):
        os.makedirs(target_img_dir)

    template = Template(MASTER_TEMPLATE)
    print("🚀 Building Pages...")
    page_urls = []
    for filename, data in site_data.items():
        page_url = SITE_URL if filename == "index.html" else SITE_URL + filename
        page_urls.append(page_url)
        with open(os.path.join(script_dir, filename), "w", encoding="utf-8") as f:
            f.write(template.render(**SHARED, **data, page_url=page_url))
        print(f"   --> Written: {filename}")

    with open(os.path.join(script_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for url in page_urls:
            f.write(f"  <url><loc>{url}</loc></url>\n")
        f.write("</urlset>\n")
    with open(os.path.join(script_dir, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}sitemap.xml\n")
    print("   --> Written: sitemap.xml, robots.txt")
    print("\n✨ Site build complete!\n")

if __name__ == "__main__":
    build_site()
