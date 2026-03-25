import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_69 = (
    '<h2>Martin Luther\u2019s Big Idea</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Luther95theses.jpg/800px-Luther95theses.jpg" '
    'alt="Painting of Martin Luther nailing his 95 Theses to the church door in Wittenberg" loading="lazy">'
    '<p class="image-caption">Martin Luther posting his 95 Theses on the door of the Castle Church in Wittenberg, 1517</p>'
    '</div>'

    '<p>The telescope\u2019s hourglass turned, and the brothers appeared in a crowded German town square. '
    'Church bells were ringing. A monk in a dark robe was striding toward a wooden church door, '
    'a sheet of paper in one hand and a hammer in the other.</p>'

    '<p>\u201cWittenberg, Germany. October 31, 1517,\u201d William whispered. '
    '\u201cThat monk is about to start a revolution \u2014 and he doesn\u2019t even know it yet.\u201d</p>'

    '<h3>The Church That Ruled Europe</h3>'

    '<p>\u201cTo understand what\u2019s about to happen, you need to understand how powerful '
    'the <strong>Catholic Church</strong> was in medieval Europe,\u201d William said. '
    '\u201cThere was no separation of church and state. The Church was the state, '
    'or at least the most powerful institution in every kingdom. '
    'The <strong>Pope</strong> in Rome was considered God\u2019s representative on Earth. '
    'He could crown kings, excommunicate emperors, and call entire nations to war.\u201d</p>'

    '<p>\u201cThe Church controlled education, hospitals, and record-keeping. '
    'It collected <strong>tithes</strong> \u2014 a ten percent tax on everyone\u2019s income. '
    'It owned roughly one-third of all the land in Europe. Bishops lived in palaces. '
    'The Pope\u2019s court in Rome was one of the wealthiest institutions in the world. '
    'For most Europeans, the Church was the only authority they knew from birth to death \u2014 '
    'it baptized them, married them, and buried them.\u201d</p>'

    '<p>\u201cBut by the 1500s, many people were angry. '
    'Some priests couldn\u2019t read. Some bishops held multiple positions and never visited their churches. '
    'Popes fought wars, fathered children, and lived in breathtaking luxury. '
    'And then there was the problem that pushed one monk over the edge: '
    '<strong>indulgences</strong>.\u201d</p>'

    '<h3>Selling Salvation</h3>'

    '<p>\u201cAn <strong>indulgence</strong> was a document from the Church that reduced your punishment for sins,\u201d '
    'William explained. \u201cOriginally, indulgences were granted for acts of genuine piety \u2014 '
    'going on a pilgrimage or doing charitable work. But over time, the Church started '
    '<strong>selling</strong> them for cash.\u201d</p>'

    '<p>\u201cIn 1517, a Dominican friar named <strong>Johann Tetzel</strong> was traveling through Germany '
    'selling indulgences to raise money for the construction of <strong>St. Peter\u2019s Basilica</strong> in Rome. '
    'Tetzel had a famous sales pitch: '
    '\u2018As soon as the coin in the coffer rings, the soul from purgatory springs!\u2019 '
    'He told people they could buy forgiveness for sins they hadn\u2019t even committed yet. '
    'He told them they could free their dead relatives from <strong>purgatory</strong> \u2014 '
    'the place where souls waited to enter heaven \u2014 by paying money.\u201d</p>'

    '<p>Robert frowned. \u201cThat sounds like a scam.\u201d</p>'

    '<p>\u201cThat\u2019s exactly what Martin Luther thought,\u201d William said.</p>'

    '<h3>The 95 Theses</h3>'

    '<p>\u201c<strong>Martin Luther</strong> was an Augustinian monk and theology professor '
    'at the University of Wittenberg,\u201d William continued. '
    '\u201cHe was a deeply religious man who had spent years studying the Bible. '
    'And the more he studied, the more he believed the Church had gone terribly wrong.\u201d</p>'

    '<p>\u201cLuther believed that salvation came through <strong>faith alone</strong> \u2014 '
    'not through buying indulgences, not through rituals or pilgrimages, '
    'but through a genuine, personal relationship with God. '
    'He believed the Bible, not the Pope, was the ultimate authority on matters of faith. '
    'And he believed every Christian had the right to read the Bible for themselves.\u201d</p>'

    '<p>\u201cOn October 31, 1517, Luther wrote <strong>95 Theses</strong> \u2014 '
    '95 arguments against indulgences and Church corruption \u2014 '
    'and (according to tradition) nailed them to the door of the Castle Church in Wittenberg. '
    'Church doors were the community bulletin boards of the time. '
    'Luther didn\u2019t think he was starting a revolution. He thought he was starting a debate.\u201d</p>'

    '<h3>The Printing Press Changes Everything</h3>'

    '<p>\u201cBut here\u2019s where the printing press \u2014 the machine we just learned about \u2014 '
    'turned a debate into a revolution,\u201d William said. '
    '\u201cWithin two weeks, printers had translated Luther\u2019s 95 Theses from Latin into German '
    'and printed thousands of copies. Within a month, they had spread across Germany. '
    'Within two months, across Europe. Luther became the first person in history '
    'to go \u2018viral.\u2019\u201d</p>'

    '<p>\u201cLuther kept writing. He published pamphlets arguing that the Pope had no special authority, '
    'that priests should be allowed to marry, that services should be held in the local language '
    'instead of Latin, and that the Bible should be translated so everyone could read it. '
    'Printers couldn\u2019t keep up with demand. Between 1518 and 1525, Luther\u2019s writings '
    'made up roughly one-third of all German-language publications.\u201d</p>'

    '<p>\u201cThe Pope ordered Luther to take it all back. Luther refused. '
    'In 1521, he was called before the <strong>Diet of Worms</strong> \u2014 '
    'an assembly of the Holy Roman Empire (not a diet of actual worms). '
    'Emperor Charles V demanded Luther recant. '
    'Luther\u2019s answer became one of the most famous statements in history: '
    '\u2018Here I stand. I can do no other. God help me.\u2019\u201d</p>'

    '<p>\u201cHe was declared an outlaw. But a sympathetic German prince, '
    '<strong>Frederick the Wise</strong>, hid Luther in Wartburg Castle. '
    'There, Luther spent his exile translating the <strong>New Testament into German</strong> \u2014 '
    'so ordinary people could read God\u2019s word for themselves. '
    'It became the best-selling book in Germany.\u201d</p>'

    '<h3>The Reformation and Its Consequences</h3>'

    '<p>\u201cLuther\u2019s ideas split Christianity,\u201d William said. '
    '\u201cHis followers became known as <strong>Protestants</strong> \u2014 '
    'because they \u2018protested\u2019 against the Catholic Church. '
    'Other reformers built on Luther\u2019s work: <strong>John Calvin</strong> in Geneva '
    'emphasized predestination and strict moral discipline. '
    '<strong>King Henry VIII</strong> of England broke with the Pope entirely '
    '(partly over theology, mostly because the Pope wouldn\u2019t grant him a divorce) '
    'and created the <strong>Church of England</strong>.\u201d</p>'

    '<p>\u201cThe Catholic Church responded with the <strong>Counter-Reformation</strong>. '
    'The <strong>Council of Trent</strong> (1545\u20131563) reformed some abuses, '
    'clarified Catholic doctrine, and launched new efforts to spread Catholicism worldwide. '
    'The <strong>Jesuits</strong>, a new religious order, became brilliant educators and missionaries, '
    'establishing schools from Rome to Japan.\u201d</p>'

    '<p>\u201cBut the split also led to violence. '
    'The <strong>French Wars of Religion</strong> (1562\u20131598) killed millions. '
    'The <strong>Thirty Years\u2019 War</strong> (1618\u20131648) devastated Central Europe, '
    'killing roughly one-third of Germany\u2019s population \u2014 one of the deadliest conflicts in human history. '
    'Catholics and Protestants slaughtered each other for over a century '
    'before Europe finally, exhaustedly, accepted that Christians could disagree.\u201d</p>'

    '<h3>A Lasting Legacy</h3>'

    '<p>\u201cThe <strong>Peace of Westphalia</strong> (1648) that ended the Thirty Years\u2019 War '
    'established a principle that would shape the modern world: '
    'each state could choose its own religion. '
    'It was the beginning of <strong>religious tolerance</strong> \u2014 '
    'the idea that government and faith should be separated, '
    'that no one should be killed for believing differently.\u201d</p>'

    '<p>\u201cIt took another 150 years and an ocean crossing '
    'for that idea to become the First Amendment of the U.S. Constitution: '
    '<em>Congress shall make no law respecting an establishment of religion.</em> '
    'That sentence has its roots right here, in this town square, '
    'with a monk and a hammer.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 140" width="700" height="140" xmlns="http://www.w3.org/2000/svg" aria-label="The Reformation">'
    '<rect width="700" height="140" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The Protestant Reformation</text>'

    '<rect x="20" y="28" width="125" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="82" y="44" text-anchor="middle" fill="#e74c3c" font-size="8" font-weight="bold">Causes</text>'
    '<text x="82" y="57" text-anchor="middle" fill="#b8a88a" font-size="7">Indulgence sales</text>'
    '<text x="82" y="68" text-anchor="middle" fill="#b8a88a" font-size="7">Church corruption</text>'
    '<text x="82" y="79" text-anchor="middle" fill="#b8a88a" font-size="7">Printing press</text>'

    '<text x="158" y="55" fill="#b8a88a" font-size="14">\u2192</text>'

    '<rect x="175" y="28" width="125" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="237" y="44" text-anchor="middle" fill="#e8a838" font-size="8" font-weight="bold">Luther (1517)</text>'
    '<text x="237" y="57" text-anchor="middle" fill="#b8a88a" font-size="7">95 Theses</text>'
    '<text x="237" y="68" text-anchor="middle" fill="#b8a88a" font-size="7">Faith alone</text>'
    '<text x="237" y="79" text-anchor="middle" fill="#b8a88a" font-size="7">Bible in German</text>'

    '<text x="313" y="55" fill="#b8a88a" font-size="14">\u2192</text>'

    '<rect x="330" y="28" width="125" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="392" y="44" text-anchor="middle" fill="#4a90d9" font-size="8" font-weight="bold">Spread</text>'
    '<text x="392" y="57" text-anchor="middle" fill="#b8a88a" font-size="7">Calvin (Geneva)</text>'
    '<text x="392" y="68" text-anchor="middle" fill="#b8a88a" font-size="7">Henry VIII (England)</text>'
    '<text x="392" y="79" text-anchor="middle" fill="#b8a88a" font-size="7">Counter-Reformation</text>'

    '<text x="468" y="55" fill="#b8a88a" font-size="14">\u2192</text>'

    '<rect x="485" y="28" width="195" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="582" y="44" text-anchor="middle" fill="#2ecc71" font-size="8" font-weight="bold">Consequences</text>'
    '<text x="582" y="57" text-anchor="middle" fill="#b8a88a" font-size="7">Wars of Religion (millions died)</text>'
    '<text x="582" y="68" text-anchor="middle" fill="#b8a88a" font-size="7">Peace of Westphalia (1648)</text>'
    '<text x="582" y="79" text-anchor="middle" fill="#b8a88a" font-size="7">Religious freedom as a principle</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">Luther\u2019s writings = 1/3 of all German publications (1518\u20131525)</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">Thirty Years\u2019 War killed ~1/3 of Germany\u2019s population</text>'
    '<text x="350" y="135" text-anchor="middle" fill="#b8a88a" font-size="9">\u201cHere I stand. I can do no other.\u201d \u2014 Martin Luther, Diet of Worms, 1521</text>'
    '</svg>'
    '</div>'

    '<p>The telescope brought them home. The church bells faded. '
    'Robert was quiet for a long time.</p>'

    '<p>\u201cOne man with a list of complaints changed the entire world,\u201d he said.</p>'

    '<p>\u201cOne man with a list and a printing press,\u201d William corrected. '
    '\u201cIdeas without distribution are just thoughts. '
    'Goodnight, Martin Luther.\u201d</p>'

    '<p>\u201cGoodnight, 95 Theses.\u201d</p>'
)

disc_69 = [
    "Luther believed every person should be able to read the Bible for themselves instead of relying on priests to interpret it. What are the advantages and risks of letting everyone interpret important texts on their own?",
    "The Reformation led to both religious freedom and devastating wars. Can great progress happen without great conflict? Can you think of other examples where a positive change also caused terrible suffering?",
    "Luther\u2019s ideas went \u2018viral\u2019 thanks to the printing press, much like ideas spread on social media today. What are the similarities between the Reformation and modern movements that spread online?"
]

quiz_69 = [
    {
        "q": "What were indulgences?",
        "options": [
            "Special prayers said by monks",
            "Documents that reduced punishment for sins, often sold for money",
            "Gifts given to the Pope on his birthday",
            "Taxes collected by local governments"
        ],
        "correct": 1
    },
    {
        "q": "What famous statement did Martin Luther make at the Diet of Worms in 1521?",
        "options": [
            "\u201cGive me liberty or give me death\u201d",
            "\u201cI have a dream\u201d",
            "\u201cHere I stand. I can do no other.\u201d",
            "\u201cThe truth shall set you free\u201d"
        ],
        "correct": 2
    },
    {
        "q": "What technology allowed Luther\u2019s 95 Theses to spread across Europe so quickly?",
        "options": [
            "The telegraph",
            "The postal system",
            "The printing press",
            "The sailing ship"
        ],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 69:
        lessons[i] = {
            "id": 69,
            "type": "history",
            "topic": "Reformation",
            "title": "Martin Luther\u2019s Big Idea",
            "readingTime": "10 min",
            "story": story_69,
            "discussion": disc_69,
            "quiz": quiz_69
        }
        print("Updated lesson 69: Martin Luther\u2019s Big Idea")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
