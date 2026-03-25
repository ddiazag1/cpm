import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_63 = (
    '<h2>The Great Plague</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Plague_in_Ashod.jpg/800px-Plague_in_Ashod.jpg" '
    'alt="The Plague of Ashdod by Nicolas Poussin" loading="lazy">'
    '<p class="image-caption">The Plague of Ashdod by Nicolas Poussin \u2014 depicting the terror and devastation of epidemic disease</p>'
    '</div>'

    '<p>William turned the hourglass dial on the brass telescope with unusual care. '
    '\u201cThis one is hard,\u201d he said quietly. \u201cBut it\u2019s one of the most important stories '
    'in human history. And you need to understand it.\u201d</p>'

    '<p>The world shifted, and the brothers found themselves standing on a stone dock '
    'in a Mediterranean port. Ships creaked at anchor. But something was wrong. '
    'The dockworkers were thin and fearful. A ship had just arrived, and no one was rushing '
    'to unload it. Instead, people backed away, covering their faces with cloth.</p>'

    '<p>\u201cThis is <strong>Messina, Sicily</strong>,\u201d William said. '
    '\u201c<strong>October 1347</strong>. Those ships just arrived from the Black Sea. '
    'And they\u2019re carrying something far more dangerous than cargo.\u201d</p>'

    '<h3>A Disease from the East</h3>'

    '<p>\u201cThe disease was the <strong>bubonic plague</strong>, caused by a bacterium called '
    '<strong><em>Yersinia pestis</em></strong>,\u201d William said. '
    '\u201cIt lived in <strong>fleas</strong> that lived on <strong>rats</strong>. '
    'When an infected flea bit a human, the bacteria entered the bloodstream. '
    'The disease had been lurking in Central Asia for centuries, '
    'but in the 1340s it began to spread westward along the <strong>Silk Road</strong> \u2014 '
    'the same trade routes the Mongols had made safe during the Pax Mongolica.\u201d</p>'

    '<p>\u201cTrade carried silk, spices, and ideas. But it also carried rats. '
    'And the rats carried fleas. And the fleas carried plague. '
    'The very connectedness that made the medieval world prosperous also made it vulnerable.\u201d</p>'

    '<p>\u201cWhen Genoese trading ships arrived in Messina from the Crimean port of Caffa, '
    'most of the sailors were already dead or dying. The harbor master tried to turn the ships away, '
    'but it was too late. The rats had already scurried down the mooring ropes and into the city.\u201d</p>'

    '<h3>The Symptoms</h3>'

    '<p>\u201cPeople called it the <strong>Black Death</strong> or the <strong>Great Pestilence</strong>,\u201d '
    'William said. \u201cThe symptoms appeared quickly. Within days of a flea bite, victims developed '
    'high fever, chills, and terrible aches. Then came the telltale sign: swollen lumps '
    'called <strong>buboes</strong> \u2014 the size of eggs or apples \u2014 in the neck, armpits, or groin. '
    'The swellings turned black (which is where the name \u2018Black Death\u2019 may come from). '
    'Victims suffered intense pain and most died within four to seven days.\u201d</p>'

    '<p>\u201cThere were even deadlier forms. <strong>Pneumonic plague</strong> attacked the lungs '
    'and spread through coughing \u2014 no fleas needed, just breathing near an infected person. '
    'It was almost 100 percent fatal without treatment. '
    '<strong>Septicemic plague</strong> entered the bloodstream directly and could kill within hours, '
    'sometimes before any symptoms appeared.\u201d</p>'

    '<p>Robert felt sick to his stomach. \u201cCouldn\u2019t doctors help?\u201d</p>'

    '<p>\u201cMedieval doctors had no idea what caused disease,\u201d William said gently. '
    '\u201cThey didn\u2019t know about bacteria \u2014 germ theory wouldn\u2019t exist for another 500 years. '
    'They thought plague was caused by \u2018bad air\u2019 (called <strong>miasma</strong>), '
    'the alignment of planets, or God\u2019s punishment for sin. '
    'Some doctors tried bloodletting, lancing the buboes, or burning aromatic herbs. '
    'Nothing worked.\u201d</p>'

    '<h3>The Spread</h3>'

    '<p>\u201cFrom Sicily, the plague spread with terrifying speed,\u201d William said. '
    '\u201cIt followed trade routes and shipping lanes. '
    'By early 1348, it had reached <strong>Italy, France, and Spain</strong>. '
    'By mid-1348, it was in <strong>England and Germany</strong>. '
    'By 1349, it had swept through <strong>Scandinavia</strong>. '
    'By 1351, it had reached <strong>Russia</strong> \u2014 completing a terrible circle '
    'back to the region where it had started.\u201d</p>'

    '<p>\u201cCities were hit hardest. People lived close together, sanitation was terrible, '
    'and rats thrived among the garbage. <strong>Florence</strong> lost half its population. '
    '<strong>Paris</strong> lost half. Some towns lost 70 or 80 percent. '
    'Entire villages were wiped out completely \u2014 abandoned forever.\u201d</p>'

    '<p>\u201cIn all, the Black Death killed an estimated <strong>75 to 200 million people</strong> '
    'across Eurasia and North Africa. In Europe alone, it killed roughly '
    '<strong>one out of every three people</strong> \u2014 '
    'perhaps 25 million out of a population of 75 million. '
    'It was the single deadliest event in recorded human history.\u201d</p>'

    '<h3>Fear, Faith, and Blame</h3>'

    '<p>\u201cWhen people are terrified and don\u2019t understand what\u2019s happening, '
    'they look for explanations \u2014 and for someone to blame,\u201d William said quietly. '
    '\u201cSome groups, called <strong>flagellants</strong>, marched through towns '
    'whipping themselves bloody, believing that extreme suffering would appease God\u2019s anger '
    'and end the plague. They attracted huge crowds but also spread the disease further.\u201d</p>'

    '<p>\u201cFar worse, many communities turned their fury on <strong>Jewish people</strong>. '
    'Rumors spread that Jews had poisoned the wells to cause the plague. '
    'It was completely false \u2014 Jews were dying of the plague at the same rate as everyone else \u2014 '
    'but mobs attacked Jewish communities across Europe. Hundreds of Jewish communities were destroyed, '
    'and thousands of Jewish people were murdered. '
    'Pope Clement VI condemned the attacks and pointed out that Jews were dying too, '
    'but his words did little to stop the violence.\u201d</p>'

    '<p>\u201cThis is one of history\u2019s most painful lessons,\u201d William said. '
    '\u201cWhen people are afraid and confused, they sometimes attack the most vulnerable '
    'instead of facing the real problem. It happened then. It has happened since.\u201d</p>'

    '<h3>The World After the Plague</h3>'

    '<p>\u201cThe Black Death didn\u2019t just kill people. It transformed European society,\u201d '
    'William said. \u201cWith one-third of the population dead, there was a massive '
    '<strong>labor shortage</strong>. Before the plague, peasants and serfs had been cheap and expendable. '
    'Now their labor was desperately needed. For the first time, ordinary workers '
    'could demand <strong>higher wages</strong>, better food, and more freedom.\u201d</p>'

    '<p>\u201cLords tried to freeze wages and force peasants back into serfdom. '
    'In England, the <strong>Statute of Laborers</strong> (1351) tried to cap wages at pre-plague levels. '
    'But it didn\u2019t work. You can\u2019t command a dead workforce back into existence. '
    'When authorities pushed too hard, peasants pushed back \u2014 '
    'the <strong>Peasants\u2019 Revolt</strong> of 1381 in England was directly fueled by plague-era frustrations.\u201d</p>'

    '<p>\u201cSerfdom \u2014 the system that had locked most Europeans into near-slavery for centuries \u2014 '
    'began to crumble. It took generations, but the Black Death set the process in motion. '
    'Peasants who had owned nothing began to acquire land from estates with no surviving heirs. '
    'The old feudal order, already weakened, started its long collapse.\u201d</p>'

    '<p>\u201cThe plague also shook people\u2019s faith in institutions. '
    'The Church had been the ultimate authority in medieval life, '
    'but it had been powerless against the plague. Priests died at even higher rates than laypeople '
    'because they tended the sick. People began to question \u2014 quietly at first \u2014 '
    'whether the Church had all the answers. '
    'This growing skepticism planted seeds that would eventually flower into the '
    '<strong>Renaissance</strong> and the <strong>Reformation</strong>.\u201d</p>'

    '<p>\u201cAnd the plague didn\u2019t truly go away. It returned every generation or so for the next 300 years. '
    'The Great Plague of London in 1665 was one of its last major European outbreaks. '
    'But <em>Yersinia pestis</em> still exists today. Modern antibiotics can treat it if caught early, '
    'but about 1,000\u20132,000 cases still occur worldwide each year.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 150" width="700" height="150" xmlns="http://www.w3.org/2000/svg" aria-label="Black Death spread and impact">'
    '<rect width="700" height="150" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The Black Death (1347\u20131351)</text>'

    '<rect x="20" y="30" width="155" height="55" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">The Cause</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Yersinia pestis bacterium</text>'
    '<text x="97" y="76" text-anchor="middle" fill="#b8a88a" font-size="7">Fleas \u2192 Rats \u2192 Humans</text>'

    '<rect x="190" y="30" width="155" height="55" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">The Toll</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">75\u2013200 million dead</text>'
    '<text x="267" y="76" text-anchor="middle" fill="#b8a88a" font-size="7">1 in 3 Europeans killed</text>'

    '<rect x="360" y="30" width="155" height="55" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">The Spread</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Silk Road \u2192 Ships \u2192 Cities</text>'
    '<text x="437" y="76" text-anchor="middle" fill="#b8a88a" font-size="7">Sicily (1347) to Russia (1351)</text>'

    '<rect x="530" y="30" width="150" height="55" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">The Aftermath</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Labor shortage \u2192 higher wages</text>'
    '<text x="605" y="76" text-anchor="middle" fill="#b8a88a" font-size="7">End of serfdom, seeds of Renaissance</text>'

    '<text x="350" y="108" text-anchor="middle" fill="#b8a88a" font-size="9">Messina (1347) \u2192 Italy \u2192 France \u2192 England \u2192 Germany \u2192 Scandinavia \u2192 Russia (1351)</text>'
    '<text x="350" y="122" text-anchor="middle" fill="#e8a838" font-size="8">The deadliest event in recorded human history \u2014 it reshaped European civilization</text>'
    '<text x="350" y="138" text-anchor="middle" fill="#b8a88a" font-size="8">Yersinia pestis still exists today \u2014 treatable with antibiotics, ~1,000 cases per year</text>'
    '</svg>'
    '</div>'

    '<p>The telescope brought them home. The harbor, the fearful faces, the silent ships \u2014 '
    'all dissolved into the warm safety of their room.</p>'

    '<p>Robert was quiet for a long time. \u201cOne-third of everyone,\u201d he said finally. '
    '\u201cI can\u2019t even imagine that.\u201d</p>'

    '<p>\u201cNo one could,\u201d William said. \u201cBut the people who survived rebuilt the world. '
    'And the world they built was different \u2014 freer, more questioning, less willing to accept '
    'the old ways just because they were old. The worst catastrophe in history planted the seeds '
    'of the modern world.\u201d</p>'

    '<p>\u201cGoodnight, William.\u201d</p>'

    '<p>\u201cGoodnight, Robert. Remember \u2014 the survivors rebuilt.\u201d</p>'
)

disc_63 = [
    "The same trade routes that spread wealth and knowledge also spread the plague. Can you think of modern examples where something that connects people also creates new dangers?",
    "During the Black Death, people blamed Jewish communities even though they were dying at the same rate. Why do you think people look for someone to blame during a crisis, and how can we resist that impulse?",
    "The labor shortage after the plague gave ordinary workers more power and helped end serfdom. Can you think of other examples in history where a disaster led to positive changes for everyday people?"
]

quiz_63 = [
    {
        "q": "What caused the bubonic plague?",
        "options": [
            "Bad air called miasma",
            "The bacterium Yersinia pestis, spread by fleas on rats",
            "Poisoned wells",
            "A curse from enemy kingdoms"
        ],
        "correct": 1
    },
    {
        "q": "Approximately what fraction of Europe\u2019s population died from the Black Death?",
        "options": ["One-tenth", "One-quarter", "One-third", "One-half"],
        "correct": 2
    },
    {
        "q": "How did the Black Death change life for surviving peasants?",
        "options": [
            "They were forced into stricter serfdom",
            "They fled to Asia to escape the plague",
            "They could demand higher wages due to the labor shortage",
            "They lost all their land to the Church"
        ],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 63:
        lessons[i] = {
            "id": 63,
            "type": "history",
            "topic": "Black Death",
            "title": "The Great Plague",
            "readingTime": "10 min",
            "story": story_63,
            "discussion": disc_63,
            "quiz": quiz_63
        }
        print("Updated lesson 63: The Great Plague")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
