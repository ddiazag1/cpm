import json

LESSONS_PATH = r'C:\Users\ddiaz\cpm\curriculum\lessons.json'

story_82 = (
    '<h2>The Jazz Age</h2>'
    '<div class="story-image">'
    '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/1925_Ford_Model_T_touring.jpg/800px-1925_Ford_Model_T_touring.jpg" '
    'alt="A 1925 Ford Model T touring car" loading="lazy">'
    '<p class="image-caption">The Ford Model T \u2014 the car that put America on wheels and changed everyday life in the 1920s</p>'
    '</div>'

    '<p>Evelyn was tapping her feet to music coming from the kitchen radio. '
    '\u201cJason, was there ever a time when <em>everyone</em> in America felt like dancing?\u201d</p>'

    '<p>Jason smiled and opened The Living World, turning the brass clasp. '
    '\u201cAs a matter of fact, there was. They called it the Roaring Twenties.\u201d</p>'

    '<p>The green light swept them into a crowded city street. Bright electric signs blinked '
    'against the night sky. Somewhere nearby, a trumpet wailed a melody '
    'unlike anything Evelyn had ever heard \u2014 fast, free, and full of joy.</p>'

    '<h3>A World Catching Its Breath</h3>'

    '<p>\u201cWorld War I ended in 1918,\u201d Jason said. \u201cMillions had died, and people on every continent '
    'were exhausted from years of fear and sacrifice. When the war was finally over, '
    'Americans felt a huge wave of relief. Soldiers came home. Factories that had built '
    'tanks and weapons switched to making cars, radios, and washing machines. '
    'The economy took off like a rocket.\u201d</p>'

    '<p>\u201cBy the 1920s, America was the richest country in the world. Wages were rising, '
    'new inventions appeared every month, and people believed the good times '
    'would never end. They called it the <strong>Roaring Twenties</strong> because life felt loud, '
    'fast, and exciting.\u201d</p>'

    '<h3>Jazz \u2014 America\u2019s Music</h3>'

    '<p>\u201cThe heartbeat of the 1920s was <strong>jazz</strong>,\u201d Jason said. '
    '\u201cJazz was born in <strong>New Orleans</strong>, created mostly by African American musicians '
    'who blended African rhythms, blues, spirituals, and ragtime into something brand new. '
    'What made jazz special was <strong>improvisation</strong> \u2014 musicians made up melodies on the spot, '
    'so every performance was unique.\u201d</p>'

    '<p>\u201cMusicians like <strong>Louis Armstrong</strong> could make a trumpet laugh and cry. '
    '<strong>Duke Ellington</strong> led one of the greatest orchestras in history at the Cotton Club in Harlem. '
    '<strong>Bessie Smith</strong>, the \u2018Empress of the Blues,\u2019 sang with a power that filled entire theaters.\u201d</p>'

    '<p>Evelyn listened to the trumpet soaring from a nearby club. '
    '\u201cIt sounds like freedom,\u201d she said.</p>'

    '<p>\u201cThat\u2019s exactly what it was,\u201d Jason said. \u201cFor Black musicians, jazz was a way to express '
    'creativity and dignity in a country that still denied them basic rights. '
    'Jazz didn\u2019t care about the color of your skin \u2014 it cared about what you could play.\u201d</p>'

    '<h3>The Harlem Renaissance</h3>'

    '<p>\u201cJazz was part of something even bigger called the <strong>Harlem Renaissance</strong>,\u201d '
    'Jason continued. \u201cIn the 1920s, the neighborhood of <strong>Harlem</strong> in New York City '
    'became the center of an explosion of African American art, literature, music, and ideas. '
    'Poets like <strong>Langston Hughes</strong> wrote about the beauty and pain of Black life in America. '
    'Writers like <strong>Zora Neale Hurston</strong> told stories of Southern Black communities '
    'with humor and honesty.\u201d</p>'

    '<p>\u201cThe Harlem Renaissance showed the world that African American culture '
    'was brilliant, original, and essential to what it meant to be American. '
    'It planted seeds of pride that would grow into the civil rights movement decades later.\u201d</p>'

    '<h3>Flappers, Cars, and Radios</h3>'

    '<p>\u201cThe 1920s changed everyday life in ways people had never imagined,\u201d Jason said. '
    '\u201cHenry Ford\u2019s <strong>Model T</strong> automobile became cheap enough for ordinary families to buy. '
    'By 1927, there were over <strong>15 million</strong> Model Ts on American roads. '
    'Suddenly, people could live far from where they worked, visit distant relatives on weekends, '
    'and take road trips just for fun.\u201d</p>'

    '<p>\u201c<strong>Radio</strong> connected the entire country for the first time. Families gathered around '
    'their radio sets to hear music, news, comedy shows, and baseball games. '
    'A jazz performance in New York could be heard in a farmhouse in Kansas the same night. '
    '<strong>Movies</strong> became wildly popular too \u2014 by the end of the decade, about 80 million Americans '
    'went to the movies every single week.\u201d</p>'

    '<p>\u201cWomen were changing too,\u201d Jason said. \u201cIn 1920, the <strong>19th Amendment</strong> '
    'finally gave women the right to vote. Young women called <strong>flappers</strong> '
    'cut their hair short, wore shorter dresses, danced to jazz, and insisted on the same freedoms as men. '
    'Not everyone approved \u2014 older generations were shocked \u2014 '
    'but the flappers were pushing American culture forward.\u201d</p>'

    '<h3>The Dark Side: Prohibition</h3>'

    '<p>\u201cNot everything about the 1920s was a party,\u201d Jason said seriously. '
    '\u201cIn 1920, the <strong>18th Amendment</strong> banned the making and selling of alcohol. '
    'This was called <strong>Prohibition</strong>. The idea was to reduce crime and improve families, '
    'but it backfired badly.\u201d</p>'

    '<p>\u201cPeople still wanted to drink, so they went to secret bars called <strong>speakeasies</strong>. '
    'Criminal gangs like the one led by <strong>Al Capone</strong> in Chicago made fortunes '
    'smuggling and selling illegal alcohol. Organized crime grew more powerful than ever. '
    'Prohibition was finally repealed in 1933 \u2014 the country admitted the experiment had failed.\u201d</p>'

    '<h3>The Crash</h3>'

    '<p>\u201cThrough the 1920s, the <strong>stock market</strong> kept climbing higher and higher,\u201d '
    'Jason said. \u201cEveryone was buying stocks \u2014 factory workers, teachers, taxi drivers. '
    'Many borrowed money to buy even more. They were sure prices would keep going up forever.\u201d</p>'

    '<p>\u201cBut on <strong>October 29, 1929</strong> \u2014 a day called <strong>Black Tuesday</strong> \u2014 '
    'the stock market crashed. Prices fell so fast that fortunes were wiped out in hours. '
    'Banks failed. Businesses closed. Millions of people lost their jobs and their savings. '
    'The Roaring Twenties were over, and the <strong>Great Depression</strong> had begun \u2014 '
    'the worst economic disaster in American history.\u201d</p>'

    '<p>Evelyn watched the bright signs on the street flicker and go dark, one by one.</p>'

    '<p>\u201cThe party couldn\u2019t last forever,\u201d she said quietly.</p>'

    '<div class="diagram">'
    '<svg viewBox="0 0 700 130" width="700" height="130" xmlns="http://www.w3.org/2000/svg" aria-label="The Roaring Twenties">'
    '<rect width="700" height="130" fill="#0f1629" rx="8"/>'
    '<text x="350" y="18" text-anchor="middle" fill="#e8a838" font-size="12" font-family="Georgia">The Roaring Twenties (1920\u20131929)</text>'

    '<rect x="20" y="30" width="155" height="50" rx="5" fill="none" stroke="#e8a838" stroke-width="2"/>'
    '<text x="97" y="48" text-anchor="middle" fill="#e8a838" font-size="9" font-weight="bold">Jazz &amp; Culture</text>'
    '<text x="97" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Armstrong, Ellington, Hughes</text>'
    '<text x="97" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Harlem Renaissance</text>'

    '<rect x="190" y="30" width="155" height="50" rx="5" fill="none" stroke="#4a90d9" stroke-width="2"/>'
    '<text x="267" y="48" text-anchor="middle" fill="#4a90d9" font-size="9" font-weight="bold">New Technology</text>'
    '<text x="267" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Model T, radio, movies</text>'
    '<text x="267" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">15 million cars on the road</text>'

    '<rect x="360" y="30" width="155" height="50" rx="5" fill="none" stroke="#2ecc71" stroke-width="2"/>'
    '<text x="437" y="48" text-anchor="middle" fill="#2ecc71" font-size="9" font-weight="bold">Social Change</text>'
    '<text x="437" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Women\u2019s suffrage (19th Amend.)</text>'
    '<text x="437" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Flappers, Prohibition</text>'

    '<rect x="530" y="30" width="150" height="50" rx="5" fill="none" stroke="#e74c3c" stroke-width="2"/>'
    '<text x="605" y="48" text-anchor="middle" fill="#e74c3c" font-size="9" font-weight="bold">The Crash (1929)</text>'
    '<text x="605" y="62" text-anchor="middle" fill="#b8a88a" font-size="8">Black Tuesday ends the party</text>'
    '<text x="605" y="74" text-anchor="middle" fill="#b8a88a" font-size="7">Great Depression begins</text>'

    '<text x="350" y="105" text-anchor="middle" fill="#b8a88a" font-size="9">The 1920s roared with jazz, technology, and change \u2014 then crashed with a lesson about limits</text>'
    '<text x="350" y="120" text-anchor="middle" fill="#b8a88a" font-size="9">The music born in this era became America\u2019s gift to the world</text>'
    '</svg>'
    '</div>'

    '<p>The book brought them home. Evelyn could still hear the echo of that trumpet.</p>'

    '<p>\u201cThe music survived, didn\u2019t it?\u201d she asked. \u201cEven after everything crashed?\u201d</p>'

    '<p>\u201cIt did,\u201d Jason said. \u201cThe stocks disappeared, the speakeasies closed, '
    'but the music \u2014 the music never stopped. '
    'Goodnight, jazz age.\u201d</p>'

    '<p>\u201cGoodnight, roaring twenties.\u201d</p>'
)

disc_82 = [
    "Jazz musicians improvised \u2014 they made up melodies on the spot instead of playing from written music. Why do you think this kind of creative freedom was so important to African American musicians in the 1920s?",
    "The 1920s brought exciting new technology like cars, radios, and movies. How do you think these inventions changed the way families spent time together?",
    "Prohibition tried to ban alcohol to make society better, but it made things worse by creating organized crime. Can you think of other times when banning something didn\u2019t work the way people expected?"
]

quiz_82 = [
    {
        "q": "Where was jazz music born?",
        "options": ["New York City", "Chicago", "New Orleans", "Memphis"],
        "correct": 2
    },
    {
        "q": "What was a speakeasy?",
        "options": [
            "A type of jazz instrument",
            "A secret bar during Prohibition",
            "A radio station",
            "A dance style popular with flappers"
        ],
        "correct": 1
    },
    {
        "q": "What happened on Black Tuesday (October 29, 1929)?",
        "options": [
            "Prohibition was passed",
            "The 19th Amendment gave women the right to vote",
            "The stock market crashed",
            "World War I ended"
        ],
        "correct": 2
    }
]

# --- insert ---
with open(LESSONS_PATH, encoding='utf-8') as f:
    lessons = json.load(f)

for i, l in enumerate(lessons):
    if l['id'] == 82:
        lessons[i] = {
            "id": 82,
            "type": "history",
            "topic": "Jazz",
            "title": "The Jazz Age",
            "readingTime": "10 min",
            "story": story_82,
            "discussion": disc_82,
            "quiz": quiz_82
        }
        print("Updated lesson 82: The Jazz Age")
        break

with open(LESSONS_PATH, 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Done!")
