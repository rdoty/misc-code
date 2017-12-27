/**
 * 2017.12.00 Example for a non-programmer friend of a basic way to switch
 * between videos in a pane on the same page. Used jQuery since it was already
 * included - and just slightly more convenient.
 */
function onLinkClick(e) {
    e.preventDefault();
    $("#media_frame").attr('src', e.target.href);
    return false;
}

$(document).ready(function() {
    $(".ytLink").click(onLinkClick);
});
