$(document).ready(function () {
    // Display Speak Message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {
        $(".siri-message li:first").text(message);
        $(".siri-message").textillate('start');
    }

    eel.expose(ShowHood)
    function ShowHood() {
        $('#Oval').attr('hidden', false);
        $('#siriwave').attr('hidden', true);
    }

});

