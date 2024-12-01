function hebbenDezelfdeLetters(woord1, woord2) {
    // Sorteren van de letters van beide woorden en vergelijken
    return woord1.split("").sort().join("") === woord2.split("").sort().join("");
}

function AoC_04_2017(datastream){
    datastream = datastream.split("\n");
    let goede_wachtwoorden = 0;
    let goede_wachtwoorden2 = 0;

    for (let opties of datastream){
        let woorden = opties.split(" ");
        let woordenSet = new Set();
        let woordenSet2 = new Set();
        let fout = false;
        let fout2 = false;

        for (let woord of woorden){
            anagram_check = woord.split("").sort().join("");
            if (woordenSet.has(woord)){
                fout = true;
                fout2 = true;
                break;
            }
            if (woordenSet2.has(anagram_check)){
                fout2 = true;
                break;
            }
            woordenSet.add(woord);
            woordenSet2.add(anagram_check);
        }

        if (!fout){
            goede_wachtwoorden += 1;
        }
        if (!fout2){
            goede_wachtwoorden2 += 1;
        }
    }

    return goede_wachtwoorden + "<br/>" + goede_wachtwoorden2;
}

function in_uit_voer(){
    const invoer = document.getElementById("invoer").value;
    document.getElementById("output").innerHTML = AoC_04_2017(invoer);
}
