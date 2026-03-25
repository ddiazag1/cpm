import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_75 = (
    '<h2>The Age of Machines</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Spinning_jenny.jpg/800px-Spinning_jenny.jpg" '
    'alt="A model of the spinning jenny, an early machine of the Industrial Revolution" loading="lazy">'
    '<p class="image-caption">The spinning jenny \u2014 one of the inventions that launched the Industrial Revolution and changed how cloth was made forever</p>'
    '</div>'

    '<p>The telescope\u2019s hourglass dial turned on its own, and the brothers appeared '
    'inside an enormous building filled with deafening noise. Huge iron machines '
    'clattered and hissed, belching clouds of steam. The air was thick with lint and soot.</p>'

    '<p>\u201cWelcome to a cotton mill in <strong>Manchester, England</strong>,\u201d William said, '
    'raising his voice above the roar. \u201cThe year is about 1820. '
    'This is the <strong>Industrial Revolution</strong> \u2014 the moment humanity figured out '
    'how to make machines do the work that human hands had done for thousands of years.\u201d</p>'

    '<p>Robert covered his ears. \u201cIt\u2019s so loud! How can anyone work in here?\u201d</p>'

    '<h3>Why Britain?</h3>'

    '<p>\u201cThe Industrial Revolution began in <strong>Britain</strong> around the 1760s, '
    'and there were good reasons why,\u201d William said. '
    '\u201cBritain had huge deposits of <strong>coal</strong> and <strong>iron</strong> \u2014 '
    'the two raw materials that powered the new machines. '
    'It had a large navy and a vast trading empire that supplied raw cotton from America and India '
    'and provided markets to sell finished goods. It had rivers and canals for transportation, '
    'a stable government that protected property and patents, '
    'and a growing population of workers ready to fill the new factories.\u201d</p>'

    '<p>\u201cBut the biggest reason was <em>invention</em>. British tinkerers, engineers, and businessmen '
    'created a wave of machines that transformed one industry after another.\u201d</p>'

    '<h3>The Steam Engine</h3>'

    '<p>\u201cThe most important invention was the <strong>steam engine</strong>,\u201d William said. '
    '\u201cEarly steam engines were used to pump water out of coal mines. '
    'But in the 1760s and 1770s, a Scottish engineer named <strong>James Watt</strong> '
    'dramatically improved the design, making it powerful enough to drive factory machines, '
    'mill wheels, and eventually locomotives.\u201d</p>'

    '<p>\u201cThe steam engine turned <strong>heat</strong> into <strong>motion</strong>. '
    'You burned coal to boil water, the steam pushed a piston, '
    'and the piston turned a wheel. For the first time in history, '
    'humans had a source of power that didn\u2019t depend on muscle, wind, or flowing water. '
    'A single steam engine could do the work of dozens of horses.\u201d</p>'

    '<p>Robert watched a great iron beam rock back and forth, driven by jets of white steam. '
    '\u201cIt\u2019s like a metal giant breathing,\u201d he said.</p>'

    '<h3>Factories and Cities</h3>'

    '<p>\u201cBefore the Industrial Revolution, most people lived in the countryside,\u201d William said. '
    '\u201cFamilies spun thread and wove cloth at home using hand-powered spinning wheels and looms. '
    'It was slow, but people worked at their own pace, near their own gardens and animals.\u201d</p>'

    '<p>\u201cMachines changed everything. The <strong>spinning jenny</strong>, the <strong>water frame</strong>, '
    'and the <strong>power loom</strong> could produce cloth hundreds of times faster than hand workers. '
    'But these machines were expensive and needed power sources, '
    'so they were gathered together in large buildings called <strong>factories</strong>. '
    'Workers had to come to the machines, not the other way around.\u201d</p>'

    '<p>\u201cPeople poured out of the countryside and into new industrial cities. '
    '<strong>Manchester</strong> grew from 25,000 people in 1772 to over 300,000 by 1850. '
    '<strong>London</strong> became the largest city in the world. '
    'But these cities grew too fast. Workers were crammed into filthy slums '
    'with no clean water, no sewers, and no fresh air. '
    'Disease spread rapidly. Life expectancy in some factory cities '
    'dropped to just <strong>29 years</strong>.\u201d</p>'

    '<h3>Child Labor</h3>'

    '<p>\u201cOne of the darkest parts of the Industrial Revolution was <strong>child labor</strong>,\u201d '
    'William said, his voice serious. \u201cChildren as young as <strong>five or six</strong> '
    'worked in factories, mines, and chimneys. In cotton mills, small children '
    'crawled under moving machinery to sweep up loose cotton \u2014 '
    'a job called \u201cscavenging\u201d that cost many children their fingers, hands, or lives.\u201d</p>'

    '<p>\u201cIn coal mines, children worked as \u201ctrappers\u201d \u2014 sitting alone in complete darkness '
    'for twelve hours a day, opening and closing ventilation doors. '
    'Others dragged heavy coal carts through tunnels too small for adults. '
    'They worked 12 to 16 hours a day, six days a week, for pennies.\u201d</p>'

    '<p>Robert looked sick. \u201cKids our age?\u201d</p>'

    '<p>\u201cYounger,\u201d William said. \u201cIt took decades of campaigning to pass laws '
    'like the <strong>Factory Acts</strong> (starting in 1833), '
    'which limited children\u2019s working hours and eventually required them to attend school instead. '
    'People like <strong>Robert Owen</strong>, a factory owner who gave his workers shorter hours, '
    'decent housing, and schools for their children, proved that factories didn\u2019t have to be cruel.\u201d</p>'

    '<h3>Railroads</h3>'

    '<p>\u201cIn 1825, the world\u2019s first public railway opened in England \u2014 '
    'the <strong>Stockton and Darlington Railway</strong>,\u201d William said. '
    '\u201cBy 1830, the <strong>Liverpool and Manchester Railway</strong> was carrying passengers '
    'at the astonishing speed of 30 miles per hour. People thought they might suffocate '
    'traveling that fast!\u201d</p>'

    '<p>\u201cRailroads changed everything. Goods that once took days to move by horse and cart '
    'now traveled in hours. Fresh food could reach cities before it spoiled. '
    'People could travel to places they had never dreamed of visiting. '
    'By 1850, Britain had over <strong>6,000 miles</strong> of railroad track, '
    'and the technology was spreading across Europe and America.\u201d</p>'

    '<h3>How It Changed Daily Life</h3>'

    '<p>\u201cThe Industrial Revolution didn\u2019t just change how things were made \u2014 '
    'it changed how people <em>lived</em>,\u201d William said. '
    '\u201cBefore it, most humans lived much the way their great-great-grandparents had. '
    'After it, everything accelerated. Clothing became cheaper. '
    'Books became affordable. Gas lamps lit the streets. '
    'The telegraph let messages cross oceans in minutes instead of months.\u201d</p>'

    '<p>\u201cBut the revolution also created new problems: pollution, inequality between factory owners '
    'and workers, and overcrowded cities. Workers began forming <strong>trade unions</strong> '
    'to fight for better wages and safer conditions. '
    'The struggle between the power of industry and the rights of workers '
    'is a story that continues to this day.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="Industrial Revolution">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The Industrial Revolution (c. 1760\u20131840)</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Steam Power</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">James Watt\u2019s engine</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Heat \u2192 motion, replacing muscle</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Factories &amp; Cities</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Manchester: 25K \u2192 300K people</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Slums, disease, life expectancy 29</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Child Labor</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Children as young as 5 in mills</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Factory Acts began reform (1833)</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Railroads</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">6,000 miles of track by 1850</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Connected cities, transformed trade</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">Machines multiplied human power \u2014 but the human cost was enormous</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">The fight for workers\u2019 rights born in these factories continues today</text>'
    '</svg>'
    '</div>'

    '<p>The telescope brought them home. Robert looked at his hands.</p>'

    '<p>\u201cKids smaller than me were working in those mines,\u201d he said quietly.</p>'

    '<p>\u201cThey were,\u201d William said. \u201cAnd people fought to change that. '
    'Every time you go to school instead of a factory, you\u2019re living the result '
    'of that fight. Goodnight, young machines.\u201d</p>'

    '<p>\u201cGoodnight, age of steam.\u201d</p>'
)

disc_75 = [
    'The Industrial Revolution made goods cheaper and life more convenient, but it also brought terrible working conditions and child labor. Do you think the good things outweighed the bad, or was the cost too high?',
    'Children as young as five worked in factories and mines during the Industrial Revolution. What do you think finally convinced people that children should be in school instead of at work?',
    'Robert Owen proved that a factory could be profitable while still treating workers well. Why do you think more factory owners didn\u2019t follow his example?'
]

quiz_75 = [
    {
        "q": "Who dramatically improved the steam engine, making it powerful enough to drive factory machines?",
        "options": ["Robert Owen", "James Watt", "George Stephenson", "Richard Arkwright"],
        "correct": 1
    },
    {
        "q": "Why did the Industrial Revolution begin in Britain?",
        "options": [
            "Britain had the largest army in Europe",
            "Britain had coal, iron, rivers, and a stable government",
            "Britain was the largest country in Europe",
            "Britain had the most farmers"
        ],
        "correct": 1
    },
    {
        "q": "What laws began to limit child labor in British factories?",
        "options": [
            "The Bill of Rights",
            "The Magna Carta",
            "The Factory Acts",
            "The Trade Union Laws"
        ],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 75:
        lessons[i] = {
            "id": 75,
            "type": "history",
            "topic": "Industrial",
            "title": "The Age of Machines",
            "readingTime": "10 min",
            "story": story_75,
            "discussion": disc_75,
            "quiz": quiz_75
        }
        print("Updated lesson 75: The Age of Machines")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
