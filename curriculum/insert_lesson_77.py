import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_77 = (
    '<h2>Breaking the Chains</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Harriet_Tubman_by_Squyer%2C_NPG%2C_c1885.jpg/800px-Harriet_Tubman_by_Squyer%2C_NPG%2C_c1885.jpg" '
    'alt="Photograph of Harriet Tubman, conductor of the Underground Railroad" loading="lazy">'
    '<p class="image-caption">Harriet Tubman \u2014 born into slavery, she escaped and then risked her life to free dozens more through the Underground Railroad</p>'
    '</div>'

    '<p>The telescope\u2019s hourglass dial began to glow, and the brothers found themselves '
    'standing in a dark forest. A woman in a worn shawl crouched behind a fallen tree, '
    'listening. In the distance, dogs barked.</p>'

    '<p>\u201cDon\u2019t make a sound,\u201d William whispered. '
    '\u201cWe\u2019re watching the <strong>Underground Railroad</strong>. '
    'This woman is leading escaped enslaved people north to freedom. '
    'If they\u2019re caught, they\u2019ll be whipped, sold, or killed.\u201d</p>'

    '<p>Robert held his breath. The woman pointed to the North Star and motioned the group forward.</p>'

    '<h3>The Transatlantic Slave Trade</h3>'

    '<p>\u201cTo understand this story, we have to go back centuries,\u201d William said. '
    '\u201cBeginning in the 1500s, European nations built the <strong>transatlantic slave trade</strong> \u2014 '
    'one of the greatest crimes in human history. Over nearly 400 years, '
    'an estimated <strong>12.5 million Africans</strong> were kidnapped from their homes, '
    'chained together, and forced onto ships bound for the Americas.\u201d</p>'

    '<p>\u201cThe voyage across the Atlantic was called the <strong>Middle Passage</strong>. '
    'Enslaved people were packed into ships so tightly they could barely move. '
    'They were chained below deck for weeks in suffocating heat, filth, and darkness. '
    'About <strong>2 million people</strong> died during the crossing \u2014 '
    'from disease, starvation, or despair. Those who resisted were beaten or thrown overboard.\u201d</p>'

    '<p>Robert felt sick. \u201cWhy did people do this?\u201d</p>'

    '<p>\u201cMoney,\u201d William said. \u201cSlaves produced tobacco, sugar, rice, and cotton \u2014 '
    'crops that made plantation owners and trading companies enormously wealthy. '
    'The entire economy of the American South was built on enslaved labor. '
    'By 1860, there were nearly <strong>4 million</strong> enslaved people in the United States.\u201d</p>'

    '<h3>Life in Slavery</h3>'

    '<p>\u201cEnslaved people were considered <strong>property</strong>, not human beings,\u201d '
    'William continued. \u201cThey could be bought, sold, and separated from their families '
    'at any moment. They worked from sunrise to sunset \u2014 and often longer \u2014 '
    'in fields, houses, and workshops. They had no legal rights. '
    'It was illegal to teach an enslaved person to read or write in most Southern states, '
    'because slave owners knew that education was power.\u201d</p>'

    '<p>\u201cBut enslaved people were never passive victims. '
    'They resisted in every way they could \u2014 slowing work, breaking tools, '
    'preserving their languages, music, and stories, running away, '
    'and sometimes rising up in rebellion. '
    '<strong>Nat Turner</strong> led a revolt in Virginia in 1831. '
    'Enslaved people built communities, families, and a culture of resilience '
    'that endures to this day.\u201d</p>'

    '<h3>The Abolitionists</h3>'

    '<p>\u201cPeople who fought to end slavery were called <strong>abolitionists</strong>,\u201d '
    'William said. \u201cIn Britain, a man named <strong>William Wilberforce</strong> '
    'spent nearly 20 years campaigning in Parliament to end the slave trade. '
    'Year after year, his bills were defeated. But he never gave up. '
    'In 1807, Britain finally abolished the slave trade, '
    'and in 1833, slavery itself was banned throughout the British Empire.\u201d</p>'

    '<p>\u201cIn America, the fight was even harder because slavery was woven into the economy. '
    '<strong>Frederick Douglass</strong>, a man who escaped slavery, '
    'became one of the most powerful speakers and writers in American history. '
    'His autobiography, published in 1845, shocked readers with its firsthand account '
    'of slavery\u2019s cruelty. He traveled the country giving speeches that moved thousands. '
    '\u201cWhat to the Slave is the Fourth of July?\u201d he asked in a famous 1852 address \u2014 '
    'pointing out that America\u2019s promise of liberty meant nothing '
    'to the 4 million people still in chains.\u201d</p>'

    '<h3>Harriet Tubman and the Underground Railroad</h3>'

    '<p>\u201cThe <strong>Underground Railroad</strong> wasn\u2019t a real railroad,\u201d '
    'William explained. \u201cIt was a secret network of safe houses, hidden routes, '
    'and brave people \u2014 called <strong>conductors</strong> \u2014 who helped enslaved people '
    'escape to free states in the North or to Canada.\u201d</p>'

    '<p>\u201cThe most famous conductor was <strong>Harriet Tubman</strong>. '
    'Born into slavery in Maryland around 1822, she escaped in 1849 '
    'by following the North Star through swamps and forests. '
    'But instead of staying safe in the North, she went back. '
    'Again and again. Over about 13 trips, she personally led roughly <strong>70 people</strong> '
    'to freedom, including her own parents and siblings. '
    'She carried a pistol \u2014 not just for protection, but to convince anyone '
    'who wanted to turn back that they had to keep going. '
    'Slave owners offered a <strong>$40,000 reward</strong> for her capture \u2014 '
    'an enormous fortune at the time. She was never caught.\u201d</p>'

    '<p>\u201cShe said: <strong>\u201cI never ran my train off the track, '
    'and I never lost a passenger.\u201d</strong>\u201d</p>'

    '<p>Robert stared at the woman in the forest. \u201cIs that her?\u201d</p>'

    '<p>\u201cSomeone like her,\u201d William said. \u201cThere were thousands of conductors. '
    'Quakers, free Black communities, ordinary families who hid people in their basements '
    'and barns. Every one of them risked prison or worse.\u201d</p>'

    '<h3>Emancipation</h3>'

    '<p>\u201cThe final blow to slavery in America came during the <strong>Civil War</strong> (1861\u20131865),\u201d '
    'William said. \u201cOn January 1, 1863, President <strong>Abraham Lincoln</strong> issued the '
    '<strong>Emancipation Proclamation</strong>, declaring that all enslaved people '
    'in the rebelling Southern states were free. It didn\u2019t immediately free everyone \u2014 '
    'the South was still fighting \u2014 but it transformed the war '
    'into a fight for human freedom.\u201d</p>'

    '<p>\u201cNearly <strong>200,000 Black soldiers</strong> served in the Union Army and Navy, '
    'fighting for their own liberty. In December 1865, after the war ended, '
    'the <strong>13th Amendment</strong> to the Constitution was ratified. '
    'It said, in plain words: <strong>\u201cNeither slavery nor involuntary servitude '
    '\u2026 shall exist within the United States.\u201d</strong> '
    'After 250 years, slavery in America was finally, legally over.\u201d</p>'

    '<p>\u201cBut freedom on paper and freedom in life are not the same thing,\u201d '
    'William added. \u201cThe fight for true equality \u2014 '
    'against segregation, discrimination, and injustice \u2014 '
    'would continue for another century and beyond. '
    'That story is still being written today.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="Abolition of Slavery">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">Breaking the Chains \u2014 The Fight to End Slavery</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Slave Trade</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">12.5 million Africans kidnapped</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">2 million died on Middle Passage</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Abolitionists</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Wilberforce, Douglass, Tubman</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Britain banned slavery 1833</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Underground Railroad</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Tubman: ~70 people freed</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">\u201cNever lost a passenger\u201d</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">13th Amendment (1865)</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Slavery abolished in the U.S.</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">200,000 Black soldiers served</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">Every person who hid a fugitive, spoke against slavery, or ran north was part of this story</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">The fight for true equality continues \u2014 freedom on paper must become freedom in life</text>'
    '</svg>'
    '</div>'

    '<p>The telescope brought them home. Robert wiped his eyes.</p>'

    '<p>\u201cHarriet Tubman could have stayed safe,\u201d he said. '
    '\u201cShe was already free. But she went back.\u201d</p>'

    '<p>\u201cThirteen times,\u201d William said. \u201cSome people can\u2019t rest '
    'while others are still in chains. That\u2019s what courage looks like \u2014 '
    'not the absence of fear, but the refusal to look away. '
    'Goodnight, freedom seekers.\u201d</p>'

    '<p>\u201cGoodnight, North Star.\u201d</p>'
)

disc_77 = [
    'Harriet Tubman escaped slavery and was safe in the North, but she risked her life to go back and free others. What do you think gave her the courage to keep going back, even knowing she could be caught?',
    'Frederick Douglass asked \u201cWhat to the Slave is the Fourth of July?\u201d \u2014 pointing out that freedom and equality meant nothing to people still enslaved. Why is it important to question whether a country\u2019s ideals match its reality?',
    'The 13th Amendment ended slavery legally, but William said \u201cfreedom on paper and freedom in life are not the same thing.\u201d What do you think that means, and can you think of examples from today?'
]

quiz_77 = [
    {
        "q": "What was the Middle Passage?",
        "options": [
            "A secret tunnel on the Underground Railroad",
            "The voyage enslaved Africans were forced to take across the Atlantic",
            "A law that ended the slave trade in Britain",
            "Frederick Douglass\u2019s escape route to the North"
        ],
        "correct": 1
    },
    {
        "q": "How many people did Harriet Tubman personally lead to freedom on the Underground Railroad?",
        "options": ["About 10", "About 70", "About 300", "About 1,000"],
        "correct": 1
    },
    {
        "q": "Which amendment to the U.S. Constitution abolished slavery?",
        "options": [
            "The 1st Amendment",
            "The 5th Amendment",
            "The 13th Amendment",
            "The 19th Amendment"
        ],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 77:
        lessons[i] = {
            "id": 77,
            "type": "history",
            "topic": "Abolition",
            "title": "Breaking the Chains",
            "readingTime": "10 min",
            "story": story_77,
            "discussion": disc_77,
            "quiz": quiz_77
        }
        print("Updated lesson 77: Breaking the Chains")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
