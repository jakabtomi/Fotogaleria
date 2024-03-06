document.addEventListener('DOMContentLoaded', function() {
    const kerdesek = [
        { kerdes: "Milyen gyakran használt objektív ideális tájképek fotózására?", valaszok: ["Teleobjektív", "Makró objektív", "Széles látószögű objektív"], helyes: 2 },
        { kerdes: "Melyik zársebesség ajánlott éles sportfotók készítéséhez?", valaszok: ["1/500 másodperc", "1/60 másodperc", "1/30 másodperc"], helyes: 0 },
        { kerdes: "Mi a HDR fotózás előnye?", valaszok: ["Alacsony zajszint sötét jelenetekben", "Jobb képminőség nagy ISO-nál", "Szélesebb dinamikatartomány"], helyes: 2 },
        { kerdes: "Melyik nem egy kompozíciós szabály a fotózásban?", valaszok: ["Harmadolás szabálya", "Aranyarány", "Szimmetria tilalma"], helyes: 2 },
        { kerdes: "Hogyan javítható a képek élessége utómunka során?", valaszok: ["Kontraszt növelésével", "Élesség növelésével", "Szín telítettségének növelésével"], helyes: 1 },
        { kerdes: "Melyik program a legnépszerűbb képszerkesztésre?", valaszok: ["Adobe Photoshop", "Microsoft Paint", "Google Docs"], helyes: 0 },
        { kerdes: "Milyen típusú fotózás során használnak gyakran állványt?", valaszok: ["Sportfotózás", "Asztrofotózás", "Portréfotózás"], helyes: 1 },
        { kerdes: "Mi a bokeh hatás a fotózásban?", valaszok: ["A háttér elmosódása", "A kép élesítése", "Színek telítettségének növelése"], helyes: 0 },
        { kerdes: "Melyik módszerrel érhető el a legmagasabb képminőség?", valaszok: ["JPEG formátum használata", "RAW formátumban történő fotózás", "Alacsony ISO használata"], helyes: 1 },
        { kerdes: "Mi jellemzi leginkább a hosszú expozíciós idejű fotókat?", valaszok: ["Gyors mozgás rögzítése", "Víz és égbolt elmosódott hatása", "Nagy mélységélesség"], helyes: 1 }
    

    ];

    let helyesValaszokSzama = 0;
    const kvizDiv = document.getElementById('kviz');

    function kvizGenerálás() {
        let kvizHTML = '';
        kerdesek.forEach((kerdes, index) => {
            kvizHTML += `<div class="kerdes"><h2>${kerdes.kerdes}</h2><ul class="valaszok">`;
            kerdes.valaszok.forEach((valasz, valaszIndex) => {
                kvizHTML += `<li><button onclick="valaszEllenorzes(${index}, ${valaszIndex}, this)">${valasz}</button></li>`;
            });
            kvizHTML += `</ul></div>`;
        });
        kvizHTML += '<div class="eredmeny" style="text-align: center; margin-top: 20px;"></div>';
        kvizDiv.innerHTML = kvizHTML;
    }

    window.valaszEllenorzes = function(kerdesIndex, valaszIndex, elem) {
        const kerdes = kerdesek[kerdesIndex];
        elem.disabled = true; 

        if (kerdes.helyes === valaszIndex) {
            elem.style.backgroundColor = 'lightgreen';
            helyesValaszokSzama++;
        } else {
            elem.style.backgroundColor = 'pink';
        }

        
        const valaszok = elem.parentNode.parentNode.querySelectorAll('button');
        valaszok.forEach(gomb => {
            if (gomb !== elem) {
                gomb.disabled = true;
                if (kerdesek[kerdesIndex].helyes === Array.from(valaszok).indexOf(gomb)) {
                    gomb.style.backgroundColor = 'lightgreen';
                }
            }
        });

        if (document.querySelectorAll('.valaszok button:not([disabled])').length === 0) {
            document.querySelector('.eredmeny').innerHTML = `Pontszámod: ${helyesValaszokSzama} / ${kerdesek.length}`;
        }
    }

    kvizGenerálás();
});
