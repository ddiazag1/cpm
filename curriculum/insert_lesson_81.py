import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_81 = (
    '<h2>The War to End All Wars</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Cheshire_Regiment_trench_Somme_1916.jpg/800px-Cheshire_Regiment_trench_Somme_1916.jpg" '
    'alt="British soldiers of the Cheshire Regiment in a trench during the Battle of the Somme in 1916" loading="lazy">'
    '<p class="image-caption">British soldiers in the trenches of the Somme (1916) \u2014 where over one million men were killed or wounded</p>'
    '</div>'

    '<p>The telescope\u2019s hourglass dial turned, and the brothers found themselves '
    'standing in a muddy ditch. The walls were made of dirt and sandbags, '
    'and the air smelled of smoke and something worse. '
    'A dull rumble shook the ground beneath their feet.</p>'

    '<p>\u201cThis is a trench,\u201d William said quietly. '
    '\u201cSomewhere in France, 1916. Welcome to World War I.\u201d</p>'

    '<h3>The Spark</h3>'

    '<p>\u201cOn <strong>June 28, 1914</strong>, a 19-year-old Bosnian Serb named <strong>Gavrilo Princip</strong> '
    'shot and killed <strong>Archduke Franz Ferdinand</strong> of Austria-Hungary and his wife Sophie '
    'in the city of <strong>Sarajevo</strong>,\u201d William said. '
    '\u201cIt was one bullet that started a war that killed 20 million people.\u201d</p>'

    '<p>\u201cBut one assassination doesn\u2019t start a world war by itself,\u201d Robert said.</p>'

    '<p>\u201cExactly right,\u201d William replied. \u201cEurope was a powder keg waiting for a spark. '
    'For decades, the great powers had been building <strong>alliances</strong> \u2014 '
    'secret promises to fight together if attacked. <strong>Germany, Austria-Hungary, and Italy</strong> '
    'formed the <strong>Triple Alliance</strong>. <strong>France, Russia, and Britain</strong> formed '
    'the <strong>Triple Entente</strong>. When Austria-Hungary declared war on Serbia, '
    'Russia mobilized to help Serbia. Germany declared war on Russia, then on France. '
    'Britain entered when Germany invaded Belgium. Within six weeks, most of Europe was at war.\u201d</p>'

    '<h3>The Trenches</h3>'

    '<p>\u201cEveryone expected a quick war,\u201d William said. \u201cGermany\u2019s <strong>Schlieffen Plan</strong> '
    'called for a lightning strike through Belgium to knock out France in six weeks, '
    'then turn east to face Russia. It almost worked \u2014 German forces came within 30 miles of Paris.\u201d</p>'

    '<p>\u201cBut the French and British stopped them at the <strong>Battle of the Marne</strong> (September 1914). '
    'Then both sides dug in. They dug <strong>trenches</strong> \u2014 vast networks of muddy ditches stretching '
    'from the English Channel to Switzerland, a distance of <strong>400 miles</strong>. '
    'The space between opposing trenches was called <strong>No Man\u2019s Land</strong> \u2014 '
    'a hellscape of barbed wire, craters, and unburied dead.\u201d</p>'

    '<p>\u201cFor the next three and a half years, millions of soldiers lived, fought, and died in these trenches. '
    'Attacks gained yards, not miles, at the cost of thousands of lives. '
    'At the <strong>Battle of the Somme</strong> (1916), the British lost <strong>57,000 men on the first day alone</strong> \u2014 '
    'the deadliest day in British military history. The entire battle lasted five months '
    'and cost over <strong>one million casualties</strong> on both sides, '
    'for a gain of just six miles.\u201d</p>'

    '<h3>New Weapons, New Horrors</h3>'

    '<p>\u201cWorld War I introduced weapons that made killing industrial,\u201d William said. '
    '\u201c<strong>Machine guns</strong> could fire 600 rounds per minute, mowing down waves of soldiers '
    'charging across open ground. <strong>Artillery</strong> rained explosive shells on trenches day and night \u2014 '
    'the constant bombardment drove soldiers mad with a condition called <strong>shell shock</strong>.\u201d</p>'

    '<p>\u201cIn April 1915, Germany unleashed a terrifying new weapon: <strong>poison gas</strong>. '
    'At the <strong>Second Battle of Ypres</strong>, a greenish-yellow cloud of <strong>chlorine gas</strong> '
    'drifted toward Allied trenches. Soldiers choked, their lungs burning. '
    'Soon both sides were using gas \u2014 chlorine, phosgene, and the dreaded <strong>mustard gas</strong>, '
    'which blistered skin and blinded its victims.\u201d</p>'

    '<p>\u201c<strong>Tanks</strong> appeared for the first time at the Somme in 1916 \u2014 '
    'lumbering metal machines that could cross trenches and crush barbed wire. '
    'And <strong>airplanes</strong>, barely a decade old, were used for scouting and then for combat. '
    'Pilots like the <strong>Red Baron</strong> became famous, but the romance of the skies '
    'couldn\u2019t hide the butchery below.\u201d</p>'

    '<h3>Gallipoli and the Wider War</h3>'

    '<p>\u201cThe war spread far beyond France,\u201d William said. '
    '\u201cIn 1915, Britain and France tried to open a new front by attacking the <strong>Ottoman Empire</strong> '
    '(modern Turkey) at <strong>Gallipoli</strong>. It was a disaster. Allied forces \u2014 '
    'including thousands of soldiers from <strong>Australia and New Zealand</strong> (the ANZACs) \u2014 '
    'were pinned on narrow beaches for eight months. Over <strong>250,000 Allied soldiers</strong> '
    'and a similar number of Ottomans became casualties. The Allies withdrew, having gained nothing.\u201d</p>'

    '<p>\u201cFighting raged in Africa, where colonial troops fought over European colonies. '
    'In the Middle East, <strong>T.E. Lawrence</strong> (\u201cLawrence of Arabia\u201d) helped organize '
    'an Arab revolt against the Ottomans. On the Eastern Front, Russia suffered catastrophic losses \u2014 '
    'contributing to the <strong>Russian Revolution of 1917</strong>, which toppled the Tsar '
    'and eventually brought the <strong>Bolsheviks</strong> to power under <strong>Lenin</strong>.\u201d</p>'

    '<h3>America Enters the War</h3>'

    '<p>\u201cThe United States stayed neutral for three years,\u201d William said. '
    '\u201cPresident <strong>Woodrow Wilson</strong> won re-election in 1916 with the slogan '
    '\u201cHe kept us out of war.\u201d But two things changed his mind.\u201d</p>'

    '<p>\u201cFirst, Germany resumed <strong>unrestricted submarine warfare</strong>, '
    'sinking any ship \u2014 including American merchant vessels \u2014 heading for Allied ports. '
    'Second, the <strong>Zimmermann Telegram</strong>: a secret German message to Mexico, '
    'promising to help Mexico reclaim Texas, New Mexico, and Arizona if Mexico joined the war '
    'against the United States. When the telegram was intercepted and published, '
    'Americans were outraged.\u201d</p>'

    '<p>\u201cOn <strong>April 6, 1917</strong>, the United States declared war on Germany. '
    'Over the next 18 months, <strong>2 million American soldiers</strong> arrived in France. '
    'They were fresh, well-supplied, and full of energy \u2014 the exhausted armies of Europe were not. '
    'American forces helped turn the tide in key battles like <strong>Belleau Wood</strong> '
    'and the <strong>Meuse-Argonne Offensive</strong>, the largest battle in American military history.\u201d</p>'

    '<h3>Armistice and Aftermath</h3>'

    '<p>\u201cBy autumn 1918, Germany was collapsing,\u201d William said. \u201cIts allies had surrendered, '
    'its army was retreating, and its people were starving from a British naval blockade. '
    'On <strong>November 11, 1918, at 11:00 a.m.</strong> \u2014 the eleventh hour of the eleventh day '
    'of the eleventh month \u2014 the guns finally fell silent. The <strong>Armistice</strong> had been signed.\u201d</p>'

    '<p>\u201cThe <strong>Treaty of Versailles</strong> (1919) officially ended the war. '
    'It forced Germany to accept full blame, pay <strong>massive reparations</strong>, '
    'give up territory, and reduce its military to almost nothing. '
    'Many historians believe the treaty\u2019s harshness planted the seeds for an even worse war '
    'just 20 years later.\u201d</p>'

    '<p>\u201cThe numbers are almost impossible to comprehend,\u201d William said. '
    '\u201c<strong>20 million dead</strong> \u2014 10 million soldiers and 10 million civilians. '
    '<strong>21 million wounded</strong>. Four empires destroyed: German, Austro-Hungarian, Ottoman, and Russian. '
    'They called it \u201cThe War to End All Wars.\u201d It wasn\u2019t.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="World War I">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">World War I (1914\u20131918)</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">The Spark (1914)</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Archduke Franz Ferdinand killed</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Alliance system triggers world war</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Trench Warfare</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">400 miles of trenches</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Somme: 1M casualties for 6 miles</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">New Weapons</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Machine guns, poison gas, tanks</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Industrial-scale killing</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Armistice (1918)</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">11th hour, 11th day, 11th month</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">20 million dead, 4 empires fallen</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">They called it \u201cThe War to End All Wars\u201d \u2014 but the harsh Treaty of Versailles sowed seeds for another</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">A generation of young men was lost in the mud of No Man\u2019s Land</text>'
    '</svg>'
    '</div>'

    '<p>The telescope brought them home. The room was very quiet. '
    'Robert stared at the floor for a long time.</p>'

    '<p>\u201cTwenty million people,\u201d Robert said. \u201cAnd they called it the war to end all wars. '
    'But it didn\u2019t end them, did it?\u201d</p>'

    '<p>\u201cNo,\u201d William said. \u201cBecause the peace was built on anger, not understanding. '
    'When you punish people instead of helping them heal, '
    'you just plant the seeds for the next war. '
    'Goodnight, lost generation.\u201d</p>'

    '<p>\u201cGoodnight, eleventh hour.\u201d</p>'
)

disc_81 = [
    "The alliance system meant that one assassination pulled dozens of nations into war. What are the dangers of making promises to fight without knowing what the future holds?",
    "Soldiers on both sides suffered terribly in the trenches and often had more in common with each other than with the leaders who sent them to war. Why do ordinary people end up paying the price for decisions made by those in power?",
    "The Treaty of Versailles punished Germany so harshly that many historians believe it helped cause World War II. What is the difference between justice and revenge, and why does it matter how you treat a defeated enemy?"
]

quiz_81 = [
    {
        "q": "What event is considered the immediate trigger for World War I?",
        "options": [
            "The sinking of the Lusitania",
            "Germany\u2019s invasion of Belgium",
            "The assassination of Archduke Franz Ferdinand",
            "The Zimmermann Telegram"
        ],
        "correct": 2
    },
    {
        "q": "What was No Man\u2019s Land?",
        "options": [
            "A neutral country that refused to join the war",
            "The dangerous area between opposing trenches",
            "Germany\u2019s code name for its submarine campaign",
            "A peace conference held in Switzerland"
        ],
        "correct": 1
    },
    {
        "q": "When did the Armistice end World War I?",
        "options": [
            "July 4, 1917",
            "January 1, 1919",
            "November 11, 1918",
            "June 28, 1914"
        ],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 81:
        lessons[i] = {
            "id": 81,
            "type": "history",
            "topic": "WWI",
            "title": "The War to End All Wars",
            "readingTime": "10 min",
            "story": story_81,
            "discussion": disc_81,
            "quiz": quiz_81
        }
        print("Updated lesson 81: The War to End All Wars")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
