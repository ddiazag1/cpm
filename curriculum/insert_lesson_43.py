import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_43 = (
    '<h2>Tiny Germs, Big Battles</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Salmonella_typhimurium.png/800px-Salmonella_typhimurium.png" '
    'alt="Salmonella bacteria magnified under an electron microscope, showing rod-shaped cells with flagella" loading="lazy">'
    '<p class="image-caption">Bacteria magnified thousands of times \u2014 tiny organisms invisible to the naked eye</p>'
    '</div>'

    '<p>William pressed his eye to the brass telescope and frowned. '
    '\u201cRobert, I sneezed eleven times today. What\u2019s making me sick?\u201d</p>'

    '<p>Robert smiled and turned the telescope\u2019s dial to its smallest setting. '
    '\u201cLet\u2019s go find out. Tonight we hunt the invisible.\u201d</p>'

    '<p>The golden light washed over them, and the brothers shrank \u2014 '
    'past the width of a hair, past the size of a dust mite, '
    'past anything visible to the naked eye \u2014 '
    'until they stood on the surface of William\u2019s own skin, '
    'a vast landscape of ridges and valleys stretching to the horizon.</p>'

    '<h3>Bacteria \u2014 The Single-Celled Survivors</h3>'

    '<p>\u201cLook around,\u201d Robert said. Dotting the skin\u2019s surface were thousands of tiny creatures \u2014 '
    'some shaped like rods, some like spheres, some like corkscrews. '
    'Each one was a single cell, far simpler than the human cells towering beneath them.</p>'

    '<p>\u201cThese are <strong>bacteria</strong>,\u201d Robert explained. '
    '\u201cThey\u2019re among the oldest living things on Earth \u2014 '
    'bacteria have been around for at least 3.5 billion years. '
    'Each one is a single cell with no nucleus. Its DNA floats freely inside, '
    'coiled in a loop. They\u2019re tiny \u2014 about one micrometer long, '
    'which means you could line up a thousand of them across the head of a pin.\u201d</p>'

    '<p>\u201cAre they all bad?\u201d William asked nervously.</p>'

    '<p>\u201cNot at all! Most bacteria are harmless, and many are incredibly helpful. '
    'Your body carries roughly <strong>38 trillion bacteria</strong> \u2014 '
    'that\u2019s about as many as your own human cells. '
    'Most of them live in your gut, forming what scientists call the <strong>gut microbiome</strong>. '
    'These friendly bacteria help you digest food, produce vitamins like vitamin K and B12, '
    'train your immune system, and even affect your mood by producing chemicals '
    'that talk to your brain.\u201d</p>'

    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Bacteriophage_structure.png/400px-Bacteriophage_structure.png" '
    'alt="Diagram of a bacteriophage virus showing its geometric head, tail, and leg-like fibers" loading="lazy">'
    '<p class="image-caption">A virus (bacteriophage) \u2014 not truly alive, but capable of hijacking living cells</p>'
    '</div>'

    '<h3>Viruses \u2014 The Hijackers</h3>'

    '<p>Something far smaller drifted past them \u2014 a tiny geometric shape, '
    'like a crystal ball covered in spikes. It was at least ten times smaller than the bacteria around it.</p>'

    '<p>\u201cThat\u2019s a <strong>virus</strong>,\u201d Robert said quietly. '
    '\u201cViruses are strange. They\u2019re not really alive \u2014 they can\u2019t eat, grow, '
    'or reproduce on their own. They\u2019re just a bundle of genetic instructions '
    '(DNA or RNA) wrapped in a protein coat. But when a virus lands on a living cell, '
    'it injects its instructions inside and <em>hijacks</em> the cell\u2019s machinery, '
    'forcing it to make thousands of copies of the virus. '
    'Eventually the cell bursts open, releasing all those copies to infect more cells.\u201d</p>'

    '<p>\u201cSo that\u2019s why I\u2019m sneezing?\u201d William asked.</p>'

    '<p>\u201cExactly. A cold virus invaded cells in your nose. '
    'The sneezing is your body\u2019s way of trying to blast the invaders out. '
    'Viruses cause colds, the flu, chickenpox, and COVID-19. '
    'Bacteria cause strep throat, ear infections, and food poisoning. '
    'The key difference: bacteria are living cells that can be killed with <strong>antibiotics</strong>. '
    'Viruses are not alive, so antibiotics don\u2019t work against them.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 160" width="700" height="160" xmlns="http://www.w3.org/2000/svg" aria-label="Bacteria versus virus comparison">'
    '<rect width="700" height="160" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">Bacteria vs. Viruses</text>'

    '<rect x="30" y="30" width="290" height="115" rx="6" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="175" y="48" text-anchor="middle" fill="#2ecc71" font-size="10" font-weight="bold">Bacteria</text>'
    '<text x="175" y="64" text-anchor="middle" fill="#b8a88a" font-size="8">Single-celled, living organisms</text>'
    '<text x="175" y="78" text-anchor="middle" fill="#b8a88a" font-size="8">Size: ~1 micrometer</text>'
    '<text x="175" y="92" text-anchor="middle" fill="#b8a88a" font-size="8">Have their own DNA + ribosomes</text>'
    '<text x="175" y="106" text-anchor="middle" fill="#b8a88a" font-size="8">Can reproduce on their own</text>'
    '<text x="175" y="120" text-anchor="middle" fill="#b8a88a" font-size="8">Killed by antibiotics</text>'
    '<text x="175" y="134" text-anchor="middle" fill="#b8a88a" font-size="8">Many are helpful (gut, soil, food)</text>'

    '<rect x="380" y="30" width="290" height="115" rx="6" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="525" y="48" text-anchor="middle" fill="#e74c3c" font-size="10" font-weight="bold">Viruses</text>'
    '<text x="525" y="64" text-anchor="middle" fill="#b8a88a" font-size="8">Not truly alive \u2014 no cells</text>'
    '<text x="525" y="78" text-anchor="middle" fill="#b8a88a" font-size="8">Size: ~0.02\u20130.3 micrometers</text>'
    '<text x="525" y="92" text-anchor="middle" fill="#b8a88a" font-size="8">Just DNA or RNA in a protein coat</text>'
    '<text x="525" y="106" text-anchor="middle" fill="#b8a88a" font-size="8">Must hijack a cell to reproduce</text>'
    '<text x="525" y="120" text-anchor="middle" fill="#b8a88a" font-size="8">Antibiotics do NOT work</text>'
    '<text x="525" y="134" text-anchor="middle" fill="#b8a88a" font-size="8">Fought with vaccines + immune system</text>'
    '</svg>'
    '</div>'

    '<h3>Your Immune System \u2014 An Army Inside You</h3>'

    '<p>The telescope carried them deeper, through the skin and into the bloodstream. '
    'Suddenly, a massive white blood cell surged past like a tank on patrol.</p>'

    '<p>\u201cYour <strong>immune system</strong> is your body\u2019s defense force,\u201d Robert said. '
    '\u201cIt has layers, like a castle. The first layer is your skin \u2014 '
    'a physical wall that keeps most germs out. Mucus in your nose and tears in your eyes '
    'contain enzymes that destroy bacteria on contact. Stomach acid kills most germs you swallow.\u201d</p>'

    '<p>\u201cBut some invaders get past the walls. That\u2019s when the second layer kicks in. '
    '<strong>White blood cells</strong> patrol your blood and tissues like soldiers. '
    'Some, called <strong>macrophages</strong>, swallow and digest germs whole \u2014 '
    'they\u2019re the front-line troops. Others, called <strong>T cells</strong>, '
    'coordinate the attack and destroy infected cells. '
    'And then there are <strong>B cells</strong>, which produce tiny Y-shaped proteins '
    'called <strong>antibodies</strong>.\u201d</p>'

    '<p>\u201cAntibodies are like custom-made keys,\u201d Robert continued. '
    '\u201cEach antibody fits one specific germ perfectly. When B cells find an invader, '
    'they produce millions of antibodies that lock onto the germ\u2019s surface, '
    'marking it for destruction. And here\u2019s the brilliant part: '
    'your B cells <strong>remember</strong> every germ they\u2019ve ever fought. '
    'If the same germ comes back years later, your body can produce antibodies '
    'within hours instead of days. That\u2019s why you usually only get chickenpox once.\u201d</p>'

    '<h3>Vaccines \u2014 Training Without the Battle</h3>'

    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Edward_Jenner2.jpg/440px-Edward_Jenner2.jpg" '
    'alt="Portrait of Edward Jenner, the physician who developed the first vaccine" loading="lazy">'
    '<p class="image-caption">Edward Jenner (1749\u20131823) \u2014 the father of vaccination</p>'
    '</div>'

    '<p>\u201cIn 1796, an English doctor named <strong>Edward Jenner</strong> noticed something '
    'remarkable,\u201d Robert said. \u201cMilkmaids who caught cowpox \u2014 a mild disease from cows \u2014 '
    'seemed to never catch <strong>smallpox</strong>, one of the deadliest diseases in history. '
    'Smallpox killed about 30 percent of the people it infected and left survivors scarred for life. '
    'It had killed hundreds of millions of people over centuries.\u201d</p>'

    '<p>\u201cJenner took material from a cowpox sore and scratched it into the arm '
    'of a young boy named James Phipps. The boy got mildly ill, then recovered. '
    'Later, Jenner exposed him to smallpox \u2014 and the boy didn\u2019t get sick. '
    'His immune system had learned to fight smallpox from the harmless cowpox.\u201d</p>'

    '<p>\u201cThat was the first <strong>vaccine</strong> \u2014 '
    'the word comes from <em>vacca</em>, Latin for cow. '
    'A vaccine gives your immune system a harmless preview of a germ \u2014 '
    'a weakened form, a dead form, or just a piece of the germ\u2019s protein coat \u2014 '
    'so your B cells can make antibodies and form memories '
    '<em>without</em> you ever getting dangerously sick. '
    'Thanks to vaccines, smallpox was completely eradicated in 1980. '
    'It\u2019s the only human disease ever wiped off the face of the Earth.\u201d</p>'

    '<h3>Antibiotics and the Resistance Problem</h3>'

    '<p>\u201cIn 1928, <strong>Alexander Fleming</strong> accidentally discovered that a mold '
    'called <em>Penicillium</em> killed bacteria growing in his lab dishes,\u201d Robert said. '
    '\u201cThis led to the first <strong>antibiotic</strong> \u2014 penicillin \u2014 '
    'which saved millions of lives during World War II and beyond. '
    'Antibiotics work by attacking parts of bacterial cells \u2014 '
    'breaking their cell walls, stopping them from copying DNA, '
    'or blocking the machinery they need to grow.\u201d</p>'

    '<p>\u201cBut here\u2019s the problem,\u201d Robert said seriously. '
    '\u201cBacteria reproduce incredibly fast \u2014 some species divide every 20 minutes. '
    'With so many copies, random mutations happen. Occasionally, a mutation makes '
    'a bacterium resistant to an antibiotic. If you stop taking your antibiotics early, '
    'you kill the weak bacteria but leave the resistant ones alive. '
    'They multiply and spread, creating <strong>antibiotic-resistant superbugs</strong> '
    'like MRSA. That\u2019s why doctors say: always finish your full course of antibiotics.\u201d</p>'

    '<h3>Louis Pasteur and the Germ Theory</h3>'

    '<p>\u201cFor most of history, people didn\u2019t even know germs existed,\u201d Robert said. '
    '\u201cThey thought diseases came from bad air or curses. '
    'In the 1860s, a French chemist named <strong>Louis Pasteur</strong> proved that '
    'microorganisms cause disease \u2014 the <strong>germ theory</strong>. '
    'He showed that heating liquids (now called <strong>pasteurization</strong>) '
    'killed harmful bacteria, making milk and wine safe. '
    'He also developed vaccines for rabies and anthrax.\u201d</p>'

    '<h3>The Power of Hand Washing</h3>'

    '<p>\u201cAnd before Pasteur, a Hungarian doctor named '
    '<strong>Ignaz Semmelweis</strong> made a heartbreaking discovery,\u201d Robert added. '
    '\u201cIn the 1840s, he noticed that mothers in hospitals were dying of infections '
    'at terrifying rates. He realized that doctors were going straight from autopsies '
    'to delivering babies <em>without washing their hands</em>. '
    'When he made doctors wash with chlorinated water, death rates dropped from '
    '18 percent to under 2 percent.\u201d</p>'

    '<p>\u201cBut other doctors mocked him. They were insulted by the suggestion '
    'that their hands were dirty. Semmelweis died in an asylum, heartbroken. '
    'Years later, Pasteur\u2019s germ theory proved he had been right all along. '
    'Today, hand washing is considered the single most effective way to prevent '
    'the spread of infectious disease.\u201d</p>'

    '<p>The telescope brought them back to the bedroom. '
    'William looked at his hands as if seeing them for the first time.</p>'

    '<p>\u201cThere\u2019s a whole invisible war happening everywhere,\u201d he said quietly.</p>'

    '<p>\u201cEvery second of every day,\u201d Robert agreed. '
    '\u201cBut your body has been winning that war for your entire life. '
    'Trillions of soldiers, on patrol right now, while you sleep.\u201d</p>'

    '<p>\u201cGoodnight, immune system,\u201d William whispered.</p>'

    '<p>\u201cGoodnight, friendly bacteria,\u201d Robert smiled. '
    '\u201cKeep up the good work.\u201d</p>'
)

disc_43 = [
    "Semmelweis was mocked for suggesting doctors should wash their hands, and he died before being proven right. Why do you think people sometimes reject ideas that later turn out to be true?",
    "Your body carries 38 trillion bacteria that help you digest food, make vitamins, and train your immune system. How does knowing this change the way you think about \u2018germs\u2019?",
    "Antibiotic-resistant superbugs are becoming a serious problem. What would happen if antibiotics stopped working entirely? How would medicine be different?"
]

quiz_43 = [
    {
        "q": "What is the main difference between bacteria and viruses?",
        "options": [
            "Bacteria are smaller than viruses",
            "Viruses are living cells and bacteria are not",
            "Bacteria are living cells; viruses are not truly alive",
            "Antibiotics kill viruses but not bacteria"
        ],
        "correct": 2
    },
    {
        "q": "Who developed the first vaccine by using cowpox to prevent smallpox?",
        "options": ["Louis Pasteur", "Alexander Fleming", "Edward Jenner", "Ignaz Semmelweis"],
        "correct": 2
    },
    {
        "q": "What Y-shaped proteins does your immune system produce to fight specific germs?",
        "options": ["Enzymes", "Hormones", "Antibodies", "Antigens"],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 43:
        lessons[i] = {
            "id": 43,
            "type": "science",
            "topic": "Biology",
            "title": "Tiny Germs, Big Battles",
            "readingTime": "10 min",
            "story": story_43,
            "discussion": disc_43,
            "quiz": quiz_43
        }
        print("Updated lesson 43: Tiny Germs, Big Battles")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
