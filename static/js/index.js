let preferredColorScheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? "Dark" : "Light";
let nonPreferredColorScheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? "Light" : "Dark";
let toggleDarkmode = () => {
    $("body").toggleClass("alt");
    $("#toggle-darkmode").text($("body").hasClass("alt") ? preferredColorScheme + "en" : nonPreferredColorScheme + "en")
}
$("document").ready(() => {
    $("#toggle-darkmode").text(nonPreferredColorScheme + "en");
});
$("#toggle-darkmode").click(toggleDarkmode);