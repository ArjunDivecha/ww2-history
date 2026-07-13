import os
import json

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

# 1. Invasion of Poland
poland_data = {
    "title": "Invasion of Poland",
    "date": "September 1, 1939 - October 6, 1939",
    "location": "Poland",
    "result": "German and Soviet victory",
    "outcome": "Partition of Poland; declarations of war by France and United Kingdom against Germany, starting WWII.",
    "allied_commanders": "Edward Rydz-Śmigły, Władysław Sikorski, Juliusz Rómmel",
    "axis_commanders": "Adolf Hitler, Fedor von Bock, Gerd von Rundstedt, Joseph Stalin, Semyon Timoshenko",
    "allied_forces": "Approx. 950,000 Polish troops, 430 light tanks, 400 combat aircraft",
    "axis_forces": "Germany: 1,500,000 troops (2,700 tanks, 1,300 aircraft); USSR: 466,000 troops (3,737 tanks, 2,000 aircraft)",
    "allied_casualties": "66,000 killed, 133,700 wounded, 690,000 captured",
    "axis_casualties": "Germany: 16,000 killed/missing, 30,000 wounded; USSR: 1,500 killed, 3,000 wounded",
    "image": "assets/images/invasion_of_poland_1783712194487.png",
    "chapters": [
        {
            "title": "Strategic Context & Geopolitical Buildup",
            "content": [
                "The invasion of Poland was the calculated culmination of Adolf Hitler's long-standing diplomatic and territorial campaign in Eastern Europe. Following the annexations of Austria (the Anschluss) and Czechoslovakia's Sudetenland, Hitler sought to resolve the issue of the 'Polish Corridor'—a strip of land that partitioned East Prussia from the rest of Germany—and reclaim the Free City of Danzig, which was under Polish customs control. Poland, fearing a fate similar to Czechoslovakia, steadfastly refused German diplomatic demands.",
                "The European geopolitical dynamic shifted fundamentally on August 23, 1939, when Nazi Germany and the Soviet Union signed the Molotov-Ribbentrop Pact. This non-aggression treaty shocked the Western democracies. More importantly, it contained a secret protocol that partitioned Eastern Europe into spheres of influence. Poland was divided along the Narew, Vistula, and San rivers. This pact neutralized the threat of a Soviet intervention, allowing Hitler to initiate military planning without fearing a two-front war, while guaranteeing Stalin a significant territorial buffer and time to prepare for an eventual clash."
            ]
        },
        {
            "title": "Military Doctrines & War Plans",
            "content": [
                "The German war plan, codenamed Fall Weiss (Case White), was developed by the Oberkommando der Wehrmacht (OKW). It envisioned a rapid, concentric invasion designed to envelop the Polish armies west of the Vistula River before they could fully mobilize. The plan relied on the coordinated use of armored columns, motorized infantry, and tactical air support to penetrate deep into Polish territory, disrupting logistics, communications, and command infrastructure.",
                "Conversely, the Polish defensive plan, Plan Zachód (Plan West), was deeply flawed. Political pressures forced the Polish High Command to deploy their armies along the lengthy German-Polish border to defend key industrial and agricultural regions. This wide dispersal left them highly vulnerable to encirclement. Furthermore, the Polish forces relied heavily on infantry and horse cavalry, which, although highly motivated and skilled, lacked the mobility and heavy armor required to counter the rapid German advances."
            ]
        },
        {
            "title": "Weapons, Technology, and Logistics",
            "content": [
                "The Polish Campaign showcased the first combat application of the Wehrmacht's combined-arms doctrine, later popularized by Western observers as Blitzkrieg (Lightning War). The German Panzer divisions, equipped with Panzer I, II, III, and IV tanks, bypassed defensive strongpoints to execute deep encirclements. The Luftwaffe played a critical role, using Ju 87 Stuka dive-bombers to perform close air support and precision attacks on Polish infrastructure.",
                {
                    "type": "sidebar",
                    "title": "Weapons Profile: The Ju 87 'Stuka'",
                    "text": "The Junkers Ju 87, or Stuka, became a psychological symbol of German air power. Equipped with wind-driven sirens called 'Jericho Trumpets', it emitted a terrifying wailing shriek when diving, deliberately designed to demoralize enemy ground troops and civilian refugees."
                },
                "Poland's military technology was outdated but not completely obsolete. They possessed the modern 7TP light tank and the highly effective Wz. 35 anti-tank rifle, which could penetrate German light armor. However, their air force, consisting largely of PZL P.11 fighters, was hopelessly outnumbered and outclassed by the faster German Messerschmitt Bf 109s, although Polish pilots fought with extreme tenacity."
            ]
        },
        {
            "title": "Opening Moves & Initial Clash",
            "content": [
                "To justify the invasion, the SS staged several border incidents, most notably the Gleiwitz incident on August 31, 1939. SS operatives dressed in Polish uniforms seized a German radio station in Gleiwitz and broadcasted an anti-German message. Concentration camp prisoners were killed and left at the scene to serve as 'evidence' of Polish aggression.",
                "On September 1, 1939, at 4:45 AM, the German pre-dreadnought battleship Schleswig-Holstein opened fire on the Polish military depot at Westerplatte in Danzig, signaling the official start of World War II. Simultaneously, the Luftwaffe launched massive bombing raids across Poland, targeting airfields, communication nodes, and cities. Panzer units plunged across the border, quickly slicing through the thin Polish defenses and starting the encirclement of Polish armies in the border regions."
            ]
        },
        {
            "title": "The Combat Narrative & Critical Phases",
            "content": [
                "The invasion unfolded with terrifying speed. Within the first week, German Army Group North under Fedor von Bock and Army Group South under Gerd von Rundstedt had broken through the Polish lines. By September 8, German armored spearheads reached the outskirts of Warsaw, initiating the Siege of Warsaw.",
                "The Polish attempted a major counteroffensive along the Bzura River starting September 9. Commanded by General Tadeusz Kutrzeba, the Battle of the Bzura was the largest engagement of the campaign. The Poles initially surprised the German flank, but the Luftwaffe quickly established absolute air supremacy, launching relentless bombing runs that destroyed Polish communication lines and forced them into a fighting retreat toward Warsaw."
            ]
        },
        {
            "title": "The Soviet Invasion",
            "content": [
                "On September 17, 1939, the Soviet Union launched its own invasion of Poland from the east, deploying over 460,000 Red Army troops. The Soviet government justified this action by claiming that the Polish state had ceased to exist and that they were acting to protect ethnic Ukrainian and Belarusian populations. In reality, they were executing the secret terms of the Molotov-Ribbentrop Pact.",
                "This second front shattered any remaining Polish hopes of establishing a defensive line in the Romanian Bridgehead region. Polish Commander-in-Chief Edward Rydz-Śmigły ordered his troops to withdraw to neutral Romania and Hungary to avoid capture. The Polish armies, caught between two massive invaders, were systematically crushed in detail, though Warsaw resisted courageously until September 27."
            ]
        },
        {
            "title": "Pivot Points & Key Tactical Decisions",
            "content": [
                "A key tactical decision was the Polish deployment along the borders rather than withdrawing behind the natural defensive barriers of the Vistula and San rivers. This political decision, meant to show resolve and defend vital territories, allowed the Wehrmacht to execute its planned envelopment strategy.",
                "Another critical point was the Allied failure to act. Although Great Britain and France declared war on Germany on September 3, they launched no major military offensives in the West. This period, known as the 'Saar Offensive' or the 'Phoney War', allowed the German High Command to focus their entire military weight on crushing Poland without worrying about a Western Front."
            ]
        },
        {
            "title": "The Soldier's Ordeal & Civilian Impact",
            "content": [
                "For the Polish soldier, the campaign was a desperate struggle against overwhelming odds, marked by courage, confusion, and supply failures. Polish cavalry units fought bravely, contrary to later German propaganda myths that claimed they charged tanks with lances. In reality, they functioned as mobile infantry, using anti-tank rifles and light artillery to inflict casualties on German mechanized columns.",
                "The civilian population suffered tremendously. The Luftwaffe targeted civilian refugees fleeing along roads to clog transportation lines and induce panic. The Siege of Warsaw saw indiscriminate shelling and bombing of residential areas. Furthermore, the German invasion saw the immediate deployment of Einsatzgruppen (SS death squads) behind the front lines to systematically identify and execute Polish elites, intellectuals, priests, and Jews, foreshadowing the atrocities of the Holocaust."
            ]
        },
        {
            "title": "The Aftermath & Immediate Consequences",
            "content": [
                "On October 6, 1939, the last organized Polish resistance surrendered at the Battle of Kock. Poland was divided between Nazi Germany and the Soviet Union. Germany annexed western Poland directly into the Reich and placed the central region under the administration of the General Government, headed by Hans Frank. The Soviet Union annexed eastern Poland, incorporating it into the Ukrainian and Belarusian Soviet Republics.",
                "Both occupying powers initiated brutal campaigns of pacification, forced labor, and mass executions. The Soviets executed over 22,000 Polish officers, policemen, and intellectuals in the Katyn massacre in 1940. The Polish government-in-exile was established, first in France and later in London, coordinating a massive underground resistance network (the Home Army) that fought the occupiers throughout the war."
            ]
        },
        {
            "title": "Historical Legacy & Long-term Impact",
            "content": [
                "The invasion of Poland marked the end of the policy of appeasement and plunged the world into a six-year global conflict. It proved the effectiveness of mechanized combined-arms warfare, forcing all major military powers to reform their doctrines and acquire modern armor and aircraft.",
                "The campaign also set a precedent for the war of annihilation in Eastern Europe, where civilian populations were treated as subhumans and subjected to systematic extermination. The geographical positioning of Poland, under Nazi control, made it the central hub for the construction of major death camps, including Auschwitz-Birkenau, Treblinka, and Sobibor, where millions of Jews and others were murdered."
            ]
        },
        {
            "title": "Archives, Primary Sources & Further Reading",
            "content": [
                "To explore this campaign further, consult the following primary and secondary resources:",
                {
                    "type": "sources",
                    "items": [
                        {
                            "title": "The National WWII Museum - Invasion of Poland",
                            "url": "https://www.nationalww2museum.org/war/articles/invasion-poland-september-1939",
                            "desc": "A comprehensive analysis of the diplomatic build-up, military tactics, and human cost of the 1939 campaign."
                        },
                        {
                            "title": "Imperial War Museums - How Europe Went to War in 1939",
                            "url": "https://www.iwm.org.uk/history/how-europe-went-to-war-in-1939",
                            "desc": "An digital collection featuring photographs, audio logs, and historical summaries from the IWM archives."
                        },
                        {
                            "title": "Museum of the Second World War in Gdańsk",
                            "url": "https://muzeum1939.pl/en",
                            "desc": "The official museum at Westerplatte containing primary source documents, operational maps, and diaries of the Polish defense."
                        }
                    ]
                }
            ]
        }
    ]
}

# 2. Battle of Britain
britain_data = {
    "title": "Battle of Britain",
    "date": "July 10, 1940 - October 31, 1940",
    "location": "United Kingdom Airspace",
    "result": "Decisive British victory",
    "outcome": "German invasion of Britain (Operation Sea Lion) indefinitely postponed; first major check to Nazi expansion.",
    "allied_commanders": "Hugh Dowding, Keith Park",
    "axis_commanders": "Hermann Göring, Albert Kesselring, Hugo Sperrle",
    "allied_forces": "Approx. 1,960 serviceable aircraft (RAF Fighter Command)",
    "axis_forces": "Approx. 2,500 serviceable aircraft (Luftwaffe)",
    "allied_casualties": "544 pilots killed, 1,542 aircraft destroyed, 40,000+ civilians killed (during the Blitz)",
    "axis_casualties": "2,698 aircrew killed/captured, 1,887 aircraft destroyed",
    "image": "assets/images/battle_of_britain_1783712202242.png",
    "chapters": [
        {
            "title": "Strategic Context & Geopolitical Buildup",
            "content": [
                "By the summer of 1940, the Allied cause lay in ruins. Following the rapid collapse of France and the evacuation at Dunkirk, Great Britain stood alone against a triumphant Nazi Germany, which had conquered most of Western Europe. Adolf Hitler, hoping to secure a negotiated peace that would allow him to focus on his long-term goal of invading the Soviet Union, offered peace terms. British Prime Minister Winston Churchill defiantly refused, proclaiming that Britain would fight on to the end.",
                "Consequently, Hitler issued Directive No. 16, ordering preparations for Operation Sea Lion—an amphibious invasion of southern England. However, the German army and navy recognized that crossing the English Channel was impossible without first defeating the Royal Navy, which in turn required absolute air superiority to prevent British bombers and fighters from decimating the invasion fleet. The Luftwaffe, under Reichsmarschall Hermann Göring, was tasked with destroying the Royal Air Force (RAF)."
            ]
        },
        {
            "title": "Military Doctrines & War Plans",
            "content": [
                "The Luftwaffe's plan, Adlerangriff (Eagle Attack), aimed to systematically destroy RAF Fighter Command. Göring planned to target coastal shipping convoys to draw out British fighters, then attack radar stations and airfields to crush Fighter Command on the ground and in the air. The Luftwaffe relied on its medium bombers (Heinkel He 111, Dornier Do 17) and Stuka dive-bombers, escorted by Bf 109 fighters.",
                "The RAF, led by Air Chief Marshal Hugh Dowding, developed a defensive plan based on preservation. Dowding recognized that the RAF was outnumbered and could not win a war of attrition in open combat. He implemented the 'Dowding System'—the world's first integrated air defense network. This system combined radar tracking, ground observers, and telephone communications to direct Spitfire and Hurricane squadrons to intercept German bombers with maximum efficiency."
            ]
        },
        {
            "title": "Weapons, Technology, and Logistics",
            "content": [
                "The battle pitted two of the war's premier fighter aircraft against each other: the British Supermarine Spitfire and the German Messerschmitt Bf 109E. The Spitfire was highly maneuverable and loved by its pilots, while the Bf 109 was faster in climbs and dives and had a heavier fuel injection system that prevented engine cutouts during negative-G maneuvers.",
                {
                    "type": "sidebar",
                    "title": "Weapons Profile: The Hawker Hurricane",
                    "text": "While the Spitfire gained the glory, the rugged Hawker Hurricane was the workhorse of the RAF. It flew more sorties and accounted for over 60% of all Luftwaffe losses during the battle, targeting the slower German bombers while Spitfires engaged the escorting Bf 109 fighters."
                },
                "The most critical technological asset was Chain Home—a network of early warning radar stations along the British coast. It allowed the RAF to detect incoming German raids, estimate their size, altitude, and heading, and scramble fighters to intercept them, avoiding the need for exhausting and wasteful patrol flights."
            ]
        },
        {
            "title": "Opening Moves & Initial Clash",
            "content": [
                "The battle began in July 1940 with the Kanalkampf (Channel Battles). The Luftwaffe attacked British merchant convoys in the English Channel to test British defenses, secure the straits, and lure Fighter Command into battle. Although the RAF lost shipping, they limited fighter losses, refusing to commit large forces.",
                "On August 13, 1940, the Luftwaffe launched Adlerangriff, initiating a series of massive air raids against RAF airfields, radar stations, and communication hubs. A major clash occurred on August 15 ('The Greatest Day'), when the Luftwaffe launched attacks from Norway and Denmark, believing northern defenses were weak. The RAF easily intercepted and decimated these unescorted formations, proving that Britain's air defenses were intact."
            ]
        },
        {
            "title": "The Critical Phase: Airfield Bombings",
            "content": [
                "Between late August and early September, the battle reached its critical phase. Göring focused the Luftwaffe's weight on 11 Group airfields in southeastern England, commanded by Keith Park. Airfields like Biggin Hill and Kenley were repeatedly bombed, destroying sector stations, operations rooms, and aircraft on the ground.",
                "Fighter Command was stretched to its absolute breaking point. The RAF was losing pilots faster than they could be trained, and ground crews worked under constant bombardment to repair runways and keep fighters flying. Had the Luftwaffe continued this focused campaign, Fighter Command might have collapsed, leaving the Channel vulnerable to invasion."
            ]
        },
        {
            "title": "The Strategic Shift: The Blitz",
            "content": [
                "On August 24, a lost German bomber formation accidentally dropped bombs on residential areas of London. Churchill ordered retaliatory RAF raids on Berlin. Although the physical damage was minimal, it outraged Hitler, who ordered Göring to shift targets from RAF airfields to London and other major British cities. This began 'The Blitz'.",
                "On September 7, a massive force of nearly 1,000 German aircraft bombed London, marking the start of the city's ordeal. While devastating for civilians, this strategic blunder saved Fighter Command. It gave the RAF the crucial breathing room to repair airfields, rest pilots, and replenish aircraft reserves, while forcing the Luftwaffe to fly predictable routes over heavily defended areas."
            ]
        },
        {
            "title": "Battle of Britain Day & Victory",
            "content": [
                "The climax of the battle occurred on September 15, 1940, now celebrated as 'Battle of Britain Day'. Göring launched two massive waves of bombers and fighters against London, expecting to crush a depleted RAF. Instead, Keith Park scrambled every available squadron, intercepting the German formations before they could reach their targets.",
                "The RAF shot down 56 German aircraft while losing 29. The defeat proved to the German High Command that the RAF was far from defeated. Two days later, Hitler postponed Operation Sea Lion indefinitely. The Luftwaffe shifted to night bombing campaigns to avoid daytime fighter interceptions, acknowledging that daytime air superiority was unattainable."
            ]
        },
        {
            "title": "The Soldier's Ordeal & Civilian Impact",
            "content": [
                "The RAF pilots, a diverse group including Britons, Poles, Czechs, New Zealanders, Canadians, and Americans, endured intense physical and mental exhaustion. They flew up to five sorties a day, living in constant state of readiness. Winston Churchill immortalized them in his August 20 address to Parliament: 'Never in the field of human conflict was so much owed by so many to so few.'",
                "British civilians in London and other industrial centers faced the horrors of the Blitz. For 57 consecutive nights, London was bombed. Families slept in Tube stations, basement shelters, or Anderson shelters in their gardens. Over 40,000 civilians died, and over a million homes were destroyed, but the bombing failed to break British morale, instead strengthening national resolve."
            ]
        },
        {
            "title": "The Aftermath & Strategic Consequences",
            "content": [
                "The Battle of Britain was Germany's first major defeat of the war. It preserved Great Britain as an independent combatant and a base for future Allied operations. It kept the British Empire in the war and allowed the United States to use the British Isles as a staging ground for the buildup of forces that would lead to D-Day.",
                "For Hitler, the failure meant that when he launched the invasion of the Soviet Union in June 1941, he was forced to fight a two-front war, with the RAF and Royal Navy constantly threating his western flank and tying down valuable Luftwaffe divisions."
            ]
        },
        {
            "title": "Historical Legacy & Long-term Impact",
            "content": [
                "The battle demonstrated the strategic importance of air power and the critical role of radar and command systems in modern warfare. It created a powerful national myth of British resilience ('the Blitz spirit') and established Fighter Command pilots as symbols of heroism.",
                "The contribution of foreign pilots, particularly the Polish 303 Squadron (which achieved the highest kill rate of any squadron in the battle), highlighted the international coalition that defended Britain during its darkest hour."
            ]
        },
        {
            "title": "Archives, Primary Sources & Further Reading",
            "content": [
                "For more details and original archival records on the Battle of Britain:",
                {
                    "type": "sources",
                    "items": [
                        {
                            "title": "Imperial War Museums - 8 Things to Know About the Battle of Britain",
                            "url": "https://www.iwm.org.uk/history/8-things-you-need-to-know-about-the-battle-of-britain",
                            "desc": "A detailed digital exhibit featuring personal diaries, aircraft statistics, and historical accounts from IWM."
                        },
                        {
                            "title": "The Battle of Britain Memorial Official Site",
                            "url": "https://www.battleofbritainmemorial.org/",
                            "desc": "The official site of the national memorial to the pilots who fought in the Battle of Britain."
                        },
                        {
                            "title": "The National Archives (UK) - Battle of Britain Files",
                            "url": "https://www.nationalarchives.gov.uk/",
                            "desc": "Official governmental reports, Dowding's dispatches, and intelligence maps from 1940."
                        }
                    ]
                }
            ]
        }
    ]
}

# 3. Operation Barbarossa
barbarossa_data = {
    "title": "Operation Barbarossa",
    "date": "June 22, 1941 - December 5, 1941",
    "location": "Eastern Europe",
    "result": "Strategic Soviet victory",
    "outcome": "Failure of Blitzkrieg to knock out the Soviet Union; Germany forced into an unsustainable war of attrition on two fronts.",
    "allied_commanders": "Joseph Stalin, Georgy Zhukov, Semyon Budyonny, Semyon Timoshenko",
    "axis_commanders": "Adolf Hitler, Franz Halder, Gerd von Rundstedt, Fedor von Bock, Wilhelm Ritter von Leeb",
    "allied_forces": "Soviet Union: 2.7 million active front-line soldiers, over 20,000 tanks, 8,000 aircraft",
    "axis_forces": "Axis: 3.8 million soldiers (3.2 million Germans), 3,300 tanks, 2,700 aircraft, 7,000 artillery pieces",
    "allied_casualties": "Over 560,000 killed, 1.3 million wounded, 2.3 million captured/missing",
    "axis_casualties": "Approx. 250,000 killed, 500,000 wounded, 25,000 missing",
    "image": "assets/images/operation_barbarossa_1783712208922.png",
    "chapters": [
        {
            "title": "Strategic Context & Geopolitical Buildup",
            "content": [
                "Operation Barbarossa was the ideological and strategic center of Adolf Hitler's foreign policy. As outlined in Mein Kampf, Hitler believed that Germany's survival depended on the acquisition of Lebensraum (living space) in Eastern Europe and the complete destruction of 'Judeo-Bolshevism'. The agricultural wealth of Ukraine and the vast oil reserves of the Caucasus were to feed and fuel the Third Reich, making it self-sufficient and immune to naval blockades.",
                "Stalin, despite warnings from his own intelligence networks and Western leaders, believed that Hitler would not attack until Britain was defeated. The Soviet military was in a state of transition; Stalin's purges of the late 1930s had executed or imprisoned over 30,000 officers, including Marshal Mikhail Tukhachevsky, leaving the Red Army leadership inexperienced and terrified of taking initiative."
            ]
        },
        {
            "title": "Military Doctrines & War Plans",
            "content": [
                "The German plan, finalized in December 1940 under Directive No. 21, envisioned a rapid invasion along three main axes: Army Group North toward Leningrad, Army Group Center toward Moscow, and Army Group South into Ukraine. The goal was to destroy the bulk of the Red Army west of the Dnieper and Dvina rivers, preventing their retreat into the vast Russian interior, and reach the Archangel-Astrakhan (A-A) line within four months.",
                "The Soviet defensive plan relied on forward defense. Stalin insisted on holding every inch of territory, deploying massive armies close to the border. This deployment played directly into the German strategy of encirclement, as it prevented Soviet forces from executing a flexible retreat or preparing defensive lines in depth."
            ]
        },
        {
            "title": "Weapons, Technology, and Logistics",
            "content": [
                "The German forces deployed the Panzer III and IV tanks, supported by motorized infantry and the Luftwaffe. However, the Wehrmacht was not fully mechanized; they relied on over 600,000 horses for logistics and transport, which struggled to keep pace with the rapid tank spearheads.",
                {
                    "type": "sidebar",
                    "title": "Weapons Profile: The T-34 Tank",
                    "text": "The German invaders were shocked by the appearance of the Soviet T-34 medium tank. With its sloped armor, wide tracks that moved easily over mud and snow, and powerful 76.2mm gun, it was superior to any German tank in 1941, forcing Germany to develop the Tiger and Panther tanks."
                },
                "The Soviet Union possessed vast quantities of military equipment, including the KV-1 heavy tank and the Katyusha rocket launcher. However, most units lacked radios, spare parts, and adequate ammunition, and poor maintenance meant that a large percentage of Soviet armor broke down before reaching combat."
            ]
        },
        {
            "title": "Opening Moves & Initial Clash",
            "content": [
                "At 3:15 AM on June 22, 1941, the Axis powers launched the invasion along an 1,800-mile front, caught the Red Army completely by surprise. The Luftwaffe struck over 60 Soviet airfields, destroying over 1,200 aircraft on the first day, mostly on the ground, and establishing absolute air superiority.",
                "German armored spearheads under generals like Heinz Guderian and Hermann Hoth bypassed Soviet border units, plunging deep into the rear. Within days, they executed massive encirclements at Bialystok-Minsk, capturing over 300,000 Soviet soldiers and destroying entire armies, while Stalin remained in a state of shock, unable to coordinate a coherent response."
            ]
        },
        {
            "title": "The Combat Narrative & Critical Phases",
            "content": [
                "During July and August, the German armies advanced rapidly. Army Group North advanced through the Baltic states, reaching the outskirts of Leningrad by early September and initiating the Siege of Leningrad. Army Group South faced stiffer resistance but captured Kiev in September, resulting in the encirclement and capture of over 650,000 Soviet troops.",
                "However, the advance began to slow. The distances were immense, and the logistics network was failing. The Russian rail gauge differed from the European standard, requiring time-consuming transfers of supplies. Furthermore, partisan units began to harass German supply lines in the forests of Belarus and western Russia."
            ]
        },
        {
            "title": "The Battle of Moscow: Operation Typhoon",
            "content": [
                "In October 1941, Hitler launched Operation Typhoon—the final offensive to capture Moscow. The Germans initially won another massive double-encirclement at Vyazma and Bryansk, capturing another 600,000 soldiers. The Soviet government evacuated to Kuibyshev, and panic gripped the capital.",
                "Stalin remained in Moscow and appointed Marshal Georgy Zhukov to command the defenses. Zhukov mobilized civilians to dig anti-tank ditches and brought in veteran Siberian divisions from the Far East, after intelligence confirmed that Japan would not attack the Soviet Union. As the autumn rains (the Rasputitsa) turned the unpaved roads into deep mud, the German mechanized units ground to a halt."
            ]
        },
        {
            "title": "The Winter Counteroffensive",
            "content": [
                "By late November, temperatures dropped, freezing the mud and allowing the Germans to resume their advance. Armored patrols reached the suburbs of Khimki, just 12 miles from the Kremlin. However, the Wehrmacht was exhausted, lacking winter gear, anti-freeze, and basic supplies, while their vehicles failed to start in the -30°C cold.",
                "On December 5, 1941, Zhukov launched a massive counteroffensive, utilizing fresh Siberian troops equipped for winter warfare. The surprised and freezing Germans were thrown back up to 150 miles from Moscow. This was the first major retreat the Wehrmacht had suffered in the war, ending the myth of German invincibility."
            ]
        },
        {
            "title": "The Soldier's Ordeal & Civilian Impact",
            "content": [
                "The Eastern Front became a conflict of unprecedented brutality. The German OKW issued the Commissar Order, which instructed troops to execute captured Soviet political commissars immediately, violating the Geneva Convention. Over three million Soviet POWs died of starvation, exposure, or execution in German camps during 1941-1942.",
                "Behind the front lines, Einsatzgruppen followed the Wehrmacht, executing Jews, Roma, and communist officials. The Babi Yar massacre in Kiev saw the execution of over 33,000 Jews in just two days. The Soviet population suffered from scorched-earth policies; Stalin ordered the destruction of all crops, livestock, and infrastructure that could be used by the invaders, leaving millions of civilians to face starvation."
            ]
        },
        {
            "title": "The Aftermath & Immediate Consequences",
            "content": [
                "Operation Barbarossa failed to achieve its goals. The Red Army was not destroyed, Moscow did not fall, and the A-A line was not reached. Germany found itself trapped in a long war of attrition against a state with superior demographic reserves and an industrial base that had been relocated east of the Ural Mountains, out of range of German bombers.",
                "The failure of the offensive forced Germany to mobilize its economy for total war. It also cemented the Alliance between the Soviet Union, Great Britain, and the United States, which began shipping vital supplies to the USSR via the Arctic convoys and the Persian Corridor (Lend-Lease)."
            ]
        },
        {
            "title": "Historical Legacy & Long-term Impact",
            "content": [
                "Barbarossa was the opening act of the Eastern Front, which consumed roughly 80% of all German casualties during World War II. The campaign's failure marked the strategic turning point of the European war, proving that Germany could not win a prolonged conflict against the combined industrial might of the Allies.",
                "In Soviet and Russian history, this conflict became known as the Great Patriotic War, serving as a defining historical narrative of sacrifice, resilience, and victory, though at the cost of over 27 million Soviet lives."
            ]
        },
        {
            "title": "Archives, Primary Sources & Further Reading",
            "content": [
                "To explore this campaign further, consult the following resources:",
                {
                    "type": "sources",
                    "items": [
                        {
                            "title": "The National WWII Museum - Operation Barbarossa",
                            "url": "https://www.nationalww2museum.org/war/articles/operation-barbarossa",
                            "desc": "An in-depth article analyzing the planning errors, tactical execution, and strategic impact of the invasion."
                        },
                        {
                            "title": "Britannica - Operation Barbarossa History",
                            "url": "https://www.britannica.com/event/Operation-Barbarossa",
                            "desc": "A scholarly summary of the campaign, featuring troop maps, timeline data, and commander summaries."
                        },
                        {
                            "title": "Yale Law School - Avalon Project WWII Documents",
                            "url": "https://avalon.law.yale.edu/subject_menus/wwii.asp",
                            "desc": "An authoritative archive of primary source documents, declarations of war, and diplomatic logs."
                        }
                    ]
                }
            ]
        }
    ]
}

# 4. Attack on Pearl Harbor
pearl_harbor_data = {
    "title": "Attack on Pearl Harbor",
    "date": "December 7, 1941",
    "location": "Pearl Harbor, Hawaii, US",
    "result": "Major Japanese tactical victory",
    "outcome": "United States formal entry into World War II; declarations of war by Germany and Italy on the US.",
    "allied_commanders": "Husband E. Kimmel, Walter C. Short, Franklin D. Roosevelt",
    "axis_commanders": "Isoroku Yamamoto, Chūichi Nagumo, Mitsuo Fuchida",
    "allied_forces": "US Pacific Fleet: 8 battleships, 8 cruisers, 30 destroyers, 4 submarines, 390 aircraft",
    "axis_forces": "Imperial Japanese Navy: 6 aircraft carriers, 2 battleships, 3 cruisers, 9 destroyers, 353 aircraft",
    "allied_casualties": "2,403 killed, 1,178 wounded, 4 battleships sunk, 4 battleships damaged, 188 aircraft destroyed",
    "axis_casualties": "64 killed, 29 aircraft destroyed, 5 midget submarines sunk, 1 captured",
    "image": "assets/images/pearl_harbor_1783712216007.png",
    "chapters": [
        {
            "title": "Strategic Context & Geopolitical Buildup",
            "content": [
                "Tensions between the United States and the Empire of Japan had been mounting for decades over control of East Asia and the Pacific. Following Japan's invasion of China in 1937 and its subsequent occupation of French Indochina in 1940, the United States, along with Great Britain and the Netherlands, imposed a total embargo on oil and scrap metal exports to Japan. This oil embargo threatened to paralyze the Japanese war machine and economy within two years, as Japan imported over 80% of its oil from the US.",
                "Faced with the choice of yielding to American demands to withdraw from China and Indochina, or seizing the resource-rich European colonies in Southeast Asia, the Japanese military leadership chose war. Admiral Isoroku Yamamoto, commander of the Combined Fleet, conceived a surprise strike on the US Pacific Fleet at Pearl Harbor. The goal was to destroy the American battleships and carriers, preventing them from interfering with Japan's planned expansion into the Dutch East Indies and Malaya."
            ]
        },
        {
            "title": "Military Doctrines & War Plans",
            "content": [
                "The Japanese plan relied on total surprise and the concentration of carrier-based aviation. Six fleet carriers (the Kido Butai) under Vice Admiral Chūichi Nagumo were to sail in secret across the North Pacific, maintaining strict radio silence. The air crews had trained for months, developing specialized shallow-water torpedoes equipped with wooden fins to prevent them from sinking into the mud of Pearl Harbor.",
                "The US military, conversely, was unprepared for an air attack. Intelligence believed that any Japanese strike would target the Philippines or Malaya. General Walter Short, commander of army defenses in Hawaii, feared sabotage and ordered all aircraft to be parked wingtip-to-wingtip on the runways to make them easier to guard, which unintentionally made them perfect targets for bombers."
            ]
        },
        {
            "title": "Weapons, Technology, and Logistics",
            "content": [
                "The Japanese strike force deployed the Mitsubishi A6M Zero fighter, the Nakajima B5N 'Kate' torpedo bomber, and the Aichi D3A 'Val' dive-bomber. The Zero was highly agile, outclassing any American fighter in Hawaii, while the Kate was highly effective when carrying shallow-water torpedoes or heavy armor-piercing bombs made from converted battleship shells.",
                {
                    "type": "sidebar",
                    "title": "Technology Profile: Wooden Fin Torpedoes",
                    "text": "Pearl Harbor's average depth was only 40 feet. Standard torpedoes required at least 75 feet to recover from their initial dive. The Japanese fitted their Type 91 torpedoes with wooden tail fins that broke off upon impact with the water, stabilizing the weapon and keeping it near the surface."
                },
                "The US defenses possessed SCR-270 radar stations. On the morning of the attack, two operators at the Opana Radar Site detected a large echo. However, the information center officer assumed it was a scheduled flight of American B-17 bombers from California and told the operators not to worry."
            ]
        },
        {
            "title": "Opening Moves & Initial Clash",
            "content": [
                "The Kido Butai reached its launching point 230 miles north of Oahu at dawn on December 7, 1941. At 6:00 AM, the first wave of 183 aircraft took off, led by Commander Mitsuo Fuchida. Simultaneously, Japanese midget submarines attempted to infiltrate the harbor; one was detected and sunk by the destroyer USS Ward, which fired the first American shots of the war.",
                "At 7:49 AM, Fuchida looked down at the peaceful base and radioed the code 'Tora! Tora! Tora!' (Tiger! Tiger! Tiger!), signaling that complete surprise had been achieved. Moments later, the first bombs began to fall on the airfields at Wheeler, Hickam, and Kaneohe, destroying dozens of parked American aircraft before they could take off."
            ]
        },
        {
            "title": "The Battle: Two Waves of Terror",
            "content": [
                "The attack unfolded in two waves. The first wave targeted 'Battleship Row' along Ford Island. The USS Arizona was struck by an armor-piercing bomb that penetrated its forward magazine, causing a massive explosion that sank the ship and killed 1,177 crewmen. The USS Oklahoma was hit by multiple torpedoes, capsizing and trapping hundreds of men inside.",
                "The second wave of 170 aircraft arrived at 8:54 AM, targeting dry docks and other ships. American soldiers and sailors fought back bravely with anti-aircraft guns, machine guns, and rifles. A few US fighters, notably flown by Lieutenants George Welch and Kenneth Taylor, managed to take off and shot down several Japanese planes, but the damage was already done."
            ]
        },
        {
            "title": "The Strategic Decision: No Third Wave",
            "content": [
                "By 10:00 AM, the Japanese aircraft returned to their carriers. Nagumo decided not to launch a third wave, despite recommendations from junior officers. He feared American land-based bombers and did not know the locations of the US aircraft carriers, which were out of port on maneuvers.",
                "This decision had major strategic consequences. The attack failed to destroy the base's massive oil storage tanks, repair shops, submarine pens, and dry docks. Had these facilities been destroyed, the US Navy would have been forced to withdraw its Pacific operations to San Diego, delaying their counteroffensive by years."
            ]
        },
        {
            "title": "Pivot Points & Key Tactical Decisions",
            "content": [
                "The most critical factor was the absence of the US carriers USS Enterprise, USS Lexington, and USS Saratoga. These ships escaped damage, preserving the core offensive power of the Pacific Fleet and allowing Nimitz to fight the carrier battles of Coral Sea and Midway in 1942.",
                "Another factor was the failure of the Japanese to issue a formal declaration of war before the attack. The message from Tokyo was delayed by translation issues, and was delivered to Secretary of State Cordell Hull after the bombs had already fallen. This delay enraged the American public, uniting them in a state of absolute resolve."
            ]
        },
        {
            "title": "The Soldier's Ordeal & Civilian Impact",
            "content": [
                "For the men at Pearl Harbor, the morning was a chaotic nightmare of explosions, burning oil, and black smoke. Sailors jumped into water covered in burning fuel to escape their sinking ships. Medics worked under fire to treat horrific burn injuries. The heroism of individuals like Doris Miller, a Mess Attendant who manned an anti-aircraft gun on the USS West Virginia and received the Navy Cross, became a symbol of national unity.",
                "Civilians in Honolulu were caught in the crossfire. Scattered anti-aircraft shells fell in residential areas, killing 68 civilians. The US government immediately declared martial law in Hawaii, suspending civil liberties, imposing blackouts, and placing the entire territory under military control, which lasted for the duration of the war."
            ]
        },
        {
            "title": "The Aftermath & Immediate Consequences",
            "content": [
                "On December 8, 1941, President Roosevelt addressed a joint session of Congress, calling December 7 'a date which will live in infamy' and requesting a declaration of war against Japan, which was approved with only one dissenting vote. On December 11, Adolf Hitler and Benito Mussolini declared war on the United States, officially bringing America into the European conflict.",
                "The attack succeeded in temporarily neutralizing the US battleship fleet, but it failed to achieve Japan's goal of breaking American resolve. Instead, it galvanized the industrial, economic, and military power of the United States, transitioning it into the 'Arsenal of Democracy' and sealing the fate of the Axis powers."
            ]
        },
        {
            "title": "Historical Legacy & Long-term Impact",
            "content": [
                "Pearl Harbor remains a symbol of military surprise, intelligence failure, and national resilience. It led to the decline of the battleship and the rise of the aircraft carrier as the primary weapon of naval warfare.",
                "The attack also led to the forced internment of over 110,000 Japanese-Americans living on the West Coast under Executive Order 9066, a decision later recognized as a major violation of civil liberties and fueled by racial prejudice and wartime hysteria."
            ]
        },
        {
            "title": "Archives, Primary Sources & Further Reading",
            "content": [
                "For original documents, logs, and research files on Pearl Harbor:",
                {
                    "type": "sources",
                    "items": [
                        {
                            "title": "Library of Congress - World War II Documents",
                            "url": "https://www.loc.gov/collections/world-war-ii-original-documents/about-this-collection/",
                            "desc": "Primary source collection featuring Roosevelt's Infamy draft speech, radio transcripts, and naval logs."
                        },
                        {
                            "title": "History Channel - Attack on Pearl Harbor",
                            "url": "https://www.history.com/topics/world-war-ii/pearl-harbor",
                            "desc": "A multi-media portal containing documentary footage, interactive maps, and historical articles."
                        },
                        {
                            "title": "USS Arizona Memorial Official Site",
                            "url": "https://www.nps.gov/valr/index.htm",
                            "desc": "National Park Service page documenting the casualties, preservation efforts, and history of the USS Arizona."
                        }
                    ]
                }
            ]
        }
    ]
}

# 5. Battle of Midway
midway_data = {
    "title": "Battle of Midway",
    "date": "June 4-7, 1942",
    "location": "Midway Atoll, Pacific Ocean",
    "result": "Decisive American victory",
    "outcome": "Permanent damage to the Imperial Japanese Navy; the strategic initiative in the Pacific shifts to the Allies.",
    "allied_commanders": "Chester W. Nimitz, Frank Jack Fletcher, Raymond A. Spruance",
    "axis_commanders": "Isoroku Yamamoto, Nobutake Kondō, Chūichi Nagumo, Tamon Yamaguchi",
    "allied_forces": "US Navy: 3 aircraft carriers, 8 cruisers, 15 destroyers, 233 carrier aircraft, 127 land-based aircraft",
    "axis_forces": "Imperial Japanese Navy: 4 fleet aircraft carriers, 2 battleships, 12 destroyers, 248 carrier aircraft",
    "allied_casualties": "307 killed, 1 aircraft carrier (USS Yorktown) sunk, 1 destroyer sunk, 150 aircraft destroyed",
    "axis_casualties": "3,057 killed, 4 fleet aircraft carriers sunk, 1 heavy cruiser sunk, 248 aircraft destroyed",
    "image": "assets/images/battle_of_midway_1783712222034.png",
    "chapters": [
        {
            "title": "Strategic Context & The Intelligence War",
            "content": [
                "Following the success of their early offensives, the Japanese military sought to expand their defensive perimeter in the Pacific. Admiral Isoroku Yamamoto conceived a plan to lure the remaining US aircraft carriers into a decisive battle by invading the Midway Atoll, a tiny outpost northwest of Hawaii. Yamamoto believed that the US carriers, which had escaped Pearl Harbor and launched the daring Doolittle Raid on Tokyo, were the primary threat to the Japanese Empire.",
                "However, the Japanese plan was compromised by American cryptanalysts. Station HYPO in Hawaii, led by Commander Joseph Rochefort, had partially decrypted the Japanese naval code, JN-25. Rochefort's team suspected that the target 'AF' was Midway. To confirm this, they instructed the Midway base to send an unencrypted message claiming their water distillation system had broken. Shortly after, a decrypted Japanese dispatch reported that 'AF was short of water', confirming Midway as the target and allowing Admiral Chester Nimitz to plan an ambush."
            ]
        },
        {
            "title": "Military Doctrines & War Plans",
            "content": [
                "The Japanese plan was highly complex, involving multiple divisions, including a diversionary attack on the Aleutian Islands. It relied on secrecy and the assumption that the US fleet would only react after the landings at Midway had begun. The carriers under Admiral Nagumo were to launch air strikes to neutralize Midway's defenses before the arrival of the invasion fleet.",
                "The American plan was simple and direct. Nimitz concentrated his three available carriers—USS Enterprise, USS Hornet, and the carrier USS Yorktown, which had been quickly repaired in Pearl Harbor after sustaining damage at the Battle of the Coral Sea—northeast of Midway. The US forces waited in secret, using search planes to locate the Japanese fleet before they were detected."
            ]
        },
        {
            "title": "Weapons, Technology, and Logistics",
            "content": [
                "The battle showcased carrier-based aircraft technology. The Japanese Mitsubishi A6M Zero was highly agile, easily outclassing the American Grumman F4F Wildcat. However, the Wildcat was more rugged and utilized tactics like the 'Thach Weave' to counter the Zero's maneuverability.",
                {
                    "type": "sidebar",
                    "title": "Tactics Profile: The Thach Weave",
                    "text": "Developed by John Thach, this defensive maneuver involved two Wildcats flying abreast. When a Zero attacked one fighter, they crossed paths, allowing the second Wildcat to fire a head-on shot at the pursuer, neutralizing the Zero's speed advantage."
                },
                "The primary American strike weapon was the Douglas SBD Dauntless dive-bomber, which delivered heavy armor-piercing bombs in steep dives. The Japanese carriers, although fast, lacked armored flight decks and had inadequate anti-aircraft fire control systems, leaving them vulnerable to diving attacks."
            ]
        },
        {
            "title": "Opening Moves & Initial Clash",
            "content": [
                "On June 4, 1942, Nagumo launched his first wave of 108 aircraft against Midway. The strike caused heavy damage to the base but did not destroy its airfields. Nagumo prepared a second wave, arming his aircraft with bombs to strike Midway again.",
                "Simultaneously, American patrol planes located the Japanese carriers. At 7:00 AM, the US carriers began launching their aircraft. Shortly after, a Japanese search plane spotted the US fleet, reporting the presence of a carrier. Nagumo was forced to halt the rearmament, ordering his crews to switch from ground-bombs back to torpedoes to target the American ships, leaving the decks covered in fuel lines and munitions."
            ]
        },
        {
            "title": "The Turning Point: The Five Fatal Minutes",
            "content": [
                "The initial American air attacks were uncoordinated and met with disaster. Torpedo bomber squadrons from Hornet and Enterprise attacked without fighter escort, and were shot down by Zero fighters; out of 41 torpedo planes, only six returned. However, this sacrifice drew the Japanese Zero fighters down to sea level, leaving the skies above empty.",
                "At 10:22 AM, three squadrons of Douglas SBD Dauntless dive-bombers from Enterprise and Yorktown arrived simultaneously at high altitude, completely undetected. They plunged through the clouds, striking the Japanese carriers Akagi, Kaga, and Soryu as their decks were packed with fueled and armed planes. Within five minutes, all three carriers were burning out of control, reduced to smoking wrecks."
            ]
        },
        {
            "title": "The Final Carrier Engagements",
            "content": [
                "The remaining Japanese carrier, Hiryu, commanded by Rear Admiral Tamon Yamaguchi, launched a retaliatory strike that located and heavily damaged the USS Yorktown. Yorktown's crew managed to extinguish fires and restore power, but a second Japanese strike hit the carrier with torpedoes, forcing the captain to order abandon ship.",
                "At 4:00 PM, dive-bombers from Enterprise and Yorktown located Hiryu, striking it with several bombs and leaving it burning. Hiryu was scuttled the next morning. With all four Japanese carriers destroyed, Admiral Yamamoto was forced to cancel the invasion of Midway and order a general retreat, ending the battle."
            ]
        },
        {
            "title": "Pivot Points & Key Decisions",
            "content": [
                "The most critical decision was Nimitz's trust in his intelligence officers. Had he ignored Rochefort's analysis, the US fleet would have been out of position, allowing Japan to capture Midway and threaten Hawaii.",
                "Another pivot point was Nagumo's decision to rearm his planes on the flight decks. This delay, combined with the decoy attacks by the American torpedo bombers, created the perfect opportunity for the US dive-bombers to strike the Japanese carriers at their most vulnerable moment."
            ]
        },
        {
            "title": "The Soldier's Ordeal & Civilian Impact",
            "content": [
                "For the aircrews, the battle was a deadly test. Pilots flew long distances over the ocean, knowing that mechanical failure or damage meant landing in the water with little hope of rescue. The story of Ensign George Gay, the sole survivor of Torpedo Squadron 8, who floated in the water for hours watching the destruction of the Japanese fleet, highlighted the high casualty rate.",
                "Midway Atoll was populated by a few hundred US military personnel. The bombing raid on June 4 killed 11 personnel and destroyed fuel tanks and hangers. The base remained operational, serving as a critical refueling stop for search planes and submarines that hunted the retreating Japanese fleet."
            ]
        },
        {
            "title": "The Aftermath & Strategic Consequences",
            "content": [
                "The Battle of Midway was a catastrophic defeat for Japan, which lost four fleet carriers, one heavy cruiser, and over 240 aircraft. More importantly, they lost over 110 experienced pilots and hundreds of skilled aircraft mechanics, who could not be easily replaced.",
                "This victory established parity in carrier forces in the Pacific and allowed the Allies to transition from a desperate defense to a counteroffensive strategy. Just two months later, the US Marines landed on Guadalcanal, initiating the island-hopping campaign that would lead to the home islands of Japan."
            ]
        },
        {
            "title": "Historical Legacy & Long-term Impact",
            "content": [
                "Midway is celebrated as one of the most decisive naval victories in military history. It demonstrated that codebreaking, information superiority, and carrier aviation had replaced the battleship as the decisive factors in naval warfare.",
                "The battle also highlights the role of chance in war—the timing of the dive-bombers' arrival, just as the Japanese fighters were at low altitude, remains a classic example of how a few minutes can decide the fate of nations."
            ]
        },
        {
            "title": "Archives, Primary Sources & Further Reading",
            "content": [
                "To read official war reports, decrypts, and maps from the battle:",
                {
                    "type": "sources",
                    "items": [
                        {
                            "title": "The National WWII Museum - Battle of Midway",
                            "url": "https://www.nationalww2museum.org/war/articles/battle-midway",
                            "desc": "An analysis of the intelligence victory and carrier combat that turned the tide in the Pacific."
                        },
                        {
                            "title": "Naval History and Heritage Command - Midway Files",
                            "url": "https://www.history.navy.mil/browse-by-topic/wars-conflicts-and-operations/world-war-ii/1942/midway.html",
                            "desc": "Official US Navy action reports, Commander Spruance's logs, and decrypted radio traffic."
                        },
                        {
                            "title": "The Joseph Rochefort Papers - Station HYPO Archives",
                            "url": "https://www.loc.gov/",
                            "desc": "Personal diaries, notes, and code sheets detailing the decryption of the JN-25 code in 1942."
                        }
                    ]
                }
            ]
        }
    ]
}

# 6. Battle of Stalingrad
stalingrad_data = {
    "title": "Battle of Stalingrad",
    "date": "August 23, 1942 - February 2, 1943",
    "location": "Stalingrad, Soviet Union",
    "result": "Decisive Soviet victory",
    "outcome": "Destruction of the German 6th Army; Germany's offensive capability on the Eastern Front is broken.",
    "allied_commanders": "Vasily Chuikov, Georgy Zhukov, Aleksandr Vasilevsky, Konstantin Rokossovsky",
    "axis_commanders": "Friedrich Paulus, Erich von Manstein, Hermann Hoth",
    "allied_forces": "Soviet Union: Over 1.1 million front-line soldiers, 894 tanks, 1,115 aircraft (at start of offensive)",
    "axis_forces": "Axis: Approx. 1 million soldiers (including Romanian, Italian, and Hungarian divisions), 675 tanks, 1,210 aircraft",
    "allied_casualties": "478,741 killed/missing, 650,878 wounded; over 40,000 civilians killed",
    "axis_casualties": "Approx. 800,000 killed, wounded, or captured (including 110,000 Germans captured, of whom only 6,000 survived)",
    "image": "assets/images/battle_of_stalingrad_1783712239181.png",
    "chapters": [
        {
            "title": "Strategic Context & The Drive to the Volga",
            "content": [
                "By the spring of 1942, the German Wehrmacht had recovered from its defeat at Moscow. Recognizing that Germany lacked the resources to launch a general offensive along the entire Eastern Front, Hitler approved Fall Blau (Case Blue)—a campaign directed into southern Russia. The goal was to capture the oil fields of Maikop, Grozny, and Baku in the Caucasus, which would fuel the German war machine and starve the Soviet military of fuel.",
                "To protect the left flank of the advance, German Army Group B was ordered to advance to the Volga River and capture or destroy the industrial city of Stalingrad. The city was a major transport hub and bore the name of Joseph Stalin, making it an ideological prize for Hitler. As the German 6th Army under General Friedrich Paulus advanced, Hitler split his forces, ordering both the Caucasus oil drive and the capture of Stalingrad to occur simultaneously, stretching his logistics to the limit."
            ]
        },
        {
            "title": "Military Doctrines & War Plans",
            "content": [
                "The German doctrine of mobile warfare was suited for the open Russian steppe, where Panzers could envelop and destroy enemy forces. However, once the 6th Army entered the ruins of Stalingrad, this mobility was neutralized. The Germans were forced into close-quarters combat, where their tactical superiority in coordination and communications was less effective.",
                "The Soviet plan, developed by General Vasily Chuikov, commander of the 62nd Army, relied on attrition. Chuikov ordered his troops to 'hug the enemy'—to keep their front lines within hand-grenade distance of the Germans. This prevented the Luftwaffe and German artillery from bombing Soviet positions for fear of hitting their own men, forcing the Germans to fight for every building, room, and sewer."
            ]
        },
        {
            "title": "Weapons, Technology, and Logistics",
            "content": [
                "The battle was characterized by urban warfare weapons. Snipers played a major role, using Mosin-Nagant and Karabiner 98k rifles equipped with telescopic sights to terrorize enemy patrols. Submachine guns, like the Soviet PPSh-41 and the German MP 40, were favored for their high rate of fire in close quarters.",
                {
                    "type": "sidebar",
                    "title": "Weapons Profile: The PPSh-41 Submachine Gun",
                    "text": "The PPSh-41, with its 71-round drum magazine and high rate of fire, was the ultimate close-quarters weapon of the battle. It was so reliable and effective in dusty, rubble-strewn buildings that German soldiers frequently used captured PPSh-41s instead of their own MP 40s."
                },
                "Logistics were a nightmare for both sides. The Soviets were forced to ferry reinforcements and supplies across the wide Volga River under constant German artillery fire and air attacks. The Germans relied on a single rail line across the steppe, which was vulnerable to partisan attacks and struggled to supply the 6th Army with fuel and ammunition."
            ]
        },
        {
            "title": "Opening Moves & Initial Clash",
            "content": [
                "The battle began on August 23, 1942, with a massive bombing raid by Luftflotte 4, which dropped thousands of tons of bombs on Stalingrad, reducing the city to rubble and killing over 40,000 civilians. German armored patrols reached the Volga north of the city on the same day.",
                "In September, the 6th Army entered the city, initiating the street fighting. The Germans advanced slowly, capturing the central railway station and the Mamayev Kurgan hill, only to face counterattacks the next day. The fighting centered on major industrial sites, including the Red October Steel Factory and the Barrikady Gun Factory, where workers produced and repaired tanks directly on the front lines."
            ]
        },
        {
            "title": "The Rat War (Rattenkrieg)",
            "content": [
                "The combat inside the ruined city was brutal, described by German soldiers as Rattenkrieg (Rat War). The battle was fought in three dimensions: in sewers, cellars, ruins, and attics. Snipers, most notably Vasily Zaytsev, who killed over 220 German soldiers during the battle, became national heroes, while their stories were used by Soviet propaganda to boost morale.",
                "Buildings like 'Pavlov's House'—a four-story apartment building fortified by Sergeant Yakov Pavlov—became famous. Pavlov's small squad defended the building for 58 days against repeated German attacks, using machine guns, anti-tank rifles, and mines, and proving that a small, determined force could hold out in the ruins."
            ]
        },
        {
            "title": "The Soviet Encirclement: Operation Uranus",
            "content": [
                "While the German 6th Army was focused on capturing the last pockets of Soviet resistance along the Volga, the Soviet High Command (Stavka), led by Zhukov and Vasilevsky, secretly massed over a million men on the northern and southern flanks of the city. These flanks were guarded by Romanian, Italian, and Hungarian armies, which lacked heavy anti-tank weapons.",
                "On November 19, 1942, the Soviets launched Operation Uranus. The Red Army smashed through the Romanian defenses, and within four days, the two pincer arms met at Kalach-na-Donu, encircling the German 6th Army, along with parts of the 4th Panzer Army and Romanian units, trapping over 250,000 Axis troops inside the city."
            ]
        },
        {
            "title": "The Siege & The Failed Relief Campaign",
            "content": [
                "General Paulus requested permission to break out of the encirclement, but Hitler refused, ordering the 6th Army to hold its positions. Reichsmarschall Hermann Göring assured Hitler that the Luftwaffe could supply the trapped army by air, claiming they could deliver 300 tons of supplies daily. In reality, the Luftwaffe lacked the transport aircraft, and Soviet fighters and anti-aircraft fire decimated their formations, averaging less than 90 tons of supplies a day.",
                "In December, Field Marshal Erich von Manstein launched Operation Winter Storm, an armored relief attempt to break the Soviet ring. However, they were halted 30 miles from the pocket. Hitler refused to allow Paulus to launch a coordinated breakout to meet Manstein's forces, condemning the 6th Army to starvation and freezing temperatures."
            ]
        },
        {
            "title": "Surrender and Tragedy",
            "content": [
                "By January 1943, the trapped German soldiers were starving, freezing, and running out of ammunition. The Soviets launched Operation Ring, systematically crushing the pocket. On January 30, Hitler promoted Paulus to Field Marshal, noting that no German field marshal had ever surrendered, implying Paulus should commit suicide.",
                "Paulus refused, and on January 31, 1943, he surrendered his headquarters. The remaining Axis forces in the northern pocket capitulated on February 2. Over 91,000 Axis soldiers were captured, including 24 generals. Placed in Soviet labor camps, most died of typhus, malnutrition, and exposure; only 6,000 survived to return to Germany after the war."
            ]
        },
        {
            "title": "The Aftermath & Strategic Consequences",
            "content": [
                "The Battle of Stalingrad was the turning point of the war in Europe. The Wehrmacht lost an entire field army, along with hundreds of thousands of allied Axis troops, armor, and aircraft. This defeat broke the back of the German offensive capability on the Eastern Front, forcing them onto a permanent defensive retreat.",
                "The victory boosted Allied morale and shattered the myth of German military invincibility. It confirmed the Red Army's capability in planning and executing large-scale encirclement operations, and marked the start of the long Soviet advance that would lead to Berlin."
            ]
        },
        {
            "title": "Historical Legacy & Long-term Impact",
            "content": [
                "Stalingrad remains a symbol of urban warfare, sacrifice, and military turning points. The battle's scale and high casualty rate make it one of the deadliest engagements in human history. The Mamayev Kurgan hill in modern Volgograd is dominated by 'The Motherland Calls' statue, commemorating the Soviet soldiers who fell during the defense of the city.",
                "The battle also highlights the disastrous impact of Hitler's ideological obsessions and micromanagement on military operations, which overrode the warnings of his generals and condemned a quarter-million soldiers to death."
            ]
        },
        {
            "title": "Archives, Primary Sources & Further Reading",
            "content": [
                "To read diaries, operational logs, and research files on the Battle of Stalingrad:",
                {
                    "type": "sources",
                    "items": [
                        {
                            "title": "History Channel - Battle of Stalingrad Summary",
                            "url": "https://www.history.com/topics/world-war-ii/battle-of-stalingrad",
                            "desc": "A comprehensive summary of the battle, featuring documentary videos, photo collections, and timelines."
                        },
                        {
                            "title": "Imperial War Museums - What to Know About the Battle of Stalingrad",
                            "url": "https://www.iwm.org.uk/history/what-you-need-to-know-about-the-battle-of-stalingrad",
                            "desc": "An archival display exploring why Stalingrad was the strategic turning point of the European conflict."
                        },
                        {
                            "title": "The Volgograd State Panoramic Museum of Stalingrad",
                            "url": "https://stalingrad-battle.ru/",
                            "desc": "The official museum repository containing original weapons, letters, diaries, and maps from the battle."
                        }
                    ]
                }
            ]
        }
    ]
}

# 7. Normandy Landings (D-Day)
dday_data = {
    "title": "Normandy Landings (D-Day)",
    "date": "June 6, 1944",
    "location": "Normandy, France",
    "result": "Decisive Allied victory",
    "outcome": "Successful establishment of a Second Front in Europe; liberation of Western Europe begins.",
    "allied_commanders": "Dwight D. Eisenhower, Bernard Montgomery, Bertram Ramsay, Trafford Leigh-Mallory",
    "axis_commanders": "Gerd von Rundstedt, Erwin Rommel, Friedrich Dollmann",
    "allied_forces": "Allied Expeditionary Force: 156,000 assault troops (73,000 Americans, 83,000 British/Canadians), 6,939 vessels, 11,590 aircraft",
    "axis_forces": "German Army Group B: Approx. 50,000 static defense troops, 3 divisions (reserve panzers under OKW control)",
    "allied_casualties": "Approx. 10,000 casualties (4,414 confirmed killed, including 2,501 Americans)",
    "axis_casualties": "Estimated 4,000 to 9,000 casualties (killed, wounded, or captured)",
    "image": "assets/images/normandy_landings_1783712245867.png",
    "chapters": [
        {
            "title": "Strategic Context & The Second Front",
            "content": [
                "For years, Soviet Premier Joseph Stalin had demanded that the Western Allies open a 'Second Front' in Western Europe to relieve the pressure on the Red Army, which was fighting the bulk of the German military on the Eastern Front. Planning for the invasion, codenamed Operation Overlord, began in 1943 under the direction of General Dwight D. Eisenhower, appointed Supreme Allied Commander.",
                "The Germans, expecting an invasion, built the 'Atlantic Wall'—a network of concrete bunkers, coastal artillery batteries, beach obstacles, and minefields stretching from Norway to Spain. Field Marshal Erwin Rommel was appointed to inspect and improve the defenses in northern France. Rommel believed that the invasion had to be defeated on the beaches within the first 24 hours, while the Allies were still vulnerable."
            ]
        },
        {
            "title": "The Intelligence War & Deception Campaigns",
            "content": [
                "To ensure success, the Allies executed Operation Bodyguard—the most elaborate deception campaign in military history. The goal was to convince the German High Command that the invasion would land at the Pas de Calais, the shortest route across the English Channel, and that any landing in Normandy was a diversion.",
                "The deception relied on double agents, fake radio traffic, and the creation of a fictitious army group, the First US Army Group (FUSAG), supposedly commanded by General George S. Patton. The Allies built fake military camps with inflatable tanks, dummy wooden landing craft, and false harbors in Kent, directly across from Calais. The deception succeeded, keeping German armored divisions positioned north of the Seine River for weeks after the actual landings."
            ]
        },
        {
            "title": "Weapons, Technology, and Logistics",
            "content": [
                "The invasion required new technological solutions. The Allies developed 'Hobart's Funnies'—specialized Sherman tanks modified for mine-clearing, bridging, and destroying concrete bunkers. They also built two massive artificial harbors, called 'Mulberry Harbors', which were towed across the Channel to allow the unloading of supplies without capturing a port.",
                {
                    "type": "sidebar",
                    "title": "Technology Profile: The PLUTO Pipeline",
                    "text": "The Allies designed the PLUTO (Pipe-Line Under the Ocean) system to pump fuel directly from England to France. These flexible steel pipelines were laid across the Channel floor, delivering millions of gallons of fuel to support the mechanized advance."
                },
                "The German defenders possessed MG 42 machine guns, which had a rate of fire of 1,200 rounds per minute, earning it the nickname 'Hitler's Buzzsaw'. Positioned in concrete bunkers overlooking the beaches, these weapons inflicted heavy casualties on the landing infantry."
            ]
        },
        {
            "title": "Opening Moves: Airborne Operations",
            "content": [
                "The invasion began shortly after midnight on June 6, 1944, with airborne operations. Over 24,000 American, British, and Canadian paratroopers were dropped behind enemy lines. The British 6th Airborne Division captured Pegasus Bridge near Caen to protect the eastern flank, while the US 82nd and 101st Airborne Divisions dropped on the western flank to secure exits from Utah Beach.",
                "The drops were chaotic, with many units scattered miles from their targets due to cloud cover and anti-aircraft fire. However, this confusion worked to the Allies' advantage, disorienting the German command, preventing coordinated counterattacks, and allowing small groups of paratroopers to harass German units."
            ]
        },
        {
            "title": "The Amphibious Assault: The Five Beaches",
            "content": [
                "At 6:30 AM, Allied troops began storming five assault beaches. The Americans landed at Utah and Omaha beaches in the west, while the British and Canadians landed at Gold, Juno, and Sword beaches in the east. The landings were preceded by a massive naval bombardment and air strikes.",
                "At Utah Beach, the US 4th Infantry Division landed in the wrong sector due to strong currents, but faced light resistance. Brigadier General Theodore Roosevelt Jr. made the famous decision: 'We’ll start the war from right here!' and directed the landing inland, securing the exits with minimal casualties."
            ]
        },
        {
            "title": "The Tragedy at Omaha Beach",
            "content": [
                "The situation at Omaha Beach was different. The preliminary bombing had missed the German defenses due to low visibility, and the heavy seas swamped many amphibious DD tanks before they reached the shore. The landing troops faced the veteran German 352nd Infantry Division, positioned on high bluffs overlooking the beach.",
                "The American soldiers were pinned down by machine-gun and artillery fire, resulting in a slaughter on the sand. Through individual courage, localized leadership, and support from Allied destroyers that sailed into shallow water to fire on bunkers, the infantry managed to scale the cliffs and breach the defenses by early afternoon."
            ]
        },
        {
            "title": "Pivot Points & Command Decisions",
            "content": [
                "A key factor was the German command structure. The German reserve panzer divisions could only be released with the personal approval of Adolf Hitler. On the morning of June 6, Hitler was asleep at Berchtesgaden, and his staff refused to wake him. By the time he authorized the release of the tanks in the afternoon, the Allied air superiority prevented them from moving without facing destruction.",
                "Furthermore, Erwin Rommel was in Germany celebrating his wife's birthday, believing that the stormy weather would prevent any invasion attempts. He rushed back to France but arrived too late to coordinate the beach defenses, which had already been breached."
            ]
        },
        {
            "title": "The Soldier's Ordeal & Civilian Impact",
            "content": [
                "For the assault troops, the landing was a terrifying experience. Many suffered from seasickness in the landing craft before being dropped into cold water under fire. The scenes of carnage on Omaha Beach, with wounded men drowning in the rising tide, left deep psychological scars on the survivors.",
                "French civilians in Normandy suffered from Allied bombing and shelling, which targeted infrastructure and towns to prevent German reinforcements from reaching the beaches. Towns like Caen and Saint-Lô were reduced to ruins, and thousands of French civilians died, though they welcomed the Allied liberators."
            ]
        },
        {
            "title": "The Aftermath & Strategic Consequences",
            "content": [
                "By the end of June 6, the Allies had landed over 156,000 men and established a beachhead in Normandy, though they failed to capture key objectives like Caen. The successful invasion created a Second Front in Europe, forcing Germany to divide its forces between East and West.",
                "Over the next two months, the Allies fought a grinding war of attrition in the Normandy bocage (hedgerows) before breaking out in Operation Cobra, which led to the liberation of Paris in August 1944 and the rapid retreat of German forces toward their own borders."
            ]
        },
        {
            "title": "Historical Legacy & Long-term Impact",
            "content": [
                "D-Day remains the largest amphibious invasion in history and a symbol of Allied coordination and military planning. The Normandy American Cemetery at Colleville-sur-Mer, overlooking Omaha Beach, serves as a poignant reminder of the high human cost of the invasion.",
                "The battle demonstrated the importance of air supremacy, amphibious technology, and intelligence deception in modern warfare, and marked the start of the final phase of the war in Europe, leading to the collapse of the Third Reich."
            ]
        },
        {
            "title": "Archives, Primary Sources & Further Reading",
            "content": [
                "To read reports, plans, and maps from the Normandy Campaign:",
                {
                    "type": "sources",
                    "items": [
                        {
                            "title": "The National WWII Museum - D-Day and Normandy",
                            "url": "https://www.nationalww2museum.org/war/topics/d-day-and-normandy-campaign",
                            "desc": "A comprehensive portal detailing the planning, execution, and stories of the D-Day landings."
                        },
                        {
                            "title": "The D-Day Story Portsmouth Museum",
                            "url": "https://theddaystory.com/",
                            "desc": "An interactive digital exhibition featuring the Overlord Embroidery, landing craft, and personal diaries."
                        },
                        {
                            "title": "US Army Center of Military History - D-Day Documents",
                            "url": "https://history.army.mil/",
                            "desc": "Official US Army historical monographs, operational maps, and unit action diaries."
                        }
                    ]
                }
            ]
        }
    ]
}

# 8. Battle of the Bulge
bulge_data = {
    "title": "Battle of the Bulge",
    "date": "December 16, 1944 - January 25, 1945",
    "location": "Ardennes region, Belgium, Luxembourg, Germany",
    "result": "Decisive Allied victory",
    "outcome": "Exhaustion of Germany's last operational reserves; the path into Germany is left virtually undefended.",
    "allied_commanders": "Dwight D. Eisenhower, Omar Bradley, George S. Patton, Bernard Montgomery",
    "axis_commanders": "Adolf Hitler, Gerd von Rundstedt, Walter Model, Hasso von Manteuffel, Sepp Dietrich",
    "allied_forces": "Approx. 83,000 troops (at start), rising to over 800,000 total troops, 1,300 tanks",
    "axis_forces": "Approx. 200,000 troops (at start), rising to 450,000 total troops, 970 tanks, 1,600 aircraft",
    "allied_casualties": "Approx. 90,000 casualties (89,500 Americans, including 19,000 killed)",
    "axis_casualties": "Estimated 80,000 to 100,000 casualties (killed, wounded, or captured)",
    "image": "assets/images/battle_of_bulge_1783712254116.png",
    "chapters": [
        {
            "title": "Strategic Context & The Final Gamble",
            "content": [
                "By the autumn of 1944, Nazi Germany was facing military collapse. Allied armies were closing in from the west, while the Soviet Red Army was preparing a massive winter offensive in the east. Adolf Hitler, refusing to accept defeat, conceived a surprise counteroffensive in the West, codenamed Unternehmen Wacht am Rhein (Operation Watch on the Rhine).",
                "Hitler's plan was to launch a surprise attack through the Ardennes region—the same forested sector used in the 1940 invasion of France—cross the Meuse River, and capture the Allied supply port of Antwerp. Hitler believed this bold stroke would split the American and British armies, shatter the Allied coalition, and force the Western Allies to sign a separate peace, allowing Germany to focus its remaining resources on the Soviet Union."
            ]
        },
        {
            "title": "Military Doctrines & War Plans",
            "content": [
                "The German plan relied on speed, surprise, and poor weather. The OKW planned to attack during a period of heavy winter storms that would ground the Allied air forces, neutralizing their air supremacy. The German armored spearheads, including the 6th Panzer Army under Sepp Dietrich and the 5th Panzer Army under Hasso von Manteuffel, were to bypass strongpoints and rush toward the Meuse.",
                "The Allied High Command was caught off guard. Believing the Ardennes was too rugged for winter operations, they used the sector as a quiet zone, deploying inexperienced divisions to get acclimated to the front, and battle-weary divisions to rest. The American lines were thinly held, with only a few divisions guarding a 75-mile front."
            ]
        },
        {
            "title": "Weapons, Technology, and Logistics",
            "content": [
                "The Germans deployed their latest heavy armor, including the Tiger II (King Tiger) and the Panther tank. These tanks possessed superior armor and guns compared to the American M4 Sherman, but were heavy, slow, and consumed large quantities of fuel, which Germany lacked.",
                {
                    "type": "sidebar",
                    "title": "Weapons Profile: The King Tiger Tank",
                    "text": "The Tiger II, or King Tiger, was the most powerful tank deployed in the Ardennes. Its 8.8cm gun and 150mm sloped front armor made it nearly invulnerable from the front, but its weight (68 tons) caused mechanical breakdowns and made crossing bridges impossible."
                },
                "Logistics were the critical bottleneck for the Wehrmacht. The German army relied on capturing American fuel depots to sustain their advance. If they failed to capture these depots quickly, their armored columns would run out of fuel and be abandoned on the forest roads."
            ]
        },
        {
            "title": "Opening Moves & Initial Clash",
            "content": [
                "At 5:30 AM on December 16, 1944, the Germans launched their offensive with a massive artillery bombardment along a 75-mile front. Panzers and infantry plunged across the border under cover of heavy fog, catching the American forces completely by surprise.",
                "The German advance created a massive 'bulge' in the Allied line. Several American units were bypassed and surrounded. In the north, the 99th and 2nd Infantry Divisions made a heroic stand at Elsenborn Ridge, preventing the 6th Panzer Army from capturing key roads. In the south, the Germans surrounded two regiments of the 106th Infantry Division on the Schnee Eifel, resulting in the surrender of over 7,000 American soldiers."
            ]
        },
        {
            "title": "The Siege of Bastogne",
            "content": [
                "The battle centered on the town of Bastogne, a vital crossroads where seven main roads in the Ardennes met. The Germans needed to capture the town to keep their supply lines moving. Eisenhower ordered the 101st Airborne Division, commanded by General Anthony McAuliffe, to hold Bastogne at all costs.",
                "By December 21, the Germans had completely surrounded Bastogne, trapping the paratroopers. Lacking winter clothing, medical supplies, and ammunition, the defenders held out in freezing temperatures. On December 22, the German commander sent a formal demand for surrender. McAuliffe issued his famous one-word reply: 'Nuts!' which boosted the morale of the defenders and the Allied public."
            ]
        },
        {
            "title": "Patton's Counteroffensive & The Clearing Skies",
            "content": [
                "At the start of the offensive, Eisenhower met with his commanders in Verdun. General George S. Patton, commander of the Third US Army, made a bold promise: he would pivot his entire army 90 degrees north and launch a counteroffensive to relieve Bastogne within three days. This required moving over 130,000 vehicles in winter conditions.",
                "On December 23, the weather cleared, allowing Allied fighter-bombers to take off. The aircraft swarmed the battlefield, bombing German columns and dropping supplies to the defenders at Bastogne. On December 26, armored units from Patton's 4th Armored Division broke through the German ring, relieving Bastogne and ending the siege."
            ]
        },
        {
            "title": "Pivot Points & Allied Decisions",
            "content": [
                "The most critical decision was the stand at Elsenborn Ridge and St. Vith, which delayed the German advance and prevented them from securing key roads. This delay allowed the Allies to bring in reinforcements, including the 82nd and 101st Airborne Divisions, and deploy them at critical choke points.",
                "Another factor was the failure of Otto Skorzeny's Operation Greif—a covert mission where German commandos dressed in American uniforms tried to capture bridges and sow confusion behind Allied lines. Although they caused initial panic, the Americans quickly established checkpoints, using trivia questions (like naming baseball players) to identify the infiltrators."
            ]
        },
        {
            "title": "The Soldier's Ordeal & War Crimes",
            "content": [
                "For the common soldier, the battle was a struggle against both the enemy and the winter. Temperatures dropped below freezing, and soldiers suffered from frostbite and trench foot. The dense forests of the Ardennes, covered in snow, became a landscape of artillery shell bursts and close-quarters combat.",
                "The battle saw notable war crimes. On December 17, an SS unit under Joachim Peiper executed 84 disarmed American prisoners of war near Malmedy. News of the Malmedy massacre spread rapidly among American units, hardening their resolve and leading to warnings that SS troops would be executed upon capture."
            ]
        },
        {
            "title": "The Aftermath & Strategic Consequences",
            "content": [
                "By late January 1945, the Allies had restored the original line, ending the battle. The Battle of the Bulge was the bloodiest single engagement fought by the US Army in the war, resulting in nearly 90,000 American casualties.",
                "However, the German offensive failed completely. Hitler had exhausted his last operational reserves of manpower, armor, and fuel in a gamble that achieved nothing. By throwing away his best remaining divisions in the West, he left the path into the German industrial heartland undefended, significantly accelerating the end of the war."
            ]
        },
        {
            "title": "Historical Legacy & Long-term Impact",
            "content": [
                "The Battle of the Bulge is remembered as a symbol of American soldier resilience and tactical flexibility. Patton's rapid pivot of the Third Army is studied in military academies as a classic example of operational mobility.",
                "The victory confirmed that Germany was defeated, leaving only the timing of the final collapse to be decided, and allowing the Allies to coordinate their final advance into Germany from both East and West."
            ]
        },
        {
            "title": "Archives, Primary Sources & Further Reading",
            "content": [
                "To explore official war maps, diaries, and logs from the Ardennes Campaign:",
                {
                    "type": "sources",
                    "items": [
                        {
                            "title": "The National WWII Museum - Battle of the Bulge",
                            "url": "https://www.nationalww2museum.org/war/articles/battle-of-the-bulge",
                            "desc": "A detailed archive of the Ardennes campaign, featuring veteran interviews and battle maps."
                        },
                        {
                            "title": "U.S. Army Center of Military History - Ardennes Campaign",
                            "url": "https://history.army.mil/",
                            "desc": "Official US Army monographs, including the green book 'The Ardennes: Battle of the Bulge'."
                        },
                        {
                            "title": "The Bastogne War Museum Official Page",
                            "url": "https://www.bastognewarmuseum.be/",
                            "desc": "Museum repository containing original artifacts, weapons, and letters from the siege of Bastogne."
                        }
                    ]
                }
            ]
        }
    ]
}

# 9. Battle of Iwo Jima
iwo_jima_data = {
    "title": "Battle of Iwo Jima",
    "date": "February 19 - March 26, 1945",
    "location": "Iwo Jima, Volcano Islands, Tokyo, Japan",
    "result": "Decisive American victory",
    "outcome": "Capture of Iwo Jima's airfields; the high human cost heavily influences the decision to use the atomic bomb.",
    "allied_commanders": "Chester W. Nimitz, Holland Smith, Marc Mitscher, Harry Schmidt",
    "axis_commanders": "Tadamichi Kuribayashi, Baron Takeichi Nishi",
    "allied_forces": "US Marine Corps and Navy: Approx. 74,000 Marines, 110,000 total personnel, 500 ships",
    "axis_forces": "Imperial Japanese Army and Navy: Approx. 21,000 garrison troops",
    "allied_casualties": "26,048 total casualties (6,821 killed, 19,189 wounded, 494 missing)",
    "axis_casualties": "Approx. 18,840 killed, only 216 captured (during the battle)",
    "image": "assets/images/battle_of_iwo_jima_1783712261591.png",
    "chapters": [
        {
            "title": "Strategic Context & The Island Hopping Campaign",
            "content": [
                "By early 1945, the Allied 'island-hopping' campaign had brought US forces to the inner defense ring of the Japanese Empire. The volcanic island of Iwo Jima, a tiny speck of black sand and sulfur located midway between the Mariana Islands and Tokyo, became a critical strategic objective. The US Army Air Forces were conducting a strategic bombing campaign against Japanese cities using B-29 Superfortresses, launched from Saipan and Tinian.",
                "However, these bombers faced challenges: they had no fighter escorts to protect them over Tokyo, and the Japanese radar station on Iwo Jima provided early warning to the home islands, allowing fighters to intercept the B-29s. Capturing Iwo Jima would eliminate the radar station, provide an emergency landing strip for damaged B-29s, and serve as a base for P-51 Mustang fighter escorts, significantly reducing bomber casualties."
            ]
        },
        {
            "title": "Military Doctrines: The Subterranean Fortress",
            "content": [
                "The Japanese commander on Iwo Jima, General Tadamichi Kuribayashi, recognized that he could not win the battle. The US possessed absolute air and naval superiority, and Japan could not reinforce the island. Kuribayashi's goal was not to win, but to inflict such high casualties on the Americans that it would break their political resolve to launch an invasion of the Japanese home islands.",
                "Kuribayashi ordered a radical shift in Japanese defensive doctrine. He forbade the traditional, suicidal banzai charges, which had decimated Japanese garrisons earlier in the war. Instead, he transformed the island into a subterranean fortress. The Japanese constructed over 11 miles of tunnels connecting 1,500 concrete bunkers, pillboxes, and artillery positions, dug deep into the volcanic rock and Mount Suribachi, leaving the surface looking deserted."
            ]
        },
        {
            "title": "Weapons, Technology, and Logistics",
            "content": [
                "The battle was characterized by close-quarters combat against fortified positions. The US Marines relied on flamethrower tanks (Sherman 'Ronson' or 'Zippo') and portable M2 flamethrowers to clear bunkers. Satchel charges containing C-4 explosive and hand grenades were used to seal tunnel entrances.",
                {
                    "type": "sidebar",
                    "title": "Weapons Profile: The Sherman Flamethrower Tank",
                    "text": "The Sherman tank equipped with a flame-thrower became the most feared weapon on the island. It could shoot a stream of burning napalm up to 100 yards, incinerating the air inside bunkers and forcing the defenders out into the open."
                },
                "The Japanese defenders utilized mortars, heavy artillery, and rocket launchers, including the 320mm spigot mortar, which fired a massive 650-pound shell that caused heavy psychological impact. They also deployed hidden anti-tank guns to target American armor on the beaches."
            ]
        },
        {
            "title": "Opening Moves & The Landing",
            "content": [
                "The landing on February 19, 1945, was preceded by a three-day naval bombardment. At 9:00 AM, the first wave of Marines from the 4th and 5th Marine Divisions landed on the southern beaches of Iwo Jima. They struggled to move in the deep, loose volcanic ash, which clogged their boots and made vehicle movement impossible.",
                "Initially, the Marines faced silence. Kuribayashi had ordered his men to hold their fire until the beaches were crowded with troops and equipment. At 10:00 AM, the Japanese opened fire from hidden positions on Mount Suribachi and the northern plateau, unleashing a crossfire of artillery, mortars, and machine guns that turned the beaches into a slaughterhouse."
            ]
        },
        {
            "title": "Mount Suribachi & The Flag Raising",
            "content": [
                "The primary American objective in the south was Mount Suribachi, a dormant volcano that dominated the landing beaches. The Marines fought their way up the slopes, clearing bunkers room by room. On February 23, 1945, a patrol from the 28th Marine Regiment reached the summit and raised a small American flag.",
                "Later that day, a larger flag was raised to make it visible across the island. Associated Press photographer Joe Rosenthal captured the event. The photograph, 'Raising the Flag on Iwo Jima', became the defining image of the Pacific War, winning the Pulitzer Prize and serving as a powerful symbol of military sacrifice."
            ]
        },
        {
            "title": "The Meatgrinder: The Northern Plateau",
            "content": [
                "With Suribachi secured, the Marines turned north to capture the airfields and the rest of the island. This phase, known as the 'meatgrinder', was the bloodiest part of the battle. The terrain was a maze of rocky ridges, sulfur ravines, and hidden cave networks. The Marines advanced only yards a day, facing constant sniper fire and counterattacks at night.",
                "The Japanese defenders fought with discipline. Cut off from food and water in their underground tunnels, they refused to surrender, forcing the Marines to systematically seal the caves. The battle continued for five weeks, culminating in a final night raid by Japanese survivors on March 26, which targeted an American airfield before being wiped out."
            ]
        },
        {
            "title": "Pivot Points & Command Decisions",
            "content": [
                "The most critical decision was Kuribayashi's defensive strategy. By forbidding banzai charges and forcing the Americans to fight for every cave, he succeeded in dragging out the battle for 36 days and inflicting heavy casualties. This was the only battle in the Pacific War where total US casualties exceeded those of the Japanese.",
                "Another factor was the US refusal to use chemical weapons. Although some commanders recommended using poison gas to clear the cave networks quickly, President Franklin D. Roosevelt maintained a strict policy against the first use of chemical weapons, preferring to accept the high Marine casualty rates instead."
            ]
        },
        {
            "title": "The Soldier's Ordeal & Civilian Impact",
            "content": [
                "For the Marines, Iwo Jima was an ordeal of close-quarters combat against an invisible enemy. The sulfur fumes, constant noise, and sight of mangled bodies caused high rates of combat fatigue. Fleet Admiral Chester Nimitz remarked: 'Among the Americans who served on Iwo Island, uncommon valor was a common virtue.'",
                "Iwo Jima had no civilian population during the battle; the Japanese military had evacuated the 1,000 civilian residents in 1944. The island was transformed into a military zone, and the environment was destroyed by the bombardment, leaving a landscape of craters and volcanic ash."
            ]
        },
        {
            "title": "The Aftermath & Strategic Consequences",
            "content": [
                "The capture of Iwo Jima cost the United States over 6,800 lives, while nearly the entire Japanese garrison of 21,000 men was killed. The airfields were quickly repaired, and by the end of the war, over 2,200 B-29 bombers had made emergency landings on the island, saving the lives of an estimated 27,000 crewmen.",
                "However, the high human cost of capturing a tiny volcanic island shocked the American public and military planning. It served as a warning of what to expect during the planned invasion of the Japanese home islands, directly influencing President Harry Truman's decision to utilize the atomic bomb to force a surrender without an invasion."
            ]
        },
        {
            "title": "Historical Legacy & Long-term Impact",
            "content": [
                "Iwo Jima is central to the history and identity of the United States Marine Corps. The Marine Corps War Memorial in Arlington, Virginia, is based on Rosenthal's flag-raising photograph. The battle is remembered as a symbol of military courage, sacrifice, and the high cost of victory in the Pacific.",
                "For Japan, the battle is remembered as a heroic but tragic defense. In 1994, Emperor Akihito visited the island, expressing condolences to the dead of both nations, and the island remains a joint memorial site where veterans gather to commemorate the reconciliation between the two former enemies."
            ]
        },
        {
            "title": "Archives, Primary Sources & Further Reading",
            "content": [
                "For research resources, maps, and original diaries from Iwo Jima:",
                {
                    "type": "sources",
                    "items": [
                        {
                            "title": "The National WWII Museum - Death at Japan's Doorstep",
                            "url": "https://www.nationalww2museum.org/war/articles/iwo-jima-and-okinawa-death-at-japans-doorstep",
                            "desc": "A detailed analysis of the landing operations, Mount Suribachi, and the strategic debate over the island."
                        },
                        {
                            "title": "USMC History Division - Iwo Jima Monographs",
                            "url": "https://www.marines.mil/News/News-Display/Article/3299797/battle-of-iwo-jima/",
                            "desc": "Official Marine Corps historical summaries, unit reports, and medal of honor citations."
                        },
                        {
                            "title": "The Tadamichi Kuribayashi Letters",
                            "url": "https://www.loc.gov/",
                            "desc": "Letters and drawings sent by General Kuribayashi to his family in Tokyo, detailing his life and thoughts on the island."
                        }
                    ]
                }
            ]
        }
    ]
}

# 10. Battle of Berlin
berlin_data = {
    "title": "Battle of Berlin",
    "date": "April 16 - May 2, 1945",
    "location": "Berlin, Germany",
    "result": "Decisive Soviet victory",
    "outcome": "Suicide of Adolf Hitler; unconditional surrender of Nazi Germany; end of World War II in Europe.",
    "allied_commanders": "Georgy Zhukov, Ivan Konev, Konstantin Rokossovsky",
    "axis_commanders": "Helmuth Weidling, Gotthard Heinrici, Theodor Busse, Adolf Hitler (in bunker)",
    "allied_forces": "Soviet Union: 2,500,000 soldiers, 6,250 tanks, 7,500 aircraft, 41,600 artillery pieces",
    "axis_forces": "German Garrison: Approx. 766,000 soldiers (mostly depleted Wehrmacht/SS divisions, Volkssturm militia, and Hitler Youth)",
    "allied_casualties": "Estimated 81,116 killed/missing, 280,251 wounded",
    "axis_casualties": "Approx. 92,000 to 100,000 killed, 220,000 wounded, 480,000 captured; over 125,000 civilians killed",
    "image": "assets/images/battle_of_berlin_1783712268854.png",
    "chapters": [
        {
            "title": "Strategic Context & The Race for the Capital",
            "content": [
                "By the spring of 1945, the Third Reich was in its death throes. The Red Army had advanced from the East, reaching the Oder River, just 40 miles from Berlin. The Western Allies had crossed the Rhine, advancing rapidly. Supreme Allied Commander Dwight D. Eisenhower decided to halt at the Elbe River, ceding the capture of Berlin to the Soviets due to agreed-upon post-war occupation zones and high casualty estimates.",
                "Soviet Premier Joseph Stalin was determined to capture the German capital before the Western Allies could reach it. Stalin wanted to secure German industrial assets, nuclear research facilities, and the ultimate symbolic prize of the Reichstag. He created a competition between his top marshals, Georgy Zhukov (1st Belorussian Front) and Ivan Konev (1st Ukrainian Front), ordering them to race each other to capture Berlin."
            ]
        },
        {
            "title": "Military Doctrines: Urban Siege",
            "content": [
                "The Soviet doctrine relied on overwhelming fire power. They massed the greatest concentration of artillery in history on the Oder front, designed to pulverize the German defenses. Once inside the city, they organized into small, heavily armed assault groups, supported by tanks and self-propelled guns, to clear buildings and streets.",
                "The German defense was disorganized and desperate. General Helmuth Weidling, commander of the Berlin Defense Area, divided the city into sectors, but lacked the men and weapons to hold them. The defenders relied on Panzerfaust anti-tank launchers to ambush Soviet tanks in the narrow streets, while using the city's subway tunnels to move troops and bypass Soviet patrols."
            ]
        },
        {
            "title": "Weapons, Technology, and Logistics",
            "content": [
                "The Soviet forces deployed the IS-2 heavy tank and the Katyusha rocket launcher, which fired salvos of rockets that devastated defensive positions. The T-34/85 tank remained the workhorse, though many were fitted with wire-mesh screens to detonate German Panzerfaust rounds before they struck the armor.",
                {
                    "type": "sidebar",
                    "title": "Weapons Profile: The Panzerfaust",
                    "text": "The Panzerfaust was a cheap, disposable anti-tank weapon fired from the shoulder. It was highly effective in urban combat, allowing a single soldier—or a child from the Hitler Youth—to destroy a Soviet heavy tank from a hidden window."
                },
                "The German defenders had limited ammunition and fuel. Many units were equipped with captured weapons and lack basic supplies. The Volkssturm (civilian militia consisting of old men and boys) were armed with outdated rifles and Panzerfausts, lacking uniforms, training, and communication radios."
            ]
        },
        {
            "title": "Opening Moves: The Seelow Heights",
            "content": [
                "The Soviet offensive began on April 16, 1945, with a massive artillery bombardment along the Oder River. Zhukov attacked the Seelow Heights, the key defensive position guarding the route to Berlin. The German 9th Army, commanded by Gotthard Heinrici, had withdrawn from their front lines, avoiding the initial bombardment.",
                "Zhukov faced difficulties on the heights, with German artillery and mud slowing the advance. Zhukov turned on searchlights to blind the defenders, but this backlit his own infantry, making them easy targets. Konev, in the south, advanced rapidly, crossing the Neisse River and forcing Stalin to allow Konev's tanks to pivot north and race Zhukov to the capital."
            ]
        },
        {
            "title": "The Siege: Entering the City",
            "content": [
                "By April 25, 1945, the Soviet fronts had met west of Berlin, completely encircling the capital. The Red Army began its advance into the city suburbs, encountering barricades, flooded canals, and fanatical resistance from SS units, including foreign volunteers (such as the French Charlemagne Division) who had nothing to lose.",
                "The combat devolved into street-by-street fighting. Soviet tanks, moving without infantry support, suffered heavy losses to Panzerfausts fired from basement windows. The Red Army adapted, using artillery to destroy buildings before the infantry entered, and using flamethrowers and grenades to clear the ruins."
            ]
        },
        {
            "title": "The Battle for the Reichstag",
            "content": [
                "The climax of the battle centered on the Reichstag building—the symbolic parliament of Germany. On April 28, Soviet troops reached the Königsplatz. The Reichstag was fortified by the Germans, who bricked up windows and dug anti-tank ditches, turning it into a fortress.",
                "On April 30, Soviet soldiers breached the building, initiating room-by-room combat in the pitch-black corridors. Late that night, Soviet soldiers raised the Red Flag over the roof of the Reichstag. The event was photographed by Yevgeny Khaldei, serving as the iconic image of Soviet victory in Berlin."
            ]
        },
        {
            "title": "Hitler's End in the Führerbunker",
            "content": [
                "While the battle was raging in the streets, Adolf Hitler remained in his subterranean Führerbunker beneath the Reich Chancellery. Physical declining and detached from reality, he spent his final days ordering non-existent armies to relieve Berlin, raging at his generals for 'betrayal', and writing his political testament.",
                "On April 30, as Soviet troops advanced close to the Chancellery, Hitler committed suicide by gunshot, while his wife Eva Braun took cyanide. Their bodies were carried up to the garden and burned, as Hitler had ordered, to prevent their capture. Joseph Goebbels, appointed Reich Chancellor, committed suicide with his wife the next day after poisoning their six children."
            ]
        },
        {
            "title": "Surrender and Tragedy",
            "content": [
                "On May 2, 1945, General Helmuth Weidling met with Soviet General Vasily Chuikov and signed the surrender of the Berlin garrison. The fighting in the city stopped. German soldiers emerged from the ruins to go into captivity.",
                "The civilian population endured tragedy. Over 125,000 Berliners died during the siege, many of suicide, hunger, or bombardment. The Soviet victory was followed by a wave of looting and mass rapes, as Soviet soldiers exacted revenge for the atrocities committed by the Wehrmacht in the East, leaving a dark mark on the liberation."
            ]
        },
        {
            "title": "The Aftermath & Strategic Consequences",
            "content": [
                "The fall of Berlin led to the unconditional surrender of all German forces on May 8, 1945 (V-E Day), ending World War II in Europe. The city was divided into four occupation zones: Soviet, American, British, and French.",
                "This division of Berlin, located deep inside the Soviet occupation zone of Germany, created the central flashpoint of the Cold War. It led to the Berlin Airlift of 1948-1949 and the construction of the Berlin Wall in 1961, which divided the city for nearly three decades."
            ]
        },
        {
            "title": "Historical Legacy & Long-term Impact",
            "content": [
                "The Battle of Berlin is remembered as the final victory over Nazi Germany, but also as a tragic climax of urban siege and civilian suffering. The Soviet War Memorial in Treptower Park, Berlin, serves as a major monument to the 80,000 Soviet soldiers who fell during the capture of the city.",
                "The battle highlights the final collapse of a dictatorial regime that chose to drag its own capital and civilian population into destruction rather than accept surrender, marking the end of the European conflict."
            ]
        },
        {
            "title": "Archives, Primary Sources & Further Reading",
            "content": [
                "To read diaries, operational logs, and research files on the Battle of Berlin:",
                {
                    "type": "sources",
                    "items": [
                        {
                            "title": "Imperial War Museums - The Battle of Berlin: Germany's Downfall",
                            "url": "https://www.iwm.org.uk/history/the-battle-of-berlin-germanys-downfall-on-the-eastern-front",
                            "desc": "An archival display exploring the tactics, key commanders, and civilian experience during the final battle of the European war."
                        },
                        {
                            "title": "VisitBerlin - Museum Berlin-Karlshorst",
                            "url": "https://www.visitberlin.de/en/museum-berlin-karlshorst",
                            "desc": "An educational guide to the historic museum at Karlshorst where the German capitulation was signed in May 1945."
                        },
                        {
                            "title": "The Soviet War Diaries - May 1945 Archives",
                            "url": "https://www.loc.gov/",
                            "desc": "Original field diaries and reports of Marshals Zhukov and Konev describing the capture of the Reichstag."
                        }
                    ]
                }
            ]
        }
    ]
}

# Write out the remaining JSON files
battles_map = {
    "poland": poland_data,
    "britain": britain_data,
    "barbarossa": barbarossa_data,
    "pearl-harbor": pearl_harbor_data,
    "midway": midway_data,
    "stalingrad": stalingrad_data,
    "d-day": dday_data,
    "bulge": bulge_data,
    "iwo-jima": iwo_jima_data,
    "berlin": berlin_data
}

# Fix URLs and add tactical maps dynamically before writing out
maps_info = {
    "poland": {
        "intro": "A reconstruction of the operational movements and main advance axes during the opening campaign of the European war:",
        "url": "../assets/images/maps/map_poland.png",
        "alt": "Invasion of Poland Tactical Map",
        "caption": "Invasion of Poland, September 1939: Showing the dual-pincer advances of German Army Group North and Army Group South converging on Warsaw, alongside the Soviet Red Army's entry from the east on September 17."
    },
    "britain": {
        "intro": "A tactical overview of the airspace divisions and key defense networks during the defense of the United Kingdom:",
        "url": "../assets/images/maps/map_britain.png",
        "alt": "Battle of Britain Tactical Map",
        "caption": "Battle of Britain, 1940: Highlighting Fighter Command's No. 10, 11, and 12 Groups defensive sectors, key radar chain stations, and the primary bomber avenues of Luftflotte 2 and 3."
    },
    "barbarossa": {
        "intro": "The vast scale of the Eastern Front invasion routes and offensive lines mapped chronologically:",
        "url": "../assets/images/maps/map_barbarossa.png",
        "alt": "Operation Barbarossa Tactical Map",
        "caption": "Operation Barbarossa, 1941: Detailing the massive three-pronged offensive by Army Groups North, Center, and South into Soviet territory, alongside major encirclement battles."
    },
    "pearl-harbor": {
        "intro": "A map illustrating the tactical vectors of the Japanese Imperial Navy's surprise strike waves over Oahu:",
        "url": "../assets/images/maps/map_pearl_harbor.png",
        "alt": "Attack on Pearl Harbor Tactical Map",
        "caption": "Pearl Harbor Attack, December 7, 1941: Displaying the Japanese strike routes over Oahu and the target battleships anchored at Battleship Row."
    },
    "midway": {
        "intro": "A reconstruction of carrier maneuvering and air search sectors in the Pacific theater:",
        "url": "../assets/images/maps/map_midway.png",
        "alt": "Battle of Midway Tactical Map",
        "caption": "Battle of Midway, June 1942: Illustrating the search sectors, aircraft carrier positions, and tactical engagement coordinates that decided the carrier battle."
    },
    "stalingrad": {
        "intro": "An operational view of the urban sectors and defensive strongpoints within the city:",
        "url": "../assets/images/maps/map_stalingrad.png",
        "alt": "Battle of Stalingrad Tactical Map",
        "caption": "Battle of Stalingrad, 1942: Mapping the urban combat sectors along the Volga River, key factory defenses, and the Soviet outer pocket lines."
    },
    "d-day": {
        "intro": "A detailed tactical beachhead map outlining the division sectors and airborne drop zones on D-Day:",
        "url": "../assets/images/maps/map_dday.png",
        "alt": "Normandy Landings Tactical Map",
        "caption": "Normandy Landings, June 6, 1944: Showing the five landing beaches (Utah, Omaha, Gold, Juno, Sword), naval bombardment units, and Allied airborne drop zones."
    },
    "bulge": {
        "intro": "A map outlining the winter salient and Allied counteroffensive lines in the Ardennes:",
        "url": "../assets/images/maps/map_bulge.png",
        "alt": "Battle of the Bulge Tactical Map",
        "caption": "Battle of the Bulge, December 1944: Detailing the German salient (the 'Bulge') through the Ardennes forest and the surrounded Bastogne pocket."
    },
    "iwo-jima": {
        "intro": "A reconstruction of the island defenses and Marine assault sectors on Iwo Jima:",
        "url": "../assets/images/maps/map_iwo_jima.png",
        "alt": "Battle of Iwo Jima Tactical Map",
        "caption": "Battle of Iwo Jima, February–March 1945: Mapping the designated US Marine landing beaches, Mount Suribachi, and General Kuribayashi's fortified cave systems."
    },
    "berlin": {
        "intro": "A tactical overview of the final Soviet assault rings and defensive sectors in Berlin:",
        "url": "../assets/images/maps/map_berlin.png",
        "alt": "Battle of Berlin Tactical Map",
        "caption": "Battle of Berlin, April–May 1945: Detailing the massive Soviet pincer movements by the 1st Belorussian and 1st Ukrainian Fronts encircling the German capital."
    }
}

# Apply URL fixes to Midway and Iwo Jima
for ch in midway_data["chapters"]:
    if ch["title"] == "Archives, Primary Sources & Further Reading":
        for item in ch["content"]:
            if isinstance(item, dict) and item.get("type") == "sources":
                for src in item["items"]:
                    if "history.navy.mil" in src["url"]:
                        src["url"] = "https://www.britannica.com/event/Battle-of-Midway"
                        src["title"] = "Encyclopedia Britannica - Battle of Midway"
                        src["desc"] = "A detailed historical overview of the carrier operations and strategic outcomes of Midway."

for ch in iwo_jima_data["chapters"]:
    if ch["title"] == "Archives, Primary Sources & Further Reading":
        for item in ch["content"]:
            if isinstance(item, dict) and item.get("type") == "sources":
                for src in item["items"]:
                    if "iwo-jima-and-okinawa" in src["url"]:
                        src["url"] = "https://www.nationalww2museum.org/war/articles/iwo-jima-sacrifice-and-sanctuary"
                        src["title"] = "The National WWII Museum - Sacrifice and Sanctuary"
                        src["desc"] = "An analysis of the battle's strategic value and the emergency landing fields on the island."

# Insert Axis Perspective and Map Chapters
axis_info = {
    "poland": "From the perspective of the Third Reich, the invasion was framed entirely as a defensive necessity and a correction of the \"humiliating\" Treaty of Versailles. German propaganda relentlessly fabricated border incidents, most notably the Gleiwitz incident, where SS operatives dressed in Polish uniforms staged an attack on a German radio station to justify the invasion. Adolf Hitler, addressing the Reichstag on the morning of September 1, explicitly framed the war as a reactive measure: <em>\"For months we have been tormented by a problem... the Danzig and the Corridor problem... I am resolved to continue to fight until the Polish Government is ready to bring about conditions which will guarantee a secure frontier.\"</em> The astonishing speed of the victory—achieved in merely five weeks—vastly inflated the German High Command's confidence. It validated Hitler's strategic gambles and fostered a dangerous sense of invincibility within the Wehrmacht that would eventually lead to the overreach of Operation Barbarossa. For the Soviet Union, the campaign was cynically justified as a necessary move to protect ethnic Ukrainians and Belarusians living in eastern Poland, while practically securing a massive territorial buffer against future German aggression.",
    "britain": "From the German perspective, the Battle of Britain was marked by hubris, intelligence failures, and mounting frustration. The <em>Luftwaffe</em> High Command severely underestimated British aircraft production capabilities, the efficacy of the radar network, and the resilience of British morale. Hermann Göring had boastfully assured Hitler that the RAF would be crushed within weeks. As German bomber losses mounted terribly against the fierce resistance of the Spitfires and Hurricanes, the morale of the German fighter pilots tasked with protecting them plummeted. They found themselves shackled to slow bombers, stripped of their tactical advantages. The profound frustration of the German fighter aces is perfectly encapsulated by an apocryphal but historically resonant exchange between Göring and the legendary fighter ace General Adolf Galland. When Göring demanded to know what the pilots needed to win the battle, Galland replied with biting sarcasm: <em>\"I should like an outfit of Spitfires for my group.\"</em> The failure to achieve air superiority was a bitter pill, but Nazi propaganda quickly spun the narrative, downplaying the defeat and framing the ongoing \"Blitz\" against British cities as a continued, triumphant offensive, masking the strategic reality that Germany had been thwarted.",
    "barbarossa": "The German perspective of Barbarossa transitioned rapidly from supreme, hubristic confidence to apocalyptic dread. Driven by racial superiority and the ideological belief that the Soviet state was inherently weak and corrupt, the German High Command anticipated a rapid collapse within weeks. Franz Halder, the Chief of the OKH General Staff, embodied this overconfidence when he wrote in his war diary on July 3, 1941, barely two weeks into the invasion: <em>\"It is thus not an exaggeration to say that the Russian Campaign has been won in the space of two weeks.\"</em> However, this arrogant certainty evaporated as the campaign progressed. The German army was utterly shocked by the fanatical, suicidal resistance of surrounded Soviet units, the appearance of the vastly superior Soviet T-34 tank, and the seemingly inexhaustible waves of enemy reinforcements. As winter set in and the logistics network collapsed, the reality of the disaster became undeniable. General Heinz Guderian, the architect of Germany's armored forces, captured the despair of the freezing, overextended troops outside Moscow: <em>\"The offensive on Moscow failed... We suffered a miserable defeat, the strength and morale of our troops being heavily depleted.\"</em> The illusion of a quick victory was shattered forever, replaced by the grim realization of an unwinnable war of annihilation.",
    "pearl-harbor": "The Japanese perspective on Pearl Harbor was a volatile mix of desperate economic necessity, supreme martial confidence, and deep underlying fatalism among its most brilliant strategists. The military hardliners in Tokyo viewed the US embargo as a deliberate act of strangulation and an existential threat to the Empire, leaving war as the only honorable recourse. The extraordinary success of the Pearl Harbor raid sparked massive celebrations in Japan, validating their belief in the spiritual superiority of the Japanese warrior over the supposedly decadent and weak Americans. However, Admiral Isoroku Yamamoto, the very architect of the attack, harbored no such illusions. Having studied and lived in the United States, he possessed a terrifyingly accurate understanding of American industrial capacity. He knew that Japan could never win a protracted war of attrition. His strategy was a desperate gamble for a quick knockout blow. Prior to the attack, when asked by Prime Minister Fumimaro Konoe about the prospects of a US-Japan war, Yamamoto issued his chillingly prophetic warning: <em>\"In the first six to twelve months of a war with the United States and Great Britain I will run wild and win victory upon victory. But then, if the war continues after that, I have no expectation of success.\"</em> His worst fears were realized; he had awakened a sleeping giant.",
    "midway": "For the Imperial Japanese Navy, Midway was a catastrophe of unimaginable proportions that shattered the myth of their invincibility. The complex plan relied heavily on surprise, and the Japanese leadership was utterly blindsided by the presence of the American carriers, believing them to be out of position or sunk. The shock of losing the core of the <em>Kido Butai</em> was so profound that the Japanese high command engaged in massive deception, hiding the true extent of the disaster not only from the Japanese public but even from the Emperor and the Imperial Japanese Army. Wounded sailors were kept strictly isolated upon returning home. Captain Mitsuo Fuchida, the legendary pilot who had led the attack on Pearl Harbor and who watched the destruction of the fleet from the deck of the doomed <em>Akagi</em> while recovering from appendicitis, later wrote of the agonizing realization of defeat. He vividly described the horror of those five fatal minutes: <em>\"Looking about, I was horrified at the destruction that had been wrought in a matter of seconds... The terrible fires were completely out of control. In a matter of minutes, the magnificent fleet which had been our country's glory was reduced to a few pathetic, smoking hulks.\"</em> The battle exposed the rigid, inflexible nature of Japanese naval doctrine when confronted with the unexpected.",
    "stalingrad": "From the German perspective, Stalingrad was a descent into an icy hell, driven by the megalomania of the <em>Führer</em>. When the 6th Army was encircled, General Paulus repeatedly requested permission to orchestrate a breakout while they still had the strength. Hitler, misled by Hermann Göring's absurd promise that the <em>Luftwaffe</em> could supply the encircled army entirely by air, furiously denied the request, ordering the 6th Army to stand fast and fight to the last man. The airlift was a dismal failure, and the soldiers in the pocket (the <em>Kessel</em>) were abandoned to starvation, freezing temperatures, and typhus. The despair of the common soldier was absolute. The diary of William Hoffman, a German soldier who perished in the pocket, documented the transition from arrogant confidence to utter hopelessness: in August he wrote of a quick victory, but by December, he penned, <em>\"We are completely isolated... We have eaten the last horses. I am ready for anything, but I cannot believe that we have been abandoned by the Führer.\"</em> When Paulus finally surrendered—shortly after Hitler cynically promoted him to Field Marshal, implying he should commit suicide rather than capitulate—it plunged the German home front into a period of profound mourning and silent realization that the war was lost. Goebbels was forced to declare \"Total War\" in response to the national shock.",
    "d-day": "The German defense was plagued by internal political dysfunction, conflicting strategic doctrines, and the overwhelming success of Allied deception. Field Marshal Erwin Rommel, the pragmatic commander tasked with fortifying the Atlantic Wall, believed the invasion had to be defeated on the beaches within the first 24 hours, utilizing close-in Panzer divisions. Conversely, his superior, Field Marshal Gerd von Rundstedt, favored keeping the armor in a central reserve to launch a massive counterattack once the Allies were inland. Hitler mediated this dispute by keeping the most potent Panzer divisions under his direct personal control. When the invasion occurred, Hitler was asleep and his aides refused to wake him; crucial hours were lost before the armor could be released. Furthermore, the German High Command remained paralyzed, convinced for weeks that Normandy was merely a diversion and the \"real\" invasion was still coming at Calais, thereby keeping vital forces locked down hundreds of miles away. Rommel had prophetically warned his aides months prior about the sheer scale of the impending Allied assault: <em>\"The first twenty-four hours of the invasion will be decisive... the fate of Germany depends on the outcome. For the Allies, as well as Germany, it will be the longest day.\"</em> By the time the German High Command realized the truth, Allied air supremacy had made it impossible for German forces to maneuver in daylight without facing annihilation.",
    "bulge": "For the German officer corps, the Ardennes Offensive was a suicide mission born of Hitler's complete detachment from military reality. The generals knew they lacked the fuel, the ammunition, and the air cover required to reach Antwerp. Their primary objective became merely surviving the inevitable Allied counterattack. The offensive relied on capturing American fuel depots to keep the panzers moving, a precarious strategy that quickly unraveled. General Hasso von Manteuffel, the highly capable commander of the 5th Panzer Army, explicitly noted the unrealistic expectations forced upon them by the High Command: <em>\"The operation was out of proportion to our strength... we had neither the fuel nor the ammunition for a sustained offensive.\"</em> When the skies cleared and Allied aircraft swarmed the battlefield, the German columns were trapped on narrow forest roads, slaughtered from the air. As the surviving German forces limped back to the Siegfried Line, leaving their destroyed armor behind, the absolute finality of their defeat was undeniable even to the most fanatical SS officers.",
    "iwo-jima": "The defense of Iwo Jima was a masterful, if doomed, execution of a strategy of attrition. General Kuribayashi recognized that defeating the overwhelming American amphibious and naval firepower was impossible. His sole objective was to inflict such horrific, unacceptable casualties on the US Marines that it would break the political will of the American public to launch a mainland invasion of Japan. He explicitly forbade suicidal banzai charges, ordering his men to remain in their fortified positions and kill at least ten Americans before dying themselves. The Japanese soldiers, enduring unimaginable conditions underground with no hope of reinforcement or survival, fought with a terrifying discipline. In his final, poignant dispatch to Tokyo before his presumed death in the final days of the battle, Kuribayashi maintained his martial dignity while acknowledging the end: <em>\"The situation is becoming very grave... We are sorry we have not been able to defend the island successfully. Now I, Kuribayashi, will lead a final charge.\"</em> His strategy succeeded in inflicting massive casualties, but failed to break the American resolve, instead pushing them toward a nuclear conclusion.",
    "berlin": "The defense of Berlin was characterized by absolute fanaticism, clinical delusion, and existential terror. Adolf Hitler, physically declining and detached from reality, spent his final days moving non-existent armies on a map, ordering phantom counterattacks to relieve the city, and raging at the \"betrayal\" of his generals. In a final act of nihilism, he issued the \"Nero Decree,\" ordering the destruction of Germany's remaining infrastructure, believing the German people had failed him and deserved to perish. For the average German civilian and soldier, the approaching Red Army represented the ultimate nightmare, driven by a deep fear of retribution for the atrocities committed by Germany in the East. An anonymous diary of a German woman in Berlin (later published as the harrowing <em>A Woman in Berlin</em>) chillingly summarized the total collapse of civilization during those final weeks: <em>\"History is happening here... it smells of corpses, burning, and the end of the world.\"</em> The surrender of the Berlin garrison on May 2nd was met with a mixture of profound relief that the fighting had stopped, and sheer terror at what the Soviet occupation would bring."
}

# Insert Axis Perspective and Map Chapters
for bid, m_info in maps_info.items():
    battle_data = battles_map[bid]
    
    # 1. Axis Perspective Chapter
    axis_chapter = {
        "title": "The Axis Perspective",
        "content": [
            axis_info[bid]
        ]
    }
    battle_data["chapters"].insert(-1, axis_chapter)
    
    # 2. Tactical Map Chapter
    map_chapter = {
        "title": "Tactical Map & Theater of Operations",
        "content": [
            m_info["intro"],
            {
                "type": "map",
                "url": m_info["url"],
                "alt": m_info["alt"],
                "caption": m_info["caption"]
            }
        ]
    }
    battle_data["chapters"].insert(-1, map_chapter)

for bid, data in battles_map.items():
    with open(f"data/{bid}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"Wrote {bid}.json")

print("All JSON files written successfully.")
