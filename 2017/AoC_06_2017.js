function AoC_06_2017(datastream){
    datastream = datastream.split("\t");
    for (blokken in datastream){
        datastream[blokken] = parseInt(datastream[blokken]);
    }

    let stappen = 0;
    let configuraties = new Array();
    while (!configuraties.includes(datastream.join(""))){
        configuraties.push(datastream.join(""));

        const hoogste_waarde = Math.max(...datastream);
        const hoogste_waarde_index = datastream.indexOf(hoogste_waarde);
        datastream[hoogste_waarde_index] = 0;
        let uitdeel_index = hoogste_waarde_index + 1;

        for (let rondes = 0; rondes < hoogste_waarde; rondes++){
            if (uitdeel_index >= datastream.length){
                uitdeel_index = 0;
            }
            datastream[uitdeel_index] += 1;
            uitdeel_index += 1;
        }
        
        stappen += 1;
    }
    const antwoord2 = configuraties.length - configuraties.indexOf(datastream.join(""));
    return stappen + "<br/>" + antwoord2;
}

function in_uit_voer(){
    const invoer = document.getElementById("invoer").value;
    document.getElementById("output").innerHTML = AoC_06_2017(invoer);
}