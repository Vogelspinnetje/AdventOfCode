function loop_door_lijst(invoer){
    const circulair_lijst = invoer + invoer;
    let teller = 0;
    let teller2 = 0;
    const volgend_item = invoer.length / 2;

    for (let letter = 0; letter < invoer.length; letter++){
        if (circulair_lijst[letter] == circulair_lijst[letter+1]){
            teller += parseInt(circulair_lijst[letter]);
        }
        if (circulair_lijst[letter] == circulair_lijst[letter+volgend_item]){
            teller2 += parseInt(circulair_lijst[letter]);
        }
    }

    return teller + "<br/>" + teller2;
}

function in_uit_voer(){
    const invoer = document.getElementById("invoer").value;
    document.getElementById("output").innerHTML = AoC_01_2017(invoer);
}