function AoC_03_2017(datastream){
    datastream = parseInt(datastream);
    let antwoord = 0;
    const ring = Math.ceil((datastream ** 0.5 -1)/2);
    const max_waarde = (ring * 2 +1) ** 2;
    const rand_lengte = ring * 2

    let afstanden_tot_midden = []
    for (let i = 0; i < 4; i++) {
        const midden = max_waarde - rand_lengte * i - ring;
        afstanden_tot_midden.push(Math.abs(datastream - midden));
    }

    return Math.min(...afstanden_tot_midden) + ring;
}

function in_uit_voer(){
    const invoer = document.getElementById("invoer").value;
    document.getElementById("output").innerHTML = AoC_03_2017(invoer);
}