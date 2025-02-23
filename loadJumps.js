console.log("loadJumps.js entered")

async function loadJumps(MitOderOhne, position) {
    try {
        // Dynamischen Dateinamen erstellen
        const dateiName = `data/Sprünge/${MitOderOhne}_Salto_aus_dem_${position}.json`;

        // JSON-Datei laden
        const response = await fetch(dateiName);
        if (!response.ok) {
            throw new Error(`Fehler: ${response.status} - Datei nicht gefunden: ${dateiName}`);
        }

        // JSON-Daten in ein Objekt umwandeln
        const data = await response.json();
        console.log(`Geladene Sprünge aus ${dateiName}:`, data);

        const array = data[`${MitOderOhne}_Salto_aus_dem_${position}`]

        return array; // Gibt die geladenen Sprünge zurück
    } catch (error) {
        console.error("Fehler beim Laden der Sprünge:", error);
        return null; // Falls ein Fehler auftritt
    }
}

async function appendJumpList(MitOderOhne, position) {
    //Überschrift generieren
    const listenÜberschrift = document.createElement("h2");
    listenÜberschrift.textContent = `Sprünge aus dem ${position}`;
    document.body.appendChild(listenÜberschrift);

    //Liste erstellen und beladen
    const spruenge = await loadJumps(MitOderOhne, position);
    const sprungListe = document.createElement("ul")

    spruenge.forEach(sprung => {
        const listElement = document.createElement("li");
        listElement.textContent = sprung.name;
        sprungListe.append(listElement);
    });

    document.body.appendChild(sprungListe);
}

async function appendAllLists(params) {
    const positionen = ["Rücken", "Bauch", "Sitz", "Stand"];

    for (const position of positionen) {
        await appendJumpList("Ohne", position); 
    }
}

appendAllLists();