send.onclick = function() {
    var cookie_date = new Date ( 2023, 01, 15 );
    var date = new Date();
    var day = date.getDate();
    var mounth = date.getMonth() + 1;
    document.cookie = "vote_date=" + mounth + "-" + day + "; expires=" + cookie_date.toGMTString();
}
