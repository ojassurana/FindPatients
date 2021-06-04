$(document).ready(function() {

    var creditState = 1;

    $(".text-6").click(function() {
        if (creditState == 1) {
            creditState = 2;
            $(".text-6").html("Contact Us");
            $(".text-5").html("Made by Ojas Surana, Sreeram Vasanth, Nihaal Manaf and Poh Jun Kang");
        } else {
            creditState = 1;
            $(".text-6").html("Credits");
            $(".text-5").html("If you encounter any issues with our website or bot, do contact us at <a href = 'mailto:covid@ojassurana.com'>covid@ojassurana.com</a>");
        };
    })

})