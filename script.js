// Card index data only — full narratives live in data/*.json → battles/*.html
const battles = [
    {
        "id": "poland",
        "title": "Invasion of Poland",
        "date": "September 1, 1939 - October 6, 1939",
        "location": "Poland",
        "result": "German and Soviet victory",
        "excerpt": "Germany and the Soviet Union invade and partition Poland—the opening of World War II in Europe and a first test of combined-arms warfare.",
        "image": "assets/images/invasion_of_poland_1783712194487.png"
    },
    {
        "id": "britain",
        "title": "Battle of Britain",
        "date": "July 10, 1940 - October 31, 1940",
        "location": "United Kingdom Airspace",
        "result": "Decisive British victory",
        "excerpt": "RAF Fighter Command denies the Luftwaffe air superiority over Britain, forcing the indefinite postponement of Operation Sea Lion.",
        "image": "assets/images/battle_of_britain_1783712202242.png"
    },
    {
        "id": "barbarossa",
        "title": "Operation Barbarossa",
        "date": "June 22, 1941 - December 5, 1941",
        "location": "Eastern Europe",
        "result": "Axis strategic failure; Soviet operational recovery",
        "excerpt": "The largest invasion in history fails to destroy the Soviet Union before winter, locking Germany into a war of attrition in the East.",
        "image": "assets/images/operation_barbarossa_1783712208922.png"
    },
    {
        "id": "pearl-harbor",
        "title": "Attack on Pearl Harbor",
        "date": "December 7, 1941",
        "location": "Pearl Harbor, Hawaii, US",
        "result": "Japanese tactical victory; strategic US mobilization",
        "excerpt": "Japan's carrier strike cripples the US battle line at Pearl Harbor—but misses the carriers, fuel, and repair yards that will fuel America's Pacific recovery.",
        "image": "assets/images/pearl_harbor_1783712216007.png"
    },
    {
        "id": "midway",
        "title": "Battle of Midway",
        "date": "June 4-7, 1942",
        "location": "Midway Atoll, Pacific Ocean",
        "result": "Decisive American victory",
        "excerpt": "Codebreaking and carrier aviation smash four Japanese fleet carriers, shifting the strategic initiative in the Pacific to the United States.",
        "image": "assets/images/battle_of_midway_1783712222034.png"
    },
    {
        "id": "stalingrad",
        "title": "Battle of Stalingrad",
        "date": "July 17, 1942 – February 2, 1943 (city fighting intensifies from August 23, 1942)",
        "location": "Stalingrad, Soviet Union",
        "result": "Decisive Soviet victory",
        "excerpt": "Urban slaughter on the Volga ends with the destruction of the German 6th Army—the great turning point on the Eastern Front.",
        "image": "assets/images/battle_of_stalingrad_1783712239181.png"
    },
    {
        "id": "d-day",
        "title": "Normandy Landings (D-Day)",
        "date": "June 6, 1944",
        "location": "Normandy, France",
        "result": "Decisive Allied victory",
        "excerpt": "The largest seaborne invasion in history opens a major Western front in Normandy and begins the liberation of northwest Europe.",
        "image": "assets/images/normandy_landings_1783712245867.png"
    },
    {
        "id": "bulge",
        "title": "Battle of the Bulge",
        "date": "December 16, 1944 – January 25, 1945",
        "location": "Ardennes region, Belgium, Luxembourg, Germany",
        "result": "Decisive Allied victory",
        "excerpt": "Hitler's last great gamble in the West punches a bulge into Allied lines in the Ardennes—then collapses under American resistance and airpower.",
        "image": "assets/images/battle_of_bulge_1783712254116.png"
    },
    {
        "id": "iwo-jima",
        "title": "Battle of Iwo Jima",
        "date": "February 19 - March 26, 1945",
        "location": "Iwo Jima, Volcano Islands (under Tokyo Prefecture), Japan",
        "result": "Decisive American victory",
        "excerpt": "Marines take a fortified volcanic island at extreme cost, securing airfields that become emergency havens for B-29 crews.",
        "image": "assets/images/battle_of_iwo_jima_1783712261591.png"
    },
    {
        "id": "berlin",
        "title": "Battle of Berlin",
        "date": "April 16 - May 2, 1945",
        "location": "Berlin, Germany",
        "result": "Decisive Soviet victory",
        "excerpt": "Soviet armies storm the Nazi capital; Hitler dies in his bunker, and the war in Europe ends days later.",
        "image": "assets/images/battle_of_berlin_1783712268854.png"
    }
];

document.addEventListener('DOMContentLoaded', () => {
    const grid = document.getElementById('battles-grid');
    if (!grid) return;

    battles.forEach((battle) => {
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

        card.addEventListener('click', () => {
            window.location.href = `battles/${battle.id}.html`;
        });

        grid.appendChild(card);
    });

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    });

    document.querySelectorAll('.card').forEach(card => observer.observe(card));
});
