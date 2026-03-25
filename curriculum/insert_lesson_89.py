import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_89 = (
    '<h2>The Information Revolution</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Eniac.jpg/800px-Eniac.jpg" '
    'alt="Two women operating the ENIAC computer, one of the first general-purpose electronic computers" loading="lazy">'
    '<p class="image-caption">ENIAC \u2014 one of the first electronic computers, built in 1945, filling an entire room</p>'
    '</div>'

    '<p>The telescope\u2019s hourglass dial turned, and the brothers appeared '
    'in a brightly lit room filled with enormous machines. '
    'Metal cabinets taller than a grown man lined every wall, '
    'connected by miles of wires. Vacuum tubes glowed orange. '
    'The room hummed and clicked and was hot enough to make them sweat.</p>'

    '<p>\u201cWhat is all this?\u201d Robert asked, eyes wide.</p>'

    '<p>\u201cThis,\u201d William said, \u201cis a <strong>computer</strong>. '
    'And it\u2019s about to change the world more than any invention since fire.\u201d</p>'

    '<h3>The First Computers</h3>'

    '<p>\u201cWe\u2019re standing inside <strong>ENIAC</strong> \u2014 the Electronic Numerical Integrator and Computer \u2014 '
    'built in 1945 at the University of Pennsylvania,\u201d William said. '
    '\u201cIt was one of the first general-purpose electronic computers. '
    'It weighed <strong>30 tons</strong>, filled an entire room, '
    'used <strong>18,000 vacuum tubes</strong>, and consumed enough electricity to power a small neighborhood. '
    'And do you know what it could do? Basic math. Slowly.\u201d</p>'

    '<p>Robert laughed. \u201cMy calculator does that.\u201d</p>'

    '<p>\u201cExactly,\u201d William said. \u201cThe story of the Digital Age is the story '
    'of how a room-sized calculator became the smartphone in your pocket \u2014 '
    'a device millions of times more powerful than ENIAC, '
    'and small enough to fit in your hand. And it happened in less than 80 years.\u201d</p>'

    '<h3>The Personal Computer</h3>'

    '<p>\u201cFor the first few decades, computers were enormous, expensive machines '
    'owned by governments, universities, and big corporations,\u201d William continued. '
    '\u201cBut in the 1970s, something changed. A new invention called the <strong>microprocessor</strong> \u2014 '
    'a tiny chip that could do the work of a room full of vacuum tubes \u2014 '
    'made it possible to build small, affordable computers.\u201d</p>'

    '<p>\u201cIn 1976, two college dropouts named <strong>Steve Jobs</strong> and <strong>Steve Wozniak</strong> '
    'built the <strong>Apple I</strong> computer in a garage in California. '
    'In 1981, <strong>IBM</strong> released its Personal Computer, or <strong>PC</strong>, '
    'which became the standard for business. A young programmer named <strong>Bill Gates</strong> '
    'wrote the operating system \u2014 <strong>MS-DOS</strong> \u2014 that ran on IBM\u2019s PC, '
    'and his company, <strong>Microsoft</strong>, eventually became one of the most valuable in the world.\u201d</p>'

    '<p>\u201cBy the late 1980s, personal computers were in millions of homes and offices. '
    'People used them to write documents, manage spreadsheets, play games, '
    'and store information. But they were still islands \u2014 '
    'each computer stood alone, unconnected to the others. '
    'The real revolution was about to come.\u201d</p>'

    '<h3>The World Wide Web</h3>'

    '<p>\u201cIn 1991, a British scientist named <strong>Tim Berners-Lee</strong>, '
    'working at CERN (a physics laboratory in Switzerland), '
    'invented the <strong>World Wide Web</strong>,\u201d William said. '
    '\u201cThe internet \u2014 a network connecting computers \u2014 already existed. '
    'But Berners-Lee created a way for anyone to share information on it '
    'using <strong>web pages</strong>, <strong>links</strong>, and <strong>browsers</strong>. '
    'He made the Web free and open to everyone. He could have become a billionaire, '
    'but he gave it away.\u201d</p>'

    '<p>\u201cThe effect was explosive. In 1993, there were about <strong>130 websites</strong> '
    'in the entire world. By 2000, there were over <strong>17 million</strong>. '
    'Today there are nearly <strong>2 billion</strong>. '
    'The Web connected humanity in a way that no invention had ever done before \u2014 '
    'not the printing press, not the telegraph, not the telephone, not television. '
    'Suddenly, a student in a small town could access the same information '
    'as a professor at a great university.\u201d</p>'

    '<h3>Smartphones and Social Media</h3>'

    '<p>\u201cIn 2007, Steve Jobs stood on a stage and held up a small rectangle of glass and metal,\u201d '
    'William said. \u201cThe <strong>iPhone</strong>. It was a phone, a camera, a music player, '
    'a map, a web browser, and a computer \u2014 all in one device. '
    'It changed everything again. Within a decade, '
    'more than <strong>3 billion people</strong> owned smartphones. '
    'For many people around the world, especially in developing countries, '
    'a smartphone was their first computer and their first connection to the internet.\u201d</p>'

    '<p>\u201c<strong>Social media</strong> followed \u2014 platforms like Facebook, Twitter, YouTube, '
    'and Instagram that let anyone share their thoughts, photos, and videos with the world. '
    'Social media helped organize revolutions, reconnect lost families, '
    'and give a voice to people who had never had one. '
    'But it also spread misinformation, created addiction, '
    'and made it harder to tell truth from fiction.\u201d</p>'

    '<h3>The Digital Divide and AI</h3>'

    '<p>\u201cNot everyone has benefited equally,\u201d William said. '
    '\u201cThe <strong>digital divide</strong> \u2014 the gap between people who have access to technology '
    'and those who don\u2019t \u2014 is one of the biggest challenges of our time. '
    'About <strong>2.6 billion people</strong> still have no internet access at all. '
    'Without it, they are cut off from education, jobs, and information '
    'that others take for granted.\u201d</p>'

    '<p>\u201cAnd now, a new chapter is beginning: <strong>artificial intelligence</strong>. '
    'Computers are learning to write, draw, translate languages, diagnose diseases, '
    'and even drive cars. AI is the most powerful technology humans have ever created, '
    'and how we use it will shape the future of civilization. '
    'Will it help solve our greatest problems \u2014 climate change, disease, poverty? '
    'Or will it create new problems we haven\u2019t imagined?\u201d</p>'

    '<p>\u201cThat\u2019s the question your generation will answer,\u201d William said.</p>'

    '<p>Robert looked at the massive ENIAC surrounding them, '
    'then thought about the phone in his pocket. '
    '\u201cFrom a room full of tubes to a device in my hand. In one lifetime.\u201d</p>'

    '<p>\u201cAnd the next leap,\u201d William said, \u201cwill be even bigger.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="Digital Age Timeline">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The Digital Age (1945\u2013Present)</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">ENIAC (1945)</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">First computers: 30 tons</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">18,000 vacuum tubes</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">PCs (1976\u201381)</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Apple, IBM, Microsoft</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Computers enter homes</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">World Wide Web (1991)</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Tim Berners-Lee, free &amp; open</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">130 sites \u2192 2 billion</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Smartphones &amp; AI</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">iPhone (2007), AI emerging</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">3 billion+ connected</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">Tim Berners-Lee gave the World Wide Web away for free \u2014 he could have been a billionaire</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">Your phone is millions of times more powerful than the computers that sent astronauts to the Moon</text>'
    '</svg>'
    '</div>'

    '<p>The telescope brought them home. Robert set it on the desk '
    'and looked at the screen of his tablet, glowing softly in the dark.</p>'

    '<p>\u201cAll the libraries in the world,\u201d he said. \u201cRight there.\u201d</p>'

    '<p>\u201cThe tool is in your hands,\u201d William said. '
    '\u201cWhat matters is what you do with it. '
    'Goodnight, information revolution.\u201d</p>'

    '<p>\u201cGoodnight, connected world.\u201d</p>'
)

disc_89 = [
    "Tim Berners-Lee invented the World Wide Web and gave it away for free instead of becoming a billionaire. Why do you think he made that choice? Was it the right one?",
    "Social media can help organize movements for justice, but it can also spread misinformation. How can you tell the difference between trustworthy information and false information online?",
    "About 2.6 billion people still have no internet access. How does the digital divide affect a child\u2019s chances in life, and what do you think should be done about it?"
]

quiz_89 = [
    {
        "q": "What was ENIAC?",
        "options": [
            "The first smartphone",
            "One of the first general-purpose electronic computers",
            "The first social media platform",
            "A type of early internet connection"
        ],
        "correct": 1
    },
    {
        "q": "Who invented the World Wide Web?",
        "options": ["Steve Jobs", "Bill Gates", "Tim Berners-Lee", "Mark Zuckerberg"],
        "correct": 2
    },
    {
        "q": "What is the \u2018digital divide\u2019?",
        "options": [
            "The gap between old and new computers",
            "The line between hardware and software",
            "The gap between people who have internet access and those who don\u2019t",
            "The difference between social media platforms"
        ],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 89:
        lessons[i] = {
            "id": 89,
            "type": "history",
            "topic": "Digital",
            "title": "The Information Revolution",
            "readingTime": "10 min",
            "story": story_89,
            "discussion": disc_89,
            "quiz": quiz_89
        }
        print("Updated lesson 89: The Information Revolution")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
