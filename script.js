const battles = [
    {
        id: 'poland',
        title: 'Invasion of Poland',
        date: 'September 1, 1939 - October 6, 1939',
        location: 'Poland',
        result: 'German and Soviet victory',
        excerpt: 'The invasion that marked the beginning of World War II, introducing the world to the devastating tactic of Blitzkrieg.',
        description: '<p>The Invasion of Poland was a joint attack on the Republic of Poland by Nazi Germany, the Slovak Republic, and the Soviet Union; which marked the beginning of World War II. The German invasion began on 1 September 1939, one week after the signing of the Molotov–Ribbentrop Pact.</p><p>Germany\'s forces used the Blitzkrieg (lightning war) tactic, characterized by extensive bombing early on to destroy the enemy\'s air capacity, railroads, communication lines, and munitions dumps, followed by a massive land invasion with overwhelming numbers of troops, tanks, and artillery.</p>',
        image: 'assets/images/invasion_of_poland_1783712194487.png'
    },
    {
        id: 'britain',
        title: 'Battle of Britain',
        date: 'July 10, 1940 - October 31, 1940',
        location: 'United Kingdom Airspace',
        result: 'Decisive British victory',
        excerpt: 'The first major military campaign fought entirely by air forces, where the RAF successfully defended the UK against the Luftwaffe.',
        description: '<p>The Battle of Britain was a military campaign of the Second World War, in which the Royal Air Force (RAF) and the Fleet Air Arm (FAA) of the Royal Navy defended the United Kingdom (UK) against large-scale attacks by Nazi Germany\'s air force, the Luftwaffe.</p><p>It was the first major military campaign fought entirely by air forces. The British victory prevented Germany from launching Operation Sea Lion, the planned amphibious and airborne invasion of Britain.</p>',
        image: 'assets/images/battle_of_britain_1783712202242.png'
    },
    {
        id: 'barbarossa',
        title: 'Operation Barbarossa',
        date: 'June 22, 1941 - December 5, 1941',
        location: 'Eastern Europe',
        result: 'Strategic Soviet victory',
        excerpt: 'The massive Axis invasion of the Soviet Union, opening the brutal Eastern Front.',
        description: '<p>Operation Barbarossa was the code name for the invasion of the Soviet Union by Nazi Germany and most of its Axis allies, which started on Sunday, 22 June 1941. It was the largest land offensive in human history, with over 10 million combatants taking part.</p><p>The operation put into action Nazi Germany\'s ideological goal of conquering the western Soviet Union so as to repopulate it with Germans. Although the Axis forces achieved significant initial successes, their offensive stalled at the Battle of Moscow and they were pushed back by a Soviet winter counteroffensive.</p>',
        image: 'assets/images/operation_barbarossa_1783712208922.png'
    },
    {
        id: 'pearl-harbor',
        title: 'Attack on Pearl Harbor',
        date: 'December 7, 1941',
        location: 'Pearl Harbor, Hawaii, US',
        result: 'Major Japanese tactical victory',
        excerpt: 'The surprise military strike by the Imperial Japanese Navy that led to the United States\' formal entry into World War II.',
        description: '<p>The Attack on Pearl Harbor was a surprise military strike by the Imperial Japanese Navy Air Service upon the United States against the naval base at Pearl Harbor in Honolulu, Territory of Hawaii, just before 08:00, on Sunday morning, December 7, 1941.</p><p>The attack killed 2,403 U.S. personnel, including 68 civilians, and destroyed or damaged 19 U.S. Navy ships, including 8 battleships. The following day, the United States declared war on Japan, formally entering World War II.</p>',
        image: 'assets/images/pearl_harbor_1783712216007.png'
    },
    {
        id: 'midway',
        title: 'Battle of Midway',
        date: 'June 4-7, 1942',
        location: 'Midway Atoll, Pacific Ocean',
        result: 'Decisive American victory',
        excerpt: 'A major naval battle in the Pacific Theater that permanently crippled the Japanese fleet.',
        description: '<p>The Battle of Midway was a major naval battle in the Pacific Theater of World War II that took place on 4–7 June 1942, six months after Japan\'s attack on Pearl Harbor. The U.S. Navy decisively defeated an attacking fleet of the Imperial Japanese Navy.</p><p>American codebreakers were able to determine the date and location of the attack, enabling the forewarned U.S. Navy to prepare its own ambush. Four Japanese aircraft carriers and a heavy cruiser were sunk, effectively destroying Japan\'s naval strength.</p>',
        image: 'assets/images/battle_of_midway_1783712222034.png'
    },
    {
        id: 'stalingrad',
        title: 'Battle of Stalingrad',
        date: 'August 23, 1942 - February 2, 1943',
        location: 'Stalingrad, Soviet Union',
        result: 'Decisive Soviet victory',
        excerpt: 'The deadliest battle of the war, marking the turning point on the Eastern Front.',
        description: '<p>The Battle of Stalingrad was a major battle on the Eastern Front of World War II where Nazi Germany and its allies unsuccessfully fought the Soviet Union for control of the city of Stalingrad in Southern Russia.</p><p>It was the largest and bloodiest battle in the history of warfare, with an estimated 2 million casualties. The German 6th Army was completely destroyed, and the Axis forces never regained the initiative in the East.</p>',
        image: 'assets/images/battle_of_stalingrad_1783712239181.png'
    },
    {
        id: 'd-day',
        title: 'Normandy Landings (D-Day)',
        date: 'June 6, 1944',
        location: 'Normandy, France',
        result: 'Decisive Allied victory',
        excerpt: 'The largest seaborne invasion in history, initiating the Western Allied effort to liberate mainland Europe.',
        description: '<p>The Normandy landings were the landing operations and associated airborne operations on Tuesday, 6 June 1944 of the Allied invasion of Normandy in Operation Overlord during World War II. Codenamed Operation Neptune and often referred to as D-Day, it was the largest seaborne invasion in history.</p><p>The operation began the liberation of France and the rest of Western Europe, and laid the foundations of the Allied victory on the Western Front.</p>',
        image: 'assets/images/normandy_landings_1783712245867.png'
    },
    {
        id: 'bulge',
        title: 'Battle of the Bulge',
        date: 'December 16, 1944 - January 25, 1945',
        location: 'Ardennes region, Western Europe',
        result: 'Decisive Allied victory',
        excerpt: 'The last major German offensive campaign on the Western Front.',
        description: '<p>The Battle of the Bulge, also known as the Ardennes Offensive, was the last major German offensive campaign on the Western Front during World War II. It was launched through the densely forested Ardennes region of Wallonia in eastern Belgium, northeast France, and Luxembourg.</p><p>The surprise attack caught the Allied forces completely off guard. American forces bore the brunt of the attack and incurred their highest casualties of any operation during the war. However, the offensive failed, severely depleting Germany\'s armored forces on the Western Front.</p>',
        image: 'assets/images/battle_of_bulge_1783712254116.png'
    },
    {
        id: 'iwo-jima',
        title: 'Battle of Iwo Jima',
        date: 'February 19 - March 26, 1945',
        location: 'Iwo Jima, Volcano Islands, Japan',
        result: 'Decisive American victory',
        excerpt: 'A major battle in which the United States Marine Corps and Navy landed on and eventually captured the island of Iwo Jima.',
        description: '<p>The Battle of Iwo Jima was a major battle in which the United States Marine Corps and Navy landed on and eventually captured the island of Iwo Jima from the Imperial Japanese Army (IJA) during World War II. The American invasion had the purpose of capturing the island with its two airfields.</p><p>The battle produced some of the fiercest and bloodiest fighting of the Pacific War. The famous photograph of the raising of the U.S. flag on Mount Suribachi by six Marines was taken during this battle.</p>',
        image: 'assets/images/battle_of_iwo_jima_1783712261591.png'
    },
    {
        id: 'berlin',
        title: 'Battle of Berlin',
        date: 'April 16 - May 2, 1945',
        location: 'Berlin, Germany',
        result: 'Decisive Soviet victory',
        excerpt: 'The final major offensive of the European theatre, culminating in the surrender of Nazi Germany.',
        description: '<p>The Battle of Berlin, designated the Berlin Strategic Offensive Operation by the Soviet Union, was the final major offensive of the European theatre of World War II. Following the Vistula–Oder Offensive of January–February 1945, the Red Army had temporarily halted on a line 60 km east of Berlin.</p><p>Soviet forces encircled the city and fought house-to-house. The battle resulted in the death of Adolf Hitler and the unconditional surrender of the city\'s garrison, effectively ending the war in Europe.</p>',
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
