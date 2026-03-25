import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_84 = (
    '<h2>The World at War \u2014 Part 2</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/USS_Bunker_Hill_hit_by_two_Kamikazes.jpg/800px-USS_Bunker_Hill_hit_by_two_Kamikazes.jpg" '
    'alt="USS Bunker Hill burning after being struck by two kamikaze planes off Okinawa in 1945" loading="lazy">'
    '<p class="image-caption">The USS Bunker Hill burns after kamikaze strikes near Okinawa, 1945 \u2014 the Pacific war was brutal and costly</p>'
    '</div>'

    '<p>Evelyn was looking at a globe, tracing her finger across the Pacific Ocean. '
    '\u201cJason, the last story ended when Germany surrendered. But the war wasn\u2019t over yet, was it?\u201d</p>'

    '<p>Jason opened The Living World and turned the brass clasp. '
    '\u201cNo,\u201d he said. \u201cAcross the world\u2019s biggest ocean, another terrible war was still raging.\u201d</p>'

    '<p>The green light carried them to a quiet harbor at dawn. Battleships sat in neat rows '
    'on calm water. Palm trees swayed in the warm breeze. '
    'Everything was peaceful \u2014 for the next few minutes.</p>'

    '<h3>Pearl Harbor</h3>'

    '<p>\u201cThis is <strong>Pearl Harbor, Hawaii</strong>,\u201d Jason said. '
    '\u201cIt\u2019s the morning of <strong>December 7, 1941</strong>. '
    'For two years, war had been raging in Europe and Asia, but the United States stayed out of it. '
    'Many Americans believed the oceans would protect them. They were wrong.\u201d</p>'

    '<p>\u201cAt 7:48 in the morning, <strong>353 Japanese warplanes</strong> roared over these mountains '
    'and attacked the American naval base without warning. In less than two hours, '
    'they sank or damaged <strong>21 ships</strong>, destroyed <strong>188 aircraft</strong>, '
    'and killed <strong>2,403 Americans</strong>. The battleship USS Arizona exploded and sank, '
    'taking 1,177 sailors with it.\u201d</p>'

    '<p>\u201cThe next day, President <strong>Franklin Roosevelt</strong> called December 7 '
    '\u201ca date which will live in infamy.\u201d Congress declared war on Japan. '
    'Three days later, Germany and Italy declared war on the United States. '
    'America was now fighting in both Europe and the Pacific.\u201d</p>'

    '<h3>Japan\u2019s Empire</h3>'

    '<p>\u201cWhy did Japan attack?\u201d Evelyn asked.</p>'

    '<p>\u201cJapan had been building an empire,\u201d Jason said. \u201cSince the 1930s, '
    'Japan\u2019s military government had invaded <strong>China</strong>, committing terrible atrocities, '
    'and then pushed into Southeast Asia to seize oil, rubber, and other resources. '
    'The United States cut off Japan\u2019s oil supply to try to stop the expansion. '
    'Japan\u2019s leaders decided to destroy the American fleet at Pearl Harbor '
    'so the U.S. couldn\u2019t interfere with their plans.\u201d</p>'

    '<p>\u201cIn the months after Pearl Harbor, Japan conquered a vast empire \u2014 '
    'the <strong>Philippines</strong>, <strong>Burma</strong>, <strong>Malaya</strong>, '
    'the <strong>Dutch East Indies</strong>, and dozens of Pacific islands. '
    'Japanese forces treated prisoners and conquered peoples with extreme cruelty. '
    'The <strong>Bataan Death March</strong> forced 75,000 American and Filipino prisoners '
    'to walk 65 miles in brutal heat \u2014 thousands died along the way.\u201d</p>'

    '<h3>Turning the Tide: Midway</h3>'

    '<p>\u201cThe turning point came in June 1942 at the <strong>Battle of Midway</strong>,\u201d '
    'Jason said. \u201cAmerican codebreakers had cracked Japan\u2019s secret messages '
    'and knew exactly where the Japanese fleet was heading. '
    'In a single day of intense fighting, American dive bombers sank '
    '<strong>four Japanese aircraft carriers</strong> \u2014 the same carriers that had attacked Pearl Harbor. '
    'Japan lost its best ships and its most experienced pilots. '
    'After Midway, Japan was on the defensive.\u201d</p>'

    '<h3>Island Hopping</h3>'

    '<p>\u201cThe Pacific Ocean is enormous,\u201d Jason said. \u201cJapan controlled thousands of islands, '
    'and each one was a fortress. American military leaders developed a strategy called '
    '<strong>island hopping</strong> \u2014 instead of attacking every island, '
    'they captured key islands and skipped the rest, moving closer and closer to Japan.\u201d</p>'

    '<p>\u201cEvery island was a desperate battle. At <strong>Guadalcanal</strong>, Marines fought for six months '
    'in steaming jungles. At <strong>Iwo Jima</strong> in February 1945, '
    '6,800 Marines were killed taking a tiny volcanic island defended by 21,000 Japanese soldiers '
    'hiding in tunnels and caves. The famous photograph of Marines raising the American flag '
    'on Mount Suribachi became one of the most recognized images in history.\u201d</p>'

    '<p>\u201cAt <strong>Okinawa</strong>, the last major battle before Japan itself, '
    'more than 12,000 Americans and over 100,000 Japanese soldiers died. '
    'Japanese pilots called <strong>kamikazes</strong> deliberately crashed their planes '
    'into American ships \u2014 a sign of how fiercely Japan would fight to defend its homeland.\u201d</p>'

    '<h3>The Atomic Bomb</h3>'

    '<p>Jason\u2019s voice became very serious. \u201cAmerican leaders faced an awful decision. '
    'Invading Japan could cost hundreds of thousands of lives on both sides. '
    'But the United States had secretly developed a new weapon \u2014 '
    'the <strong>atomic bomb</strong>, the most destructive weapon ever created.\u201d</p>'

    '<p>\u201cOn <strong>August 6, 1945</strong>, an American plane dropped an atomic bomb on the city of '
    '<strong>Hiroshima</strong>. In an instant, a single bomb destroyed an entire city. '
    'About <strong>80,000 people</strong> were killed immediately, '
    'and tens of thousands more died later from burns and radiation. '
    'Three days later, on August 9, a second atomic bomb was dropped on <strong>Nagasaki</strong>, '
    'killing about <strong>40,000</strong> people instantly.\u201d</p>'

    '<p>\u201cOn <strong>August 15, 1945</strong>, Japanese Emperor <strong>Hirohito</strong> announced Japan\u2019s surrender. '
    'World War II \u2014 the deadliest war in human history \u2014 was finally over. '
    'Across the world, an estimated <strong>70 to 85 million people</strong> had died.\u201d</p>'

    '<p>Evelyn was very quiet. \u201cDid they have to use the bomb?\u201d she asked.</p>'

    '<p>\u201cPeople have been debating that question ever since,\u201d Jason said gently. '
    '\u201cSome say it saved millions of lives by ending the war quickly. '
    'Others say it was wrong to use such a terrible weapon on cities full of civilians. '
    'There may not be a simple answer \u2014 but the question is one every generation must ask.\u201d</p>'

    '<h3>Aftermath and Hope</h3>'

    '<p>\u201cAfter the war, something remarkable happened,\u201d Jason said. '
    '\u201cInstead of punishing Japan, the United States helped rebuild it. '
    'Under General <strong>Douglas MacArthur</strong>, Japan became a democracy, '
    'rebuilt its economy, and eventually became one of America\u2019s closest allies. '
    'The same thing happened in Europe with the <strong>Marshall Plan</strong>, '
    'which sent billions of dollars to rebuild shattered countries \u2014 '
    'including former enemies Germany and Italy.\u201d</p>'

    '<p>\u201cAnd in 1945, fifty nations came together to create the <strong>United Nations</strong> \u2014 '
    'an organization dedicated to preventing another world war. Its charter begins: '
    '<strong>\u201cWe the peoples of the United Nations, determined to save succeeding generations '
    'from the scourge of war\u2026\u201d</strong> The world had learned, at a terrible cost, '
    'that nations must find ways to talk instead of fight.\u201d</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="WWII Pacific Theater">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">World War II in the Pacific (1941\u20131945)</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">Pearl Harbor (1941)</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">2,403 Americans killed</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">America enters the war</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Midway (1942)</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">4 Japanese carriers sunk</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Turning point of the Pacific war</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">Island Hopping</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Guadalcanal, Iwo Jima, Okinawa</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Brutal battles, island by island</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">War Ends (1945)</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Atomic bombs, Japan surrenders</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">United Nations founded</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">70\u201385 million people died in WWII \u2014 the deadliest conflict in human history</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">From the ashes, the world chose rebuilding over revenge and created the United Nations</text>'
    '</svg>'
    '</div>'

    '<p>The book brought them home. Evelyn set the globe spinning slowly.</p>'

    '<p>\u201cThey rebuilt each other,\u201d she said. \u201cEven after all that.\u201d</p>'

    '<p>\u201cThat\u2019s the part worth remembering most,\u201d Jason said. '
    '\u201cNot just the destruction, but the choice to rebuild \u2014 even your enemies. '
    'That took a different kind of courage. '
    'Goodnight, Pacific.\u201d</p>'

    '<p>\u201cGoodnight, brave world.\u201d</p>'
)

disc_84 = [
    "After the war, the United States helped rebuild Japan and Germany instead of punishing them. Why do you think helping former enemies was a better choice than revenge?",
    "The atomic bomb ended the war quickly but killed over 100,000 civilians. Do you think there are some weapons that should never be used, even to end a war?",
    "The United Nations was created so countries could talk instead of fight. What makes it so hard for countries to solve disagreements peacefully, and what do you think helps?"
]

quiz_84 = [
    {
        "q": "What event caused the United States to enter World War II?",
        "options": [
            "The invasion of Poland",
            "The fall of France",
            "The attack on Pearl Harbor",
            "The Battle of Midway"
        ],
        "correct": 2
    },
    {
        "q": "Why was the Battle of Midway a turning point in the Pacific war?",
        "options": [
            "Japan invaded the United States mainland",
            "The U.S. sank four Japanese aircraft carriers",
            "Japan surrendered after the battle",
            "The atomic bomb was first tested there"
        ],
        "correct": 1
    },
    {
        "q": "What international organization was founded after WWII to prevent future wars?",
        "options": [
            "The League of Nations",
            "NATO",
            "The United Nations",
            "The European Union"
        ],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 84:
        lessons[i] = {
            "id": 84,
            "type": "history",
            "topic": "WWII",
            "title": "The World at War \u2014 Part 2",
            "readingTime": "10 min",
            "story": story_84,
            "discussion": disc_84,
            "quiz": quiz_84
        }
        print("Updated lesson 84: The World at War \u2014 Part 2")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
