function AoC_07_2017(datastream){
    datastream = datastream.split("\n");
    const connecties = new Map();

    let eerste_toren = "";
    let verwijzende_torens = new Set();

    for (torens of datastream){
        if (torens.length > 10){
            torens = torens.split("->");
            const gesplitte_verwijzing = torens[1].split(", ");
            connecties.set(torens[0].trim(), gesplitte_verwijzing);

            verwijzende_torens.add(torens[0].slice(0, -6))
        }
        else {
            connecties.set(torens, "")
        }
    }

    for (torens of verwijzende_torens){
        
    }


    let txt = "";
    for (const x of connecties.entries()){
        txt += x + "<br/>";
    }

    return txt;
}

function in_uit_voer(){
    const invoer = document.getElementById("invoer").value;
    document.getElementById("output").innerHTML = AoC_07_2017(invoer);
}