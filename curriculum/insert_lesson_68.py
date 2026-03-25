import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_68 = (
    '<h2>The Machine That Changed the World</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/PrintMus_038.jpg/800px-PrintMus_038.jpg" '
    'alt="A reconstruction of Gutenberg\u2019s printing press" loading="lazy">'
    '<p class="image-caption">A reconstruction of Gutenberg\u2019s printing press \u2014 the machine that launched the information age</p>'
    '</div>'

    '<p>Evelyn was copying a poem into her notebook, carefully writing each letter. '
    '\u201cThis is taking forever,\u201d she sighed. \u201cImagine having to copy an entire book by hand.\u201d</p>'

    '<p>Jason opened The Living World and turned the brass clasp. '
    '\u201cPeople did exactly that for a thousand years. '
    'Let me show you the man who ended it.\u201d</p>'

    '<p>The green light carried them into a dim workshop that smelled of ink and hot metal. '
    'A bearded man in a leather apron was carefully arranging tiny metal letters '
    'into a wooden frame, working by candlelight. Behind him stood a massive wooden machine '
    'that looked like a wine press.</p>'

    '<h3>A World Before Printing</h3>'

    '<p>\u201cBefore we meet him, you need to understand what books were like before this moment,\u201d '
    'Jason said. \u201cIn medieval Europe, every single book was copied <strong>by hand</strong>. '
    'Monks in monasteries spent years \u2014 sometimes an entire lifetime \u2014 '
    'copying a single Bible. Each page was painstakingly written with a quill pen on '
    '<strong>vellum</strong>, which was made from calfskin. A single Bible required '
    'the skins of about 250 calves.\u201d</p>'

    '<p>\u201cBecause books took so long to make, they were incredibly rare and expensive. '
    'A handwritten Bible cost roughly the same as a house. '
    'Most churches didn\u2019t even own a complete Bible. '
    'Universities might have a few dozen books chained to desks so students couldn\u2019t steal them. '
    'In all of Europe, there were perhaps a few thousand books in total. '
    'The vast majority of people \u2014 more than 90 percent \u2014 could not read.\u201d</p>'

    '<p>\u201cKnowledge was controlled by those who controlled books: '
    'the Church, the universities, the nobility. '
    'If you wanted to spread a new idea, you had to copy it by hand and hope someone passed it along. '
    'Ideas moved at the speed of a monk\u2019s pen.\u201d</p>'

    '<h3>Johannes Gutenberg</h3>'

    '<p>\u201cThat man,\u201d Jason pointed to the figure at the workbench, '
    '\u201cis <strong>Johannes Gutenberg</strong>, a German goldsmith from Mainz. '
    'Around 1440, he invented something that would transform civilization: '
    '<strong>movable type</strong> and the <strong>printing press</strong>.\u201d</p>'

    '<p>\u201cNow, printing itself wasn\u2019t entirely new. The Chinese had invented '
    '<strong>woodblock printing</strong> centuries earlier, and a Korean inventor named '
    '<strong>Choe Yun-ui</strong> had created movable metal type around 1230. '
    'But Gutenberg\u2019s genius was putting together a complete <strong>system</strong> '
    'that made mass printing practical for the first time in Europe.\u201d</p>'

    '<p>\u201cHere\u2019s how it worked,\u201d Jason said, stepping closer to the workbench. '
    '\u201cFirst, Gutenberg used his goldsmithing skills to create a special metal alloy \u2014 '
    'a mixture of lead, tin, and antimony \u2014 that melted easily, '
    'flowed smoothly into molds, and hardened quickly. '
    'He carved a letter in reverse on a steel punch, '
    'hammered it into a copper mold (called a <strong>matrix</strong>), '
    'and then poured the molten metal in. '
    'Out popped a perfect, identical piece of <strong>movable type</strong> \u2014 '
    'a tiny metal block with a raised letter on top.\u201d</p>'

    '<p>\u201cHe made hundreds of copies of each letter. '
    'A typesetter arranged the individual letters into words, '
    'words into lines, lines into pages. '
    'The page of type was locked into a frame, coated with oil-based ink '
    '(another Gutenberg innovation \u2014 previous inks were water-based and wouldn\u2019t stick to metal), '
    'and pressed against a sheet of paper using a modified wine press or olive press.\u201d</p>'

    '<p>\u201cWhen the page was printed, the type could be taken apart and '
    '<strong>reused</strong> to set the next page. '
    'That was the revolutionary part \u2014 the letters were <em>movable</em>. '
    'One set of type could print an unlimited number of different pages.\u201d</p>'

    '<h3>The Gutenberg Bible</h3>'

    '<p>\u201cGutenberg\u2019s masterpiece was the <strong>Gutenberg Bible</strong>, '
    'printed around 1455,\u201d Jason said. \u201cIt was a Latin Bible of 1,282 pages, '
    'printed in two columns of 42 lines each (which is why it\u2019s also called the <strong>42-line Bible</strong>). '
    'About 180 copies were printed \u2014 some on paper, some on vellum. '
    'Each copy was then <strong>hand-decorated</strong> with colored initials and illustrations '
    'by artists called <strong>rubricators</strong>, so every copy was unique.\u201d</p>'

    '<p>\u201cIt was stunningly beautiful \u2014 so well made that many people thought '
    'the copies <em>were</em> handwritten. But the speed was the miracle. '
    'A monk might spend two years copying a single Bible. '
    'Gutenberg\u2019s press could produce 180 copies in the same time. '
    'Today, about 49 copies survive. Each one is worth around $30 million.\u201d</p>'

    '<p>Evelyn stared at the press. \u201cSo it was like a copy machine?\u201d</p>'

    '<p>\u201cBetter,\u201d Jason said. \u201cA copy machine copies what already exists. '
    'The printing press created something that didn\u2019t exist before: '
    '<strong>mass communication</strong>.\u201d</p>'

    '<h3>The Explosion of Ideas</h3>'

    '<p>\u201cWithin 50 years of Gutenberg\u2019s invention, '
    'printing presses had spread to every major city in Europe,\u201d Jason said. '
    '\u201cBy 1500, an estimated <strong>20 million books</strong> had been printed \u2014 '
    'more than all the handwritten books produced in the previous thousand years combined. '
    'The price of a book dropped by about 80 percent. '
    'For the first time, ordinary people could afford to own books.\u201d</p>'

    '<p>\u201cAnd that changed <em>everything</em>.\u201d</p>'

    '<p>\u201c<strong>Literacy</strong> exploded. People who could never have afforded a handwritten manuscript '
    'could now buy a printed pamphlet for a few pennies. '
    'Schools multiplied because there were finally enough books for students to read. '
    'Ideas that would have taken decades to spread by hand '
    'could now reach thousands of people in weeks.\u201d</p>'

    '<p>\u201cThe <strong>Protestant Reformation</strong> \u2014 which we\u2019ll learn about soon \u2014 '
    'would have been impossible without the printing press. '
    'When Martin Luther posted his 95 Theses in 1517, printers turned them into pamphlets '
    'that spread across Germany in two weeks and across Europe in a month. '
    'Without printing, Luther would have been just another priest with a complaint. '
    'With printing, he started a revolution.\u201d</p>'

    '<p>\u201cThe <strong>Scientific Revolution</strong> depended on printing too. '
    'Scientists could publish their findings and have them read by other scientists across Europe. '
    'Copernicus published his theory that the Earth orbited the Sun. '
    'Galileo published his telescopic observations. '
    'Isaac Newton published his laws of motion. '
    'Each built on the others\u2019 work \u2014 because they could <em>read</em> the others\u2019 work.\u201d</p>'

    '<h3>The First Internet</h3>'

    '<p>\u201cPeople sometimes call the printing press the <strong>internet of its time</strong>,\u201d '
    'Jason said. \u201cAnd the comparison is almost perfect. '
    'Before printing, information was controlled by a small elite. '
    'After printing, anyone with access to a press could share ideas with the world. '
    'Before the internet, information was controlled by publishers, broadcasters, and governments. '
    'After the internet, anyone with a connection could reach millions.\u201d</p>'

    '<p>\u201cBoth inventions created an explosion of knowledge \u2014 and an explosion of misinformation. '
    'Just as the internet is full of both brilliant research and dangerous nonsense, '
    'the early printing world was full of both scientific breakthroughs and conspiracy theories. '
    'People printed pamphlets blaming witches for plagues, '
    'fake miracle cures, and political propaganda. '
    'The challenge of sorting good information from bad is not a modern problem \u2014 '
    'it\u2019s as old as Gutenberg.\u201d</p>'

    '<p>\u201cBut the balance tips toward progress. '
    'When more people can read, think, and share ideas, '
    'the world gets better \u2014 slowly, messily, but undeniably. '
    'The printing press didn\u2019t just change how books were made. '
    'It changed how <em>humans think</em>.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 140" width="700" height="140" xmlns="http://www.w3.org/2000/svg" aria-label="Impact of the Printing Press">'
    '<rect width="700" height="140" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">Before &amp; After Gutenberg</text>'

    '<rect x="30" y="30" width="300" height="100" rx="6" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="180" y="48" text-anchor="middle" fill="#e74c3c" font-size="10" font-weight="bold">Before Printing (pre-1450)</text>'
    '<text x="180" y="65" text-anchor="middle" fill="#b8a88a" font-size="8">Books copied by hand (years per Bible)</text>'
    '<text x="180" y="80" text-anchor="middle" fill="#b8a88a" font-size="8">One Bible cost as much as a house</text>'
    '<text x="180" y="95" text-anchor="middle" fill="#b8a88a" font-size="8">90%+ of Europeans illiterate</text>'
    '<text x="180" y="110" text-anchor="middle" fill="#b8a88a" font-size="8">A few thousand books in all of Europe</text>'
    '<text x="180" y="125" text-anchor="middle" fill="#b8a88a" font-size="8">Ideas spread at the speed of a pen</text>'

    '<rect x="370" y="30" width="300" height="100" rx="6" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="520" y="48" text-anchor="middle" fill="#2ecc71" font-size="10" font-weight="bold">After Printing (by 1500)</text>'
    '<text x="520" y="65" text-anchor="middle" fill="#b8a88a" font-size="8">180 Bibles in the time of 1 handwritten copy</text>'
    '<text x="520" y="80" text-anchor="middle" fill="#b8a88a" font-size="8">Book prices dropped 80%</text>'
    '<text x="520" y="95" text-anchor="middle" fill="#b8a88a" font-size="8">Literacy began to rise across all classes</text>'
    '<text x="520" y="110" text-anchor="middle" fill="#b8a88a" font-size="8">20 million+ books printed in 50 years</text>'
    '<text x="520" y="125" text-anchor="middle" fill="#b8a88a" font-size="8">Ideas spread in weeks, not decades</text>'
    '</svg>'
    '</div>'

    '<p>The book carried them home. Evelyn looked at her notebook, '
    'at the pen in her hand, and then at the bookshelf across the room.</p>'

    '<p>\u201cEvery one of those books exists because of that machine,\u201d she said.</p>'

    '<p>\u201cEvery one,\u201d Jason agreed. '
    '\u201cAnd every school. And every library. And every newspaper. '
    'One machine, five hundred years ago. Goodnight, Mr. Gutenberg.\u201d</p>'

    '<p>\u201cGoodnight, movable type.\u201d</p>'
)

disc_68 = [
    "Gutenberg\u2019s printing press has been called \u2018the internet of its time.\u2019 In what ways are they similar? In what ways is the internet even more powerful \u2014 or more dangerous?",
    "Before the printing press, the Church and universities controlled most knowledge. What happens to powerful institutions when ordinary people suddenly get access to information?",
    "The printing press spread both brilliant ideas and dangerous misinformation. Is there any way to have the benefits of free information without the risks? Should someone decide what gets printed?"
]

quiz_68 = [
    {
        "q": "What was Gutenberg\u2019s key innovation that made mass printing possible?",
        "options": [
            "Inventing paper",
            "Movable metal type with a complete printing system",
            "Water-based ink that dried faster",
            "Woodblock carving techniques"
        ],
        "correct": 1
    },
    {
        "q": "How many books had been printed in Europe by 1500 \u2014 about 50 years after Gutenberg?",
        "options": [
            "About 5,000",
            "About 100,000",
            "About 20 million",
            "About 1 billion"
        ],
        "correct": 2
    },
    {
        "q": "Why is the Gutenberg Bible also called the 42-line Bible?",
        "options": [
            "It contained 42 books of the Bible",
            "It took 42 years to print",
            "Each page had two columns of 42 lines each",
            "Only 42 copies were made"
        ],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 68:
        lessons[i] = {
            "id": 68,
            "type": "history",
            "topic": "Printing",
            "title": "The Machine That Changed the World",
            "readingTime": "10 min",
            "story": story_68,
            "discussion": disc_68,
            "quiz": quiz_68
        }
        print("Updated lesson 68: The Machine That Changed the World")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
