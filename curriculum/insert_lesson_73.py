import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_73 = (
    '<h2>The Shot Heard Round the World</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Declaration_of_Independence_%281819%29%2C_by_John_Trumbull.jpg/800px-Declaration_of_Independence_%281819%29%2C_by_John_Trumbull.jpg" '
    'alt="John Trumbull painting of the signing of the Declaration of Independence" loading="lazy">'
    '<p class="image-caption">The signing of the Declaration of Independence \u2014 July 4, 1776</p>'
    '</div>'

    '<p>The telescope\u2019s hourglass dial turned, and the brothers appeared on a village green '
    'in the gray light before dawn. Farmers in homespun clothes clutched muskets '
    'and stood in rough lines facing a road.</p>'

    '<p>\u201cThis is <strong>Lexington, Massachusetts</strong>,\u201d William said quietly. '
    '\u201cApril 19, 1775. In a few minutes, the American Revolution begins.\u201d</p>'

    '<h3>Why a Revolution?</h3>'

    '<p>\u201cAfter the French and Indian War (1754\u20131763), Britain was deep in debt,\u201d William said. '
    '\u201cTo raise money, Parliament imposed new taxes on the 13 colonies \u2014 '
    'the <strong>Stamp Act</strong>, the <strong>Townshend Acts</strong>, and the <strong>Tea Act</strong>. '
    'The colonists were furious. They had no representatives in the British Parliament, '
    'so they had no voice in the taxes they were being forced to pay. '
    'Their rallying cry became: <strong>\u201cNo taxation without representation!\u201d</strong>\u201d</p>'

    '<p>\u201cTensions exploded in 1770 at the <strong>Boston Massacre</strong>, '
    'when British soldiers fired into a crowd, killing five colonists. '
    'In 1773, colonists dressed as Mohawk Indians dumped 342 chests of tea '
    'into Boston Harbor \u2014 the <strong>Boston Tea Party</strong>. Britain responded with harsh laws '
    'the colonists called the <strong>Intolerable Acts</strong>, which shut down Boston\u2019s port '
    'and placed Massachusetts under military control.\u201d</p>'

    '<h3>Lexington and Concord</h3>'

    '<p>\u201cOn April 18, 1775, British soldiers marched from Boston to seize colonial weapons stored in Concord,\u201d '
    'William said. \u201c<strong>Paul Revere</strong> and <strong>William Dawes</strong> rode through the night '
    'to warn the colonists: \u2018The regulars are coming!\u2019\u201d</p>'

    '<p>\u201cAt dawn on the Lexington green, about 70 colonial militia \u2014 called <strong>minutemen</strong> '
    'because they could be ready to fight in a minute \u2014 faced 700 British soldiers. '
    'Someone fired a shot \u2014 no one knows who. In the brief battle that followed, '
    '8 minutemen were killed. The British marched on to Concord.\u201d</p>'

    '<p>\u201cBut on the way back to Boston, hundreds of colonial militia fired on the British from behind '
    'stone walls, trees, and fences. By the end of the day, 73 British soldiers were dead '
    'and 174 were wounded. The \u201cshot heard round the world\u201d had been fired, '
    'and the American Revolution had begun.\u201d</p>'

    '<h3>The Declaration of Independence</h3>'

    '<p>\u201cIn June 1776, the Continental Congress asked <strong>Thomas Jefferson</strong> '
    'to write a document explaining why the colonies were declaring independence,\u201d William said. '
    '\u201cJefferson was just 33 years old. In 17 days, he wrote one of the most important documents '
    'in human history: the <strong>Declaration of Independence</strong>.\u201d</p>'

    '<p>\u201cIts most famous words: <strong>\u201cWe hold these truths to be self-evident, '
    'that all men are created equal, that they are endowed by their Creator '
    'with certain unalienable Rights, that among these are Life, Liberty, '
    'and the pursuit of Happiness.\u201d</strong>\u201d</p>'

    '<p>\u201cOn <strong>July 4, 1776</strong>, the Continental Congress adopted the Declaration. '
    'The 13 colonies were now the United States of America \u2014 at least on paper. '
    'They still had to win the war.\u201d</p>'

    '<h3>The War</h3>'

    '<p>\u201cThe odds were terrible,\u201d William said. \u201cBritain had the most powerful military in the world \u2014 '
    'a professional army, the world\u2019s largest navy, and vast resources. '
    'The Continental Army under <strong>George Washington</strong> was a ragged collection '
    'of farmers and merchants with little training, few supplies, and no navy.\u201d</p>'

    '<p>\u201cWashington\u2019s genius was <em>survival</em>. He didn\u2019t need to destroy the British army \u2014 '
    'he just needed to keep his army alive long enough to exhaust Britain\u2019s will to fight. '
    'The brutal winter at <strong>Valley Forge</strong> (1777\u20131778) nearly destroyed the army \u2014 '
    '2,000 soldiers died of disease and cold \u2014 but those who survived emerged tougher and better trained.\u201d</p>'

    '<p>\u201cThe turning point was the <strong>Battle of Saratoga</strong> (1777), '
    'where a major British army surrendered. This victory convinced <strong>France</strong> '
    'to enter the war on America\u2019s side. French money, soldiers, and especially their navy '
    'changed everything.\u201d</p>'

    '<p>\u201cIn 1781, Washington and the French trapped the British army at <strong>Yorktown, Virginia</strong>. '
    'General <strong>Cornwallis</strong> surrendered 8,000 soldiers. '
    'The war was effectively over. In 1783, Britain recognized American independence '
    'in the <strong>Treaty of Paris</strong>.\u201d</p>'

    '<h3>A New Kind of Government</h3>'

    '<p>\u201cThe Americans didn\u2019t just win a war \u2014 they created a new kind of government,\u201d William said. '
    '\u201cThe <strong>Constitution</strong>, written in 1787, established a republic with separation of powers \u2014 '
    'a <strong>legislative</strong> branch (Congress) to make laws, an <strong>executive</strong> branch (the President) to enforce them, '
    'and a <strong>judicial</strong> branch (the courts) to interpret them. '
    'The <strong>Bill of Rights</strong> guaranteed freedoms like speech, religion, and the press.\u201d</p>'

    '<p>\u201cGeorge Washington became the first president. When his term ended, '
    'he voluntarily gave up power \u2014 something almost unheard of in history. '
    'King George III of England reportedly said that if Washington really did that, '
    'he would be \u201cthe greatest man in the world.\u201d\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="American Revolution">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The American Revolution (1775\u20131783)</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Causes</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">No taxation w/o representation</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Boston Tea Party, Intolerable Acts</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Key Moments</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Lexington (1775), July 4 (1776)</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Saratoga, Valley Forge, Yorktown</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">The Idea</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">\u201cAll men are created equal\u201d</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Government by the people</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Legacy</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Constitution + Bill of Rights</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Inspired revolutions worldwide</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">Washington voluntarily gave up power \u2014 King George called him \u201cthe greatest man in the world\u201d</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">The Declaration\u2019s promise of equality would take centuries \u2014 and is still being fulfilled</text>'
    '</svg>'
    '</div>'

    '<p>The telescope brought them home. Robert picked up a penny '
    'and looked at George Washington\u2019s face.</p>'

    '<p>\u201cHe could have been king,\u201d Robert said. \u201cBut he walked away.\u201d</p>'

    '<p>\u201cThat\u2019s what made the revolution real,\u201d William said. '
    '\u201cNot winning the war \u2014 giving up the power afterward. '
    'Goodnight, revolutionaries.\u201d</p>'

    '<p>\u201cGoodnight, shot heard round the world.\u201d</p>'
)

disc_73 = [
    "The Declaration says \u2018all men are created equal,\u2019 but many of its signers owned slaves. How should we think about leaders who wrote ideals they didn\u2019t fully live up to?",
    "Washington voluntarily gave up power after two terms as president. Why was this so important for the future of democracy?",
    "The American Revolution inspired revolutions around the world. Do you think the idea that \u2018people should govern themselves\u2019 is a universal truth, or is it a particularly American idea?"
]

quiz_73 = [
    {
        "q": "What was the colonists\u2019 main complaint against British taxes?",
        "options": [
            "The taxes were too high",
            "No taxation without representation",
            "They wanted to trade with France instead",
            "The taxes were unfair to farmers"
        ],
        "correct": 1
    },
    {
        "q": "Who wrote the Declaration of Independence?",
        "options": ["George Washington", "Benjamin Franklin", "Thomas Jefferson", "John Adams"],
        "correct": 2
    },
    {
        "q": "Which battle convinced France to join the American side?",
        "options": ["Lexington", "Yorktown", "Valley Forge", "Saratoga"],
        "correct": 3
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 73:
        lessons[i] = {
            "id": 73,
            "type": "history",
            "topic": "Revolution",
            "title": "The Shot Heard Round the World",
            "readingTime": "10 min",
            "story": story_73,
            "discussion": disc_73,
            "quiz": quiz_73
        }
        print("Updated lesson 73: The Shot Heard Round the World")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
