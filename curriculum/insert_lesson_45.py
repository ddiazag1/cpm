import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_45 = (
    '<h2>Thinking Like a Scientist</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Pasteur-pet.jpg/440px-Pasteur-pet.jpg" '
    'alt="Portrait of Louis Pasteur working in his laboratory" loading="lazy">'
    '<p class="image-caption">Louis Pasteur in his laboratory \u2014 a scientist who changed the world by asking the right questions</p>'
    '</div>'

    '<p>William sat on his bed, frowning at a puddle of spilled milk on the floor. '
    '\u201cRobert, why does milk go bad? And why doesn\u2019t honey go bad? '
    'And why \u2014 \u201d</p>'

    '<p>Robert held up his hand and laughed. \u201cYou\u2019re already doing it, you know.\u201d</p>'

    '<p>\u201cDoing what?\u201d</p>'

    '<p>\u201cThinking like a scientist. Every great discovery starts with someone asking '
    '<em>why</em>.\u201d Robert picked up the telescope. '
    '\u201cTonight, we\u2019re not going to any particular place. '
    'We\u2019re going to learn the most powerful tool in science \u2014 '
    'the way scientists <em>think</em>.\u201d</p>'

    '<p>The golden light swept them away \u2014 not to outer space or into the bloodstream, '
    'but to a grand hall filled with floating images: '
    'Galileo on a tower, Pasteur in his lab, Darwin on the deck of the <em>Beagle</em>, '
    'scientists past and present frozen in their moments of discovery.</p>'

    '<h3>Step One: Observation</h3>'

    '<p>\u201cEvery scientific discovery begins with <strong>observation</strong> \u2014 '
    'paying careful attention to the world,\u201d Robert said. '
    '\u201cYou noticed that milk spoils but honey doesn\u2019t. '
    'That\u2019s an observation. A scientist doesn\u2019t just say \u2018huh, weird\u2019 '
    'and walk away. A scientist writes it down and asks: <em>why?</em>\u201d</p>'

    '<p>\u201cIn the 1830s, a young naturalist named <strong>Charles Darwin</strong> '
    'sailed to the Gal\u00e1pagos Islands on a ship called the <em>Beagle</em>. '
    'He observed that finches on different islands had different shaped beaks. '
    'Some had thick beaks for cracking seeds. Others had thin beaks for catching insects. '
    'Others had long beaks for probing cactus flowers. Same type of bird, different tools. '
    'He wrote everything down.\u201d</p>'

    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Darwin%27s_finches_by_Gould.jpg/800px-Darwin%27s_finches_by_Gould.jpg" '
    'alt="Illustrations of four Darwin finch species with differently shaped beaks" loading="lazy">'
    '<p class="image-caption">Darwin\u2019s finches \u2014 different beak shapes for different food sources</p>'
    '</div>'

    '<h3>Step Two: Hypothesis</h3>'

    '<p>\u201cAfter observing, a scientist forms a <strong>hypothesis</strong> \u2014 '
    'an educated guess that tries to explain what they observed,\u201d Robert said. '
    '\u201cA hypothesis isn\u2019t a random guess. It\u2019s based on what you already know, '
    'and it must be <strong>testable</strong> \u2014 '
    'you have to be able to design an experiment that could prove it wrong.\u201d</p>'

    '<p>\u201cDarwin\u2019s hypothesis: the finches all descended from a common ancestor, '
    'but over many generations, their beaks changed shape because birds with beaks '
    'better suited to the available food survived and reproduced more successfully. '
    'He called this <strong>natural selection</strong>.\u201d</p>'

    '<p>\u201cNotice what Darwin did <em>not</em> do,\u201d Robert said. '
    '\u201cHe didn\u2019t start with the answer and look for evidence to support it. '
    'He started with observations and built an explanation that fit the facts. '
    'That distinction is the heart of scientific thinking.\u201d</p>'

    '<h3>Step Three: Experiment</h3>'

    '<p>\u201cA hypothesis means nothing until it\u2019s tested,\u201d Robert continued. '
    '\u201cAn <strong>experiment</strong> is a carefully designed test. '
    'The key to a good experiment is <strong>controlling variables</strong> \u2014 '
    'changing only one thing at a time so you know what caused the result.\u201d</p>'

    '<p>The hall shifted, and they stood beside <strong>Galileo Galilei</strong> '
    'at the top of a tall tower in Pisa, Italy, around 1590.</p>'

    '<p>\u201cFor 2,000 years, everyone believed Aristotle\u2019s claim that heavier objects '
    'fall faster than lighter ones,\u201d Robert said. \u201cIt seemed obvious \u2014 '
    'drop a cannonball and a feather, and the cannonball hits first. '
    'But Galileo asked: is the feather slower because it\u2019s lighter, '
    'or because <em>air resistance</em> slows it down?\u201d</p>'

    '<p>\u201cSo he dropped two iron balls of different weights from the tower. '
    'Same material \u2014 so roughly the same air resistance relative to their weight. '
    'They hit the ground at almost exactly the same time. '
    'Galileo had controlled the variable (air resistance) '
    'and isolated the factor he wanted to test (weight). '
    'That\u2019s brilliant experimental design.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 200" width="700" height="200" xmlns="http://www.w3.org/2000/svg" aria-label="The scientific method">'
    '<rect width="700" height="200" fill="#0f1629" rx="8"/>'
    '<text x="350" y="20" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The Scientific Method</text>'

    '<rect x="30" y="40" width="100" height="40" rx="8" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="80" y="58" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Observe</text>'
    '<text x="80" y="70" text-anchor="middle" fill="#b8a88a" font-size="7">Notice something</text>'

    '<line x1="130" y1="60" x2="155" y2="60" stroke="#b8a88a" stroke-width="1.5" marker-end="url(#arrow45)"/>'

    '<rect x="155" y="40" width="100" height="40" rx="8" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="205" y="58" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Hypothesize</text>'
    '<text x="205" y="70" text-anchor="middle" fill="#b8a88a" font-size="7">Propose explanation</text>'

    '<line x1="255" y1="60" x2="280" y2="60" stroke="#b8a88a" stroke-width="1.5" marker-end="url(#arrow45)"/>'

    '<rect x="280" y="40" width="100" height="40" rx="8" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="330" y="58" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Experiment</text>'
    '<text x="330" y="70" text-anchor="middle" fill="#b8a88a" font-size="7">Test the idea</text>'

    '<line x1="380" y1="60" x2="405" y2="60" stroke="#b8a88a" stroke-width="1.5" marker-end="url(#arrow45)"/>'

    '<rect x="405" y="40" width="100" height="40" rx="8" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="455" y="58" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Analyze</text>'
    '<text x="455" y="70" text-anchor="middle" fill="#b8a88a" font-size="7">Study the data</text>'

    '<line x1="505" y1="60" x2="530" y2="60" stroke="#b8a88a" stroke-width="1.5" marker-end="url(#arrow45)"/>'

    '<rect x="530" y="40" width="120" height="40" rx="8" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="590" y="58" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Conclude</text>'
    '<text x="590" y="70" text-anchor="middle" fill="#b8a88a" font-size="7">Support or revise</text>'

    '<path d="M590,80 Q590,120 330,120 Q80,120 80,80" fill="none" stroke="#4a90d9" stroke-width="1.5" stroke-dasharray="4 3"/>'
    '<text x="335" y="115" text-anchor="middle" fill="#4a90d9" font-size="8">If results don\u2019t support hypothesis \u2192 revise and test again</text>'

    '<defs><marker id="arrow45" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">'
    '<path d="M0,0 L6,3 L0,6" fill="#b8a88a"/></marker></defs>'

    '<text x="350" y="155" text-anchor="middle" fill="#b8a88a" font-size="9" font-weight="bold">+ Peer Review</text>'
    '<text x="350" y="170" text-anchor="middle" fill="#b8a88a" font-size="8">Other scientists check your work, repeat your experiments, and try to prove you wrong.</text>'
    '<text x="350" y="185" text-anchor="middle" fill="#b8a88a" font-size="8">Only ideas that survive this challenge become accepted science.</text>'
    '</svg>'
    '</div>'

    '<h3>Step Four: Data and Evidence</h3>'

    '<p>\u201cAn experiment produces <strong>data</strong> \u2014 measurements, observations, numbers,\u201d '
    'Robert said. \u201cA scientist doesn\u2019t just remember what happened. '
    'They record everything carefully so others can check their work. '
    'The data is the <strong>evidence</strong> \u2014 '
    'the facts that either support or contradict the hypothesis.\u201d</p>'

    '<p>\u201cThis is where <strong>bias</strong> becomes dangerous,\u201d Robert warned. '
    '\u201cBias is when you see what you <em>want</em> to see instead of what\u2019s actually there. '
    'Maybe you love your hypothesis so much that you ignore data that contradicts it. '
    'Or maybe you only run the experiment until you get the result you wanted. '
    'Good scientists fight bias by keeping careful records, '
    'using large sample sizes, and being honest when the data doesn\u2019t match their prediction.\u201d</p>'

    '<h3>Step Five: Conclusion and Peer Review</h3>'

    '<p>\u201cAfter analyzing the data, a scientist draws a <strong>conclusion</strong>,\u201d Robert said. '
    '\u201cDid the evidence support the hypothesis? Or did it contradict it? '
    'Both answers are valuable. A failed hypothesis isn\u2019t a failed experiment \u2014 '
    'it\u2019s new knowledge. You\u2019ve learned something the universe doesn\u2019t do.\u201d</p>'

    '<p>\u201cThen comes the hardest part: <strong>peer review</strong>. '
    'The scientist publishes their methods, data, and conclusions, '
    'and other scientists around the world try to poke holes in the work. '
    'They repeat the experiments. They look for mistakes. They challenge every assumption. '
    'Only ideas that survive this gauntlet of criticism become accepted science. '
    'It\u2019s brutal, but it\u2019s what makes science trustworthy.\u201d</p>'

    '<h3>Pasteur\u2019s Swan-Neck Flasks</h3>'

    '<p>The hall carried them to a laboratory in Paris, 1859. '
    '<strong>Louis Pasteur</strong> stood before rows of elegant glass flasks '
    'with long, curved necks shaped like swan necks.</p>'

    '<p>\u201cFor centuries, people believed in <strong>spontaneous generation</strong> \u2014 '
    'the idea that living things could spring from nonliving matter,\u201d Robert said. '
    '\u201cLeave meat out and maggots appear. Leave grain in a dark corner and mice show up. '
    'People thought the meat <em>created</em> the maggots.\u201d</p>'

    '<p>\u201cPasteur designed a brilliant experiment. He boiled broth in two types of flask. '
    'In a regular open flask, the broth quickly became cloudy with microorganisms. '
    'But in his <strong>swan-neck flask</strong>, the broth stayed clear \u2014 '
    'for days, weeks, months, even years. The curved neck let air in '
    'but trapped dust and microbes in the bend. '
    'No contamination could reach the broth.\u201d</p>'

    '<p>\u201cWhen Pasteur broke the neck of the flask, letting dust fall in, '
    'the broth clouded within days. Proof: the microbes came from the <em>air</em>, '
    'not from the broth itself. Life comes from life \u2014 not from nothing. '
    'Spontaneous generation was dead, and the germ theory of disease was born.\u201d</p>'

    '<h3>Theory vs. Hypothesis \u2014 A Crucial Difference</h3>'

    '<p>\u201cPeople often say \u2018it\u2019s just a theory\u2019 as if a theory is a guess,\u201d Robert said. '
    '\u201cBut in science, a <strong>theory</strong> and a <strong>hypothesis</strong> '
    'are very different things.\u201d</p>'

    '<p>\u201cA <strong>hypothesis</strong> is a single testable prediction: '
    '\u2018I think heavier objects fall faster.\u2019 '
    'A <strong>theory</strong> is a broad, well-tested explanation supported by '
    'mountains of evidence from many experiments, many scientists, and many years. '
    'The theory of gravity, the germ theory of disease, the theory of evolution \u2014 '
    'these aren\u2019t guesses. They\u2019re the most rigorously tested ideas in all of human knowledge.\u201d</p>'

    '<p>\u201cDoes that mean theories are proven forever?\u201d William asked.</p>'

    '<p>\u201cNo \u2014 and that\u2019s what makes science special,\u201d Robert said. '
    '\u201cAll scientific knowledge is <strong>provisional</strong>. '
    'It\u2019s the best explanation we have <em>right now</em>, '
    'based on the evidence we have <em>right now</em>. '
    'If new evidence contradicts a theory, the theory gets revised or replaced. '
    'Newton\u2019s laws of motion worked perfectly for 200 years \u2014 '
    'until Einstein showed they were incomplete at very high speeds and strong gravity. '
    'Newton wasn\u2019t <em>wrong</em> exactly \u2014 his laws still work for everyday situations \u2014 '
    'but Einstein\u2019s theory was more complete.\u201d</p>'

    '<p>\u201cScience <em>changes its mind</em> when the evidence demands it. '
    'That\u2019s not a weakness \u2014 it\u2019s science\u2019s greatest strength. '
    'No other way of knowing is brave enough to say: '
    '\u2018We were wrong, and here\u2019s what we\u2019ve learned.\u2019\u201d</p>'

    '<h3>Tying It All Together</h3>'

    '<p>The images in the grand hall began to connect \u2014 threads of gold light linking '
    'one discovery to the next. Galileo\u2019s experiments led to Newton\u2019s laws. '
    'Pasteur\u2019s germ theory led to Jenner\u2019s vaccines. '
    'Darwin\u2019s observations of finches led to our understanding of DNA and genetics. '
    'Every lesson they had learned \u2014 atoms, cells, planets, forces, ecosystems \u2014 '
    'was connected in a vast web of knowledge built by people who asked <em>why</em> '
    'and had the courage to follow the evidence wherever it led.</p>'

    '<p>\u201cThis is what we\u2019ve been doing all along,\u201d William realized. '
    '\u201cEvery night with the telescope \u2014 observing, asking questions, '
    'looking for evidence, building understanding.\u201d</p>'

    '<p>\u201cYou\u2019ve been thinking like a scientist since the very first night,\u201d '
    'Robert said proudly. \u201cThe scientific method isn\u2019t just for laboratories '
    'and people in white coats. It\u2019s for anyone who looks at the world and asks: '
    '<em>I wonder why?</em>\u201d</p>'

    '<p>The telescope brought them home one last time. '
    'William held it carefully, feeling its familiar weight in his hands \u2014 '
    'the instrument that had shown him the rings of Saturn, the inside of a cell, '
    'the dance of atoms, the bones of dinosaurs, and the birth of stars.</p>'

    '<p>\u201cGoodnight, Robert,\u201d William said. '
    '\u201cThank you for teaching me to ask why.\u201d</p>'

    '<p>\u201cYou already knew how,\u201d Robert said. '
    '\u201cI just showed you where to point the telescope. '
    'Goodnight, scientist.\u201d</p>'

    '<p>\u201cGoodnight, universe,\u201d William whispered. '
    '\u201cI\u2019m not done asking questions.\u201d</p>'
)

disc_45 = [
    "Robert says that science \u2018changes its mind\u2019 when new evidence appears, and that this is a strength, not a weakness. Do you agree? Can you think of other areas of life where changing your mind based on new information is a good thing?",
    "Pasteur\u2019s swan-neck flask experiment was elegant and simple, yet it overturned centuries of belief. Why do you think the best experiments are often the simplest ones?",
    "Throughout these lessons, you\u2019ve learned about atoms, cells, planets, forces, ecosystems, and more. Which discovery or idea was the most surprising to you, and why? What question do you still want answered?"
]

quiz_45 = [
    {
        "q": "What is the correct order of the scientific method?",
        "options": [
            "Hypothesize, observe, conclude, experiment",
            "Observe, hypothesize, experiment, analyze, conclude",
            "Experiment, observe, hypothesize, conclude",
            "Conclude, observe, experiment, hypothesize"
        ],
        "correct": 1
    },
    {
        "q": "In science, what is the difference between a hypothesis and a theory?",
        "options": [
            "A theory is just a guess; a hypothesis is proven",
            "A hypothesis is a testable prediction; a theory is a well-tested explanation supported by extensive evidence",
            "They mean the same thing",
            "A hypothesis is always correct; a theory can be wrong"
        ],
        "correct": 1
    },
    {
        "q": "What did Pasteur\u2019s swan-neck flask experiment disprove?",
        "options": [
            "The germ theory of disease",
            "The theory of evolution",
            "Spontaneous generation",
            "The law of conservation of mass"
        ],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 45:
        lessons[i] = {
            "id": 45,
            "type": "science",
            "topic": "Biology",
            "title": "Thinking Like a Scientist",
            "readingTime": "10 min",
            "story": story_45,
            "discussion": disc_45,
            "quiz": quiz_45
        }
        print("Updated lesson 45: Thinking Like a Scientist")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
