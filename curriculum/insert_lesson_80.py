import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_80 = (
    '<h2>The Scramble for Africa</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Punch_Rhodes_Colossus.png/800px-Punch_Rhodes_Colossus.png" '
    'alt="Punch magazine cartoon showing Cecil Rhodes as a colossus striding from Cape Town to Cairo" loading="lazy">'
    '<p class="image-caption">The Rhodes Colossus \u2014 an 1892 Punch cartoon showing Cecil Rhodes\u2019 ambition to build a telegraph line from Cape Town to Cairo</p>'
    '</div>'

    '<p>Evelyn was looking at a map of Africa. Every country was drawn in a different color, '
    'and the borders were strangely straight \u2014 long lines cutting across rivers and mountains '
    'as if drawn with a ruler.</p>'

    '<p>\u201cJason, why are Africa\u2019s borders so straight?\u201d she asked.</p>'

    '<p>Jason opened The Living World and turned the brass clasp. '
    '\u201cBecause they were drawn by people who had never been there,\u201d he said. '
    'The green light carried them to a grand hall in Berlin.</p>'

    '<h3>The Berlin Conference</h3>'

    '<p>\u201cIt\u2019s November 1884,\u201d Jason said. \u201cWe\u2019re in the <strong>Berlin Conference</strong>, '
    'organized by German Chancellor <strong>Otto von Bismarck</strong>. Representatives from '
    '<strong>14 European nations</strong> are sitting around this table, drawing lines on a map of Africa. '
    'They are carving up an entire continent \u2014 and not a single African has been invited.\u201d</p>'

    '<p>\u201cBefore this conference, Europeans controlled only about <strong>10 percent</strong> of Africa \u2014 '
    'mostly coastal trading posts,\u201d Jason continued. \u201cBut new technologies changed everything. '
    '<strong>Quinine</strong> protected them from malaria. <strong>Steamships</strong> could navigate rivers. '
    'And <strong>machine guns</strong> \u2014 especially the Maxim gun \u2014 gave tiny European forces '
    'devastating firepower against African armies armed with spears and older rifles.\u201d</p>'

    '<p>\u201cThe conference set rules for how European nations could claim African territory: '
    'you had to notify other European powers and show you could \u201ceffectively occupy\u201d the land. '
    'Within <strong>30 years</strong>, European nations had seized <strong>90 percent of Africa</strong>. '
    'Only <strong>Ethiopia</strong> and <strong>Liberia</strong> remained independent.\u201d</p>'

    '<h3>Who Took What?</h3>'

    '<p>\u201c<strong>Britain</strong> claimed the largest share,\u201d Jason said. '
    '\u201cEgypt, Sudan, Kenya, Uganda, Nigeria, the Gold Coast (Ghana), Rhodesia (Zimbabwe and Zambia), '
    'and South Africa. The British dream was a continuous empire from \u201cCape to Cairo.\u201d\u201d</p>'

    '<p>\u201c<strong>France</strong> took most of West and North Africa \u2014 '
    'Algeria, Senegal, Mali, Ivory Coast, Madagascar, and more. French West Africa alone '
    'was larger than the entire United States.\u201d</p>'

    '<p>\u201c<strong>Germany</strong> seized Tanganyika (Tanzania), Namibia, Cameroon, and Togo. '
    '<strong>Portugal</strong> held Angola and Mozambique. <strong>Italy</strong> took Libya, Eritrea, '
    'and part of Somalia. <strong>Spain</strong> controlled small territories in Morocco and Western Sahara.\u201d</p>'

    '<p>\u201cThe borders they drew cut through ethnic groups, languages, and kingdoms '
    'that had existed for centuries. People who were enemies were forced into the same colony. '
    'People who were family were split between different European powers. '
    'Those arbitrary lines remain Africa\u2019s borders today.\u201d</p>'

    '<h3>King Leopold\u2019s Congo</h3>'

    '<p>\u201cThe worst horror was in the <strong>Congo</strong>,\u201d Jason said, his voice serious. '
    '\u201cKing <strong>Leopold II of Belgium</strong> didn\u2019t claim the Congo for Belgium \u2014 '
    'he claimed it as his <strong>personal property</strong>. He called it the <strong>Congo Free State</strong>, '
    'but it was anything but free.\u201d</p>'

    '<p>\u201cLeopold forced the Congolese people to harvest <strong>rubber</strong> from wild vines. '
    'Those who didn\u2019t meet their quotas had their <strong>hands cut off</strong> \u2014 '
    'men, women, and even children. Villages that resisted were burned. '
    'Hostages were taken to force compliance. '
    'An estimated <strong>10 million Congolese people died</strong> under Leopold\u2019s rule \u2014 '
    'roughly half the population.\u201d</p>'

    '<p>Evelyn looked horrified. \u201cHow could one person do that?\u201d</p>'

    '<p>\u201cBecause the world let him,\u201d Jason said. \u201cFor decades, Leopold hid the truth '
    'behind a facade of civilization and charity. It took brave people \u2014 '
    'journalists like <strong>E.D. Morel</strong> and missionaries who smuggled out photographs \u2014 '
    'to expose the atrocities. The international outcry finally forced Belgium '
    'to take the Congo away from Leopold in 1908. But the damage was done.\u201d</p>'

    '<h3>Exploitation Everywhere</h3>'

    '<p>\u201cThe Congo was the most extreme case, but exploitation happened everywhere,\u201d Jason said. '
    '\u201cEuropean colonizers extracted Africa\u2019s <strong>gold, diamonds, copper, rubber, ivory, and palm oil</strong> '
    'and shipped the wealth back to Europe. Africans were forced to work in mines and on plantations '
    'for little or no pay. Colonial governments imposed <strong>hut taxes</strong> and <strong>head taxes</strong> '
    'that forced Africans into the cash economy, working for European companies '
    'just to pay taxes to European governments.\u201d</p>'

    '<p>\u201cEducation was limited to what colonizers needed \u2014 clerks, translators, and low-level workers. '
    'African languages, religions, and traditions were suppressed. '
    'Colonial governments used a strategy called <strong>divide and rule</strong> \u2014 '
    'they elevated one ethnic group over others, creating rivalries that hadn\u2019t existed before. '
    'These manufactured divisions would haunt Africa long after independence.\u201d</p>'

    '<h3>Resistance</h3>'

    '<p>\u201cBut Africans never stopped fighting back,\u201d Jason said firmly. '
    '\u201c<strong>Emperor Menelik II of Ethiopia</strong> defeated an Italian invasion force '
    'at the <strong>Battle of Adwa</strong> in 1896 \u2014 one of the few times an African army '
    'decisively defeated a European colonial power. Ethiopia remained independent, '
    'and Adwa became a symbol of African resistance worldwide.\u201d</p>'

    '<p>\u201cThe <strong>Zulu</strong> kingdom in southern Africa fought fiercely against the British. '
    'At the <strong>Battle of Isandlwana</strong> (1879), 20,000 Zulu warriors overwhelmed '
    'a British force of 1,800, killing over 1,300. The <strong>Herero and Nama</strong> peoples '
    'in German Namibia revolted in 1904, leading Germany to commit what many historians call '
    'the <strong>first genocide of the 20th century</strong> \u2014 killing an estimated 80 percent '
    'of the Herero population.\u201d</p>'

    '<p>\u201cAcross the continent, resistance took many forms: armed rebellion, work stoppages, '
    'cultural preservation, and the seeds of nationalist movements '
    'that would eventually win independence in the 1950s and 1960s.\u201d</p>'

    '<h3>The Lasting Impact</h3>'

    '<p>\u201cWhen African nations finally gained independence, they inherited borders that made no sense, '
    'economies designed to export raw materials rather than serve their own people, '
    'and ethnic divisions that colonizers had deliberately inflamed,\u201d Jason said. '
    '\u201cMany of Africa\u2019s modern challenges \u2014 civil wars, poverty, political instability \u2014 '
    'trace directly back to the Scramble for Africa.\u201d</p>'

    '<p>\u201cUnderstanding this history is not about blame,\u201d Jason said. '
    '\u201cIt\u2019s about understanding why the world looks the way it does today.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="Scramble for Africa">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The Scramble for Africa (1884\u20131914)</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Berlin Conference (1884)</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">14 European nations divide Africa</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">No Africans invited</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Leopold\u2019s Congo</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">10 million Congolese dead</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Hands cut off for missed quotas</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Resistance</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Ethiopia defeats Italy at Adwa</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Zulu, Herero uprisings</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">By 1914</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">90% of Africa colonized</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Only Ethiopia + Liberia free</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">Europeans drew borders with rulers \u2014 cutting through nations that had existed for centuries</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">Africa\u2019s modern challenges trace directly to the era of colonial exploitation</text>'
    '</svg>'
    '</div>'

    '<p>The book brought them home. Evelyn looked at the map of Africa again, '
    'at all those impossibly straight lines.</p>'

    '<p>\u201cThose borders are still there,\u201d she said. \u201cPeople are still living '
    'inside lines that strangers drew.\u201d</p>'

    '<p>\u201cThat\u2019s why history matters,\u201d Jason said. '
    '\u201cYou can\u2019t fix what you don\u2019t understand. '
    'Goodnight, stolen continent.\u201d</p>'

    '<p>\u201cGoodnight, people who fought back.\u201d</p>'
)

disc_80 = [
    "At the Berlin Conference, 14 European nations divided Africa without inviting a single African representative. What does it mean when decisions about your life are made by people who have never met you?",
    "Journalists and missionaries risked their lives to expose the atrocities in Leopold\u2019s Congo. Why is it important for people to speak up when they see injustice, even when it is dangerous?",
    "Many of Africa\u2019s modern borders were drawn by European colonizers who ignored existing ethnic groups and kingdoms. How can borders that were created unfairly still cause problems more than 100 years later?"
]

quiz_80 = [
    {
        "q": "What was the Berlin Conference of 1884?",
        "options": [
            "A peace treaty ending a European war",
            "A meeting where European nations set rules for claiming African territory",
            "A gathering of African leaders to resist colonialism",
            "A trade agreement between Africa and Europe"
        ],
        "correct": 1
    },
    {
        "q": "Which African nation defeated an Italian invasion force at the Battle of Adwa in 1896?",
        "options": ["Nigeria", "South Africa", "Ethiopia", "Egypt"],
        "correct": 2
    },
    {
        "q": "What happened in King Leopold II\u2019s Congo Free State?",
        "options": [
            "Congolese people were given self-government",
            "An estimated 10 million people died under forced labor and brutality",
            "Belgium built schools and hospitals across the region",
            "The Congo became the wealthiest nation in Africa"
        ],
        "correct": 1
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 80:
        lessons[i] = {
            "id": 80,
            "type": "history",
            "topic": "Colonialism",
            "title": "The Scramble for Africa",
            "readingTime": "10 min",
            "story": story_80,
            "discussion": disc_80,
            "quiz": quiz_80
        }
        print("Updated lesson 80: The Scramble for Africa")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
