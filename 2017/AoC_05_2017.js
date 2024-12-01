function deel2(datastream2){
    let positie = 0;
    let volgende_stap = 0;
    let aantal_stappen = 0;

    while (positie < datastream2.length){
        volgende_stap = positie + datastream2[positie];
        if (datastream2[positie] >= 3){
            datastream2[positie] -= 1;
        }
        else {
            datastream2[positie] += 1;
        }
        positie = volgende_stap;
        aantal_stappen += 1;
    }

    return aantal_stappen;
}

function AoC_05_2017(datastream){
    datastream = datastream.split("\n");
    for (let instructies in datastream){
        datastream[instructies] = parseInt(datastream[instructies]);
    }
    
    const antwoord2 = deel2([...datastream]);
    
    let positie = 0;
    let volgende_stap = 0;
    let aantal_stappen = 0;

    while (positie < datastream.length){
        volgende_stap = positie + datastream[positie];
        datastream[positie] += 1;
        positie = volgende_stap;
        aantal_stappen += 1;
    }

    return aantal_stappen + "<br/>" + antwoord2;
}


function in_uit_voer(){
    const invoer = document.getElementById("invoer").value;
    document.getElementById("output").innerHTML = AoC_05_2017(invoer);
    console.log(invoer)
}
