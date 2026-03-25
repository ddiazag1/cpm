import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_74 = (
    '<h2>Liberty, Equality, Fraternity</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Prise_de_la_Bastille.jpg/800px-Prise_de_la_Bastille.jpg" '
    'alt="Painting of the Storming of the Bastille on July 14, 1789" loading="lazy">'
    '<p class="image-caption">The Storming of the Bastille \u2014 July 14, 1789, the day that ignited the French Revolution</p>'
    '</div>'

    '<p>Evelyn traced her finger over a map of Europe. \u201cJason, you said the American Revolution '
    'inspired other countries. Did France have a revolution too?\u201d</p>'

    '<p>Jason smiled and opened The Living World, turning the brass clasp until the hourglass symbol glowed. '
    '\u201cFrance had one of the biggest, most dramatic revolutions in all of history.\u201d</p>'

    '<p>The green light carried them to a narrow cobblestone street in Paris. '
    'The air smelled of bread \u2014 or rather, the painful absence of it. '
    'Thin, ragged people lined up outside an empty bakery, their faces hollow with hunger.</p>'

    '<h3>A Kingdom in Crisis</h3>'

    '<p>\u201cIn the late 1700s, France was the most powerful country in Europe,\u201d '
    'Jason said. \u201cBut underneath the glittering palaces, the nation was falling apart. '
    'King <strong>Louis XVI</strong> and Queen <strong>Marie Antoinette</strong> lived in unimaginable luxury '
    'at the Palace of <strong>Versailles</strong> \u2014 a building with 700 rooms, '
    '1,200 fireplaces, and gardens stretching for miles.\u201d</p>'

    '<p>\u201cMeanwhile, ordinary French people were starving. France was divided into '
    '<strong>Three Estates</strong>. The <strong>First Estate</strong> was the clergy \u2014 '
    'church leaders who owned 10 percent of all the land and paid almost no taxes. '
    'The <strong>Second Estate</strong> was the nobility \u2014 about 400,000 people '
    'who held the best jobs, the biggest estates, and special privileges. '
    'And then there was the <strong>Third Estate</strong> \u2014 everyone else. '
    'That was <strong>98 percent</strong> of the population: peasants, workers, merchants, and lawyers. '
    'They paid nearly all the taxes and had almost no political power.\u201d</p>'

    '<p>Evelyn frowned. \u201cThat\u2019s not fair at all.\u201d</p>'

    '<p>\u201cIt wasn\u2019t,\u201d Jason agreed. \u201cAnd it got worse. France had spent enormous amounts of money '
    'helping America win its revolution \u2014 ironically, fighting for freedom abroad '
    'while denying it at home. The royal treasury was empty. '
    'Then in 1788, terrible harvests caused the price of bread to skyrocket. '
    'Bread was the main food for ordinary people, and suddenly a single loaf '
    'cost more than a worker earned in a day.\u201d</p>'

    '<h3>The Estates-General and the National Assembly</h3>'

    '<p>\u201cIn May 1789, King Louis XVI called a meeting of the <strong>Estates-General</strong> \u2014 '
    'representatives from all three estates \u2014 for the first time in 175 years,\u201d Jason said. '
    '\u201cHe needed them to approve new taxes. But the Third Estate had a different plan.\u201d</p>'

    '<p>\u201cWhen the Third Estate was locked out of the meeting hall, '
    'they gathered at a nearby indoor <strong>tennis court</strong> and swore the famous '
    '<strong>Tennis Court Oath</strong> \u2014 a promise not to disband until they had written '
    'a new constitution for France. They called themselves the <strong>National Assembly</strong>, '
    'declaring that they, not the king, represented the people.\u201d</p>'

    '<h3>Storming the Bastille</h3>'

    '<p>\u201cThe king sent soldiers to Paris,\u201d Jason continued. '
    '\u201cThe people feared a military crackdown. On <strong>July 14, 1789</strong>, '
    'an angry crowd marched to the <strong>Bastille</strong> \u2014 an old fortress and prison '
    'that symbolized royal tyranny. They stormed it, overwhelmed the guards, '
    'and tore it down stone by stone.\u201d</p>'

    '<p>\u201cThe fall of the Bastille was the spark that lit the revolution. '
    'Across France, peasants burned manor houses and destroyed records of their debts. '
    'The old order was crumbling.\u201d</p>'

    '<p>Evelyn watched as crowds surged through the streets carrying torches, '
    'shouting three words that would echo through history: '
    '<strong>\u201cLibert\u00e9! \u00c9galit\u00e9! Fraternit\u00e9!\u201d</strong> \u2014 '
    'Liberty! Equality! Brotherhood!</p>'

    '<h3>The Declaration of the Rights of Man</h3>'

    '<p>\u201cIn August 1789, the National Assembly adopted the <strong>Declaration of the Rights of Man '
    'and of the Citizen</strong>,\u201d Jason said. \u201cInspired by America\u2019s Declaration of Independence, '
    'it declared that all men are born free and equal, that sovereignty belongs to the nation \u2014 '
    'not the king \u2014 and that everyone has the right to liberty, property, security, '
    'and resistance to oppression.\u201d</p>'

    '<p>\u201cA woman named <strong>Olympe de Gouges</strong> wrote a companion document, '
    'the <em>Declaration of the Rights of Woman</em>, arguing that women deserved equal rights too. '
    'Sadly, her ideas were rejected, and she was later executed for speaking out.\u201d</p>'

    '<h3>The Reign of Terror</h3>'

    '<p>\u201cHere is where the revolution turned dark,\u201d Jason said quietly. '
    '\u201cKing Louis XVI was arrested, put on trial, and executed by <strong>guillotine</strong> '
    'in January 1793. Marie Antoinette was executed nine months later.\u201d</p>'

    '<p>\u201cA lawyer named <strong>Maximilien Robespierre</strong> rose to power '
    'and became the leader of the <strong>Committee of Public Safety</strong>. '
    'He believed that terror was necessary to protect the revolution. '
    'During the <strong>Reign of Terror</strong> (1793\u20131794), '
    'an estimated <strong>17,000 people</strong> were executed by guillotine, '
    'and thousands more died in prison. Anyone could be accused of being '
    'an \u201cenemy of the revolution\u201d \u2014 even former revolutionaries.\u201d</p>'

    '<p>Evelyn looked horrified. \u201cThey were killing the people on their own side?\u201d</p>'

    '<p>\u201cYes,\u201d Jason said. \u201cThe revolution began eating its own children. '
    'Finally, in July 1794, Robespierre himself was arrested and executed. '
    'The Terror was over, but France was exhausted and unstable.\u201d</p>'

    '<h3>Napoleon Rises</h3>'

    '<p>\u201cOut of this chaos, a young military general named <strong>Napoleon Bonaparte</strong> '
    'seized power in 1799,\u201d Jason said. \u201cHe promised to restore order '
    'and keep the revolution\u2019s best ideas \u2014 equality before the law, religious freedom, '
    'and careers based on talent rather than birth. '
    'Many French people were so tired of chaos that they welcomed a strong leader, '
    'even if it meant giving up some of the freedom they had fought for.\u201d</p>'

    '<p>\u201cThe revolution had started with a dream of liberty, equality, and brotherhood. '
    'It achieved real and lasting changes \u2014 the end of feudalism, the idea that governments '
    'must answer to the people, and a declaration of human rights that still inspires the world. '
    'But it also showed how quickly a fight for freedom can turn violent '
    'when fear takes the place of justice.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="French Revolution Timeline">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The French Revolution (1789\u20131799)</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Causes</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Debt, famine, inequality</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">98% paid taxes, 2% had power</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Bastille (July 14, 1789)</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Fortress stormed by the people</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Declaration of Rights of Man</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Reign of Terror</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">17,000 executed (1793\u20131794)</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Robespierre\u2019s rise and fall</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Napoleon (1799)</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Military general seizes power</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Order from chaos</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">Libert\u00e9, \u00c9galit\u00e9, Fraternit\u00e9 \u2014 ideals that changed the world forever</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">But freedom without justice can devour the very people who fight for it</text>'
    '</svg>'
    '</div>'

    '<p>The book brought them home. Evelyn sat quietly for a moment.</p>'

    '<p>\u201cThey wanted the same things as the Americans,\u201d she said. '
    '\u201cBut it went so wrong.\u201d</p>'

    '<p>\u201cIt did,\u201d Jason said. \u201cFreedom is precious, but it takes more than courage to keep it. '
    'It takes patience, and laws, and remembering that even your enemies are human. '
    'Goodnight, revolutionaries.\u201d</p>'

    '<p>\u201cGoodnight, libert\u00e9.\u201d</p>'
)

disc_74 = [
    'The French Revolution started with beautiful ideals \u2014 liberty, equality, brotherhood \u2014 but led to the Reign of Terror. How can a movement for freedom turn so violent, and what can people do to prevent that from happening?',
    'The Third Estate was 98 percent of the population but had almost no political power. Why do you think the First and Second Estates were able to keep this unfair system going for so long?',
    'Olympe de Gouges argued that the Declaration of the Rights of Man should include women too, but she was executed for speaking out. Why is it important to keep expanding who counts as \u201ceveryone\u201d when we talk about rights?'
]

quiz_74 = [
    {
        "q": "What event on July 14, 1789, is considered the start of the French Revolution?",
        "options": [
            "The Tennis Court Oath",
            "The execution of Louis XVI",
            "The Storming of the Bastille",
            "The march on Versailles"
        ],
        "correct": 2
    },
    {
        "q": "What percentage of France\u2019s population belonged to the Third Estate?",
        "options": ["50 percent", "75 percent", "90 percent", "98 percent"],
        "correct": 3
    },
    {
        "q": "Who led the Reign of Terror as head of the Committee of Public Safety?",
        "options": ["Napoleon Bonaparte", "Louis XVI", "Maximilien Robespierre", "Olympe de Gouges"],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 74:
        lessons[i] = {
            "id": 74,
            "type": "history",
            "topic": "Revolution",
            "title": "Liberty, Equality, Fraternity",
            "readingTime": "10 min",
            "story": story_74,
            "discussion": disc_74,
            "quiz": quiz_74
        }
        print("Updated lesson 74: Liberty, Equality, Fraternity")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
