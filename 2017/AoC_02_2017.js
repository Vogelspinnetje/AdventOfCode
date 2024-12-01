function opdracht2(datastream){
    let antwoord = 0;
    let break_buiten = false;
    for (regels of datastream){
        regels = regels.split("\t");
        for (let getallen = 0; getallen <= regels.length; getallen++){
            for (let volgende = 0; volgende <= regels.length; volgende++){
                if (volgende == getallen){
                    continue;
                }
                if (regels[getallen] % regels[volgende] == 0){
                    antwoord += regels[getallen] / regels[volgende];
                    break;
                }
            }
            if (break_buiten){
                break;
            }
        }
    }
    return antwoord;
}

function AoC_02_2017(datastream){
    datastream = datastream.split("\n");
    let antwoord = 0;
    for (regels of datastream){
        let hoogste = 0;
        let laagste = Infinity;
        for (getallen of regels.split("\t")){
            if (hoogste < parseInt(getallen)){
                hoogste = parseInt(getallen);
            }
            if (laagste > parseInt(getallen)){
                laagste = parseInt(getallen);
            }
        }
        antwoord += hoogste - laagste;
    }
    const antwoord2 = opdracht2(datastream);
    
    return antwoord + "<br/>" + antwoord2;
}

function in_uit_voer(){
    const invoer = document.getElementById("invoer").value;
    document.getElementById("output").innerHTML = AoC_02_2017(invoer);
}