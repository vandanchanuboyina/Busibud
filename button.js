import $ from "jquery";

const rootApp = document.getElementById("root");
rootApp.innerHTML = '<button id="toggleButton">ON</button>';

$(document).ready(function() {
    $("#toggleButton").click(function() {
        const currentState = $(this).text();
        if (currentState === "ON") {
            $(this).text("OFF");
        } else {
            $(this).text("ON");
        }
    });
});
