
document.addEventListener('DOMContentLoaded', function() {
    
    document.getElementById("id_order").type="number";
    document.getElementById("id_order").min="1";

    var item = document.createElement("small");
    item.id = 'help_text'
    item.className = "timezonewarning"
    var text = document.createTextNode("Maxmimum Order Value is 9");
    item.appendChild(text);

    document.getElementsByClassName("form-row field-order")[0].appendChild(item);


    var dropdown = document.getElementById("id_parent");
    dropdown.addEventListener("change", function(){

        if(!dropdown.options[dropdown.selectedIndex].value){
            document.getElementById("id_order").max="9";
            
            document.getElementById("help_text").innerHTML = "Maxmimum Order Value is 9"
        }
        else{
            document.getElementById("id_order").max="20"

            document.getElementById("help_text").innerHTML = "Maxmimum Order Value is 20"
        }
    }, false);


});
