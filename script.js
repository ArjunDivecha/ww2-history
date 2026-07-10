const battles = [
    {
        id: 'poland',
        title: 'Invasion of Poland',
        date: 'September 1, 1939 - October 6, 1939',
        location: 'Poland',
        result: 'German and Soviet victory',
        excerpt: 'The invasion that marked the beginning of World War II, introducing the world to the devastating tactic of Blitzkrieg.',
        description: '<p><strong>Strategic Context:</strong> The German invasion of Poland on September 1, 1939, codenamed <em>Fall Weiss</em> (Case White), was the immediate catalyst for World War II in Europe. Emboldened by the Molotov-Ribbentrop Pact which secured Soviet non-intervention and partitioned Eastern Europe, Hitler sought to reclaim territory lost after WWI and secure <em>Lebensraum</em>.</p><p><strong>Tactical Execution:</strong> The campaign introduced the world to <em>Blitzkrieg</em> (Lightning War). This doctrine relied on the close coordination of <em>Luftwaffe</em> close air support, mechanized Panzer divisions, and motorized infantry to encircle and annihilate Polish forces before they could mobilize. The Polish army, though fiercely brave, was numerically and technologically outmatched, particularly in armor and air superiority. By September 17, the Soviet Union invaded from the east, sealing Poland\'s fate.</p><p><strong>Consequences for the War:</strong> The invasion compelled Britain and France to declare war on Germany, formally igniting a global conflict. It proved the terrifying efficacy of mechanized warfare, rendering static trench defenses obsolete. Furthermore, the brutal occupation of Poland set the grim precedent for the Holocaust and the ruthlessness of the war on the Eastern Front.</p>',
        image: 'assets/images/invasion_of_poland_1783712194487.png'
    },
    {
        id: 'britain',
        title: 'Battle of Britain',
        date: 'July 10, 1940 - October 31, 1940',
        location: 'United Kingdom Airspace',
        result: 'Decisive British victory',
        excerpt: 'The first major military campaign fought entirely by air forces, where the RAF successfully defended the UK against the Luftwaffe.',
        description: '<p><strong>Strategic Context:</strong> Following the fall of France, Britain stood alone. Hitler\'s Directive No. 16 outlined Operation Sea Lion, the amphibious invasion of the British Isles. However, an invasion required absolute air superiority over the English Channel to prevent the Royal Navy from intercepting the invasion fleet.</p><p><strong>Tactical Execution:</strong> The <em>Luftwaffe</em>, under Hermann Göring, launched massive raids against RAF Fighter Command infrastructure, airfields, and radar stations (the Dowding System). The British possessed critical advantages: fighting over home territory, the revolutionary integrated air defense system utilizing radar, and the exceptional performance of the Supermarine Spitfire and Hawker Hurricane. When the Luftwaffe fatally shifted focus to bombing London (The Blitz) in September, Fighter Command was given vital time to recover, eventually inflicting unsustainable losses on the German bombers.</p><p><strong>Consequences for the War:</strong> The RAF\'s victory was Germany\'s first major strategic defeat. It forced the indefinite postponement of Operation Sea Lion and ensured Britain remained a formidable unsinkable aircraft carrier. This allowed the eventual buildup of Allied forces for the bomber offensive and the eventual D-Day landings. It also forced Hitler to fight a two-front war when he invaded the Soviet Union the following year.</p>',
        image: 'assets/images/battle_of_britain_1783712202242.png'
    },
    {
        id: 'barbarossa',
        title: 'Operation Barbarossa',
        date: 'June 22, 1941 - December 5, 1941',
        location: 'Eastern Europe',
        result: 'Strategic Soviet victory',
        excerpt: 'The massive Axis invasion of the Soviet Union, opening the brutal Eastern Front.',
        description: '<p><strong>Strategic Context:</strong> Launched on June 22, 1941, Operation Barbarossa was the realization of Hitler\'s primary ideological goal: the destruction of "Judeo-Bolshevism" and the acquisition of <em>Lebensraum</em> in the East. It was the largest and most lethal military operation in human history, involving over three million Axis troops along a 1,800-mile front.</p><p><strong>Tactical Execution:</strong> The Axis forces achieved stunning initial successes, utilizing massive <em>Kesselschlacht</em> (cauldron battles) to encircle and capture millions of Soviet troops at Minsk, Smolensk, and Kiev. However, the German High Command (OKW) underestimated Soviet reserves, industrial resilience, and the sheer logistical nightmare of the Russian vastness. As the autumn rains (<em>Rasputitsa</em>) turned roads into mud, and the brutal Russian winter set in, the German advance ground to a halt at the gates of Moscow.</p><p><strong>Consequences for the War:</strong> Barbarossa\'s failure was the turning point of the entire conflict. Germany failed to secure a quick victory and found itself trapped in a grueling war of attrition against an enemy with vastly superior manpower and industrial capacity. The Eastern Front became the meat grinder of the Wehrmacht, consuming roughly 80% of all German military casualties in the war.</p>',
        image: 'assets/images/operation_barbarossa_1783712208922.png'
    },
    {
        id: 'pearl-harbor',
        title: 'Attack on Pearl Harbor',
        date: 'December 7, 1941',
        location: 'Pearl Harbor, Hawaii, US',
        result: 'Major Japanese tactical victory',
        excerpt: 'The surprise military strike by the Imperial Japanese Navy that led to the United States\' formal entry into World War II.',
        description: '<p><strong>Strategic Context:</strong> Faced with a crippling US oil embargo due to their expansion in China and French Indochina, the Japanese Empire determined that war with the United States was inevitable. Admiral Isoroku Yamamoto devised a preemptive strike to cripple the US Pacific Fleet, buying Japan the 6 to 12 months needed to conquer Southeast Asia and secure vital resources.</p><p><strong>Tactical Execution:</strong> On the morning of December 7, 1941, a massive Japanese carrier strike force (the <em>Kido Butai</em>) launched 353 aircraft in two waves. The attack achieved complete tactical surprise, sinking or severely damaging eight battleships, including the USS Arizona, and destroying nearly 200 aircraft. However, the Japanese failed to target the base\'s vital oil storage facilities, submarine pens, and crucially, the US aircraft carriers, which were out at sea.</p><p><strong>Consequences for the War:</strong> The attack was a catastrophic strategic blunder. Instead of forcing a negotiated peace, it instantly united a previously isolationist American public in a state of absolute resolve. It brought the colossal industrial and economic might of the United States fully into the war against both Japan and Germany (who inexplicably declared war on the US four days later), ultimately sealing the doom of the Axis powers.</p>',
        image: 'assets/images/pearl_harbor_1783712216007.png'
    },
    {
        id: 'midway',
        title: 'Battle of Midway',
        date: 'June 4-7, 1942',
        location: 'Midway Atoll, Pacific Ocean',
        result: 'Decisive American victory',
        excerpt: 'A major naval battle in the Pacific Theater that permanently crippled the Japanese fleet.',
        description: '<p><strong>Strategic Context:</strong> Seeking to eliminate the US aircraft carriers that had escaped Pearl Harbor and secure the defensive perimeter of the Japanese Empire, Admiral Yamamoto orchestrated an elaborate trap at the Midway Atoll. However, American codebreakers (Station HYPO) had partially decrypted the Japanese JN-25 naval code, uncovering the date and location of the attack.</p><p><strong>Tactical Execution:</strong> Armed with this intelligence, Admiral Chester Nimitz positioned his three available carriers (Enterprise, Hornet, and the hastily repaired Yorktown) to ambush the Japanese fleet. The battle on June 4, 1942, hinged on timing and luck. American torpedo bombers were decimated but drew Japanese defensive fighters down to the deck. Minutes later, American SBD Dauntless dive bombers arrived unopposed high above, catching the Japanese carriers with decks full of aircraft, fuel, and ordnance. In a miraculous five-minute window, three Japanese fleet carriers were mortally wounded; a fourth was sunk later that day.</p><p><strong>Consequences for the War:</strong> Midway was the decisive turning point of the Pacific War. The loss of four elite fleet carriers and hundreds of irreplaceable veteran pilots permanently crippled the offensive capability of the Imperial Japanese Navy. The strategic initiative shifted permanently to the United States, allowing the Allies to begin their relentless island-hopping campaign toward the Japanese home islands.</p>',
        image: 'assets/images/battle_of_midway_1783712222034.png'
    },
    {
        id: 'stalingrad',
        title: 'Battle of Stalingrad',
        date: 'August 23, 1942 - February 2, 1943',
        location: 'Stalingrad, Soviet Union',
        result: 'Decisive Soviet victory',
        excerpt: 'The deadliest battle of the war, marking the turning point on the Eastern Front.',
        description: '<p><strong>Strategic Context:</strong> In the summer of 1942, Hitler launched Case Blue, a massive offensive directed toward the oil fields of the Caucasus. As the German 6th Army advanced, Hitler became obsessed with capturing Stalingrad, a major industrial center on the Volga River bearing the name of his ideological nemesis.</p><p><strong>Tactical Execution:</strong> The battle devolved into the most brutal urban warfare in history (<em>Rattenkrieg</em> or "Rat War"). The <em>Luftwaffe</em> reduced the city to rubble, which ironically created perfect defensive positions for the deeply entrenched Soviet 62nd Army under General Chuikov. While the German 6th Army bled itself white taking 90% of the city in agonizing house-to-house fighting, the Soviets secretly massed a million men on the flanks. In November, Operation Uranus smashed through the weaker Romanian and Italian armies on the German flanks, encircling the entire 6th Army inside the ruined city. Hitler forbade a breakout, leading to the starvation and surrender of over 90,000 German soldiers by February 1943.</p><p><strong>Consequences for the War:</strong> Stalingrad is widely considered the psychological and military turning point of World War II. The myth of the invincible <em>Wehrmacht</em> was shattered. The loss of an entire field army, along with massive amounts of materiel, broke the back of the German war machine. From Stalingrad onward, the strategic initiative on the Eastern Front belonged exclusively to the Soviet Union, beginning the long, bloody drive to Berlin.</p>',
        image: 'assets/images/battle_of_stalingrad_1783712239181.png'
    },
    {
        id: 'd-day',
        title: 'Normandy Landings (D-Day)',
        date: 'June 6, 1944',
        location: 'Normandy, France',
        result: 'Decisive Allied victory',
        excerpt: 'The largest seaborne invasion in history, initiating the Western Allied effort to liberate mainland Europe.',
        description: '<p><strong>Strategic Context:</strong> Operation Overlord was the culmination of years of Allied planning to open a massive second front in Western Europe, relieving pressure on the Soviets and beginning the liberation of occupied France. It required an unprecedented logistical buildup in Britain and a complex deception campaign (Operation Bodyguard) to convince the Germans the invasion would occur at the Pas de Calais.</p><p><strong>Tactical Execution:</strong> On June 6, 1944, under the command of General Dwight D. Eisenhower, over 156,000 American, British, and Canadian troops stormed five beaches (Utah, Omaha, Gold, Juno, Sword). The amphibious assault was preceded by massive naval bombardment and the dropping of airborne divisions behind enemy lines to secure bridges and causeways. Omaha beach saw the fiercest resistance and highest casualties, as troops faced heavily fortified bluffs untouched by the preliminary bombardment. However, overwhelming Allied naval gunfire, air supremacy, and the sheer courage of the infantry eventually breached the Atlantic Wall.</p><p><strong>Consequences for the War:</strong> The successful lodgment at Normandy sealed the fate of Nazi Germany. It forced Hitler into a two-front war that his depleted forces could not sustain. Over the next two months, the Allies broke out of the Normandy bocage, leading to the rapid liberation of Paris and the chaotic retreat of German forces toward their own borders.</p>',
        image: 'assets/images/normandy_landings_1783712245867.png'
    },
    {
        id: 'bulge',
        title: 'Battle of the Bulge',
        date: 'December 16, 1944 - January 25, 1945',
        location: 'Ardennes region, Western Europe',
        result: 'Decisive Allied victory',
        excerpt: 'The last major German offensive campaign on the Western Front.',
        description: '<p><strong>Strategic Context:</strong> By late 1944, Allied forces were closing in on the German border. In a desperate gamble to reverse the tide, Hitler orchestrated <em>Unternehmen Wacht am Rhein</em> (Operation Watch on the Rhine). The goal was to punch through the weakly defended Ardennes forest, cross the Meuse River, and capture the vital port of Antwerp, splitting the Allied armies and forcing a negotiated peace on the Western Front.</p><p><strong>Tactical Execution:</strong> Launched on December 16 under the cover of dense winter weather that grounded Allied airpower, the German offensive achieved total surprise. They created a massive "bulge" in the American lines. The battle was characterized by bitter cold, confused fighting, and heroic American defensive stands, notably by the 101st Airborne Division at the besieged crossroads town of Bastogne. When the skies cleared in late December, Allied airpower devastated German supply lines, and General George S. Patton\'s Third Army executed a brilliant 90-degree pivot to break the siege of Bastogne, collapsing the German salient.</p><p><strong>Consequences for the War:</strong> It was the largest and bloodiest battle fought by the United States in World War II. Hitler\'s gamble failed catastrophically. The offensive completely exhausted the last operational reserves of the <em>Wehrmacht</em> and the <em>Luftwaffe</em>. Germany\'s armored forces were decimated, leaving the path into the German heartland virtually undefended and accelerating the end of the war in Europe.</p>',
        image: 'assets/images/battle_of_bulge_1783712254116.png'
    },
    {
        id: 'iwo-jima',
        title: 'Battle of Iwo Jima',
        date: 'February 19 - March 26, 1945',
        location: 'Iwo Jima, Volcano Islands, Japan',
        result: 'Decisive American victory',
        excerpt: 'A major battle in which the United States Marine Corps and Navy landed on and eventually captured the island of Iwo Jima.',
        description: '<p><strong>Strategic Context:</strong> As the American island-hopping campaign closed in on the Japanese home islands, the volcanic island of Iwo Jima became a critical objective. The US Army Air Forces needed it as an emergency landing strip for B-29 Superfortresses conducting bombing raids on Japan, and as a base for P-51 Mustang fighter escorts.</p><p><strong>Tactical Execution:</strong> Under the command of General Tadamichi Kuribayashi, the Japanese completely altered their defensive doctrine. Instead of contesting the beaches, they constructed a brilliant, massive subterranean network of deeply dug-in bunkers, tunnels, and hidden artillery positions across the island, particularly within Mount Suribachi. When the US Marines landed on February 19, 1945, they faced a concealed, fanatical enemy that fought virtually to the last man. The fighting was unspeakably savage, requiring Marines to systematically clear pillboxes with flamethrowers and satchel charges over five weeks of relentless combat.</p><p><strong>Consequences for the War:</strong> Iwo Jima was the only battle in the Pacific where total American casualties exceeded those of the Japanese, although Japanese fatalities were vastly higher. The horrific cost of taking a tiny, heavily fortified island deeply shocked the American public and military leadership. This demonstrated the immense blood sacrifice that would be required for a ground invasion of the Japanese home islands (Operation Downfall), heavily influencing President Truman\'s later decision to use atomic weapons.</p>',
        image: 'assets/images/battle_of_iwo_jima_1783712261591.png'
    },
    {
        id: 'berlin',
        title: 'Battle of Berlin',
        date: 'April 16 - May 2, 1945',
        location: 'Berlin, Germany',
        result: 'Decisive Soviet victory',
        excerpt: 'The final major offensive of the European theatre, culminating in the surrender of Nazi Germany.',
        description: '<p><strong>Strategic Context:</strong> By April 1945, the Third Reich was in its death throes. The Red Army had advanced from the Volga to the Oder River, just 40 miles from Berlin. Stalin, driven by a desire for vengeance and the acquisition of geopolitical spoils (including German nuclear research), ordered a massive, rushed offensive to take the capital before the Western Allies could arrive.</p><p><strong>Tactical Execution:</strong> Over 2.5 million Soviet troops, backed by unimaginable artillery superiority, encircled the ruined city. The defense of Berlin was left to a desperate amalgamation of depleted Wehrmacht units, the SS, and poorly equipped <em>Volkssturm</em> (militia) and Hitler Youth. The fighting was apocalyptic, involving ferocious street-by-street and room-by-room combat. The Red Army relentlessly pushed toward the Reichstag and the Führerbunker. On April 30, as Soviet troops fought just blocks away, Adolf Hitler committed suicide.</p><p><strong>Consequences for the War:</strong> The fall of Berlin resulted in the unconditional surrender of Nazi Germany on May 8, 1945, ending the war in Europe. However, the battle also sowed the seeds of the Cold War. The brutal occupation of the city and its subsequent division into occupation zones by the victorious Allies created the flashpoint that would define global geopolitics for the next half-century.</p>',
        image: 'assets/images/battle_of_berlin_1783712268854.png'
    }
];

document.addEventListener('DOMContentLoaded', () => {
    const grid = document.getElementById('battles-grid');
    const modal = document.getElementById('battle-modal');
    const closeModalBtn = document.getElementById('close-modal');
    
    // Elements to update in modal
    const modalImg = document.getElementById('modal-img');
    const modalDate = document.getElementById('modal-date');
    const modalTitle = document.getElementById('modal-title');
    const modalLocation = document.getElementById('modal-location');
    const modalResult = document.getElementById('modal-result');
    const modalDesc = document.getElementById('modal-description');

    // Render cards
    battles.forEach((battle, index) => {
        const card = document.createElement('article');
        card.className = 'card';
        card.dataset.id = battle.id;
        
        card.innerHTML = `
            <div class="card-img-wrapper">
                <img src="${battle.image}" alt="${battle.title}" class="card-img" loading="lazy">
            </div>
            <div class="card-content">
                <span class="card-date">${battle.date}</span>
                <h3 class="card-title">${battle.title}</h3>
                <p class="card-excerpt">${battle.excerpt}</p>
                <div class="card-read-more">
                    Explore <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                </div>
            </div>
        `;
        
        // Add click event to open modal
        card.addEventListener('click', () => openModal(battle));
        
        grid.appendChild(card);
    });

    // Modal Functions
    function openModal(battle) {
        modalImg.src = battle.image;
        modalImg.alt = battle.title;
        modalDate.textContent = battle.date;
        modalTitle.textContent = battle.title;
        modalLocation.textContent = battle.location;
        modalResult.textContent = battle.result;
        modalDesc.innerHTML = battle.description;
        
        modal.classList.remove('hidden');
        document.body.style.overflow = 'hidden'; // Prevent background scrolling
    }

    function closeModal() {
        modal.classList.add('hidden');
        document.body.style.overflow = ''; // Restore background scrolling
    }

    closeModalBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', (e) => {
        if (e.target.classList.contains('modal-backdrop')) {
            closeModal();
        }
    });

    // Keyboard support for closing modal
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
            closeModal();
        }
    });

    // Intersection Observer for fade-in scroll animation
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Optional: stop observing once it's visible
                // observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    });

    document.querySelectorAll('.card').forEach(card => {
        observer.observe(card);
    });
});
